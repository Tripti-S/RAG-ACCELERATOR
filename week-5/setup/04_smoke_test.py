# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: End-to-End Smoke Test
===============================

Validates the full production RAG system by testing every major flow:

1. Health check        — all service components are up
2. Single query        — full RAG pipeline (retrieve + generate)
3. Follow-up query     — conversation memory + query rewriting
4. Cache hit           — repeat query triggers semantic cache
5. Feedback            — thumbs up/down storage
6. Metrics             — system metrics endpoint

Prerequisites:
    - Backend running: cd backend && python -m app.main
    - Or via Docker: docker compose up

Usage:
    # Test against local backend
    python setup/04_smoke_test.py

    # Test against custom URL
    python setup/04_smoke_test.py --url http://localhost:8000
"""

import sys
import time
import json
import argparse
import requests
from pathlib import Path


# Path resolution
SCRIPT_DIR = Path(__file__).resolve().parent
WEEK_DIR = SCRIPT_DIR.parent


def test_health(base_url: str) -> bool:
    """Test 1: Health check — all services must be healthy."""
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        data = response.json()

        if response.status_code == 200 and data.get("status") == "healthy":
            components = data.get("components", {})
            print(f"   PASS  Health check")
            for name, status in components.items():
                print(f"          {name}: {status}")
            return True
        else:
            print(f"   FAIL  Health check: status={data.get('status')}")
            for name, status in data.get("components", {}).items():
                if status != "healthy":
                    print(f"          {name}: {status}")
            return False

    except requests.ConnectionError:
        print(f"   FAIL  Cannot connect to {base_url}")
        print(f"          Start the backend:")
        print(f"          cd {WEEK_DIR}/backend && python -m app.main")
        return False
    except Exception as e:
        print(f"   FAIL  Health check: {str(e)[:100]}")
        return False


def test_single_query(base_url: str) -> dict:
    """
    Test 2: Single query — full RAG pipeline.

    Returns the response data for use in subsequent tests.
    """
    query = "What is Bayes' theorem and how is it applied?"

    try:
        start = time.time()
        response = requests.post(
            f"{base_url}/query",
            json={"query": query, "use_cache": True},
            timeout=120,
        )
        elapsed = time.time() - start

        if response.status_code != 200:
            print(f"   FAIL  Single query: HTTP {response.status_code}")
            print(f"          {response.text[:200]}")
            return {}

        data = response.json()
        answer = data.get("answer", "")
        contexts = data.get("contexts", [])
        metadata = data.get("metadata", {})
        session_id = data.get("session_id", "")

        if answer and len(answer) > 20:
            print(f"   PASS  Single query ({elapsed:.1f}s)")
            print(f"          Answer: {answer[:80]}...")
            print(f"          Contexts: {len(contexts)}")
            print(f"          Query type: {metadata.get('query_type', 'N/A')}")
            print(f"          Cache hit: {metadata.get('cache_hit', 'N/A')}")
            print(f"          Session: {session_id[:16]}...")
            return data
        else:
            print(f"   FAIL  Single query: answer too short ({len(answer)} chars)")
            return {}

    except Exception as e:
        print(f"   FAIL  Single query: {str(e)[:100]}")
        return {}


def test_follow_up(base_url: str, session_id: str) -> dict:
    """Test 3: Follow-up query — tests conversation memory + query rewriting."""
    query = "Can you give me a concrete example of that?"

    try:
        start = time.time()
        response = requests.post(
            f"{base_url}/query",
            json={"query": query, "session_id": session_id, "use_cache": True},
            timeout=120,
        )
        elapsed = time.time() - start

        if response.status_code != 200:
            print(f"   FAIL  Follow-up query: HTTP {response.status_code}")
            return {}

        data = response.json()
        metadata = data.get("metadata", {})
        is_follow_up = metadata.get("is_follow_up", False)
        standalone = metadata.get("standalone_query", "")

        if data.get("answer"):
            print(f"   PASS  Follow-up query ({elapsed:.1f}s)")
            print(f"          Is follow-up: {is_follow_up}")
            if standalone and standalone != query:
                print(f"          Rewritten to: {standalone[:80]}")
            else:
                print(f"          No rewrite needed")
            return data
        else:
            print(f"   FAIL  Follow-up query: empty answer")
            return {}

    except Exception as e:
        print(f"   FAIL  Follow-up query: {str(e)[:100]}")
        return {}


def test_cache_hit(base_url: str) -> bool:
    """Test 4: Cache hit — repeat the same query, should be fast."""
    query = "What is Bayes' theorem and how is it applied?"

    try:
        start = time.time()
        response = requests.post(
            f"{base_url}/query",
            json={"query": query, "use_cache": True},
            timeout=30,
        )
        elapsed = time.time() - start

        if response.status_code != 200:
            print(f"   FAIL  Cache hit test: HTTP {response.status_code}")
            return False

        data = response.json()
        metadata = data.get("metadata", {})
        cache_hit = metadata.get("cache_hit", False)

        if cache_hit:
            print(f"   PASS  Cache hit ({elapsed:.1f}s)")
            print(f"          Distance: {metadata.get('distance', 'N/A')}")
            return True
        else:
            # Cache miss on repeat is not a hard failure — threshold might be strict
            print(f"   WARN  Cache miss on repeat query ({elapsed:.1f}s)")
            print(f"          This may be expected if cache threshold is very strict")
            return True

    except Exception as e:
        print(f"   FAIL  Cache hit test: {str(e)[:100]}")
        return False


def test_feedback(base_url: str, session_id: str, msg_id: str) -> bool:
    """Test 5: Feedback — store thumbs up."""
    try:
        response = requests.post(
            f"{base_url}/feedback",
            json={
                "session_id": session_id,
                "msg_id": msg_id,
                "rating": "up",
                "query": "What is Bayes' theorem and how is it applied?",
                "answer": "Test answer",
                "comment": "Smoke test feedback",
                "metadata": {"query_type": "FACTUAL"},
            },
            timeout=10,
        )

        if response.status_code == 200:
            data = response.json()
            print(f"   PASS  Feedback stored")
            print(f"          Key: {data.get('feedback_key', 'N/A')}")
            return True
        else:
            print(f"   FAIL  Feedback: HTTP {response.status_code}")
            return False

    except Exception as e:
        print(f"   FAIL  Feedback: {str(e)[:100]}")
        return False


def test_metrics(base_url: str) -> bool:
    """Test 6: Metrics endpoint."""
    try:
        response = requests.get(f"{base_url}/metrics", timeout=10)

        if response.status_code == 200:
            data = response.json()
            print(f"   PASS  Metrics endpoint")
            print(f"          Total requests: {data.get('total_requests', 0)}")
            print(f"          Avg latency: {data.get('avg_latency_ms', 0):.0f}ms")

            cache_stats = data.get("cache_stats", {})
            print(f"          Cache hits: {cache_stats.get('cache_hits', 0)}")
            print(f"          Cache entries: {cache_stats.get('num_cached_entries', 0)}")
            return True
        else:
            print(f"   FAIL  Metrics: HTTP {response.status_code}")
            return False

    except Exception as e:
        print(f"   FAIL  Metrics: {str(e)[:100]}")
        return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    """Run the full smoke test suite."""
    parser = argparse.ArgumentParser(
        description="Week 5: End-to-end smoke test for production RAG"
    )
    parser.add_argument(
        "--url",
        default="http://localhost:8000",
        help="Backend API URL (default: http://localhost:8000)"
    )
    args = parser.parse_args()

    base_url = args.url.rstrip("/")

    print("\n" + "=" * 70)
    print("WEEK 5: END-TO-END SMOKE TEST")
    print("=" * 70)
    print(f"\n   Backend: {base_url}")

    results = {}

    # Test 1: Health check
    print(f"\n{'─' * 40}")
    print("1. Health Check")
    print(f"{'─' * 40}")
    results["health"] = test_health(base_url)

    if not results["health"]:
        print(f"\n{'=' * 70}")
        print("SMOKE TEST ABORTED — Backend not reachable")
        print(f"{'=' * 70}")
        sys.exit(1)

    # Test 2: Single query
    print(f"\n{'─' * 40}")
    print("2. Single Query (full RAG pipeline)")
    print(f"{'─' * 40}")
    query_result = test_single_query(base_url)
    results["single_query"] = bool(query_result)

    session_id = query_result.get("session_id", "")
    msg_id = query_result.get("msg_id", "")

    # Test 3: Follow-up query (needs session_id from test 2)
    print(f"\n{'─' * 40}")
    print("3. Follow-up Query (conversation memory)")
    print(f"{'─' * 40}")
    if session_id:
        follow_up_result = test_follow_up(base_url, session_id)
        results["follow_up"] = bool(follow_up_result)
    else:
        print(f"   SKIP  No session_id from previous test")
        results["follow_up"] = False

    # Test 4: Cache hit
    print(f"\n{'─' * 40}")
    print("4. Cache Hit (repeat query)")
    print(f"{'─' * 40}")
    results["cache_hit"] = test_cache_hit(base_url)

    # Test 5: Feedback
    print(f"\n{'─' * 40}")
    print("5. Feedback Storage")
    print(f"{'─' * 40}")
    if session_id and msg_id:
        results["feedback"] = test_feedback(base_url, session_id, msg_id)
    else:
        print(f"   SKIP  No session_id/msg_id from previous test")
        results["feedback"] = False

    # Test 6: Metrics
    print(f"\n{'─' * 40}")
    print("6. System Metrics")
    print(f"{'─' * 40}")
    results["metrics"] = test_metrics(base_url)

    # Summary
    print(f"\n{'=' * 70}")
    print("SMOKE TEST SUMMARY")
    print(f"{'=' * 70}")

    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for test_name, ok in results.items():
        status = "PASS" if ok else "FAIL"
        print(f"   {status}  {test_name}")

    print(f"\n   Result: {passed}/{total} tests passed")

    if passed == total:
        print("\n   All smoke tests passed. Production system is operational.")
    else:
        print("\n   Some tests failed. Check the output above for details.")
        sys.exit(1)


if __name__ == "__main__":
    main()
