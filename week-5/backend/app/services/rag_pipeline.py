# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Production RAG Pipeline Service
========================================

Production-grade RAG pipeline using Hybrid + Voyage Reranking (Week 3 Technique 1b).

Production decision:
- Two-stage LLM routing won Week 3 evaluation (marginally).
- But Hybrid + Voyage reranking is 2.2x faster and cheaper with ~85-90% of the quality.
- In production, you pick the best cost-accuracy-latency tradeoff. That's this.

Architecture (split pipeline):
- Retrieval Pipeline: VoyageTextEmbedder + SparseEmbedder -> QdrantHybridRetriever -> VoyageReranker
- Generation: Direct GoogleGenAIChatGenerator call with dynamically selected prompt template

Why split (not one connected pipeline)?
- Retrieval is fixed for all queries; prompt template changes per query type (from query_router)
- We need intermediate outputs (retrieved contexts) for caching, feedback, and observability
- Connected pipelines don't expose intermediate outputs cleanly
- Split is what production systems actually do — composable services

Stack:
- Dense embeddings: Voyage-4-lite (2048d) — MUST match week3_hybrid_recursive index
- Sparse embeddings: BM25 via FastEmbed — MUST match week3_hybrid_recursive index
- Retriever: Custom QdrantHybridRetriever (fixes Haystack prefetch bug)
- Reranker: Voyage rerank-2.5
- Generator: Google Gemini 2.5 Flash
- Collection: week3_hybrid_recursive

Usage:
    from app.services.rag_pipeline import get_rag_pipeline

    pipeline = get_rag_pipeline()
    result = await pipeline.retrieve(query)
    answer = await pipeline.generate(query, result.contexts, prompt_template)
"""

import os
import time
import asyncio
import contextvars
from contextlib import nullcontext
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field

# Enable Haystack content tracing for Opik (if OPIK_API_KEY is set)
os.environ["HAYSTACK_CONTENT_TRACING_ENABLED"] = "true"

from haystack import Pipeline, Document
from haystack.dataclasses import ChatMessage

# Opik tracing (optional — no-op decorator if not installed)
try:
    import opik
    _opik_track = opik.track
except ImportError:
    def _opik_track(**kwargs):
        def _noop(func):
            return func
        return _noop

# Dense embedder: Voyage (2048d) — matches week3_hybrid_recursive collection
from haystack_integrations.components.embedders.voyage_embedders import VoyageTextEmbedder

# Sparse embedder: BM25 — matches week3_hybrid_recursive collection
from haystack_integrations.components.embedders.fastembed import FastembedSparseTextEmbedder

# Generator: Gemini
from haystack_integrations.components.generators.google_genai import GoogleGenAIChatGenerator

# Local components (self-contained — no imports from week 3)
from app.components import QdrantHybridRetriever, VoyageReranker

# Opik integration (optional — only if API key is set)
try:
    import opik
    from opik import opik_context
    from opik.integrations.haystack import OpikConnector
    OPIK_AVAILABLE = True
except ImportError:
    OPIK_AVAILABLE = False


# ---------------------------------------------------------------------------
# Result dataclasses
# ---------------------------------------------------------------------------

@dataclass
class RetrievalResult:
    """Structured result from the retrieval pipeline."""
    contexts: List[Document]
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class RAGResult:
    """Structured result from the full RAG pipeline (retrieval + generation)."""
    answer: str
    contexts: List[Dict[str, Any]]
    metadata: Dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Production RAG Pipeline
# ---------------------------------------------------------------------------

class ProductionRAGPipeline:
    """
    Production-grade Hybrid + Voyage Reranking RAG pipeline.

    Singleton pattern: initialize once, reuse for all requests.

    Split architecture:
    - retrieve(): runs the Haystack retrieval pipeline, returns contexts
    - generate(): calls the LLM with contexts + prompt template, returns answer
    - query(): convenience method that runs both (retrieve → generate)
    """

    _instance = None
    _initialized = False

    def __new__(cls):
        """Singleton — only one pipeline instance across all requests."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize pipeline components. Called once."""
        if self._initialized:
            return

        print("\n" + "=" * 70)
        print("INITIALIZING PRODUCTION RAG PIPELINE")
        print("=" * 70)

        self._init_config()
        self._init_retrieval_pipeline()
        self._init_generator()

        self._initialized = True
        print("\n" + "=" * 70)
        print("PRODUCTION RAG PIPELINE READY")
        print("=" * 70)

    # -------------------------------------------------------------------
    # Initialization
    # -------------------------------------------------------------------

    def _init_config(self):
        """Load configuration from environment."""
        self.collection_name = os.getenv("QDRANT_COLLECTION", "week3_hybrid_recursive")
        self.qdrant_url = os.getenv("QDRANT_URL")
        self.qdrant_api_key = os.getenv("QDRANT_API_KEY")
        self.voyage_api_key = os.getenv("VOYAGE_API_KEY")
        self.gemini_model = os.getenv("LLM_MODEL", "gemini-2.5-flash")
        self.fallback_model = os.getenv("LLM_FALLBACK_MODEL", "gemini-2.5-flash-lite")

        # Voyage dense embeddings — MUST match the index
        self.dense_model = os.getenv("VOYAGE_EMBED_MODEL", "voyage-4-lite")
        self.dense_dimension = int(os.getenv("VOYAGE_DIMENSION", "2048"))

        # Sparse embeddings — BM25 via FastEmbed
        self.sparse_model = os.getenv("SPARSE_MODEL", "Qdrant/bm25")

        # Retrieval config
        self.prefetch_k = 50       # After RRF fusion
        self.dense_prefetch = 100  # Dense vector prefetch
        self.sparse_prefetch = 100  # Sparse vector prefetch
        self.rerank_k = 10         # After Voyage reranking

        # Opik config
        self.opik_api_key = os.getenv("OPIK_API_KEY")
        self.opik_workspace = os.getenv("OPIK_WORKSPACE", "default")
        self.opik_project = os.getenv("OPIK_PROJECT_NAME", "rag-accelerator-prod")

        # Validate required vars
        required = {
            "QDRANT_URL": self.qdrant_url,
            "QDRANT_API_KEY": self.qdrant_api_key,
            "VOYAGE_API_KEY": self.voyage_api_key,
            "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY"),
        }
        missing = [k for k, v in required.items() if not v]
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")

        print(f"\n   Configuration:")
        print(f"   Collection: {self.collection_name}")
        print(f"   Dense Model: {self.dense_model} ({self.dense_dimension}d)")
        print(f"   Sparse Model: {self.sparse_model}")
        print(f"   Reranker: Voyage rerank-2.5")
        print(f"   Generator: {self.gemini_model}")
        print(f"   Pipeline: Dense({self.dense_prefetch}) + Sparse({self.sparse_prefetch}) -> RRF({self.prefetch_k}) -> Rerank({self.rerank_k})")

    def _init_retrieval_pipeline(self):
        """
        Build the Haystack retrieval pipeline.

        Pipeline:
            VoyageTextEmbedder -> QdrantHybridRetriever -> VoyageReranker
            (+ FastembedSparseTextEmbedder feeding into retriever)

        This pipeline handles embedding, search, and reranking.
        Generation is handled separately for prompt template flexibility.
        """
        print("\n   Building retrieval pipeline...")

        # Configure Opik if available
        opik_enabled = False
        if OPIK_AVAILABLE and self.opik_api_key:
            try:
                opik.configure(
                    api_key=self.opik_api_key,
                    workspace=self.opik_workspace
                )
                opik_enabled = True
                print(f"   Opik tracing enabled (workspace: {self.opik_workspace})")
            except Exception as e:
                print(f"   Opik configuration failed: {e}")

        self.retrieval_pipeline = Pipeline()

        # Add Opik tracer if enabled
        if opik_enabled:
            self.retrieval_pipeline.add_component(
                "opik_tracer", OpikConnector(self.opik_project)
            )

        # Dense embedder: Voyage (matches week3_hybrid_recursive collection)
        dense_embedder = VoyageTextEmbedder(
            model=self.dense_model,
            output_dimension=self.dense_dimension
        )
        self.retrieval_pipeline.add_component("dense_embedder", dense_embedder)
        print(f"   + Dense Embedder: {self.dense_model}")

        # Sparse embedder: BM25 (matches week3_hybrid_recursive collection)
        sparse_embedder = FastembedSparseTextEmbedder(model=self.sparse_model)
        self.retrieval_pipeline.add_component("sparse_embedder", sparse_embedder)
        print(f"   + Sparse Embedder: {self.sparse_model}")

        # Hybrid retriever with explicit prefetch limits
        retriever = QdrantHybridRetriever(
            url=self.qdrant_url,
            api_key=self.qdrant_api_key,
            collection_name=self.collection_name,
            top_k=self.prefetch_k,
            dense_prefetch_limit=self.dense_prefetch,
            sparse_prefetch_limit=self.sparse_prefetch
        )
        self.retrieval_pipeline.add_component("retriever", retriever)
        print(f"   + Hybrid Retriever: {self.collection_name}")

        # Voyage reranker
        reranker = VoyageReranker(
            model="rerank-2.5",
            top_k=self.rerank_k,
            api_key=self.voyage_api_key
        )
        self.retrieval_pipeline.add_component("reranker", reranker)
        print(f"   + Voyage Reranker: rerank-2.5 (top {self.rerank_k})")

        # Connect: embedders -> retriever -> reranker
        self.retrieval_pipeline.connect("dense_embedder.embedding", "retriever.query_embedding")
        self.retrieval_pipeline.connect("sparse_embedder.sparse_embedding", "retriever.query_sparse_embedding")
        self.retrieval_pipeline.connect("retriever.documents", "reranker.documents")

        # Warm up components that have local models to load
        print("\n   Warming up components...")
        for name, component in [("sparse_embedder", sparse_embedder), ("retriever", retriever), ("reranker", reranker), ("dense_embedder", dense_embedder)]:
            if hasattr(component, "warm_up"):
                component.warm_up()
                print(f"   Warmed up: {name}")
        print("   All components ready")

    def _init_generator(self):
        """Initialize primary and fallback LLM generators."""
        self.generator = GoogleGenAIChatGenerator(model=self.gemini_model)
        self.fallback_generator = GoogleGenAIChatGenerator(model=self.fallback_model)
        print(f"\n   Generator ready: {self.gemini_model} (fallback: {self.fallback_model})")

    # -------------------------------------------------------------------
    # Error classification helpers
    # -------------------------------------------------------------------

    @staticmethod
    def _is_rate_limit_error(error: Exception) -> bool:
        """Check if error is a 429 rate limit / quota exhaustion."""
        err = str(error).lower()
        return "429" in err or "rate limit" in err or "resource exhausted" in err or "quota" in err

    @staticmethod
    def _is_server_error(error: Exception) -> bool:
        """Check if error is a 503 / server overloaded."""
        err = str(error).lower()
        return "503" in err or "service unavailable" in err or "overloaded" in err

    # -------------------------------------------------------------------
    # Retrieval
    # -------------------------------------------------------------------

    async def retrieve(self, query: str, max_retries: int = 3) -> RetrievalResult:
        """
        Run the retrieval pipeline: embed → hybrid search → rerank.

        Uses start_as_current_span (not @opik.track) so that:
        1. The "retrieve" span nests under the caller's parent trace
        2. copy_context() inside the with block captures the span, so
           Haystack's OpikConnector nests sub-components under "retrieve"

        Args:
            query: User's search query (should be standalone — rewritten if follow-up)
            max_retries: Retry attempts on transient failures

        Returns:
            RetrievalResult with reranked Document objects and timing metadata
        """
        start_time = time.time()

        for attempt in range(max_retries):
            try:
                # start_as_current_span pushes "retrieve" onto the ContextVar stack.
                # copy_context() inside captures it, so OpikConnector nests under it.
                # nullcontext(None) when Opik is not installed — no-op.
                span_ctx = opik.start_as_current_span("retrieve") if OPIK_AVAILABLE else nullcontext(None)
                with span_ctx as span_data:
                    if span_data is not None:
                        span_data.input = {"query": query}

                    # copy_context INSIDE the with block so the snapshot includes "retrieve"
                    ctx = contextvars.copy_context()
                    loop = asyncio.get_running_loop()
                    result = await loop.run_in_executor(
                        None,
                        lambda: ctx.run(
                            self.retrieval_pipeline.run,
                            data={
                                "dense_embedder": {"text": query},
                                "sparse_embedder": {"text": query},
                                "reranker": {"query": query},
                            }
                        )
                    )

                    contexts = result["reranker"]["documents"]
                    elapsed = time.time() - start_time

                    if span_data is not None:
                        span_data.output = {
                            "num_contexts": len(contexts),
                            "retrieval_time_seconds": round(elapsed, 3),
                        }

                    return RetrievalResult(
                        contexts=contexts,
                        metadata={
                            "retrieval_time_seconds": round(elapsed, 3),
                            "num_contexts": len(contexts),
                            "attempt": attempt + 1,
                        }
                    )

            except Exception as e:
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) + 1
                    print(f"   Retrieval failed (attempt {attempt + 1}/{max_retries}): {str(e)[:100]}")
                    print(f"   Retrying in {wait_time}s...")
                    await asyncio.sleep(wait_time)
                else:
                    raise RuntimeError(
                        f"Retrieval failed after {max_retries} attempts: {str(e)}"
                    )

    # -------------------------------------------------------------------
    # Generation
    # -------------------------------------------------------------------

    @_opik_track(name="generate")
    async def generate(
        self,
        query: str,
        contexts: List[Document],
        prompt_messages: List[ChatMessage],
    ) -> str:
        """
        Generate an answer using the LLM with provided contexts and prompt.

        Retry + fallback strategy:
        - 503 (server error): retry once with same model, then fallback
        - 429 (rate limit): skip retry, fallback immediately
        - Other errors: raise immediately

        Args:
            query: Original user query (for logging/tracing)
            contexts: Retrieved documents from retrieve()
            prompt_messages: Pre-built ChatMessage list from query_router

        Returns:
            Generated answer string
        """
        start_time = time.time()
        loop = asyncio.get_running_loop()
        original_error = None

        # Try primary model (up to 2 attempts for 503)
        for attempt in range(2):
            try:
                result = await loop.run_in_executor(
                    None,
                    lambda: self.generator.run(messages=prompt_messages)
                )
                answer = result["replies"][0].text
                elapsed = time.time() - start_time
                print(f"   Generation complete ({elapsed:.2f}s, {len(answer)} chars)")
                return answer

            except Exception as e:
                original_error = e
                if self._is_rate_limit_error(e):
                    print(f"   Rate limited on {self.gemini_model}, falling back to {self.fallback_model}")
                    break  # Go to fallback immediately
                elif self._is_server_error(e) and attempt == 0:
                    print(f"   Server error (503) on {self.gemini_model}, retrying in 2s...")
                    await asyncio.sleep(2)
                    continue  # Retry once
                elif self._is_server_error(e) and attempt == 1:
                    print(f"   Server error persists, falling back to {self.fallback_model}")
                    break  # Go to fallback
                else:
                    raise  # Unknown error — don't mask it

        # Fallback to lite model
        try:
            result = await loop.run_in_executor(
                None,
                lambda: self.fallback_generator.run(messages=prompt_messages)
            )
            answer = result["replies"][0].text
            elapsed = time.time() - start_time
            print(f"   Generation complete via fallback {self.fallback_model} ({elapsed:.2f}s, {len(answer)} chars)")

            # Log recoverable error metadata to Opik span
            if OPIK_AVAILABLE:
                try:
                    opik_context.update_current_span(metadata={
                        "fallback_used": True,
                        "fallback_model": self.fallback_model,
                        "original_error": str(original_error),
                    })
                except Exception:
                    pass

            return answer
        except Exception as e:
            raise RuntimeError(
                f"Generation failed on both {self.gemini_model} and {self.fallback_model}: {e}"
            )

    # -------------------------------------------------------------------
    # Streaming Generation
    # -------------------------------------------------------------------

    async def generate_stream(
        self,
        query: str,
        contexts: List[Document],
        prompt_messages: List[ChatMessage],
    ) -> asyncio.Queue:
        """
        Stream tokens from the LLM via an asyncio.Queue.

        Uses GoogleGenAIChatGenerator.run_async() with a per-request
        streaming_callback that pushes each token to the queue.
        None is pushed when generation completes.

        Retry + fallback (same strategy as generate()):
        - 503: retry once with primary, then fallback to lite
        - 429: fallback to lite immediately

        Args:
            query: Original user query (for logging)
            contexts: Retrieved documents
            prompt_messages: Pre-built ChatMessage list from query_router

        Returns:
            asyncio.Queue that yields token strings, then None on completion.
            The full answer string is stored as queue.full_answer after None.
        """
        token_queue: asyncio.Queue = asyncio.Queue()
        token_queue.stream_error = None
        token_queue.fallback_used = False
        token_queue.fallback_metadata = None

        async def _callback(chunk) -> None:
            if chunk.content:
                await token_queue.put(chunk.content)

        async def _run():
            try:
                original_error = None

                # Try primary model (up to 2 attempts for 503)
                for attempt in range(2):
                    try:
                        result = await self.generator.run_async(
                            messages=prompt_messages,
                            streaming_callback=_callback,
                        )
                        token_queue.full_answer = result["replies"][0].text
                        await token_queue.put(None)
                        return
                    except Exception as e:
                        original_error = e
                        if self._is_rate_limit_error(e):
                            print(f"   Stream rate limited on {self.gemini_model}, falling back to {self.fallback_model}")
                            break
                        elif self._is_server_error(e) and attempt == 0:
                            print(f"   Stream server error (503) on {self.gemini_model}, retrying in 2s...")
                            await asyncio.sleep(2)
                            continue
                        elif self._is_server_error(e) and attempt == 1:
                            print(f"   Stream server error persists, falling back to {self.fallback_model}")
                            break
                        else:
                            raise

                # Fallback to lite model
                result = await self.fallback_generator.run_async(
                    messages=prompt_messages,
                    streaming_callback=_callback,
                )
                token_queue.full_answer = result["replies"][0].text
                token_queue.fallback_used = True
                token_queue.fallback_metadata = {
                    "fallback_model": self.fallback_model,
                    "original_error": str(original_error),
                }
                await token_queue.put(None)

            except Exception as e:
                token_queue.full_answer = ""
                token_queue.stream_error = e
                await token_queue.put(None)

        # Launch generation as a background task
        asyncio.create_task(_run())
        return token_queue

    # -------------------------------------------------------------------
    # Convenience: full query (retrieve + generate)
    # -------------------------------------------------------------------

    async def query(
        self,
        query: str,
        prompt_messages: List[ChatMessage],
        max_retries: int = 3
    ) -> RAGResult:
        """
        Run the full RAG pipeline: retrieve contexts, then generate answer.

        This is the main entry point for the FastAPI backend. It returns
        structured results compatible with semantic caching and feedback.

        Args:
            query: User's query (should be standalone — rewritten if follow-up)
            prompt_messages: Pre-built ChatMessage list from query_router
            max_retries: Retry attempts per stage

        Returns:
            RAGResult with answer, formatted contexts, and metadata
        """
        total_start = time.time()

        # Stage 1: Retrieve
        retrieval_result = await self.retrieve(query, max_retries=max_retries)

        # Stage 2: Generate
        answer = await self.generate(
            query=query,
            contexts=retrieval_result.contexts,
            prompt_messages=prompt_messages,
            max_retries=max_retries
        )

        # Format contexts for response (serializable)
        formatted_contexts = []
        for rank, doc in enumerate(retrieval_result.contexts, 1):
            formatted_contexts.append({
                "rank": rank,
                "score": round(doc.score, 4) if doc.score else 0.0,
                "content": doc.content,
                "metadata": {
                    "file_path": doc.meta.get("file_path", "unknown"),
                    "category": doc.meta.get("category", "unknown"),
                    "file_type": doc.meta.get("file_type", "unknown"),
                }
            })

        total_time = time.time() - total_start

        return RAGResult(
            answer=answer,
            contexts=formatted_contexts,
            metadata={
                "total_time_seconds": round(total_time, 3),
                "retrieval_time_seconds": retrieval_result.metadata.get("retrieval_time_seconds", 0),
                "generation_time_seconds": round(total_time - retrieval_result.metadata.get("retrieval_time_seconds", 0), 3),
                "num_contexts": len(formatted_contexts),
                "collection": self.collection_name,
                "dense_model": self.dense_model,
                "reranker_model": "voyage-rerank-2.5",
                "generator_model": self.gemini_model,
            }
        )

    # -------------------------------------------------------------------
    # Health check
    # -------------------------------------------------------------------

    def is_healthy(self) -> bool:
        """Check if the pipeline is initialized and components are ready."""
        return self._initialized


# ---------------------------------------------------------------------------
# Singleton accessor
# ---------------------------------------------------------------------------

_rag_pipeline: Optional[ProductionRAGPipeline] = None


def get_rag_pipeline() -> ProductionRAGPipeline:
    """
    Get or create the global RAG pipeline instance.

    Singleton ensures we initialize expensive components (embedding models,
    Qdrant client, Voyage client) exactly once across all requests.
    """
    global _rag_pipeline
    if _rag_pipeline is None:
        _rag_pipeline = ProductionRAGPipeline()
    return _rag_pipeline
