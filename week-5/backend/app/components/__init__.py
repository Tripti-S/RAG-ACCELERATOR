# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Production Haystack Components
=======================================

Self-contained retrieval components for production RAG.

These are adapted from Week 3's proven components, copied here so
Week 5 has zero import dependencies on earlier weeks. In production,
your service must be self-contained — no fragile cross-module imports.

Components:
- QdrantHybridRetriever: Dense + Sparse + RRF fusion (fixes Haystack prefetch bug)
- VoyageReranker: Voyage AI rerank-2.5 with graceful fallback

Production decision: We use Hybrid + Voyage Reranking (Technique 1b from Week 3),
NOT Two-Stage LLM routing. Two-stage was only marginally better in quality but
2.2x slower and more expensive. In production, cost-accuracy-latency tradeoff wins.
"""

from .qdrant_hybrid_retriever import QdrantHybridRetriever
from .voyage_reranker import VoyageReranker

__all__ = [
    "QdrantHybridRetriever",
    "VoyageReranker",
]
