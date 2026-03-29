# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Verify and Index Documents
====================================

Checks whether the week3_hybrid_recursive collection exists with documents.
If the collection is empty or missing, provides instructions for indexing.

The production backend expects documents to already exist in the week3_hybrid_recursive
collection (indexed during Week 3). This script verifies that prerequisite
and guides you through re-indexing if needed.

Usage:
    # Check if collection exists and has documents
    python setup/02_index_documents.py

    # Force check and show collection details
    python setup/02_index_documents.py --details
"""

import os
import sys
import argparse
from pathlib import Path

from dotenv import load_dotenv

# Path resolution
SCRIPT_DIR = Path(__file__).resolve().parent
WEEK_DIR = SCRIPT_DIR.parent          # week5_production/
PROJECT_ROOT = WEEK_DIR.parent        # rag-accelerator-code/


def load_environment() -> dict:
    """Load and validate environment variables."""
    # Try week5 .env first, then project root
    env_file = WEEK_DIR / ".env"
    if not env_file.exists():
        env_file = PROJECT_ROOT / ".env"

    if env_file.exists():
        load_dotenv(env_file)

    required_vars = ["QDRANT_URL", "QDRANT_API_KEY"]
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
            f"Set them in {WEEK_DIR}/.env"
        )

    env_vars["QDRANT_COLLECTION"] = os.getenv("QDRANT_COLLECTION", "week3_hybrid_recursive")
    return env_vars


def check_collection(env_vars: dict, show_details: bool = False) -> dict:
    """
    Check if the target collection exists and has documents.

    Args:
        env_vars: Environment variables with Qdrant credentials
        show_details: Whether to print detailed collection info

    Returns:
        Dict with collection status information
    """
    from qdrant_client import QdrantClient

    client = QdrantClient(
        url=env_vars["QDRANT_URL"],
        api_key=env_vars["QDRANT_API_KEY"],
        timeout=15,
    )

    collection_name = env_vars["QDRANT_COLLECTION"]

    # List all collections
    collections = client.get_collections()
    collection_names = [c.name for c in collections.collections]

    print(f"\n   Qdrant collections found: {len(collection_names)}")

    if collection_name not in collection_names:
        return {
            "exists": False,
            "collection": collection_name,
            "document_count": 0,
            "available_collections": collection_names,
        }

    # Get collection details
    info = client.get_collection(collection_name)
    doc_count = info.points_count

    print(f"   Collection: {collection_name}")
    print(f"   Documents: {doc_count}")

    if show_details:
        print(f"\n   Collection Details:")
        print(f"   Status: {info.status}")
        print(f"   Vectors count: {info.vectors_count}")
        print(f"   Indexed vectors: {info.indexed_vectors_count}")

        # Show vector config
        if hasattr(info.config, "params") and info.config.params:
            vectors = info.config.params.vectors
            if isinstance(vectors, dict):
                for name, config in vectors.items():
                    print(f"   Vector '{name}': {config.size}d, {config.distance}")
            else:
                print(f"   Vector: {vectors.size}d, {vectors.distance}")

    return {
        "exists": True,
        "collection": collection_name,
        "document_count": doc_count,
        "available_collections": collection_names,
    }


def main():
    """Check collection status and guide indexing if needed."""
    parser = argparse.ArgumentParser(
        description="Week 5: Verify document collection for production RAG"
    )
    parser.add_argument(
        "--details",
        action="store_true",
        help="Show detailed collection information"
    )
    args = parser.parse_args()

    print("\n" + "=" * 70)
    print("WEEK 5: VERIFY DOCUMENT COLLECTION")
    print("=" * 70)

    try:
        env_vars = load_environment()
        result = check_collection(env_vars, show_details=args.details)

        print(f"\n{'=' * 70}")

        if not result["exists"]:
            print("COLLECTION NOT FOUND")
            print(f"{'=' * 70}")
            print(f"\n   The collection '{result['collection']}' does not exist.")
            print(f"   Available collections: {result['available_collections']}")
            print(f"\n   To create it, run the Week 3 indexing pipeline:")
            print(f"   cd {PROJECT_ROOT / 'week-3' / 'scripts' / 'indexing'}")
            print(f"   python 01_index_hybrid.py --full")
            print(f"\n   Or change QDRANT_COLLECTION in .env to use an existing collection.")
            sys.exit(1)

        elif result["document_count"] == 0:
            print("COLLECTION EMPTY")
            print(f"{'=' * 70}")
            print(f"\n   The collection '{result['collection']}' exists but has 0 documents.")
            print(f"\n   To index documents, run the Week 3 indexing pipeline:")
            print(f"   cd {PROJECT_ROOT / 'week-3' / 'scripts' / 'indexing'}")
            print(f"   python 01_index_hybrid.py --full")
            sys.exit(1)

        else:
            print("COLLECTION READY")
            print(f"{'=' * 70}")
            print(f"\n   Collection '{result['collection']}' has {result['document_count']} documents.")
            print(f"   Ready for production RAG queries.")
            print(f"\n   Next: python setup/03_setup_redis.py")

    except Exception as e:
        print(f"\nError: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
