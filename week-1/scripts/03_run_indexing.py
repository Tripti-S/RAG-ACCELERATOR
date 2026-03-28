# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Phase 1: Run FastEmbed Indexing (Test with Subset First)
=======================================================

Process Probability for Data Science documentation using FastEmbed. Starts with a small subset for testing,
then can scale to full dataset.

Strategy:
1. Test with first 5 markdown files + 1 GitHub digest
2. If successful, process remaining files
3. No rate limiting needed - FastEmbed is local!
"""

import os
import time
from pathlib import Path
from typing import List
from dotenv import load_dotenv
from tqdm import tqdm

# Get project root (script -> rag_pipeline -> week1_foundations -> root)
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent

# Import from renamed module in current directory
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import from renamed module (need to import dynamically)
import importlib.util
module_path = os.path.join(os.path.dirname(__file__), "02_create_pipeline.py")
spec = importlib.util.spec_from_file_location("create_pipeline", module_path)
create_pipeline_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(create_pipeline_module)
create_fastembed_indexing_pipeline = create_pipeline_module.create_fastembed_indexing_pipeline

def get_file_subset(data_dir: str, test_mode: bool = True, single_dir: str = None):
    """
    Get files from processed dataset (markdown + conversational)
    """
    candidates = [
        Path(data_dir) / "processed",
        PROJECT_ROOT / "week-1" / "data" / "processed",
        SCRIPT_DIR.parent / "data" / "processed",
    ]

    data_path = None
    for candidate in candidates:
        if candidate.exists():
            data_path = candidate
            break

    if data_path is None:
        print("❌ Could not find processed dataset directory. Checked:")
        for candidate in candidates:
            print(f"   - {candidate}")
        return []

    if single_dir:
        single_dir_path = data_path / single_dir
        if not single_dir_path.exists():
            print(f"❌ single_dir not found: {single_dir_path}")
            return []

        md_files = list(single_dir_path.rglob("*.md"))
        txt_files = list(single_dir_path.rglob("*.txt"))
    else:
        markdown_path = data_path / "markdown"
        conversational_path = data_path / "conversational"

        md_files = list(markdown_path.rglob("*.md")) if markdown_path.exists() else []
        txt_files = list(conversational_path.rglob("*.txt")) if conversational_path.exists() else []

    all_files = sorted(md_files + txt_files)

    print(f"📁 Processed dataset detected at: {data_path}")
    print(f"   - Markdown files: {len(md_files)}")
    print(f"   - Conversational TXT files: {len(txt_files)}")
    print(f"   - Total files: {len(all_files)}")

    if test_mode and len(all_files) > 15:
        print("🧪 TEST MODE: Using first 15 files")
        return [str(f) for f in all_files[:15]]
    else:
        return [str(f) for f in all_files]

def run_fastembed_indexing(collection_name: str = None, test_mode: bool = True, single_dir: str = None):
    """
    Run the FastEmbed indexing pipeline.
    
    Args:
        collection_name (str): Custom collection name
        test_mode (bool): If True, process only subset of files
        single_dir (str): If specified, process only files from this directory (e.g., 'probability_python_sdk_filtered')
    """
    load_dotenv(PROJECT_ROOT / ".env")

    # Get data directory (always relative to project root)
    data_dir = str(PROJECT_ROOT / "data")

    print(f"📂 Looking for data in: {data_dir}")
    files_to_process = get_file_subset(data_dir, test_mode, single_dir)
    
    if not files_to_process:
        print("❌ No files found to process!")
        return
    
    print("\n🔧 Creating FastEmbed indexing pipeline...")
    
    try:
        # Create the pipeline
        pipeline, env_config = create_fastembed_indexing_pipeline(collection_name)
        
        print(f"\n🚀 Starting indexing process...")
        print(f"🧠 Model: {env_config['fastembed_model']}")
        print(f"📊 Target Collection: {collection_name or env_config['collection_name']}")
        print(f"📁 Files to process: {len(files_to_process)}")
        
        start_time = time.time()
        
        # Run the pipeline
        print("\n⚡ Processing files (no rate limits with FastEmbed!)...")
        
        result = pipeline.run(
            data={
                "file_type_router": {"sources": files_to_process}
            }
        )
        
        end_time = time.time()
        processing_time = end_time - start_time

        # Display results
        print(f"\n✅ FastEmbed indexing completed!")
        print(f"⏱️  Total processing time: {processing_time:.2f} seconds")
        print(f"📊 Average time per file: {processing_time/len(files_to_process):.2f} seconds")

        # Check if documents were written
        documents_written = result.get("document_writer", {}).get("documents_written", 0)
        if documents_written:
            print(f"📝 Documents written to Qdrant: {documents_written}")

        # --- Save results to required files ---
        import json
        # 1. Save ag_results_naive_baseline.json
        naive_baseline_path = Path(r"C:/Users/singhtripti/rag-capstone-week-2/week-2/scripts/week1_naive/ag_results_naive_baseline.json")
        naive_baseline_path.parent.mkdir(parents=True, exist_ok=True)
        with open(naive_baseline_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)

        # 2. Save to eval_results and rag_results (dummy content for now)
        eval_results_path = Path(r"C:/Users/singhtripti/rag-capstone-week-2/week-2/evaluations/eval_results/naive_eval_results.json")
        rag_results_path = Path(r"C:/Users/singhtripti/rag-capstone-week-2/week-2/evaluations/rag_results/naive_rag_results.json")
        eval_results_path.parent.mkdir(parents=True, exist_ok=True)
        rag_results_path.parent.mkdir(parents=True, exist_ok=True)
        with open(eval_results_path, "w", encoding="utf-8") as f:
            json.dump({"summary": "Naive baseline eval results", "result": result}, f, indent=2)
        with open(rag_results_path, "w", encoding="utf-8") as f:
            json.dump({"summary": "Naive baseline rag results", "result": result}, f, indent=2)

        # 3. Print to walkthrough_traces/naive_full.txt
        walkthrough_path = Path(r"C:/Users/singhtripti/rag-capstone-week-2/week-2/artifacts/walkthrough_traces/naive_full.txt")
        walkthrough_path.parent.mkdir(parents=True, exist_ok=True)
        with open(walkthrough_path, "w", encoding="utf-8") as f:
            f.write("FastEmbed Indexing Walkthrough (Naive Baseline)\n")
            f.write(f"Processed files: {len(files_to_process)}\n")
            f.write(f"Total processing time: {processing_time:.2f} seconds\n")
            f.write(f"Average time per file: {processing_time/len(files_to_process):.2f} seconds\n")
            f.write(f"Documents written: {documents_written}\n")
            f.write("\nResult keys: " + ", ".join(result.keys()) + "\n")

        print(f"\n📝 Results written to: {naive_baseline_path}")
        print(f"📝 Eval results: {eval_results_path}")
        print(f"📝 RAG results: {rag_results_path}")
        print(f"📝 Walkthrough trace: {walkthrough_path}")

        print("\n🎯 Next steps:")
        if test_mode:
            print("1. Verify documents in Qdrant")
            print("2. Test RAG queries")
            print("3. If successful, run with test_mode=False for full dataset")
        else:
            print("1. All documents indexed successfully!")
            print("2. Ready for RAG queries")
            print("3. Test with test_fastembed_rag.py")

        return result
        
    except Exception as e:
        print(f"❌ FastEmbed indexing failed: {str(e)}")
        import traceback
        traceback.print_exc()
        raise

def main():
    """Main function with command line options."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Run FastEmbed indexing for Probability for Data Science RAG")
    parser.add_argument("--collection", help="Custom collection name")
    parser.add_argument("--full", action="store_true", help="Process all files (~250 files, 5-10 minutes)")
    parser.add_argument("--test", action="store_true", help="Process test subset only (~13 files, 30-60 seconds) [DEFAULT]")
    parser.add_argument("--single-dir", help="Process only files from single directory (e.g., 'probability_python_sdk_filtered')")
    
    args = parser.parse_args()
    
    # Determine test mode
    if args.full:
        test_mode = False
    else:
        test_mode = True  # Default to test mode
    
    print("🚀 FastEmbed Indexing for Probability for Data Science RAG")
    print("=" * 50)
    
    mode_str = "TEST (subset)" if test_mode else "FULL (all files)"
    if args.single_dir:
        mode_str = f"SINGLE DIR: {args.single_dir}"
    print(f"🎯 Mode: {mode_str}")
    
    if args.collection:
        print(f"📊 Collection: {args.collection}")
    
    try:
        result = run_fastembed_indexing(
            collection_name=args.collection,
            test_mode=test_mode,
            single_dir=args.single_dir
        )
        
        print("\n🎉 Indexing completed successfully!")
        
    except Exception as e:
        print(f"\n💥 Indexing failed: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()