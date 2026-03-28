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
=========================================

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
    """
    AST-based code chunker using tree-sitter.

    Intelligently splits code while preserving semantic units like
    functions, classes, and methods.
    """

    def __init__(
        self,
        code_chunk_size: int = 2048,
        markdown_chunk_size: int = 400,
        overlap_percentage: float = 0.1
    ):
        """
        Initialize AST code chunker.

        Args:
            code_chunk_size: Target non-whitespace chars for code (default: 2048)
            markdown_chunk_size: Target words for markdown (default: 400)
            overlap_percentage: Overlap fraction (default: 0.1 = 10%)
        """
        self.code_chunk_size = code_chunk_size
        self.markdown_chunk_size = markdown_chunk_size
        self.overlap_percentage = overlap_percentage

        # Initialize parsers if tree-sitter is available
        self.parsers = {}
        if TREE_SITTER_AVAILABLE:
            self._initialize_parsers()

        # Markdown-aware recursive splitter with logical boundaries
        # Priority: headers → code block ends → JSON ends → paragraphs → sentences
        # Key insight: prioritize ENDINGS (}\n, ```\n) over starts
        markdown_separators = [
            "\n## ",          # H2 headers (new major section)
            "\n### ",         # H3 headers (subsection)
            "\n#### ",        # H4 headers
            "\n```\n\n",      # End of code block + blank line (highest priority for code)
            "\n```\n",        # End of code block
            "}\n\n",          # JSON/code object end + blank line
            "}\n",            # JSON/code object end
            "\n---\n",        # Horizontal rules
            "\n\n",           # Paragraph breaks
            ".\n",            # Sentence ending at line break
            ". ",             # Sentence boundary
            "?\n",            # Question at line break
            "? ",             # Question boundary
            "!\n",            # Exclamation at line break
            "! ",             # Exclamation boundary
            "\n",             # Line breaks (low priority)
        ]
        self.markdown_splitter = RecursiveCharacterTextSplitter(
            chunk_size=3000,        # ~500-600 words
            chunk_overlap=300,      # 10% overlap
            separators=markdown_separators,
            keep_separator='end',   # Keep separator at end of chunk
            is_separator_regex=False
        )

    def _initialize_parsers(self):
        """Initialize tree-sitter parsers for supported languages."""
        try:
            # Python parser
            py_language = Language(tree_sitter_python.language())
            py_parser = Parser(py_language)
            self.parsers['python'] = (py_parser, py_language)

            # JavaScript parser
            js_language = Language(tree_sitter_javascript.language())
            js_parser = Parser(js_language)
            self.parsers['javascript'] = (js_parser, js_language)

            # TypeScript parser
            ts_language = Language(tree_sitter_typescript.language_typescript())
            ts_parser = Parser(ts_language)
            self.parsers['typescript'] = (ts_parser, ts_language)

        except Exception as e:
            print(f"⚠️  Error initializing parsers: {e}")

    def _detect_language(self, doc: Document) -> Optional[str]:
        """
        Detect programming language from document metadata or file extension.

        Args:
            doc: Document to analyze

        Returns:
            Language name or None
        """
        # 1. Check explicit language in metadata (highest priority)
        if "language" in doc.meta:
            return doc.meta["language"]

        # 2. Check content_type from deduplication manifest
        # If marked as "code", assume Python (since SDK is Python)
        if doc.meta.get("content_type") == "code":
            return "python"

        # 3. Check file path extension (fallback)
        if "file_path" in doc.meta:
            ext = Path(doc.meta["file_path"]).suffix.lower()
            ext_map = {
                ".py": "python",
                ".js": "javascript",
                ".jsx": "javascript",
                ".ts": "typescript",
                ".tsx": "typescript",
                ".md": "markdown",
                ".txt": "text"
            }
            return ext_map.get(ext)

        return None

    def _count_non_whitespace(self, text: str) -> int:
        """Count non-whitespace characters in text."""
        return len(re.sub(r'\s', '', text))

    def _chunk_code_with_ast(
        self,
        content: str,
        language: str
    ) -> List[str]:
        """
        Chunk code using AST parsing.

        Args:
            content: Code content
            language: Programming language

        Returns:
            List of code chunks
        """
        if not TREE_SITTER_AVAILABLE or language not in self.parsers:
            # Fallback to simple chunking
            return self._chunk_code_simple(content)

        parser, lang = self.parsers[language]

        try:
            # Parse code into AST
            tree = parser.parse(bytes(content, "utf-8"))
            root_node = tree.root_node

            # Get top-level nodes (functions, classes, etc.)
            chunks = []
            current_chunk = []
            current_size = 0

            for child in root_node.children:
                node_text = content[child.start_byte:child.end_byte]
                node_size = self._count_non_whitespace(node_text)

                # If node alone exceeds chunk size, split it recursively
                if node_size > self.code_chunk_size:
                    # Flush current chunk if any
                    if current_chunk:
                        chunks.append("\n".join(current_chunk))
                        current_chunk = []
                        current_size = 0

                    # Recursively split large node
                    sub_chunks = self._split_large_node(node_text, child, language)
                    chunks.extend(sub_chunks)

                # If adding node would exceed size, flush current chunk
                elif current_size + node_size > self.code_chunk_size:
                    if current_chunk:
                        chunks.append("\n".join(current_chunk))
                    current_chunk = [node_text]
                    current_size = node_size

                # Otherwise, add to current chunk
                else:
                    current_chunk.append(node_text)
                    current_size += node_size

            # Flush remaining
            if current_chunk:
                chunks.append("\n".join(current_chunk))

            return chunks if chunks else [content]

        except Exception as e:
            print(f"⚠️  AST parsing failed: {e}. Using simple chunking.")
            return self._chunk_code_simple(content)

    def _split_large_node(
        self,
        node_text: str,
        node,
        language: str
    ) -> List[str]:
        """
        Recursively split a large AST node.

        Args:
            node_text: Node text content
            node: Tree-sitter node
            language: Programming language

        Returns:
            List of chunks
        """
        # If node has children, split by children
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

        # No children, split by lines as fallback
        return self._chunk_code_simple(node_text)

    def _chunk_code_simple(self, content: str) -> List[str]:
        """
        Simple line-based code chunking fallback.

        Args:
            content: Code content

        Returns:
            List of chunks
        """
        lines = content.split("\n")
        chunks = []
        current_chunk = []
        current_size = 0

        overlap_lines = max(1, int(len(lines) * self.overlap_percentage))

        for line in lines:
            line_size = self._count_non_whitespace(line)

            if current_size + line_size > self.code_chunk_size and current_chunk:
                chunks.append("\n".join(current_chunk))

                # Add overlap
                current_chunk = current_chunk[-overlap_lines:] if overlap_lines else []
                current_size = sum(self._count_non_whitespace(l) for l in current_chunk)

            current_chunk.append(line)
            current_size += line_size

        if current_chunk:
            chunks.append("\n".join(current_chunk))

        return chunks if chunks else [content]

    def chunk_document(self, doc: Document) -> List[Document]:
        """
        Chunk a single document using AST or fallback.

        Args:
            doc: Document to chunk

        Returns:
            List of chunked documents
        """
        language = self._detect_language(doc)

        # Markdown/text: use markdown-aware recursive chunking
        if language in ["markdown", "text", None]:
            # Use LangChain's markdown-aware splitter
            chunks_text = self.markdown_splitter.split_text(doc.content)

            # Convert to Haystack Documents, filter empty chunks
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

        # Code: use AST chunking
        chunks_text = self._chunk_code_with_ast(doc.content, language)

        # Convert to Haystack Documents (filter empty chunks)
        chunked_docs = []
        chunk_index = 0
        for chunk_text in chunks_text:
            # Skip empty or whitespace-only chunks
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
    """Haystack component wrapper for AST code chunker."""

    def __init__(
        self,
        code_chunk_size: int = 2048,
        markdown_chunk_size: int = 512,
        overlap_percentage: float = 0.1
    ):
        """
        Initialize AST code chunker component.

        Args:
            code_chunk_size: Target non-whitespace chars for code
            markdown_chunk_size: Target words for markdown
            overlap_percentage: Overlap fraction
        """
        self.chunker = ASTCodeChunker(
            code_chunk_size=code_chunk_size,
            markdown_chunk_size=markdown_chunk_size,
            overlap_percentage=overlap_percentage
        )

    @component.output_types(documents=List[Document])
    def run(self, documents: List[Document]) -> Dict[str, List[Document]]:
        """
        Chunk documents using AST-based approach.

        Args:
            documents: List of documents to chunk

        Returns:
            Dictionary with "documents" key containing chunked documents
        """
        all_chunks = []

        for doc in documents:
            chunks = self.chunker.chunk_document(doc)
            all_chunks.extend(chunks)

        return {"documents": all_chunks}


def create_ast_chunker(
    code_chunk_size: int = 2048,
    markdown_chunk_size: int = 400
) -> ASTCodeChunkerComponent:
    """
    Factory function to create AST code chunker.

    Args:
        code_chunk_size: Target size for code chunks
        markdown_chunk_size: Target size for markdown chunks

    Returns:
        Configured ASTCodeChunkerComponent
    """
    return ASTCodeChunkerComponent(
        code_chunk_size=code_chunk_size,
        markdown_chunk_size=markdown_chunk_size
    )


if __name__ == "__main__":
    """Test AST code chunker with sample code."""

    # Sample Python code
    sample_code = '''
def hello_world():
    """A simple function."""
    print("Hello, world!")

class MCP:
    """Model Context Protocol implementation."""

    def __init__(self, name: str):
        self.name = name

    def connect(self):
        """Connect to server."""
        return f"Connected to {self.name}"

    def disconnect(self):
        """Disconnect from server."""
        return f"Disconnected from {self.name}"
'''

    sample_doc = Document(
        content=sample_code,
        meta={"file_path": "test.py", "language": "python"}
    )

    print(f"{'='*60}")
    print(f"Testing AST Code Chunker")
    print(f"{'='*60}")

    chunker = ASTCodeChunkerComponent(code_chunk_size=100)  # Small size for testing
    result = chunker.run(documents=[sample_doc])

    chunks = result["documents"]
    print(f"\nOriginal code: {len(sample_code)} characters")
    print(f"Number of AST chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i+1} ---")
        print(f"Method: {chunk.meta.get('chunk_method')}")
        print(f"Language: {chunk.meta.get('detected_language')}")
        print(f"Length: {len(chunk.content)} chars")
        print(f"Preview:\n{chunk.content[:150]}...")
