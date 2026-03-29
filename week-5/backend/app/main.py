# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Production FastAPI Backend
====================================

REST API for the production RAG system. Wires all services together:

Request flow (POST /query):
    1. Session handling (use provided session_id or generate new)
    2. Conversation memory: rewrite follow-ups into standalone queries
    3. Semantic cache check (sub-50ms on hit)
    4. Query classification: determine query type (FACTUAL, HOW_TO, etc.)
    5. Retrieval: Dense + Sparse + RRF + Voyage Reranking
    6. Prompt building: type-specific template + retrieved contexts
    7. Generation: Gemini Flash with specialized prompt
    8. Cache the result for future queries
    9. Store messages in conversation history
   10. Return structured response with msg_id for feedback

Endpoints:
    POST /query           — Full RAG pipeline with memory + routing + cache
    POST /query/stream    — SSE streaming version of /query
    POST /feedback        — Store user feedback (thumbs up/down)
    GET  /conversation/{session_id} — Conversation history
    GET  /health          — Service health check
    GET  /metrics         — Cache stats, latency, feedback summary
"""

import os
import re
import time
import json
import asyncio
import uuid
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse

# Opik tracing (optional — only if API key is set)
try:
    import opik
    from opik import opik_context
    OPIK_AVAILABLE = True
except ImportError:
    OPIK_AVAILABLE = False


def _set_thread_id(thread_id: str):
    """Set thread_id on the current Opik trace for conversation grouping."""
    if OPIK_AVAILABLE:
        try:
            opik_context.update_current_trace(thread_id=thread_id)
        except Exception:
            pass


# Cache for streaming eval re-trigger (lazy-loaded on first call)
_eval_config_cache = None


def _trigger_eval(client, trace_id: str):
    """
    Manually trigger online evaluation rules on a trace.

    Auto-trigger is disabled (sampling_rate=0) so evaluation only runs when
    we explicitly call this — after the trace output contains the actual answer.
    This avoids wasted evals on empty streaming outputs and ensures every trace
    (streaming and non-streaming) gets evaluated exactly once.

    Caches project_id and rule_ids on first call (one-time REST lookup).
    """
    global _eval_config_cache
    try:
        if _eval_config_cache is None:
            project = client.rest_client.projects.retrieve_project(
                name=client.project_name
            )
            rules = client.rest_client.automation_rule_evaluators.find_evaluators(
                project_id=project.id
            )
            rule_ids = [r.id for r in rules.content] if rules.content else []
            _eval_config_cache = {"project_id": project.id, "rule_ids": rule_ids}

        if not _eval_config_cache["rule_ids"]:
            return

        client.rest_client.manual_evaluation.evaluate_traces(
            project_id=_eval_config_cache["project_id"],
            entity_ids=[trace_id],
            rule_ids=_eval_config_cache["rule_ids"],
            entity_type="trace",
        )
    except Exception:
        pass


from .config import settings
from .models import (
    QueryRequest,
    QueryResponse,
    ContextItem,
    FeedbackRequest,
    FeedbackResponse,
    ConversationResponse,
    ConversationMessage,
    HealthResponse,
    MetricsResponse,
)
from .services import (
    get_rag_pipeline,
    get_semantic_cache,
    get_conversation_service,
    get_query_router,
)


class _NoopRagPipeline:
    """Fallback pipeline used when core RAG initialization fails."""

    async def retrieve(self, *args, **kwargs):
        raise RuntimeError("RAG pipeline unavailable")

    async def generate(self, *args, **kwargs):
        raise RuntimeError("RAG pipeline unavailable")

    async def generate_stream(self, *args, **kwargs):
        raise RuntimeError("RAG pipeline unavailable")

    def is_healthy(self) -> bool:
        return False


class _NoopQueryRouter:
    """Fallback router used when query router initialization fails."""

    async def classify(self, *args, **kwargs):
        raise RuntimeError("Query router unavailable")

    def build_prompt(self, *args, **kwargs):
        raise RuntimeError("Query router unavailable")

    def is_healthy(self) -> bool:
        return False


class _NoopSemanticCache:
    """Fallback cache service used when Redis cache initialization fails."""

    def get(self, query: str):
        return None

    def set(self, query: str, answer: str, contexts):
        return None

    def get_stats(self):
        return {
            "cache_hits": 0,
            "cache_misses": 0,
            "total_queries": 0,
            "hit_rate_percent": 0.0,
            "num_cached_entries": 0,
            "distance_threshold": None,
            "degraded_mode": True,
        }

    def is_healthy(self) -> bool:
        return False


class _NoopConversationService:
    """Fallback conversation service used when Redis conversation initialization fails."""

    @staticmethod
    def create_session_id() -> str:
        return f"sess_{uuid.uuid4().hex}"

    async def rewrite_if_needed(self, query: str, session_id: str):
        return {
            "original_query": query,
            "standalone_query": query,
            "is_follow_up": False,
            "history_length": 0,
            "degraded_mode": True,
        }

    def add_message(self, session_id: str, role: str, content: str, metadata=None) -> str:
        return f"msg_{uuid.uuid4().hex[:12]}"

    def get_history(self, session_id: str):
        return []

    def get_session_info(self, session_id: str):
        return {
            "session_id": session_id,
            "degraded_mode": True,
            "storage": "disabled",
        }

    def is_healthy(self) -> bool:
        return False


def _is_degraded_mode() -> bool:
    """Return True when one or more Redis-backed services are using no-op fallback."""
    return (
        isinstance(app.state.pipeline, _NoopRagPipeline)
        or isinstance(app.state.router, _NoopQueryRouter)
        or isinstance(app.state.cache, _NoopSemanticCache)
        or isinstance(app.state.conversation, _NoopConversationService)
    )


# ---------------------------------------------------------------------------
# Lifespan: startup and shutdown
# ---------------------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Initialize all services at startup. Cleanup at shutdown.

    Heavy components (embedding models, Redis connections, Qdrant clients)
    are initialized once here and reused for all requests via singletons.
    """
    print("\n" + "=" * 70)
    print("STARTING PRODUCTION RAG API")
    print("=" * 70)

    # Initialize critical services first (with degraded fallback)
    try:
        app.state.pipeline = get_rag_pipeline()
    except Exception as e:
        print(f"   Warning: RAG pipeline unavailable, running in degraded mode ({str(e)[:120]})")
        app.state.pipeline = _NoopRagPipeline()

    try:
        app.state.router = get_query_router()
    except Exception as e:
        print(f"   Warning: query router unavailable, running in degraded mode ({str(e)[:120]})")
        app.state.router = _NoopQueryRouter()

    # Initialize Redis-backed services with degraded-mode fallback
    try:
        app.state.cache = get_semantic_cache()
    except Exception as e:
        print(f"   Warning: semantic cache unavailable, running without cache ({str(e)[:120]})")
        app.state.cache = _NoopSemanticCache()

    try:
        app.state.conversation = get_conversation_service()
    except Exception as e:
        print(f"   Warning: conversation memory unavailable, running without memory ({str(e)[:120]})")
        app.state.conversation = _NoopConversationService()

    # Request-level metrics (reset on restart)
    app.state.request_count = 0
    app.state.total_latency_ms = 0.0
    app.state.total_cost_usd = 0.0
    app.state.feedback_events = {}

    print("\n" + "=" * 70)
    print("PRODUCTION RAG API READY")
    print("=" * 70)

    yield

    # Flush pending Opik traces before shutdown
    if OPIK_AVAILABLE:
        try:
            opik.flush_tracker()
        except Exception:
            pass
    print("\n   Shutting down Production RAG API...")


# ---------------------------------------------------------------------------
# FastAPI app
# ---------------------------------------------------------------------------

app = FastAPI(
    title=settings.APP_NAME,
    description="ProbablAI: Production RAG system for probability and statistics learning, with conversation memory, query routing, semantic cache, and feedback",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS for Streamlit frontend
# Allow Railway public domains, localhost (dev), and any configured frontend origin
_extra_origins = [o.strip() for o in os.environ.get("ALLOWED_ORIGINS", "").split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",
        "http://localhost:3000",
        "http://127.0.0.1:8501",
        "http://127.0.0.1:3000",
    ] + _extra_origins,
    allow_origin_regex=r"https://.*\.railway\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Error handlers
# ---------------------------------------------------------------------------

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Structured JSON error for HTTP exceptions."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "status_code": exc.status_code},
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Structured JSON error for unexpected exceptions."""
    print(f"   Unexpected error on {request.url.path}: {exc}")
    import traceback
    traceback.print_exc()

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc) if settings.DEBUG else "An unexpected error occurred",
            "status_code": 500,
        },
    )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _estimate_cost(cache_hit: bool, num_llm_calls: int = 1) -> float:
    """
    Estimate cost per query for the metrics dashboard.

    Rough estimates for our stack:
    - Voyage embedding: ~$0.0001 per query
    - Voyage reranking: ~$0.0005 per 10 docs
    - Gemini Flash: ~$0.002-0.005 per call
    - Cache hit: $0.00 (FastEmbed is local, Redis is pre-paid)
    """
    if cache_hit:
        return 0.0

    voyage_embed = 0.0001
    voyage_rerank = 0.0005
    gemini_per_call = 0.003
    return round(voyage_embed + voyage_rerank + (gemini_per_call * num_llm_calls), 6)


def _stream_text_chunks(text: str, chunk_size: int = 3):
    """
    Split text into word chunks while preserving markdown whitespace.

    Used for simulated streaming of non-streaming LLM output.
    Real token streaming requires GoogleGenAIChatGenerator streaming_callback,
    which is a future enhancement.

    Args:
        text: Text to chunk
        chunk_size: Words per chunk (3 for smooth streaming feel)

    Yields:
        Text chunks with preserved whitespace and structure
    """
    parts = re.split(r'(\s+)', text)
    current_chunk = []
    word_count = 0

    for part in parts:
        current_chunk.append(part)
        if part.strip():
            word_count += 1
            if word_count >= chunk_size:
                yield ''.join(current_chunk)
                current_chunk = []
                word_count = 0

    if current_chunk:
        yield ''.join(current_chunk)


# ---------------------------------------------------------------------------
# Traced pipeline logic (Opik parent trace — child spans nest under this)
# ---------------------------------------------------------------------------

async def _run_query_pipeline_inner(
    query_text: str, session_id: str, use_cache: bool, start_time: float
) -> QueryResponse:
    """
    Core RAG pipeline logic. Decorated with @opik.track at module level
    so all nested @opik.track calls (retrieve, classify, generate, rewrite)
    become child spans under this parent trace.
    """
    # Set thread_id for conversation grouping in Opik
    _set_thread_id(session_id)

    # Capture Opik trace ID for feedback linking
    opik_trace_id = None
    if OPIK_AVAILABLE:
        try:
            trace_data = opik_context.get_current_trace_data()
            if trace_data:
                opik_trace_id = trace_data.id
        except Exception:
            pass

    # Step 1: Rewrite if follow-up (conditional — skips LLM on first turn)
    rewrite_result = await app.state.conversation.rewrite_if_needed(
        query_text, session_id
    )
    standalone_query = rewrite_result["standalone_query"]
    is_follow_up = rewrite_result["is_follow_up"]

    # Step 2: Check semantic cache
    cached = app.state.cache.get(standalone_query) if use_cache else None

    if cached:
        # Cache hit — fast path
        latency_ms = (time.time() - start_time) * 1000
        cost = _estimate_cost(cache_hit=True)

        # Store messages in conversation history
        app.state.conversation.add_message(session_id, "user", query_text)
        msg_id = app.state.conversation.add_message(
            session_id, "assistant", cached["answer"],
            metadata={"cache_hit": True, "trace_id": opik_trace_id, "source": "semantic_cache"}
        )

        # Track metrics
        app.state.request_count += 1
        app.state.total_latency_ms += latency_ms
        app.state.total_cost_usd += cost

        return QueryResponse(
            answer=cached["answer"],
            contexts=[ContextItem(**ctx) for ctx in cached["contexts"]],
            metadata={
                "cache_hit": True,
                "latency_ms": round(latency_ms, 2),
                "cost_usd": cost,
                "distance": cached.get("distance", 0),
                "is_follow_up": is_follow_up,
                "standalone_query": standalone_query if is_follow_up else None,
                "trace_id": opik_trace_id,
                "stream_mode": "non_stream",
            },
            session_id=session_id,
            msg_id=msg_id,
        )

    # Step 3: Cache miss — run full pipeline
    # 3a. Classify query
    classification = await app.state.router.classify(standalone_query)
    query_type = classification["category"]

    # 3b. Retrieve contexts
    retrieval_result = await app.state.pipeline.retrieve(standalone_query)

    # 3c. Build type-specific prompt
    prompt_messages = app.state.router.build_prompt(
        standalone_query, retrieval_result.contexts, query_type
    )

    # 3d. Generate answer
    answer = await app.state.pipeline.generate(
        standalone_query, retrieval_result.contexts, prompt_messages
    )

    # 3e. Format contexts for response and cache
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
            },
        })

    # 3f. Cache the result (with manual Opik span)
    cache_store_span = None
    if OPIK_AVAILABLE:
        try:
            from opik import Opik as OpikClient
            _trace = opik_context.get_current_trace_data()
            _span = opik_context.get_current_span_data()
            if _trace:
                cache_store_span = OpikClient().span(
                    trace_id=_trace.id,
                    parent_span_id=_span.id if _span else None,
                    name="cache-store",
                    input={"query": standalone_query},
                )
        except Exception:
            pass

    app.state.cache.set(standalone_query, answer, formatted_contexts)

    if cache_store_span:
        try:
            cache_store_span.end(output={"stored": True, "query": standalone_query})
        except Exception:
            pass

    # Step 4: Store messages in conversation history
    num_llm_calls = 2 if is_follow_up else 1  # rewrite + classify
    num_llm_calls += 1  # generation

    app.state.conversation.add_message(session_id, "user", query_text)
    msg_id = app.state.conversation.add_message(
        session_id, "assistant", answer,
        metadata={
            "query_type": query_type,
            "cache_hit": False,
            "trace_id": opik_trace_id,
            "source": "rag_pipeline",
            "stream_mode": "non_stream",
        }
    )

    # Step 5: Track metrics
    latency_ms = (time.time() - start_time) * 1000
    cost = _estimate_cost(cache_hit=False, num_llm_calls=num_llm_calls)

    app.state.request_count += 1
    app.state.total_latency_ms += latency_ms
    app.state.total_cost_usd += cost

    # Build response metadata
    metadata = {
        "cache_hit": False,
        "latency_ms": round(latency_ms, 2),
        "cost_usd": cost,
        "query_type": query_type,
        "query_type_confidence": classification["confidence"],
        "num_contexts": len(formatted_contexts),
        "retrieval_time_seconds": retrieval_result.metadata.get("retrieval_time_seconds", 0),
        "is_follow_up": is_follow_up,
        "standalone_query": standalone_query if is_follow_up else None,
        "trace_id": opik_trace_id,
        "stream_mode": "non_stream",
    }

    return QueryResponse(
        answer=answer,
        contexts=[ContextItem(**ctx) for ctx in formatted_contexts],
        metadata=metadata,
        session_id=session_id,
        msg_id=msg_id,
    )


# Apply @opik.track decorator conditionally (no-op if opik not installed)
if OPIK_AVAILABLE:
    _run_query_pipeline = opik.track(name="rag-query")(_run_query_pipeline_inner)
else:
    _run_query_pipeline = _run_query_pipeline_inner


# ---------------------------------------------------------------------------
# POST /query — Main RAG endpoint
# ---------------------------------------------------------------------------

@app.post("/query", response_model=QueryResponse, tags=["RAG"])
async def query(request: QueryRequest):
    """
    Full RAG pipeline with conversation memory, query routing, and caching.

    Flow:
    1. Rewrite follow-up queries using conversation history
    2. Check semantic cache (sub-50ms on hit)
    3. On miss: classify → retrieve → build prompt → generate → cache
    4. Store messages in conversation history
    5. Return answer with msg_id for feedback
    """
    start_time = time.time()

    # Session handling: use provided or generate new
    session_id = request.session_id or app.state.conversation.create_session_id()

    try:
        response = await _run_query_pipeline(
            request.query, session_id, request.use_cache, start_time
        )

        # Trigger online eval (sampling_rate=0 disables auto-trigger,
        # so we manually trigger after the trace has the full answer)
        if OPIK_AVAILABLE and response.metadata.get("trace_id"):
            try:
                from opik import Opik as OpikClient
                opik.flush_tracker(timeout=5)
                _client = OpikClient()
                _trigger_eval(_client, response.metadata["trace_id"])
            except Exception:
                pass

        return response
    except Exception as e:
        print(f"   Query failed: {e}")
        raise HTTPException(status_code=500, detail=f"Query failed: {str(e)}")


# ---------------------------------------------------------------------------
# Traced streaming pipeline setup (retrieval phase only — generation streams separately)
# ---------------------------------------------------------------------------

async def _run_stream_pipeline_setup_inner(query_text, session_id, use_cache):
    """
    Run pre-generation pipeline: rewrite → cache → classify → retrieve.
    Decorated with @opik.track so child spans nest under this parent trace.
    Captures Opik trace/span IDs so the SSE generator can create a manual
    generate-stream span tied back to this trace.
    """
    _set_thread_id(session_id)

    # Capture Opik context IDs for manual generate-stream span later
    opik_trace_id = None
    opik_span_id = None
    if OPIK_AVAILABLE:
        try:
            trace_data = opik_context.get_current_trace_data()
            span_data = opik_context.get_current_span_data()
            if trace_data:
                opik_trace_id = trace_data.id
            if span_data:
                opik_span_id = span_data.id
        except Exception:
            pass

    rewrite_result = await app.state.conversation.rewrite_if_needed(query_text, session_id)
    standalone_query = rewrite_result["standalone_query"]
    is_follow_up = rewrite_result["is_follow_up"]

    cached = None
    if use_cache:
        cached = app.state.cache.get(standalone_query)

    if cached:
        return {
            "standalone_query": standalone_query,
            "is_follow_up": is_follow_up,
            "cached": cached,
            "opik_trace_id": opik_trace_id,
            "opik_span_id": opik_span_id,
        }

    classification = await app.state.router.classify(standalone_query)
    retrieval_result = await app.state.pipeline.retrieve(standalone_query)

    prompt_messages = app.state.router.build_prompt(
        standalone_query, retrieval_result.contexts, classification["category"]
    )

    return {
        "standalone_query": standalone_query,
        "is_follow_up": is_follow_up,
        "cached": None,
        "classification": classification,
        "retrieval_result": retrieval_result,
        "prompt_messages": prompt_messages,
        "opik_trace_id": opik_trace_id,
        "opik_span_id": opik_span_id,
    }


if OPIK_AVAILABLE:
    _run_stream_pipeline_setup = opik.track(name="rag-query-stream")(_run_stream_pipeline_setup_inner)
else:
    _run_stream_pipeline_setup = _run_stream_pipeline_setup_inner


# ---------------------------------------------------------------------------
# POST /query/stream — SSE streaming endpoint
# ---------------------------------------------------------------------------

@app.post("/query/stream", tags=["RAG"])
async def query_stream(request: QueryRequest, req: Request):
    """
    Streaming RAG query with Server-Sent Events (SSE).

    Streams pipeline progress as events:
    - session: session_id for the conversation
    - rewrite: if query was rewritten from follow-up
    - cache_status: whether query was cached
    - classification: detected query type
    - context: retrieved contexts (one per context)
    - token: answer text chunks
    - done: final metadata
    - error: if something went wrong
    """
    async def event_generator():
        start_time = time.time()

        session_id = request.session_id or app.state.conversation.create_session_id()
        yield f"event: session\ndata: {json.dumps({'session_id': session_id})}\n\n"

        try:
            # Run traced pipeline setup (rewrite → cache → classify → retrieve)
            setup = await _run_stream_pipeline_setup(
                request.query, session_id, request.use_cache
            )

            standalone_query = setup["standalone_query"]
            is_follow_up = setup["is_follow_up"]

            if is_follow_up:
                yield f"event: rewrite\ndata: {json.dumps({'original': request.query, 'standalone': standalone_query})}\n\n"

            # Cache hit — fast path
            cached = setup.get("cached")
            if cached:
                yield f"event: cache_status\ndata: {json.dumps({'cache_hit': True, 'distance': cached.get('distance', 0)})}\n\n"

                for ctx in cached["contexts"]:
                    yield f"event: context\ndata: {json.dumps(ctx)}\n\n"
                    await asyncio.sleep(0.01)

                for chunk in _stream_text_chunks(cached["answer"], chunk_size=3):
                    yield f"event: token\ndata: {json.dumps({'token': chunk})}\n\n"
                    await asyncio.sleep(0.02)

                app.state.conversation.add_message(session_id, "user", request.query)
                msg_id = app.state.conversation.add_message(
                    session_id, "assistant", cached["answer"],
                    metadata={
                        "cache_hit": True,
                        "trace_id": setup.get("opik_trace_id", ""),
                        "source": "semantic_cache",
                        "stream_mode": "simulated_cached_chunks",
                    }
                )

                latency_ms = (time.time() - start_time) * 1000
                app.state.request_count += 1
                app.state.total_latency_ms += latency_ms

                yield f"event: done\ndata: {json.dumps({'cache_hit': True, 'latency_ms': round(latency_ms, 2), 'cost_usd': 0.0, 'msg_id': msg_id, 'session_id': session_id, 'trace_id': setup.get('opik_trace_id', ''), 'stream_mode': 'simulated_cached_chunks'})}\n\n"
                return

            # Cache miss — stream generation
            classification = setup["classification"]
            retrieval_result = setup["retrieval_result"]
            prompt_messages = setup["prompt_messages"]
            query_type = classification["category"]

            yield f"event: cache_status\ndata: {json.dumps({'cache_hit': False})}\n\n"
            yield f"event: classification\ndata: {json.dumps(classification)}\n\n"

            # Stream contexts
            formatted_contexts = []
            for rank, doc in enumerate(retrieval_result.contexts, 1):
                ctx = {
                    "rank": rank,
                    "score": round(doc.score, 4) if doc.score else 0.0,
                    "content": doc.content,
                    "metadata": {
                        "file_path": doc.meta.get("file_path", "unknown"),
                        "category": doc.meta.get("category", "unknown"),
                        "file_type": doc.meta.get("file_type", "unknown"),
                    },
                }
                formatted_contexts.append(ctx)
                yield f"event: context\ndata: {json.dumps(ctx)}\n\n"
                await asyncio.sleep(0.01)

                if await req.is_disconnected():
                    return

            # Create manual Opik span for generate-stream, tied to the parent trace
            stream_span = None
            if OPIK_AVAILABLE and setup.get("opik_trace_id"):
                try:
                    from opik import Opik as OpikClient
                    _opik_client = OpikClient()
                    stream_span = _opik_client.span(
                        trace_id=setup["opik_trace_id"],
                        parent_span_id=setup.get("opik_span_id"),
                        name="generate-stream",
                        type="llm",
                        input={"query": standalone_query},
                    )
                except Exception:
                    pass

            # Stream real LLM tokens
            token_queue = await app.state.pipeline.generate_stream(
                standalone_query, retrieval_result.contexts, prompt_messages
            )

            while True:
                token = await token_queue.get()
                if token is None:
                    break
                yield f"event: token\ndata: {json.dumps({'token': token})}\n\n"

                if await req.is_disconnected():
                    if stream_span:
                        try:
                            stream_span.end(output={"response": "(client disconnected)"})
                        except Exception:
                            pass
                    return

            answer = getattr(token_queue, 'full_answer', '')
            stream_error = getattr(token_queue, 'stream_error', None)
            fallback_used = getattr(token_queue, 'fallback_used', False)
            fallback_metadata = getattr(token_queue, 'fallback_metadata', None)

            # End the Opik span — error or success
            if stream_span:
                try:
                    if stream_error:
                        stream_span.end(output={
                            "error": str(stream_error),
                            "exception_type": type(stream_error).__name__,
                        })
                    else:
                        span_output = {"response": answer}
                        if fallback_used and fallback_metadata:
                            span_output["fallback_used"] = True
                            span_output.update(fallback_metadata)
                        stream_span.end(output=span_output)
                except Exception:
                    pass

            # Unrecoverable error — send error event, skip cache/messages
            if stream_error:
                yield f"event: error\ndata: {json.dumps({'error': str(stream_error)})}\n\n"
                return

            # Patch the Opik trace output with the final answer.
            # @opik.track on _run_stream_pipeline_setup ends the trace before
            # generation starts, so its output is the setup dict (no answer).
            # This update adds the answer so online eval rules can score it.
            # Both messages go through the same client streamer queue, so the
            # update arrives at the server after trace creation — no race.
            if OPIK_AVAILABLE and setup.get("opik_trace_id") and answer:
                try:
                    from opik import Opik as OpikClient
                    _client = OpikClient()
                    _client.update_trace(
                        trace_id=setup["opik_trace_id"],
                        project_name=_client.project_name,
                        output={"answer": answer},
                    )
                    _client.flush(timeout=5)
                    # Re-trigger online eval on the updated trace so the rule
                    # scores the actual answer (not the empty initial output)
                    _trigger_eval(_client, setup["opik_trace_id"])
                except Exception:
                    pass

            # Cache the result (with manual Opik span tied to parent trace)
            cache_store_span = None
            if OPIK_AVAILABLE and setup.get("opik_trace_id"):
                try:
                    from opik import Opik as OpikClient
                    cache_store_span = OpikClient().span(
                        trace_id=setup["opik_trace_id"],
                        parent_span_id=setup.get("opik_span_id"),
                        name="cache-store",
                        input={"query": standalone_query},
                    )
                except Exception:
                    pass

            if request.use_cache and answer:
                app.state.cache.set(standalone_query, answer, formatted_contexts)

            if cache_store_span:
                try:
                    cache_store_span.end(output={"stored": True, "query": standalone_query})
                except Exception:
                    pass

            # Store messages
            app.state.conversation.add_message(session_id, "user", request.query)
            msg_id = app.state.conversation.add_message(
                session_id, "assistant", answer,
                metadata={
                    "query_type": query_type,
                    "cache_hit": False,
                    "trace_id": setup.get("opik_trace_id", ""),
                    "source": "rag_pipeline",
                    "stream_mode": "real_tokens",
                }
            )

            latency_ms = (time.time() - start_time) * 1000
            _stream_llm_calls = (2 if is_follow_up else 1) + 1  # rewrite (if any) + classify + generate
            cost = _estimate_cost(cache_hit=False, num_llm_calls=_stream_llm_calls)

            app.state.request_count += 1
            app.state.total_latency_ms += latency_ms
            app.state.total_cost_usd += cost

            yield f"event: done\ndata: {json.dumps({'cache_hit': False, 'latency_ms': round(latency_ms, 2), 'cost_usd': cost, 'query_type': query_type, 'msg_id': msg_id, 'session_id': session_id, 'num_contexts': len(formatted_contexts), 'trace_id': setup.get('opik_trace_id', ''), 'stream_mode': 'real_tokens'})}\n\n"

        except Exception as e:
            yield f"event: error\ndata: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
    )


# ---------------------------------------------------------------------------
# POST /feedback — User feedback
# ---------------------------------------------------------------------------

@app.post("/feedback", response_model=FeedbackResponse, tags=["Feedback"])
async def submit_feedback(request: FeedbackRequest):
    """Log user feedback (thumbs up/down) to Opik trace."""
    metadata = request.metadata or {}
    trace_id = metadata.get("trace_id", "")

    # Validate msg_id belongs to session history when storage is available.
    linked_message = None
    degraded = _is_degraded_mode()
    try:
        history = app.state.conversation.get_history(request.session_id)
        for msg in history:
            if msg.get("msg_id") == request.msg_id:
                linked_message = msg
                break
    except Exception:
        # Keep feedback non-blocking if history lookup itself fails.
        degraded = True

    if not degraded and linked_message is None:
        raise HTTPException(
            status_code=404,
            detail=f"Message '{request.msg_id}' not found in session '{request.session_id}'",
        )

    # Prefer explicit trace_id from request metadata; fall back to message metadata.
    if not trace_id and linked_message:
        trace_id = (linked_message.get("metadata") or {}).get("trace_id", "")

    # Persist lightweight local feedback linkage for diagnostics.
    app.state.feedback_events[request.msg_id] = {
        "session_id": request.session_id,
        "msg_id": request.msg_id,
        "rating": request.rating,
        "trace_id": trace_id,
        "reason": metadata.get("reason", ""),
        "comment": request.comment or "",
        "timestamp": time.time(),
    }

    if OPIK_AVAILABLE and trace_id:
        try:
            from opik import Opik as OpikClient
            radio_reason = metadata.get("reason")
            score = {
                "id": trace_id,
                "name": "user_feedback",
                "value": 1.0 if request.rating == "up" else 0.0,
                "category_name": radio_reason if radio_reason else ("positive" if request.rating == "up" else "negative"),
                "reason": request.comment if request.comment else None,
            }
            _opik_client = OpikClient()
            _opik_client.log_traces_feedback_scores(scores=[score])
            _opik_client.flush(timeout=5)
            print(f"   Feedback logged to Opik: {request.rating}, trace={trace_id[:12]}...")
        except Exception as e:
            print(f"   Opik feedback error: {e}")
            # Feedback failure is non-critical; log but don't return error
    else:
        print(f"   Feedback skipped: opik={'yes' if OPIK_AVAILABLE else 'no'}, trace_id={trace_id or 'missing'}")

    return FeedbackResponse(status="stored", feedback_key=request.msg_id)


# ---------------------------------------------------------------------------
# GET /conversation/{session_id} — Conversation history
# ---------------------------------------------------------------------------

@app.get("/conversation/{session_id}", response_model=ConversationResponse, tags=["Conversation"])
async def get_conversation(session_id: str):
    """Get conversation history for a session."""
    try:
        raw_messages = app.state.conversation.get_history(session_id)
        session_info = app.state.conversation.get_session_info(session_id)

        messages = []
        for msg in raw_messages:
            try:
                messages.append(ConversationMessage(**msg))
            except Exception:
                # Skip malformed or legacy records rather than failing the whole endpoint.
                continue

        return ConversationResponse(
            session_id=session_id,
            messages=messages,
            session_info=session_info,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get conversation: {str(e)}")


# ---------------------------------------------------------------------------
# GET /health — Service health
# ---------------------------------------------------------------------------

@app.get("/health", response_model=HealthResponse, tags=["Monitoring"])
async def health_check():
    """Health check for all service components."""
    try:
        # Check if all services initialized and their dependencies are reachable
        pipeline_ok = app.state.pipeline.is_healthy()
        cache_ok = app.state.cache.is_healthy()      # pings Redis internally
        conversation_ok = app.state.conversation.is_healthy()  # pings Redis internally

        # Redis health is indicated by cache + conversation both being healthy
        redis_ok = cache_ok and conversation_ok

        all_ok = pipeline_ok and cache_ok and conversation_ok
        degraded_mode = _is_degraded_mode()

        return HealthResponse(
            status="healthy" if all_ok else "degraded",
            timestamp=time.time(),
            components={
                "rag_pipeline": "healthy" if pipeline_ok else "unhealthy",
                "semantic_cache": "healthy" if cache_ok else "unhealthy",
                "conversation": "healthy" if conversation_ok else "unhealthy",
                "redis": "healthy" if redis_ok else "unhealthy",
                "degraded_mode": "true" if degraded_mode else "false",
            },
        )

    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Health check failed: {str(e)}")


# ---------------------------------------------------------------------------
# GET /metrics — System metrics
# ---------------------------------------------------------------------------

@app.get("/metrics", response_model=MetricsResponse, tags=["Monitoring"])
async def get_metrics():
    """System metrics: cache stats, latency, cost."""
    try:
        cache_stats = app.state.cache.get_stats()
        cache_stats["degraded_mode"] = _is_degraded_mode()
        cache_stats["feedback_events_count"] = len(app.state.feedback_events)

        avg_latency = (
            app.state.total_latency_ms / app.state.request_count
            if app.state.request_count > 0 else 0
        )

        return MetricsResponse(
            total_requests=app.state.request_count,
            avg_latency_ms=round(avg_latency, 2),
            total_cost_usd=round(app.state.total_cost_usd, 4),
            cache_stats=cache_stats,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get metrics: {str(e)}")


# ---------------------------------------------------------------------------
# GET / — API info
# ---------------------------------------------------------------------------

@app.get("/", tags=["General"])
async def root():
    """API info and available endpoints."""
    return {
        "name": settings.APP_NAME,
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "query": "POST /query",
            "stream": "POST /query/stream",
            "feedback": "POST /feedback",
            "conversation": "GET /conversation/{session_id}",
            "health": "GET /health",
            "metrics": "GET /metrics",
        },
    }


# ---------------------------------------------------------------------------
# Development server
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    print(f"\n   Starting {settings.APP_NAME}")
    print(f"   URL: http://localhost:8000")
    print(f"   Docs: http://localhost:8000/docs")
    print(f"   Debug: {settings.DEBUG}")

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level="info",
    )
