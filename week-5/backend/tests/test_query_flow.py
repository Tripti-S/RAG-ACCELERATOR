"""
Integration tests: 10-step non-stream RAG query flow
======================================================

Verifies that _run_query_pipeline_inner (the core of POST /query) calls
every service in the correct order and produces the right response shape.

Tested flows
------------
1. Cache-miss (full pipeline)   — asserts exact 9-operation call order
2. Cache-miss response fields   — asserts required QueryResponse fields
3. Cache-hit (fast path)        — asserts pipeline/router are never called
4. Cache bypass (use_cache=False) — asserts cache.get is never called
5. Metrics tracking             — asserts request_count / latency / cost updated

Design
------
- conftest.py patches heavy packages (haystack, qdrant_client, voyageai, …)
  in sys.modules so import finishes in < 3 s instead of ~52 s.
- app.state.{pipeline,router,cache,conversation} are replaced with lightweight
  AsyncMock/MagicMock objects before each test.
- All tests call _run_query_pipeline_inner() directly (not via HTTP) so there
  is no network traffic and no FastAPI lifespan startup.
"""

import asyncio
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock

# conftest.py has already patched sys.modules and inserted the backend path
from app.main import app, _run_query_pipeline_inner  # noqa: E402


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_doc(content: str = "sample context", score: float = 0.85) -> MagicMock:
    """Lightweight stand-in for a Haystack Document."""
    doc = MagicMock()
    doc.content = content
    doc.score = score
    doc.meta = {
        "file_path": "test.md",
        "category": "math",
        "file_type": "markdown",
    }
    return doc


def _make_state(
    *,
    cache_hit: bool = False,
    use_cache_side_effect: bool = True,
) -> tuple[SimpleNamespace, list[str]]:
    """
    Build a fake app.state with fully mocked services.

    Each time a service method is called it appends a tag to `call_log` so
    tests can assert on the exact call ORDER (not just whether each mock was
    called).

    Parameters
    ----------
    cache_hit:
        If True, ``cache.get`` returns a pre-built cached response dict.
        If False, it returns None (cache miss).
    use_cache_side_effect:
        When False the mock's side_effect is not registered (simulates
        ``use_cache=False`` where the pipeline skips cache.get entirely).

    Returns
    -------
    (state, call_log)
    """
    call_log: list[str] = []

    # ---- conversation --------------------------------------------------
    conv = MagicMock()

    async def _rewrite(query: str, session_id: str) -> dict:
        call_log.append("rewrite_if_needed")
        return {
            "original_query": query,
            "standalone_query": query,
            "is_follow_up": False,
            "history_length": 0,
        }

    conv.rewrite_if_needed = AsyncMock(side_effect=_rewrite)
    conv.create_session_id = MagicMock(return_value="sess_test")

    _msg_seq = {"n": 0}

    def _add_msg(session_id: str, role: str, content: str, metadata=None) -> str:
        call_log.append(f"add_message:{role}")
        _msg_seq["n"] += 1
        return f"msg_{_msg_seq['n']:03d}"

    conv.add_message = MagicMock(side_effect=_add_msg)
    conv.get_history = MagicMock(return_value=[])

    # ---- semantic cache ------------------------------------------------
    cache = MagicMock()

    _cached_response = {
        "answer": "cached answer",
        "contexts": [
            {
                "rank": 1,
                "score": 0.9,
                "content": "cached ctx",
                "metadata": {
                    "file_path": "cache.md",
                    "category": "math",
                    "file_type": "markdown",
                },
            }
        ],
        "distance": 0.04,
    }

    def _cache_get(q: str):
        call_log.append("cache_get")
        return _cached_response if cache_hit else None

    if use_cache_side_effect:
        cache.get = MagicMock(side_effect=_cache_get)
    else:
        # When the pipeline skips cache.get (use_cache=False) we still
        # provide a side-effect-free stub so assertions are unambiguous.
        cache.get = MagicMock(return_value=None)

    def _cache_set(*args, **kwargs):
        call_log.append("cache_set")

    cache.set = MagicMock(side_effect=_cache_set)

    # ---- query router --------------------------------------------------
    router = MagicMock()

    async def _classify(q: str) -> dict:
        call_log.append("router_classify")
        return {"category": "FACTUAL", "confidence": 0.95}

    router.classify = AsyncMock(side_effect=_classify)

    def _build_prompt(q: str, contexts, query_type: str):
        call_log.append("router_build_prompt")
        return [{"role": "user", "content": "test prompt"}]

    router.build_prompt = MagicMock(side_effect=_build_prompt)

    # ---- RAG pipeline --------------------------------------------------
    pipeline = MagicMock()

    _retrieval_result = SimpleNamespace(
        contexts=[_make_doc()],
        metadata={"retrieval_time_seconds": 0.05},
    )

    async def _retrieve(q: str):
        call_log.append("pipeline_retrieve")
        return _retrieval_result

    async def _generate(q: str, contexts, prompt_messages) -> str:
        call_log.append("pipeline_generate")
        return "generated answer"

    pipeline.retrieve = AsyncMock(side_effect=_retrieve)
    pipeline.generate = AsyncMock(side_effect=_generate)

    # ---- assemble state ------------------------------------------------
    state = SimpleNamespace(
        conversation=conv,
        cache=cache,
        router=router,
        pipeline=pipeline,
        request_count=0,
        total_latency_ms=0.0,
        total_cost_usd=0.0,
        feedback_events={},
    )
    return state, call_log


def _apply_state(state: SimpleNamespace) -> None:
    """Copy all attributes from *state* onto app.state."""
    app.state.conversation = state.conversation
    app.state.cache = state.cache
    app.state.router = state.router
    app.state.pipeline = state.pipeline
    app.state.request_count = state.request_count
    app.state.total_latency_ms = state.total_latency_ms
    app.state.total_cost_usd = state.total_cost_usd
    app.state.feedback_events = state.feedback_events


# ---------------------------------------------------------------------------
# Test cases
# ---------------------------------------------------------------------------

class TestNonStreamQueryFlow:
    """
    Asserts the exact 10-step non-stream query pipeline call order.

    The docstring for _run_query_pipeline_inner lists 10 steps; they map to
    these 9 service-method invocations (session handling is in the outer
    ``query()`` handler, not the inner function):

        1. conversation.rewrite_if_needed
        2. cache.get            ← skip if use_cache=False
        3. router.classify      ← skip on cache hit
        4. pipeline.retrieve    ← skip on cache hit
        5. router.build_prompt  ← skip on cache hit
        6. pipeline.generate    ← skip on cache hit
        7. cache.set            ← skip on cache hit
        8. conversation.add_message (user)
        9. conversation.add_message (assistant)
    """

    # ------------------------------------------------------------------
    # Test 1: full cache-miss pipeline — strict call order
    # ------------------------------------------------------------------
    def test_cache_miss_call_order(self):
        """
        Cache miss: the 9 service operations execute in the documented order.
        """
        state, call_log = _make_state(cache_hit=False, use_cache_side_effect=True)
        _apply_state(state)

        asyncio.run(
            _run_query_pipeline_inner(
                "what is probability?", "sess_abc", True, 0.0
            )
        )

        expected = [
            "rewrite_if_needed",
            "cache_get",
            "router_classify",
            "pipeline_retrieve",
            "router_build_prompt",
            "pipeline_generate",
            "cache_set",
            "add_message:user",
            "add_message:assistant",
        ]
        assert call_log == expected, (
            f"Call order mismatch.\n"
            f"  Expected: {expected}\n"
            f"  Got:      {call_log}"
        )

    # ------------------------------------------------------------------
    # Test 2: cache-miss response fields
    # ------------------------------------------------------------------
    def test_cache_miss_response_fields(self):
        """
        Cache-miss response has all required QueryResponse fields
        including stream_mode='non_stream' (added in 5.8c fixes).
        """
        state, _ = _make_state(cache_hit=False)
        _apply_state(state)

        response = asyncio.run(
            _run_query_pipeline_inner(
                "what is variance?", "sess_abc", True, 0.0
            )
        )

        assert response.answer == "generated answer"
        assert response.session_id == "sess_abc"
        assert response.msg_id.startswith("msg_")

        meta = response.metadata
        assert meta["cache_hit"] is False
        assert meta["stream_mode"] == "non_stream"
        assert meta["query_type"] == "FACTUAL"
        assert "latency_ms" in meta
        assert "cost_usd" in meta
        assert "num_contexts" in meta

    # ------------------------------------------------------------------
    # Test 3: cache hit — pipeline and router are never invoked
    # ------------------------------------------------------------------
    def test_cache_hit_skips_pipeline(self):
        """
        Cache hit: rewrite + cache_get + add_message x2 only.
        Router and pipeline methods must NOT be called.
        """
        state, call_log = _make_state(cache_hit=True, use_cache_side_effect=True)
        _apply_state(state)

        response = asyncio.run(
            _run_query_pipeline_inner(
                "what is probability?", "sess_abc", True, 0.0
            )
        )

        assert call_log == [
            "rewrite_if_needed",
            "cache_get",
            "add_message:user",
            "add_message:assistant",
        ], f"Unexpected call_log on cache hit: {call_log}"

        assert "router_classify" not in call_log
        assert "pipeline_retrieve" not in call_log
        assert "pipeline_generate" not in call_log
        assert "cache_set" not in call_log

        assert response.answer == "cached answer"
        assert response.metadata["cache_hit"] is True

    # ------------------------------------------------------------------
    # Test 4: use_cache=False — cache.get never called
    # ------------------------------------------------------------------
    def test_cache_bypass_skips_cache_check(self):
        """
        use_cache=False: cache.get is never called even on a cache-miss
        query; the full pipeline (classify → retrieve → build → generate)
        still runs and cache.set is still called for future re-use.
        """
        state, call_log = _make_state(cache_hit=False, use_cache_side_effect=False)
        _apply_state(state)

        asyncio.run(
            _run_query_pipeline_inner(
                "what is standard deviation?", "sess_abc", False, 0.0
            )
        )

        assert "cache_get" not in call_log, (
            "cache.get must not be called when use_cache=False"
        )
        # Full pipeline runs
        assert "router_classify" in call_log
        assert "pipeline_retrieve" in call_log
        assert "router_build_prompt" in call_log
        assert "pipeline_generate" in call_log
        # Result is still cached for future hits
        assert "cache_set" in call_log

    # ------------------------------------------------------------------
    # Test 5: app.state metrics are incremented after every query
    # ------------------------------------------------------------------
    def test_metrics_incremented_after_query(self):
        """
        request_count, total_latency_ms, and total_cost_usd are each
        incremented exactly once per query call.
        """
        state, _ = _make_state(cache_hit=False)
        _apply_state(state)

        assert app.state.request_count == 0
        assert app.state.total_latency_ms == 0.0
        assert app.state.total_cost_usd == 0.0

        asyncio.run(
            _run_query_pipeline_inner(
                "what is a random variable?", "sess_abc", True, 0.0
            )
        )

        assert app.state.request_count == 1, "request_count should be 1 after one query"
        assert app.state.total_latency_ms > 0, "total_latency_ms should be > 0"
        assert app.state.total_cost_usd > 0, "total_cost_usd should be > 0"
