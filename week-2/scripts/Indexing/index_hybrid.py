# ============================================================================
# Week 2 - Single Strategy Indexing (Hybrid Included)
# ============================================================================

import os
import sys
import json
import time
from pathlib import Path
from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).resolve().parent
WEEK2_DIR = SCRIPT_DIR.parent
PROJECT_ROOT = WEEK2_DIR.parent

sys.path.insert(0, str(SCRIPT_DIR))

from naive_chunker import NaiveChunker
from logical_chunker import SentenceChunker, RecursiveChunker
from semantic_chunker import SemanticChunkerComponent
from hybrid_chunker import HybridChunkerComponent
from create_chunking_pipeline import create_chunking_pipeline


# ----------------------------------------------------------------------------
# Load Manifest
# ----------------------------------------------------------------------------

def load_manifest(manifest_file: Path):
    if not manifest_file.exists():
        raise FileNotFoundError(f"Manifest not found: {manifest_file}")

    with open(manifest_file, "r", encoding="utf-8") as f:
        return json.load(f)


def get_data_files(manifest_file: Path, test_mode: bool):
    print("📋 Loading deduplication manifest...")
    manifest = load_manifest(manifest_file)

    selected_entries = [
        entry for entry in manifest["selected_files"]
        if entry.get("selected", True)
    ]

    if test_mode:
        selected_entries = selected_entries[:5]
        print("🧪 TEST MODE (5 files)")
    else:
        print("🚀 FULL MODE")

    file_paths = [entry["filepath"] for entry in selected_entries]

    metadata_map = {
        entry["filepath"]: {
            "content_type": entry.get("content_type", "documentation")
        }
        for entry in selected_entries
    }

    print(f"📁 Files to process: {len(file_paths)}")
    return file_paths, metadata_map


# ----------------------------------------------------------------------------
# Strategy Factory
# ----------------------------------------------------------------------------

def get_strategy(strategy_key):

    strategies = {

        "naive_medium": {
            "name": "Naive Medium (400w/50)",
            "chunker": NaiveChunker(variant="medium"),
            "collection": "week2_naive_medium"
        },

        "recursive": {
            "name": "Recursive (2000c/200)",
            "chunker": RecursiveChunker(),
            "collection": "week2_recursive"
        },

        "semantic": {
            "name": "Semantic",
            "chunker": SemanticChunkerComponent(),
            "collection": "week2_semantic"
        },

        "hybrid": {
            "name": "Hybrid",
            "chunker": HybridChunkerComponent(),
            "collection": "week2_hybrid"
        }
    }

    if strategy_key not in strategies:
        raise ValueError(f"Invalid strategy: {strategy_key}")

    return strategies[strategy_key]


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main():

    import argparse

    parser = argparse.ArgumentParser(
        description="Index a single chunking strategy"
    )

    parser.add_argument(
        "strategy",
        choices=["naive_medium", "recursive", "semantic", "hybrid"],
        help="Chunking strategy"
    )

    parser.add_argument(
        "--full",
        action="store_true",
        help="Process full dataset"
    )

    args = parser.parse_args()
    test_mode = not args.full

    load_dotenv(PROJECT_ROOT / ".env")

    manifest_file = WEEK2_DIR / "scripts" / "outputs" / "selected_files_manifest.json"

    files_to_process, metadata_map = get_data_files(
        manifest_file,
        test_mode
    )

    strategy = get_strategy(args.strategy)

    print("\n" + "=" * 70)
    print(f"📊 INDEXING STRATEGY: {strategy['name']}")
    print("🧠 EMBEDDER: all-MiniLM-L6-v2 (384d, 512 tokens)")
    print("=" * 70)

    pipeline, _ = create_chunking_pipeline(
        chunker_component=strategy["chunker"],
        collection_name=strategy["collection"],
        strategy_name=strategy["name"],
        metadata_map=metadata_map,
        embedder_type="minilm"
    )

    print("\n🚀 Starting indexing...")

    start = time.time()

    pipeline.run({
        "file_type_router": {"sources": files_to_process}
    })

    end = time.time()

    print("\n✅ Indexing complete!")
    print(f"⏱️  Time taken: {end - start:.2f} seconds")
    print(f"🎯 Collection: {strategy['collection']}")


if __name__ == "__main__":
    main()