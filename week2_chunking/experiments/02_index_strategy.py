# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 2: Index Single Chunking Strategy
=======================================

Indexes MCP documentation using ONE chunking strategy at a time.

Available Strategies:
1. naive_small - 200 words, 25 overlap
2. naive_medium - 400 words, 50 overlap
3. naive_large - 800 words, 100 overlap
4. sentence - 6 sentences, 2 sentence overlap
5. recursive - 2000 chars, 200 overlap (hierarchical)
6. semantic - adaptive size, similarity-based
7. ast_code - 2048 chars code, 400 words markdown/text

Available Embedders:
- bge (default) - BGE-large-en-v1.5 via FastEmbed (512 token limit, 1024d)
- voyage - Voyage-4-lite via API (32K token limit, 1024d)

Usage:
    python week2_chunking/experiments/02_index_strategy.py naive_medium --test
    python week2_chunking/experiments/02_index_strategy.py naive_medium --full --embedder voyage
    python week2_chunking/experiments/02_index_strategy.py recursive --full

Adapted from phase2_chunking/02_index_strategy.py
"""

import os
import sys
import json
import time
from pathlib import Path
from typing import List
from dotenv import load_dotenv

# Path resolution - works when run from any directory
SCRIPT_DIR = Path(__file__).resolve().parent      # experiments/
WEEK_DIR = SCRIPT_DIR.parent                       # week2_chunking/
PROJECT_ROOT = WEEK_DIR.parent                     # rag-workshop-classroom/
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

# Add week2_chunking to path for strategy imports
sys.path.insert(0, str(WEEK_DIR))

from strategies.naive_chunker import NaiveChunker
from strategies.logical_chunker import SentenceChunker, RecursiveChunker
from strategies.semantic_chunker import SemanticChunkerComponent
from strategies.ast_code_chunker import ASTCodeChunkerComponent

# Import pipeline creator (handle numbered filename)
import importlib.util
pipeline_module_path = SCRIPT_DIR / "01_create_chunking_pipeline.py"
spec = importlib.util.spec_from_file_location("create_chunking_pipeline", pipeline_module_path)
pipeline_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pipeline_module)
create_chunking_pipeline = pipeline_module.create_chunking_pipeline
analyze_chunk_truncation = pipeline_module.analyze_chunk_truncation
print_truncation_warning = pipeline_module.print_truncation_warning
EMBEDDER_CONFIGS = pipeline_module.EMBEDDER_CONFIGS


def load_manifest(manifest_file: Path) -> dict:
    """Load deduplication manifest."""
    if not manifest_file.exists():
        raise FileNotFoundError(
            f"Manifest not found: {manifest_file}\n"
            f"Run deduplication first: python week2_chunking/deduplication/01_deduplicate_documents.py"
        )

    with open(manifest_file, 'r') as f:
        return json.load(f)


def get_data_files(manifest_file: Path, test_mode: bool = True):
    """
    Get list of files and metadata from deduplication manifest.

    Args:
        manifest_file: Path to selected_files_manifest.json
        test_mode: If True, use balanced sample (5 code + 5 docs)

    Returns:
        Tuple[List[str], Dict]: (file_paths, metadata_map)
            - file_paths: List of file paths to index
            - metadata_map: Dict mapping filepath → metadata
    """
    # Load manifest
    print("📋 Loading deduplication manifest...")
    manifest = load_manifest(manifest_file)

    print(f"   Total files in manifest: {manifest['manifest_metadata']['files_selected']}")
    print(f"   Deduplication reduction: {manifest['manifest_metadata']['reduction_percentage']}%")

    # Get selected files
    selected_entries = [
        entry
        for entry in manifest['selected_files']
        if entry['selected']
    ]

    if test_mode:
        # Get balanced sample: 5 code files + 5 doc files
        code_entries = [e for e in selected_entries if e.get('content_type') == 'code']
        doc_entries = [e for e in selected_entries if e.get('content_type') == 'documentation']

        selected_entries = code_entries[:5] + doc_entries[:5]

        print(f"🧪 TEST MODE: Using balanced sample")
        print(f"   Code files: {len([e for e in selected_entries if e.get('content_type') == 'code'])}")
        print(f"   Doc files: {len([e for e in selected_entries if e.get('content_type') == 'documentation'])}")
    else:
        print("🚀 FULL MODE: Processing all deduplicated files")

    file_paths = [entry['filepath'] for entry in selected_entries]

    # Build metadata map: filepath → metadata
    metadata_map = {
        entry['filepath']: {
            'content_type': entry.get('content_type', 'documentation'),
            'source_dir': entry.get('source_dir', ''),
            'selection_reason': entry.get('selection_reason', '')
        }
        for entry in selected_entries
    }

    print(f"📁 Files to process: {len(file_paths)}")

    return file_paths, metadata_map


def index_strategy(
    strategy_name: str,
    chunker_component,
    collection_name: str,
    files_to_process: List[str],
    metadata_map: dict = None,
    embedder_type: str = "bge"
):
    """
    Index documents using a specific chunking strategy.

    Args:
        strategy_name: Human-readable strategy name
        chunker_component: Chunking component instance
        collection_name: Qdrant collection name
        files_to_process: List of file paths to index
        metadata_map: Optional filepath → metadata mapping from manifest
        embedder_type: "bge" for FastEmbed BGE, "voyage" for Voyage API

    Returns:
        dict: Indexing results and timing
    """
    print("\n" + "="*70)
    print(f"📊 INDEXING STRATEGY: {strategy_name}")
    print(f"🧠 EMBEDDER: {EMBEDDER_CONFIGS[embedder_type]['name']}")
    print("="*70)

    try:
        # Create pipeline for this strategy
        pipeline, env_config = create_chunking_pipeline(
            chunker_component=chunker_component,
            collection_name=collection_name,
            strategy_name=strategy_name,
            metadata_map=metadata_map,
            embedder_type=embedder_type
        )

        print(f"\n🚀 Starting indexing...")
        print(f"📁 Files to process: {len(files_to_process)}")

        start_time = time.time()

        # Run pipeline with intermediate output capture to analyze chunks
        result = pipeline.run(
            data={
                "file_type_router": {"sources": files_to_process}
            },
            include_outputs_from={"chunker"}  # Capture chunks for truncation analysis
        )

        end_time = time.time()
        processing_time = end_time - start_time

        # Get results
        documents_written = result.get("document_writer", {}).get("documents_written", 0)

        # Analyze token truncation from captured chunks
        chunked_docs = result.get("chunker", {}).get("documents", [])
        truncation_stats = {}
        if chunked_docs:
            max_tokens = env_config.get('max_tokens', 512)
            truncation_stats = analyze_chunk_truncation(chunked_docs, max_tokens=max_tokens)
            print_truncation_warning(truncation_stats, strategy_name, embedder_type)

        print(f"\n✅ Indexing completed!")
        print(f"⏱️  Processing time: {processing_time:.2f} seconds")
        print(f"📝 Documents written: {documents_written}")
        print(f"⚡ Avg time per file: {processing_time/len(files_to_process):.2f} seconds")

        return {
            "strategy": strategy_name,
            "collection": collection_name,
            "embedder": embedder_type,
            "embedding_dimension": env_config.get('embedding_dimension'),
            "documents_written": documents_written,
            "processing_time": processing_time,
            "files_processed": len(files_to_process),
            "truncation_stats": truncation_stats,
            "success": True
        }

    except Exception as e:
        print(f"❌ Indexing failed for {strategy_name}: {str(e)}")
        import traceback
        traceback.print_exc()

        return {
            "strategy": strategy_name,
            "collection": collection_name,
            "success": False,
            "error": str(e)
        }


def run_single_strategy(strategy_key: str, test_mode: bool = True, embedder_type: str = "bge"):
    """
    Index documents using a single chunking strategy.

    Args:
        strategy_key: Strategy identifier (naive_small, naive_medium, etc.)
        test_mode: If True, use subset of files for testing
        embedder_type: "bge" for FastEmbed BGE, "voyage" for Voyage API
    """
    # Load from project root .env
    env_path = PROJECT_ROOT / ".env"
    load_dotenv(env_path)

    # Collection suffix for non-default embedders
    collection_suffix = f"_{embedder_type}" if embedder_type != "bge" else ""

    # Define all 7 strategies
    strategies = {
        "naive_small": {
            "name": "Naive Small (200w/25)",
            "chunker": NaiveChunker(variant="small"),
            "collection": f"week2_naive_small{collection_suffix}"
        },
        "naive_medium": {
            "name": "Naive Medium (400w/50)",
            "chunker": NaiveChunker(variant="medium"),
            "collection": f"week2_naive_medium{collection_suffix}"
        },
        "naive_large": {
            "name": "Naive Large (800w/100)",
            "chunker": NaiveChunker(variant="large"),
            "collection": f"week2_naive_large{collection_suffix}"
        },
        "sentence": {
            "name": "Sentence-Based (6 sent)",
            "chunker": SentenceChunker(),
            "collection": f"week2_sentence{collection_suffix}"
        },
        "recursive": {
            "name": "Recursive (2000c/200)",
            "chunker": RecursiveChunker(),
            "collection": f"week2_recursive{collection_suffix}"
        },
        "semantic": {
            "name": "Semantic (Adaptive)",
            "chunker": SemanticChunkerComponent(),
            "collection": f"week2_semantic{collection_suffix}"
        },
        "ast_code": {
            "name": "AST Code (2048c/400w)",
            "chunker": ASTCodeChunkerComponent(),
            "collection": f"week2_ast_code{collection_suffix}"
        }
    }

    if strategy_key not in strategies:
        print(f"❌ Invalid strategy: {strategy_key}")
        print(f"   Valid options: {', '.join(strategies.keys())}")
        return None

    strategy = strategies[strategy_key]

    # Get manifest file path from artifacts directory
    manifest_file = ARTIFACTS_DIR / "selected_files_manifest.json"

    if not manifest_file.exists():
        print(f"❌ Manifest not found: {manifest_file}")
        print("\nRun deduplication first:")
        print("   python week2_chunking/deduplication/01_deduplicate_documents.py")
        return None

    # Get file paths and metadata from manifest
    files_to_process, metadata_map = get_data_files(manifest_file, test_mode)

    if not files_to_process:
        print("❌ No files found in manifest!")
        return None

    # Index the strategy
    result = index_strategy(
        strategy_name=strategy["name"],
        chunker_component=strategy["chunker"],
        collection_name=strategy["collection"],
        files_to_process=files_to_process,
        metadata_map=metadata_map,
        embedder_type=embedder_type
    )

    if result.get("success"):
        print(f"\n🎯 Collection created: {strategy['collection']}")
        print("   Ready for RAG queries!")

    return result


def main():
    """Main function with command line options."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Index a single chunking strategy for Week 2 experiments"
    )
    parser.add_argument(
        "strategy",
        choices=["naive_small", "naive_medium", "naive_large",
                 "sentence", "recursive", "semantic", "ast_code"],
        help="Chunking strategy to index"
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Process all files (~184 files)"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Process test subset only (~10 files) [DEFAULT]"
    )
    parser.add_argument(
        "--embedder",
        choices=["bge", "voyage"],
        default="bge",
        help="Embedder to use: bge (FastEmbed, 512 tokens) or voyage (API, 32K tokens)"
    )

    args = parser.parse_args()

    # Determine test mode
    test_mode = not args.full  # Default to test mode unless --full specified

    print("🚀 Week 2: Single Strategy Indexing")
    print("="*50)
    print(f"🎯 Strategy: {args.strategy}")
    print(f"🧠 Embedder: {args.embedder}")
    print(f"🧪 Mode: {'TEST (subset)' if test_mode else 'FULL (all files)'}")

    try:
        result = run_single_strategy(args.strategy, test_mode=test_mode, embedder_type=args.embedder)

        if result and result.get("success"):
            print("\n🎉 Strategy indexed successfully!")
            sys.exit(0)
        else:
            print("\n⚠️  Indexing failed. Check logs above.")
            sys.exit(1)

    except Exception as e:
        print(f"\n💥 Fatal error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
