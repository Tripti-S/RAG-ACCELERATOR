# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Verify Production Environment
=======================================

Checks that all dependencies, API keys, and service connections are working
before running the production RAG system.

Verifies:
1. Python version (3.11+)
2. Required packages
3. API keys (Qdrant, Google Gemini, Voyage AI, Redis)
4. Network connectivity (Qdrant Cloud, Redis Cloud)

Usage:
    python setup/01_verify_environment.py
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Path resolution
SCRIPT_DIR = Path(__file__).resolve().parent
WEEK_DIR = SCRIPT_DIR.parent          # week5_production/
PROJECT_ROOT = WEEK_DIR.parent        # rag-accelerator-code/


# ---------------------------------------------------------------------------
# Check functions
# ---------------------------------------------------------------------------

def check_python_version() -> bool:
    """Check that Python 3.11+ is available."""
    major, minor = sys.version_info[:2]
    version_str = f"{major}.{minor}.{sys.version_info[2]}"

    if major >= 3 and minor >= 11:
        print(f"   PASS  Python {version_str}")
        return True
    else:
        print(f"   FAIL  Python {version_str} (need 3.11+)")
        return False


def check_packages() -> bool:
    """Check that required Python packages are installed."""
    required_packages = [
        ("fastapi", "fastapi"),
        ("uvicorn", "uvicorn"),
        ("haystack", "haystack-ai"),
        ("haystack_integrations.components.embedders.voyage_embedders", "voyage-embedders-haystack"),
        ("haystack_integrations.components.embedders.fastembed", "fastembed-haystack"),
        ("haystack_integrations.components.generators.google_genai", "google-genai-haystack"),
        ("fastembed", "fastembed"),
        ("redis", "redis"),
        ("qdrant_client", "qdrant-client"),
        ("voyageai", "voyageai"),
        ("pydantic_settings", "pydantic-settings"),
        ("dotenv", "python-dotenv"),
        ("numpy", "numpy"),
        ("streamlit", "streamlit"),
    ]

    all_ok = True
    for import_name, pip_name in required_packages:
        try:
            __import__(import_name)
            print(f"   PASS  {pip_name}")
        except ImportError:
            print(f"   FAIL  {pip_name} (pip install {pip_name})")
            all_ok = False

    # Optional packages
    optional_packages = [
        ("opik", "opik"),
    ]

    for import_name, pip_name in optional_packages:
        try:
            __import__(import_name)
            print(f"   PASS  {pip_name} (optional)")
        except ImportError:
            print(f"   SKIP  {pip_name} (optional - observability)")

    return all_ok


def check_env_vars() -> bool:
    """Check that required environment variables are set."""
    required_vars = {
        "QDRANT_URL": "Qdrant Cloud URL (https://cloud.qdrant.io/)",
        "QDRANT_API_KEY": "Qdrant Cloud API key",
        "GOOGLE_API_KEY": "Google Gemini API key (https://aistudio.google.com/apikey)",
        "VOYAGE_API_KEY": "Voyage AI API key (https://dash.voyageai.com/)",
        "REDIS_HOST": "Redis Cloud host",
        "REDIS_PASSWORD": "Redis Cloud password",
    }

    all_ok = True
    for var, description in required_vars.items():
        value = os.getenv(var)
        if value and value.strip() and not value.startswith("your_"):
            # Mask the value for security
            masked = value[:8] + "..." if len(value) > 8 else "***"
            print(f"   PASS  {var} = {masked}")
        else:
            print(f"   FAIL  {var} not set")
            print(f"          Get it from: {description}")
            all_ok = False

    return all_ok


def check_qdrant_connection() -> bool:
    """Test connectivity to Qdrant Cloud."""
    try:
        from qdrant_client import QdrantClient

        url = os.getenv("QDRANT_URL")
        api_key = os.getenv("QDRANT_API_KEY")
        collection = os.getenv("QDRANT_COLLECTION", "week3_hybrid_recursive")

        if not url or not api_key:
            print("   SKIP  Qdrant (missing credentials)")
            return False

        client = QdrantClient(url=url, api_key=api_key, timeout=10)
        collections = client.get_collections()
        collection_names = [c.name for c in collections.collections]

        if collection in collection_names:
            info = client.get_collection(collection)
            print(f"   PASS  Qdrant connected: {collection} ({info.points_count} documents)")
            return True
        else:
            print(f"   WARN  Qdrant connected but collection '{collection}' not found")
            print(f"          Available: {collection_names}")
            print(f"          Run: python setup/02_index_documents.py")
            return True  # Connection works, collection just needs creating

    except Exception as e:
        print(f"   FAIL  Qdrant connection: {str(e)[:100]}")
        return False


def check_redis_connection() -> bool:
    """Test connectivity to Redis Cloud."""
    try:
        import redis

        host = os.getenv("REDIS_HOST", "localhost")
        port = int(os.getenv("REDIS_PORT", "6379"))
        password = os.getenv("REDIS_PASSWORD", "")
        username = os.getenv("REDIS_USERNAME", "default")
        use_ssl = os.getenv("REDIS_SSL", "true").lower() == "true"

        client = redis.Redis(
            host=host,
            port=port,
            username=username,
            password=password,
            ssl=use_ssl,
            socket_timeout=10,
            decode_responses=True,
        )

        client.ping()
        info = client.info("memory")
        used_mb = info.get("used_memory_human", "unknown")
        print(f"   PASS  Redis connected: {host}:{port} (memory: {used_mb})")
        return True

    except Exception as e:
        print(f"   FAIL  Redis connection: {str(e)[:100]}")
        return False


def check_google_api() -> bool:
    """Verify Google Gemini API key works."""
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key or api_key.startswith("your_"):
            print("   SKIP  Google Gemini (missing API key)")
            return False

        from haystack_integrations.components.generators.google_genai import GoogleGenAIChatGenerator
        from haystack.dataclasses import ChatMessage

        generator = GoogleGenAIChatGenerator(model="gemini-2.5-flash")
        result = generator.run(messages=[ChatMessage.from_user("Say 'OK' and nothing else.")])
        reply = result["replies"][0].text.strip()

        print(f"   PASS  Google Gemini API: responded '{reply[:20]}'")
        return True

    except Exception as e:
        print(f"   FAIL  Google Gemini API: {str(e)[:100]}")
        return False


def check_voyage_api() -> bool:
    """Verify Voyage AI API key works."""
    try:
        api_key = os.getenv("VOYAGE_API_KEY")
        if not api_key or api_key.startswith("your_"):
            print("   SKIP  Voyage AI (missing API key)")
            return False

        import voyageai

        client = voyageai.Client(api_key=api_key)
        result = client.embed(["test"], model="voyage-4-lite")

        dim = len(result.embeddings[0])
        print(f"   PASS  Voyage AI API: voyage-4-lite ({dim}d)")
        return True

    except Exception as e:
        print(f"   FAIL  Voyage AI API: {str(e)[:100]}")
        return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    """Run all environment verification checks."""
    print("\n" + "=" * 70)
    print("WEEK 5: VERIFY PRODUCTION ENVIRONMENT")
    print("=" * 70)

    # Load environment
    env_file = WEEK_DIR / ".env"
    if env_file.exists():
        load_dotenv(env_file)
        print(f"\n   Loaded: {env_file}")
    else:
        # Try project root
        root_env = PROJECT_ROOT / ".env"
        if root_env.exists():
            load_dotenv(root_env)
            print(f"\n   Loaded: {root_env}")
        else:
            print(f"\n   WARNING: No .env file found")
            print(f"   Copy .env.example to .env and fill in credentials:")
            print(f"   cp {WEEK_DIR}/.env.example {WEEK_DIR}/.env")

    results = {}

    # 1. Python version
    print(f"\n{'─' * 40}")
    print("1. Python Version")
    print(f"{'─' * 40}")
    results["python"] = check_python_version()

    # 2. Packages
    print(f"\n{'─' * 40}")
    print("2. Required Packages")
    print(f"{'─' * 40}")
    results["packages"] = check_packages()

    # 3. Environment variables
    print(f"\n{'─' * 40}")
    print("3. Environment Variables")
    print(f"{'─' * 40}")
    results["env_vars"] = check_env_vars()

    # 4. Qdrant connection
    print(f"\n{'─' * 40}")
    print("4. Qdrant Cloud Connection")
    print(f"{'─' * 40}")
    results["qdrant"] = check_qdrant_connection()

    # 5. Redis connection
    print(f"\n{'─' * 40}")
    print("5. Redis Cloud Connection")
    print(f"{'─' * 40}")
    results["redis"] = check_redis_connection()

    # 6. Google Gemini API
    print(f"\n{'─' * 40}")
    print("6. Google Gemini API")
    print(f"{'─' * 40}")
    results["google"] = check_google_api()

    # 7. Voyage AI API
    print(f"\n{'─' * 40}")
    print("7. Voyage AI API")
    print(f"{'─' * 40}")
    results["voyage"] = check_voyage_api()

    # Summary
    print(f"\n{'=' * 70}")
    print("VERIFICATION SUMMARY")
    print(f"{'=' * 70}")

    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for check, ok in results.items():
        status = "PASS" if ok else "FAIL"
        print(f"   {status}  {check}")

    print(f"\n   Result: {passed}/{total} checks passed")

    if passed == total:
        print("\n   All checks passed. Ready to run the production system.")
        print("\n   Next steps:")
        print("   1. python setup/02_index_documents.py   (if collection is empty)")
        print("   2. python setup/03_setup_redis.py       (create cache index)")
        print("   3. python setup/04_smoke_test.py        (end-to-end test)")
    else:
        print("\n   Some checks failed. Fix the issues above and re-run.")
        sys.exit(1)


if __name__ == "__main__":
    main()
