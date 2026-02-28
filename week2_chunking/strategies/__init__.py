# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 2: Chunking Strategies
============================

Seven chunking strategies for RAG experiments:

Naive (fixed-size word-based):
- naive_small: 200 words, 25 overlap
- naive_medium: 400 words, 50 overlap
- naive_large: 800 words, 100 overlap

Boundary-aware:
- sentence: 6 sentences, 2 sentence overlap
- recursive: 2000 chars, 200 overlap (hierarchical)

Content-aware:
- semantic: Adaptive size based on semantic similarity
- ast_code: AST parsing for code, word-based for markdown
"""

from .naive_chunker import NaiveChunker
from .logical_chunker import SentenceChunker, RecursiveChunker
from .semantic_chunker import SemanticChunkerComponent
from .ast_code_chunker import ASTCodeChunkerComponent
from .metadata_enricher import MetadataEnricher

__all__ = [
    "NaiveChunker",
    "SentenceChunker",
    "RecursiveChunker",
    "SemanticChunkerComponent",
    "ASTCodeChunkerComponent",
    "MetadataEnricher",
]
