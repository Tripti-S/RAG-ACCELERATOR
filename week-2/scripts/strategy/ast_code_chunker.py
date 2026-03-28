# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 2: AST-Based Code Chunking Strategy
========================================

Implements intelligent code chunking using Abstract Syntax Tree (AST) parsing.
Based on CAST (Code-Aware Semantic Tree) algorithm.

How It Works:
1. For CODE files: Parse into AST using tree-sitter, preserve function/class boundaries
2. For MARKDOWN files: Use markdown-aware recursive splitting (headers, code blocks, paragraphs)

This hybrid approach combines the best of both worlds:
- AST parsing preserves code semantics (functions, classes stay together)
- Markdown-aware splitting respects document structure (headers, code blocks)

Key Features:
- Tree-sitter AST parsing for Python, JavaScript, TypeScript
- Markdown-aware recursive splitting (better than generic recursive)
- Preserves function/class boundaries in code
- Respects ## headers, ``` code blocks, paragraphs in markdown

Parameters:
- Code files: 2048 non-whitespace characters, 10% overlap
- Markdown files: 3000 characters (~500-600 words), 10% overlap

Best for: Mixed codebases with both code and documentation.
"""

from typing import List, Dict, Optional
from pathlib import Path
import re

from haystack import component, Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import Language as LangChainLanguage

try:
    from tree_sitter import Language, Parser
    import tree_sitter_python
    import tree_sitter_javascript
    import tree_sitter_typescript
    TREE_SITTER_AVAILABLE = True
except ImportError:
    TREE_SITTER_AVAILABLE = False
    print("⚠️  tree-sitter not available. Install with: pip install tree-sitter tree-sitter-python tree-sitter-javascript tree-sitter-typescript")

class ASTCodeChunker:
    def __init__(self, code_chunk_size: int = 2048, markdown_chunk_size: int = 400, overlap_percentage: float = 0.1):
        self.code_chunk_size = code_chunk_size
        self.markdown_chunk_size = markdown_chunk_size
        self.overlap_percentage = overlap_percentage
        self.parsers = {}
        if TREE_SITTER_AVAILABLE:
            self._initialize_parsers()
        markdown_separators = [
            "\n## ", "\n### ", "\n#### ", "\n```\n\n", "\n```\n", "}\n\n", "}\n", "\n---\n", "\n\n", ".\n", ". ", "?\n", "? ", "!\n", "! ", "\n"
        ]
        self.markdown_splitter = RecursiveCharacterTextSplitter(
            chunk_size=3000,
            chunk_overlap=300,
            separators=markdown_separators,
            keep_separator='end',
            is_separator_regex=False
        )
    def _initialize_parsers(self):
        try:
            py_language = Language(tree_sitter_python.language())
            py_parser = Parser(py_language)
            self.parsers['python'] = (py_parser, py_language)
            js_language = Language(tree_sitter_javascript.language())
            js_parser = Parser(js_language)
            self.parsers['javascript'] = (js_parser, js_language)
            ts_language = Language(tree_sitter_typescript.language_typescript())
            ts_parser = Parser(ts_language)
            self.parsers['typescript'] = (ts_parser, ts_language)
        except Exception as e:
            print(f"⚠️  Error initializing parsers: {e}")
    def _detect_language(self, doc: Document) -> Optional[str]:
        if "language" in doc.meta:
            return doc.meta["language"]
        if doc.meta.get("content_type") == "code":
            return "python"
        if "file_path" in doc.meta:
            ext = Path(doc.meta["file_path"]).suffix.lower()
            ext_map = {".py": "python", ".js": "javascript", ".jsx": "javascript", ".ts": "typescript", ".tsx": "typescript", ".md": "markdown", ".txt": "text"}
            return ext_map.get(ext)
        return None
    def _count_non_whitespace(self, text: str) -> int:
        return len(re.sub(r'\s', '', text))
    def _chunk_code_with_ast(self, content: str, language: str) -> List[str]:
        if not TREE_SITTER_AVAILABLE or language not in self.parsers:
            return self._chunk_code_simple(content)
        parser, lang = self.parsers[language]
        try:
            tree = parser.parse(bytes(content, "utf-8"))
            root_node = tree.root_node
            chunks = []
            current_chunk = []
            current_size = 0
            for child in root_node.children:
                node_text = content[child.start_byte:child.end_byte]
                node_size = self._count_non_whitespace(node_text)
                if node_size > self.code_chunk_size:
                    if current_chunk:
                        chunks.append("\n".join(current_chunk))
                        current_chunk = []
                        current_size = 0
                    sub_chunks = self._split_large_node(node_text, child, language)
                    chunks.extend(sub_chunks)
                elif current_size + node_size > self.code_chunk_size:
                    if current_chunk:
                        chunks.append("\n".join(current_chunk))
                    current_chunk = [node_text]
                    current_size = node_size
                else:
                    current_chunk.append(node_text)
                    current_size += node_size
            if current_chunk:
                chunks.append("\n".join(current_chunk))
            return chunks if chunks else [content]
        except Exception as e:
            print(f"⚠️  AST parsing failed: {e}. Using simple chunking.")
            return self._chunk_code_simple(content)
    def _split_large_node(self, node_text: str, node, language: str) -> List[str]:
        if node.child_count > 0:
            chunks = []
            current_chunk = []
            current_size = 0
            for child in node.children:
                child_text = node_text[child.start_byte - node.start_byte:child.end_byte - node.start_byte]
                child_size = self._count_non_whitespace(child_text)
                if current_size + child_size > self.code_chunk_size:
                    if current_chunk:
                        chunks.append("\n".join(current_chunk))
                    current_chunk = [child_text]
                    current_size = child_size
                else:
                    current_chunk.append(child_text)
                    current_size += child_size
            if current_chunk:
                chunks.append("\n".join(current_chunk))
            return chunks
        return self._chunk_code_simple(node_text)
    def _chunk_code_simple(self, content: str) -> List[str]:
        lines = content.split("\n")
        chunks = []
        current_chunk = []
        current_size = 0
        overlap_lines = max(1, int(len(lines) * self.overlap_percentage))
        for line in lines:
            line_size = self._count_non_whitespace(line)
            if current_size + line_size > self.code_chunk_size and current_chunk:
                chunks.append("\n".join(current_chunk))
                current_chunk = current_chunk[-overlap_lines:] if overlap_lines else []
                current_size = sum(self._count_non_whitespace(l) for l in current_chunk)
            current_chunk.append(line)
            current_size += line_size
        if current_chunk:
            chunks.append("\n".join(current_chunk))
        return chunks if chunks else [content]
    def chunk_document(self, doc: Document) -> List[Document]:
        language = self._detect_language(doc)
        if language in ["markdown", "text", None]:
            chunks_text = self.markdown_splitter.split_text(doc.content)
            valid_chunks = []
            chunk_index = 0
            for chunk_text in chunks_text:
                if not chunk_text or not chunk_text.strip():
                    continue
                chunk_doc = Document(
                    content=chunk_text,
                    meta={
                        **doc.meta,
                        "chunk_method": "ast_md_logical",
                        "detected_language": language or "markdown",
                        "chunk_index": chunk_index,
                        "original_doc_id": doc.id
                    }
                )
                valid_chunks.append(chunk_doc)
                chunk_index += 1
            return valid_chunks
        chunks_text = self._chunk_code_with_ast(doc.content, language)
        chunked_docs = []
        chunk_index = 0
        for chunk_text in chunks_text:
            if not chunk_text or not chunk_text.strip():
                continue
            chunk_doc = Document(
                content=chunk_text,
                meta={
                    **doc.meta,
                    "chunk_method": "ast_code",
                    "detected_language": language,
                    "chunk_index": chunk_index,
                    "target_size": self.code_chunk_size,
                    "overlap_pct": self.overlap_percentage,
                    "original_doc_id": doc.id
                }
            )
            chunked_docs.append(chunk_doc)
            chunk_index += 1
        return chunked_docs

@component
class ASTCodeChunkerComponent:
    def __init__(self, code_chunk_size: int = 2048, markdown_chunk_size: int = 512, overlap_percentage: float = 0.1):
        self.chunker = ASTCodeChunker(
            code_chunk_size=code_chunk_size,
            markdown_chunk_size=markdown_chunk_size,
            overlap_percentage=overlap_percentage
        )
    @component.output_types(documents=List[Document])
    def run(self, documents: List[Document]) -> Dict[str, List[Document]]:
        all_chunks = []
        for doc in documents:
            chunks = self.chunker.chunk_document(doc)
            all_chunks.extend(chunks)
        return {"documents": all_chunks}

def create_ast_chunker(code_chunk_size: int = 2048, markdown_chunk_size: int = 400) -> ASTCodeChunkerComponent:
    return ASTCodeChunkerComponent(
        code_chunk_size=code_chunk_size,
        markdown_chunk_size=markdown_chunk_size
    )
