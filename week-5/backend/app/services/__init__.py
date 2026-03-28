# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Production Backend Services
=====================================

Service layer for the production RAG system.

All services are singletons — initialized once at startup, reused across requests.
Each service manages its own connections (Redis, Qdrant, API clients).

Services:
- rag_pipeline: Hybrid + Voyage Reranking retrieval + LLM generation
- semantic_cache: Redis HNSW vector cache for sub-50ms repeated query responses
- conversation: Redis-backed sliding window memory + conditional query rewriting
- query_router: Query classification + type-specific prompt templates
- feedback: User feedback logged to Opik traces via /feedback endpoint
"""

from .rag_pipeline import get_rag_pipeline, ProductionRAGPipeline
from .semantic_cache import get_semantic_cache, SemanticCache
from .conversation import get_conversation_service, ConversationService
from .query_router import get_query_router, QueryRouter

__all__ = [
    "get_rag_pipeline",
    "ProductionRAGPipeline",
    "get_semantic_cache",
    "SemanticCache",
    "get_conversation_service",
    "ConversationService",
    "get_query_router",
    "QueryRouter",
]
