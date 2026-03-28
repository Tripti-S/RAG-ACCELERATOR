# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Setup Redis for Production Services
=============================================

Creates and verifies the Redis structures needed by the production RAG system:

1. Semantic Cache HNSW index  — for sub-50ms query-to-query similarity lookup
2. Conversation namespace     — for session-based message storage

Each structure is verified with a test write/read cycle.

Prerequisites:
    - Redis Cloud instance running (https://cloud.redis.io/)
    - REDIS_HOST, REDIS_PORT, REDIS_PASSWORD set in .env

Usage:
    python setup/03_setup_redis.py

    # Reset: drop existing index and recreate
    python setup/03_setup_redis.py --reset
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path

from dotenv import load_dotenv
import redis
from redis.commands.search.field import VectorField, TextField, NumericField
from redis.commands.search.index_definition import IndexDefinition, IndexType

# Path resolution
SCRIPT_DIR = Path(__file__).resolve().parent
WEEK_DIR = SCRIPT_DIR.parent          # week5_production/
PROJECT_ROOT = WEEK_DIR.parent        # rag-accelerator-code/


def load_environment() -> dict:
    """Load and validate Redis environment variables."""
    env_file = WEEK_DIR / ".env"
    if not env_file.exists():
        env_file = PROJECT_ROOT / ".env"
    if env_file.exists():
        load_dotenv(env_file)

    required_vars = ["REDIS_HOST", "REDIS_PASSWORD"]
    env_vars = {}
    missing = []

    for var in required_vars:
        value = os.getenv(var)
        if not value or value.startswith("your_"):
            missing.append(var)
        env_vars[var] = value

    if missing:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing)}\n"
            f"Set them in {WEEK_DIR}/.env\n"
            f"Get Redis credentials from: https://cloud.redis.io/"
        )

    env_vars["REDIS_PORT"] = int(os.getenv("REDIS_PORT", "6379"))
    env_vars["REDIS_USERNAME"] = os.getenv("REDIS_USERNAME", "default")
    env_vars["REDIS_SSL"] = os.getenv("REDIS_SSL", "true").lower() == "true"

    # Cache settings
    env_vars["CACHE_EMBED_DIMENSION"] = int(os.getenv("CACHE_EMBED_DIMENSION", "2048"))

    return env_vars


def get_redis_client(env_vars: dict, decode_responses: bool = True) -> redis.Redis:
    """Create a Redis client from environment variables."""
    return redis.Redis(
        host=env_vars["REDIS_HOST"],
        port=env_vars["REDIS_PORT"],
        username=env_vars["REDIS_USERNAME"],
        password=env_vars["REDIS_PASSWORD"],
        ssl=env_vars["REDIS_SSL"],
        decode_responses=decode_responses,
        socket_timeout=10,
    )


# ---------------------------------------------------------------------------
# 1. Semantic Cache HNSW Index
# ---------------------------------------------------------------------------

def setup_semantic_cache(env_vars: dict, reset: bool = False) -> bool:
    """
    Create the RediSearch HNSW vector index for semantic caching.

    The semantic cache uses this index for O(log n) approximate nearest neighbor
    search across cached query embeddings. Without this index, the cache service
    will create it on first startup, but pre-creating it here lets us verify
    the RediSearch module is available.

    Args:
        env_vars: Environment configuration
        reset: If True, drop and recreate existing index

    Returns:
        True if setup succeeded
    """
    INDEX_NAME = "semantic_cache_idx"
    KEY_PREFIX = "cache:query:"

    # Use binary mode for the cache (embedding vectors are raw bytes)
    client = get_redis_client(env_vars, decode_responses=False)

    # Check if index already exists
    try:
        info = client.ft(INDEX_NAME).info()
        num_docs = 0
        for key in ("num_docs", b"num_docs"):
            if key in info:
                num_docs = int(info[key])
                break

        if reset:
            print(f"   Dropping existing index '{INDEX_NAME}' ({num_docs} entries)...")
            client.ft(INDEX_NAME).dropindex(delete_documents=True)
        else:
            print(f"   HNSW index '{INDEX_NAME}' already exists ({num_docs} entries)")
            return True

    except redis.exceptions.ResponseError as e:
        err_msg = str(e).lower()
        if "no such index" in err_msg or "unknown index" in err_msg:
            pass  # Index doesn't exist yet — create it below
        elif "unknown command" in err_msg:
            print(f"   FAIL  RediSearch module not available on this Redis instance")
            print(f"          Redis Cloud free tier includes RediSearch.")
            print(f"          Redis OSS requires the RediSearch module to be loaded.")
            return False
        else:
            raise

    # Create the HNSW index
    dimension = env_vars["CACHE_EMBED_DIMENSION"]

    print(f"   Creating HNSW index '{INDEX_NAME}'...")
    print(f"   Dimension: {dimension}, Metric: COSINE")
    print(f"   HNSW params: M=40, EF_CONSTRUCTION=200, INITIAL_CAP=1000")

    schema = (
        TextField("query"),
        TextField("answer"),
        NumericField("timestamp"),
        VectorField(
            "embedding",
            "HNSW",
            {
                "TYPE": "FLOAT32",
                "DIM": dimension,
                "DISTANCE_METRIC": "COSINE",
                "INITIAL_CAP": 1000,
                "M": 40,
                "EF_CONSTRUCTION": 200,
            }
        ),
    )

    client.ft(INDEX_NAME).create_index(
        schema,
        definition=IndexDefinition(
            prefix=[KEY_PREFIX],
            index_type=IndexType.HASH
        )
    )

    # Verify
    client.ft(INDEX_NAME).info()
    print(f"   PASS  Semantic cache HNSW index created")
    return True


# ---------------------------------------------------------------------------
# 2. Conversation Namespace
# ---------------------------------------------------------------------------

def setup_conversation(env_vars: dict, reset: bool = False) -> bool:
    """
    Verify conversation storage namespace works.

    Conversation uses Redis Lists (no special index needed). This test
    verifies that basic List operations work with the configured credentials.

    Args:
        env_vars: Environment configuration
        reset: If True, clean up test keys

    Returns:
        True if setup succeeded
    """
    client = get_redis_client(env_vars, decode_responses=True)

    test_key = "chat:__setup_test__:messages"
    test_meta_key = "chat:__setup_test__:meta"

    try:
        # Test write: RPUSH + LTRIM + EXPIRE pipeline
        test_message = json.dumps({
            "msg_id": "msg_test123",
            "role": "user",
            "content": "Setup test message",
            "timestamp": time.time(),
        })

        pipe = client.pipeline()
        pipe.rpush(test_key, test_message)
        pipe.ltrim(test_key, -10, -1)
        pipe.expire(test_key, 60)
        pipe.hset(test_meta_key, "created_at", str(time.time()))
        pipe.expire(test_meta_key, 60)
        pipe.execute()

        # Test read: LRANGE
        messages = client.lrange(test_key, 0, -1)
        assert len(messages) >= 1, "No messages returned"

        parsed = json.loads(messages[-1])
        assert parsed["msg_id"] == "msg_test123", "Message content mismatch"

        # Cleanup test keys
        client.delete(test_key, test_meta_key)

        print(f"   PASS  Conversation storage (Redis Lists + Pipeline)")
        return True

    except Exception as e:
        # Cleanup on failure
        client.delete(test_key, test_meta_key)
        print(f"   FAIL  Conversation storage: {str(e)[:100]}")
        return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    """Setup and verify all Redis structures."""
    parser = argparse.ArgumentParser(
        description="Week 5: Setup Redis for production RAG services"
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Drop and recreate existing HNSW index"
    )
    args = parser.parse_args()

    print("\n" + "=" * 70)
    print("WEEK 5: SETUP REDIS FOR PRODUCTION SERVICES")
    print("=" * 70)

    try:
        env_vars = load_environment()

        # Verify basic connectivity first
        client = get_redis_client(env_vars)
        client.ping()
        info = client.info("memory")
        used_mb = info.get("used_memory_human", "unknown")
        print(f"\n   Redis connected: {env_vars['REDIS_HOST']}:{env_vars['REDIS_PORT']}")
        print(f"   Memory usage: {used_mb}")

        results = {}

        # 1. Semantic Cache HNSW Index
        print(f"\n{'─' * 40}")
        print("1. Semantic Cache (HNSW Vector Index)")
        print(f"{'─' * 40}")
        results["semantic_cache"] = setup_semantic_cache(env_vars, reset=args.reset)

        # 2. Conversation Storage
        print(f"\n{'─' * 40}")
        print("2. Conversation Storage (Redis Lists)")
        print(f"{'─' * 40}")
        results["conversation"] = setup_conversation(env_vars, reset=args.reset)

        # Summary
        print(f"\n{'=' * 70}")
        print("REDIS SETUP SUMMARY")
        print(f"{'=' * 70}")

        passed = sum(1 for v in results.values() if v)
        total = len(results)

        for name, ok in results.items():
            status = "PASS" if ok else "FAIL"
            print(f"   {status}  {name}")

        print(f"\n   Result: {passed}/{total} structures verified")

        if passed == total:
            print("\n   Redis is ready for production.")
            print("   Next: python setup/04_smoke_test.py")
        else:
            print("\n   Some structures failed. Check the errors above.")
            sys.exit(1)

    except Exception as e:
        print(f"\nError: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
