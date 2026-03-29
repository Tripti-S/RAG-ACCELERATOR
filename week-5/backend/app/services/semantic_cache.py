# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Production Semantic Cache with Redis HNSW
===================================================

Semantic cache using RediSearch HNSW vector indexing for sub-50ms lookups.

Why semantic cache?
A RAG pipeline takes 10-25 seconds per query. Many user queries are variations
of the same question. Semantic caching catches these by comparing query embeddings
rather than exact strings — "What is MCP?" and "Explain MCP" hit the same cache.

Architecture:
- RediSearch HNSW index for O(log n) approximate nearest neighbor search
- Voyage AI (voyage-4-lite, 2048d) for cache embeddings — same model as retrieval
- Redis Cloud for persistent storage with automatic TTL eviction
- Cosine distance for semantic similarity measurement

Production insight — same embedder for cache and retrieval:
Both the RAG pipeline and the cache use Voyage-4-lite (2048d). Using the same
model simplifies deployment (no local ONNX model to ship in Docker) and ensures
query embeddings are consistent across the system.

Performance:
- Cache lookup: <50ms (HNSW index)
- Full RAG pipeline: ~10-25s
- Speedup: 200-500x on cache hits
- Why not FLAT index? FLAT = O(n) linear scan. HNSW = O(log n). At 10K cached
  queries, FLAT takes ~600ms vs HNSW ~20ms. Production systems use HNSW.

Usage:
    from app.services.semantic_cache import get_semantic_cache

    cache = get_semantic_cache()

    # Check cache first
    cached = cache.get(query)
    if cached:
        return cached  # Sub-50ms response

    # Cache miss — run full pipeline, then cache the result
    result = await pipeline.query(query, prompt_messages)
    cache.set(query, result.answer, result.contexts)
"""

import os
import time
import json
import hashlib
import numpy as np
from typing import Optional, Dict, Any, List

import redis
from redis.commands.search.field import VectorField, TextField, NumericField
from redis.commands.search.index_definition import IndexDefinition, IndexType
from redis.commands.search.query import Query
from app.config import settings

# Opik tracing (optional — no-op decorator if not installed)
try:
    import opik
    from opik import opik_context
    _opik_track = opik.track
    OPIK_AVAILABLE = True
except ImportError:
    def _opik_track(**kwargs):
        def _noop(func):
            return func
        return _noop
    OPIK_AVAILABLE = False


# ---------------------------------------------------------------------------
# Cache Embedder (internal — only used for query-to-query similarity)
# ---------------------------------------------------------------------------

class _CacheEmbedder:
    """
    Lightweight embedder for cache query similarity.

    Uses Voyage AI API (same model as retrieval pipeline) for embeddings.
    Keeps deployment simple — no local ONNX model to ship in Docker.

    Model: voyage-4-lite (2048d) by default, configurable via env vars.
    """

    def __init__(self, model: str, dimension: int):
        import voyageai
        self.client = voyageai.Client()
        self.model_name = model
        self.dimension = dimension
        print(f"   Cache embedder ready: {model} ({dimension}d)")

    def embed(self, text: str) -> np.ndarray:
        """
        Embed a single query string via Voyage AI API.

        Args:
            text: Query text to embed

        Returns:
            numpy array of shape (dimension,), dtype float32
        """
        result = self.client.embed(
            [text], model=self.model_name, output_dimension=self.dimension
        )
        return np.array(result.embeddings[0], dtype=np.float32)


# ---------------------------------------------------------------------------
# Production Semantic Cache
# ---------------------------------------------------------------------------

class SemanticCache:
    """
    Production semantic cache using RediSearch HNSW vector indexing.

    Sub-50ms cache lookups via HNSW approximate nearest neighbor search.
    Stores query-answer-context triples with automatic TTL eviction.

    Distance threshold controls the accuracy vs hit-rate tradeoff:
    - 0.06 (default): Ultra-conservative — only near-exact semantic matches
    - 0.10: Moderate — catches paraphrases, risks some false positives
    - 0.20: Aggressive — high hit rate, may return wrong cached answers

    Production recommendation: Start conservative (0.06). A wrong cached answer
    is far worse than a cache miss. Tune upward only after observing false
    positive rates in production logs.

    Singleton pattern: one cache instance across all requests.
    """

    INDEX_NAME = "semantic_cache_idx"
    KEY_PREFIX = "cache:query:"
    METRICS_KEY = "cache:metrics"

    _instance = None
    _initialized = False

    def __new__(cls):
        """Singleton — one cache instance across all requests."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize cache: Redis connection, embedder, HNSW index."""
        if self._initialized:
            return

        print("\n   Initializing semantic cache...")

        self._init_config()
        self._init_redis()
        self._init_embedder()
        self._create_index()

        self._initialized = True
        print("   Semantic cache ready")

    # -------------------------------------------------------------------
    # Initialization
    # -------------------------------------------------------------------

    def _init_config(self):
        """Load cache configuration from environment."""
        # Redis connection (shared with conversation.py)
        self.redis_host = settings.REDIS_HOST
        self.redis_port = settings.REDIS_PORT
        self.redis_password = settings.REDIS_PASSWORD
        self.redis_username = settings.REDIS_USERNAME
        self.redis_ssl = settings.REDIS_SSL

        # Cache embedding model (same as retrieval — Voyage API)
        self.embed_model = settings.CACHE_EMBED_MODEL
        self.embed_dimension = settings.CACHE_EMBED_DIMENSION

        # Cache behavior
        self.distance_threshold = settings.CACHE_DISTANCE_THRESHOLD
        self.ttl = settings.CACHE_TTL  # 24 hours

        print(f"   Cache config: model={self.embed_model}, dim={self.embed_dimension}")
        print(f"   Cache config: threshold={self.distance_threshold}, ttl={self.ttl}s")

    def _init_redis(self):
        """Connect to Redis with SSL support for cloud deployments."""
        self.redis_client = redis.Redis(
            host=self.redis_host,
            port=self.redis_port,
            username=self.redis_username,
            password=self.redis_password,
            ssl=self.redis_ssl,
            decode_responses=False  # Binary mode — embedding vectors are raw bytes
        )

        # Verify connection before proceeding
        try:
            self.redis_client.ping()
            print(f"   Redis connected: {self.redis_host}:{self.redis_port}")
        except redis.ConnectionError as e:
            raise ConnectionError(
                f"Cannot connect to Redis at {self.redis_host}:{self.redis_port}. "
                f"Check REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, and REDIS_SSL. "
                f"Error: {e}"
            )

    def _init_embedder(self):
        """Initialize the cache embedding model (FastEmbed, local)."""
        self.embedder = _CacheEmbedder(
            model=self.embed_model,
            dimension=self.embed_dimension
        )

    def _increment_metric(self, field: str) -> None:
        """Persist cache metrics in Redis so they survive process restarts."""
        try:
            self.redis_client.hincrby(self.METRICS_KEY, field, 1)
        except Exception:
            pass

    def _get_metric(self, field: str) -> int:
        """Read a persisted cache metric from Redis, defaulting to 0 on failure."""
        try:
            value = self.redis_client.hget(self.METRICS_KEY, field)
            if value is None:
                return 0
            return int(self._decode(value))
        except Exception:
            return 0

    def _create_index(self):
        """
        Create RediSearch HNSW vector index for fast similarity search.

        HNSW parameters (tuned for caches up to ~100K entries):
        - M=40: Bi-directional links per node. Higher = better recall, slower build.
        - EF_CONSTRUCTION=200: Build-time search effort. Higher = better index quality.
        - INITIAL_CAP=1000: Pre-allocated capacity (grows automatically).
        """
        try:
            self.redis_client.ft(self.INDEX_NAME).info()
            print(f"   HNSW index '{self.INDEX_NAME}' exists")
            return
        except redis.exceptions.ResponseError as e:
            err_msg = str(e).lower()
            if "no such index" not in err_msg and "unknown index" not in err_msg:
                raise  # Re-raise unexpected RediSearch errors

        print(f"   Creating HNSW index '{self.INDEX_NAME}'...")

        schema = (
            TextField("query"),
            TextField("answer"),
            NumericField("timestamp"),
            VectorField(
                "embedding",
                "HNSW",
                {
                    "TYPE": "FLOAT32",
                    "DIM": self.embed_dimension,
                    "DISTANCE_METRIC": "COSINE",
                    "INITIAL_CAP": 1000,
                    "M": 40,
                    "EF_CONSTRUCTION": 200,
                }
            ),
        )

        self.redis_client.ft(self.INDEX_NAME).create_index(
            schema,
            definition=IndexDefinition(
                prefix=[self.KEY_PREFIX],
                index_type=IndexType.HASH
            )
        )

        print(f"   HNSW index created (dim={self.embed_dimension}, metric=COSINE)")

    # -------------------------------------------------------------------
    # Cache Operations
    # -------------------------------------------------------------------

    @_opik_track(name="cache-lookup")
    def get(self, query: str) -> Optional[Dict[str, Any]]:
        """
        Look up a semantically similar query in cache.

        Uses HNSW vector search to find the closest cached query by cosine
        distance. Returns the cached response only if distance is below
        the configured threshold.

        The KNN search returns only lightweight fields (query, answer, timestamp).
        Full contexts are fetched separately via hget — avoids returning heavy
        payloads in the vector search itself.

        Args:
            query: User's question to look up

        Returns:
            Cached response dict if found within threshold:
                {answer, contexts, original_query, distance, cache_lookup_ms}
            None if no match or on error (cache failures are non-fatal)
        """
        if not query or not query.strip():
            return None

        start_time = time.time()

        # Embed the query for vector similarity search
        query_embedding = self.embedder.embed(query)
        query_vector = query_embedding.tobytes()

        # KNN search: find the single nearest cached query by embedding distance
        # Only return lightweight fields — contexts fetched separately if hit
        knn_query = Query(
            "*=>[KNN 1 @embedding $vec AS distance]"
        ).return_fields("query", "answer", "timestamp", "distance").dialect(2)

        try:
            results = self.redis_client.ft(self.INDEX_NAME).search(
                knn_query,
                query_params={"vec": query_vector}
            )

            lookup_ms = (time.time() - start_time) * 1000

            if results.total > 0:
                top = results.docs[0]
                distance = float(self._decode(top.distance))

                if distance < self.distance_threshold:
                    self._increment_metric("cache_hits")

                    # Decode text fields (decode_responses=False returns bytes)
                    cached_query = self._decode(top.query)
                    cached_answer = self._decode(top.answer)

                    # Fetch contexts separately (too large for KNN result set)
                    cache_key = self._decode(top.id)
                    contexts_raw = self.redis_client.hget(cache_key, "contexts")
                    contexts = json.loads(contexts_raw) if contexts_raw else []

                    print(f"   CACHE HIT: distance={distance:.4f}, lookup={lookup_ms:.0f}ms")
                    print(f"   Matched: '{cached_query[:60]}...'")

                    if OPIK_AVAILABLE:
                        try:
                            opik_context.update_current_span(output={"cache_hit": True, "distance": round(distance, 4), "lookup_ms": round(lookup_ms, 1)})
                        except Exception:
                            pass

                    return {
                        "answer": cached_answer,
                        "contexts": contexts,
                        "original_query": cached_query,
                        "distance": distance,
                        "cache_lookup_ms": round(lookup_ms, 1),
                    }

            # No match within threshold
            self._increment_metric("cache_misses")
            print(f"   CACHE MISS: lookup={lookup_ms:.0f}ms")

            if OPIK_AVAILABLE:
                try:
                    opik_context.update_current_span(output={"cache_hit": False, "lookup_ms": round(lookup_ms, 1)})
                except Exception:
                    pass

            return None

        except Exception as e:
            # Cache lookup failure is non-fatal — pipeline continues without cache
            self._increment_metric("cache_misses")
            print(f"   Cache lookup error: {str(e)[:100]}")
            return None

    def set(self, query: str, answer: str, contexts: List[Dict[str, Any]]) -> None:
        """
        Store a query-answer-context triple in the cache.

        The entry is automatically indexed by RediSearch (prefix-based key
        matching) and expires after the configured TTL.

        Uses MD5 hash of query for deterministic keys — repeating the same
        query overwrites the existing entry instead of creating duplicates.

        Args:
            query: User's question
            answer: Generated answer
            contexts: Retrieved contexts used to generate the answer
        """
        if not query or not answer:
            return

        # Embed the query for vector similarity indexing
        query_embedding = self.embedder.embed(query)

        # Deterministic key from query hash (same query = same key = overwrite)
        query_hash = hashlib.md5(query.encode()).hexdigest()
        cache_key = f"{self.KEY_PREFIX}{query_hash}"

        # Store as Redis hash — RediSearch auto-indexes via KEY_PREFIX match
        mapping = {
            "query": query,
            "answer": answer,
            "contexts": json.dumps(contexts),
            "timestamp": str(time.time()),
            "embedding": query_embedding.tobytes(),
        }

        try:
            self.redis_client.hset(cache_key, mapping=mapping)

            if self.ttl:
                self.redis_client.expire(cache_key, self.ttl)

            print(f"   Cached: '{query[:50]}...'")

        except Exception as e:
            # Cache write failure is non-fatal — pipeline still returns the answer
            print(f"   Cache write error: {str(e)[:100]}")

    # -------------------------------------------------------------------
    # Metrics & Management
    # -------------------------------------------------------------------

    def get_stats(self) -> Dict[str, Any]:
        """
        Get cache performance statistics.

        Returns:
            Dict with hit/miss counts, hit rate, and HNSW index size.
        """
        cache_hits = self._get_metric("cache_hits")
        cache_misses = self._get_metric("cache_misses")
        total = cache_hits + cache_misses
        hit_rate = (cache_hits / total * 100) if total > 0 else 0.0

        # Read index size from RediSearch
        num_docs = 0
        try:
            info = self.redis_client.ft(self.INDEX_NAME).info()
            # Handle both str and bytes keys (depends on redis-py version)
            for key in ("num_docs", b"num_docs"):
                if key in info:
                    num_docs = int(info[key])
                    break
        except Exception:
            pass

        return {
            "cache_hits": cache_hits,
            "cache_misses": cache_misses,
            "total_queries": total,
            "hit_rate_percent": round(hit_rate, 1),
            "num_cached_entries": num_docs,
            "distance_threshold": self.distance_threshold,
        }

    def clear(self) -> int:
        """
        Clear all cached entries.

        Returns:
            Number of cache keys deleted.
        """
        cache_keys = self.redis_client.keys(f"{self.KEY_PREFIX}*")
        if cache_keys:
            deleted = self.redis_client.delete(*cache_keys)
            print(f"   Cache cleared: {deleted} entries removed")
            return deleted
        return 0

    def drop_index(self) -> None:
        """Drop the HNSW vector index and all cached entries (for testing/cleanup)."""
        try:
            self.redis_client.ft(self.INDEX_NAME).dropindex(delete_documents=True)
            print(f"   Dropped index '{self.INDEX_NAME}'")
        except redis.exceptions.ResponseError:
            print(f"   Index '{self.INDEX_NAME}' does not exist")

    def is_healthy(self) -> bool:
        """Check if Redis connection and HNSW index are operational."""
        try:
            self.redis_client.ping()
            self.redis_client.ft(self.INDEX_NAME).info()
            return True
        except Exception:
            return False

    # -------------------------------------------------------------------
    # Internal helpers
    # -------------------------------------------------------------------

    @staticmethod
    def _decode(value: Any) -> str:
        """
        Decode bytes to string.

        Needed because we use decode_responses=False for binary vector support.
        All text fields from Redis come back as bytes and need explicit decoding.
        """
        if isinstance(value, bytes):
            return value.decode("utf-8")
        return str(value) if value is not None else ""


# ---------------------------------------------------------------------------
# Singleton accessor
# ---------------------------------------------------------------------------

_semantic_cache: Optional[SemanticCache] = None


def get_semantic_cache() -> SemanticCache:
    """
    Get or create the global semantic cache instance.

    Singleton ensures we initialize the HNSW index, Redis connection,
    and Voyage embedder exactly once across all requests.
    """
    global _semantic_cache
    if _semantic_cache is None:
        _semantic_cache = SemanticCache()
    return _semantic_cache
