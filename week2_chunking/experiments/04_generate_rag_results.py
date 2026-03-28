# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 2: Generate RAG Results for Single Strategy
=================================================

Queries ONE chunking strategy collection with the evaluation questions
and generates JSON results file for comparison.

Output Format:
- One JSON file per strategy run
- Contains: question, retrieved contexts, metadata, generated answer
- Enables side-by-side comparison of chunk quality

Embedder Support:
- Auto-detects embedder from collection name (_voyage suffix = Voyage API)
- Collections indexed with Voyage use Voyage text embedder for queries

Usage:
    python week2_chunking/experiments/04_generate_rag_results.py naive_medium
    python week2_chunking/experiments/04_generate_rag_results.py naive_medium_voyage
    python week2_chunking/experiments/04_generate_rag_results.py semantic --model gemini-2.5-flash

Adapted from phase2_chunking/04_generate_rag_results.py
"""

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# Path resolution - works when run from any directory
SCRIPT_DIR = Path(__file__).resolve().parent      # experiments/
WEEK_DIR = SCRIPT_DIR.parent                       # week2_chunking/
PROJECT_ROOT = WEEK_DIR.parent                     # rag-workshop-classroom/
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
RAG_RESULTS_DIR = WEEK_DIR / "rag_results"

# Add week2_chunking to path
sys.path.insert(0, str(WEEK_DIR))

# Import RAG pipeline creator (handle numbered filename)
import importlib.util
rag_pipeline_module_path = SCRIPT_DIR / "03_create_rag_pipeline.py"
spec = importlib.util.spec_from_file_location("create_rag_pipeline", rag_pipeline_module_path)
rag_pipeline_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rag_pipeline_module)
create_rag_pipeline = rag_pipeline_module.create_rag_pipeline
query_rag_pipeline = rag_pipeline_module.query_rag_pipeline
EMBEDDER_CONFIGS = rag_pipeline_module.EMBEDDER_CONFIGS


def load_evaluation_questions(questions_file: str) -> List[Dict]:
    """
    Load evaluation questions from JSON file.

    Args:
        questions_file: Path to questions JSON

    Returns:
        List of question dictionaries
    """
    with open(questions_file, 'r') as f:
        data = json.load(f)

    return data["questions"]


def generate_results_for_strategy(
    strategy_name: str,
    collection_name: str,
    questions: List[Dict],
    model: str = None
) -> Dict:
    """
    Generate RAG results for a single chunking strategy.

    Args:
        strategy_name: Human-readable strategy name
        collection_name: Qdrant collection name
        questions: List of evaluation questions
        model: Gemini model to use (optional)

    Returns:
        Dictionary with strategy results
    """
    print("\n" + "="*70)
    print(f"📊 GENERATING RESULTS: {strategy_name}")
    print("="*70)

    try:
        # Create RAG pipeline for this collection (auto-detects embedder)
        pipeline, env_config = create_rag_pipeline(collection_name, model=model)

        embedder_type = env_config.get('embedder_type', 'bge')
        embedder_name = EMBEDDER_CONFIGS[embedder_type]['name']

        print(f"🤖 Using Model: {env_config['model']}")
        print(f"🧠 Using Embedder: {embedder_name}")

        results = {
            "strategy": strategy_name,
            "collection": collection_name,
            "embedder_type": embedder_type,
            "embedder_name": embedder_name,
            "embedding_dimension": env_config.get("embedding_dimension"),
            "llm_model": env_config["model"],
            "top_k": 10,
            "dataset": "human_eval_8q",
            "generated_at": datetime.now().isoformat(),
            "results": []
        }

        print(f"\n🤖 Querying with {len(questions)} questions...")

        start_time = time.time()

        for i, q in enumerate(questions, 1):
            question_id = q["question_id"]
            question_text = q["question"]

            print(f"\n[{i}/{len(questions)}] Question {question_id}: {question_text[:60]}...")

            question_start_time = time.time()

            # Query the pipeline
            rag_result = query_rag_pipeline(pipeline, question_text)

            query_time = time.time() - question_start_time

            # Extract retrieved contexts and metadata
            contexts = []
            for rank, doc in enumerate(rag_result["retrieved_documents"], 1):
                context_meta = {
                    "rank": rank,
                    "score": doc.score,
                    "content": doc.content,
                    "metadata": {
                        # Source document info
                        "file_path": doc.meta.get("file_path", "unknown"),
                        "source_id": doc.meta.get("source_id"),
                        "source_dir": doc.meta.get("source_dir"),
                        "content_type": doc.meta.get("content_type"),
                        # Chunk position info (for traceability)
                        "split_id": doc.meta.get("split_id"),
                        "split_idx_start": doc.meta.get("split_idx_start"),
                        "_split_overlap": doc.meta.get("_split_overlap"),
                        # Chunking strategy metadata
                        "chunk_method": doc.meta.get("chunk_method", "unknown"),
                        "chunk_size": doc.meta.get("chunk_size"),
                        "chunk_overlap": doc.meta.get("chunk_overlap"),
                        "split_unit": doc.meta.get("split_unit"),
                        "detected_language": doc.meta.get("detected_language"),
                        "target_size": doc.meta.get("target_size")
                    }
                }
                contexts.append(context_meta)

            # Add to results
            question_result = {
                "question_id": question_id,
                "question": question_text,
                "category": q.get("category"),
                "difficulty": q.get("difficulty"),
                "primary_content_type": q.get("primary_content_type"),
                "retrieved_contexts": contexts,
                "generated_answer": rag_result["answer"],
                "num_contexts_retrieved": len(contexts),
                "query_time_seconds": round(query_time, 2)
            }

            results["results"].append(question_result)

            print(f"   📚 Retrieved {len(contexts)} contexts")
            print(f"   ✅ Generated response ({len(rag_result['answer'])} chars)")
            print(f"   ⏱️  Query time: {query_time:.2f}s")

            # Brief pause to avoid rate limits
            time.sleep(0.5)

        total_time = time.time() - start_time

        # Add processing time metrics
        results["processing_time"] = total_time
        results["avg_time_per_question"] = total_time / len(questions) if questions else 0

        print(f"\n✅ Completed {strategy_name}")
        print(f"⏱️  Total time: {total_time:.2f}s")
        print(f"📊 Avg time per question: {total_time / len(questions):.2f}s")

        return results

    except Exception as e:
        print(f"❌ Failed to generate results for {strategy_name}: {str(e)}")
        import traceback
        traceback.print_exc()

        return {
            "strategy": strategy_name,
            "collection": collection_name,
            "error": str(e),
            "success": False
        }


def run_single_strategy_rag(strategy_key: str, model: str = None, embedder_type: str = "bge"):
    """
    Generate RAG results for a single chunking strategy.

    Args:
        strategy_key: Strategy identifier (naive_small, naive_medium, etc.)
        model: Gemini model to use (optional)
        embedder_type: "bge" for FastEmbed BGE, "voyage" for Voyage API

    Returns:
        dict: Results dictionary
    """
    # Collection suffix for non-default embedders
    collection_suffix = f"_{embedder_type}" if embedder_type != "bge" else ""

    # Define all 7 strategies
    strategies = {
        "naive_small": {
            "name": "Naive Small (200w/25)",
            "collection": f"week2_naive_small{collection_suffix}"
        },
        "naive_medium": {
            "name": "Naive Medium (400w/50)",
            "collection": f"week2_naive_medium{collection_suffix}"
        },
        "naive_large": {
            "name": "Naive Large (800w/100)",
            "collection": f"week2_naive_large{collection_suffix}"
        },
        "sentence": {
            "name": "Sentence-Based (6 sent)",
            "collection": f"week2_sentence{collection_suffix}"
        },
        "recursive": {
            "name": "Recursive (2000c/200)",
            "collection": f"week2_recursive{collection_suffix}"
        },
        "semantic": {
            "name": "Semantic (Adaptive)",
            "collection": f"week2_semantic{collection_suffix}"
        },
        "ast_code": {
            "name": "AST Code (2048c/400w)",
            "collection": f"week2_ast_code{collection_suffix}"
        }
    }

    if strategy_key not in strategies:
        print(f"❌ Invalid strategy: {strategy_key}")
        print(f"   Valid options: {', '.join(strategies.keys())}")
        return None

    strategy = strategies[strategy_key]

    # Create output directory
    RAG_RESULTS_DIR.mkdir(exist_ok=True)
    print(f"📂 Output directory: {RAG_RESULTS_DIR}")

    # Load evaluation questions
    questions_file = ARTIFACTS_DIR / "human_eval_questions.json"
    print(f"📋 Loading questions from: {questions_file}")

    if not questions_file.exists():
        print(f"❌ Questions file not found: {questions_file}")
        print("   Please ensure human_eval_questions.json is in the artifacts/ directory.")
        return None

    questions = load_evaluation_questions(str(questions_file))
    print(f"✅ Loaded {len(questions)} evaluation questions")

    print("\n" + "="*70)
    print(f"🚀 WEEK 2: GENERATING RAG RESULTS")
    print("="*70)
    print(f"📊 Strategy: {strategy['name']}")
    print(f"❓ Questions: {len(questions)}")
    print(f"📁 Output: {RAG_RESULTS_DIR}")

    # Generate results for strategy
    results = generate_results_for_strategy(
        strategy_name=strategy["name"],
        collection_name=strategy["collection"],
        questions=questions,
        model=model
    )

    # Save results to JSON file
    if results.get("success", True):  # Default to True if key missing
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Include embedder suffix in filename for non-default embedders
        embedder_suffix = f"_{embedder_type}" if embedder_type != "bge" else ""
        output_file = RAG_RESULTS_DIR / f"rag_results_{strategy_key}{embedder_suffix}_{timestamp}.json"

        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)

        print(f"\n💾 Saved: {output_file.name}")
        print(f"📁 Full path: {output_file}")

        print("\n🎯 Next Steps:")
        print("1. Review JSON file in rag_results/")
        print("2. Run evaluation: python experiments/05_evaluate_results.py")
        print("3. View results: streamlit run experiments/06_view_results.py")

    return results


def main():
    """Main function with command line options."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate RAG results for a single chunking strategy"
    )
    parser.add_argument(
        "strategy",
        choices=["naive_small", "naive_medium", "naive_large",
                 "sentence", "recursive", "semantic", "ast_code"],
        help="Chunking strategy to generate results for"
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Gemini model to use (default: gemini-2.5-flash)"
    )
    parser.add_argument(
        "--embedder",
        choices=["bge", "voyage"],
        default="bge",
        help="Embedder used for indexing: bge (FastEmbed) or voyage (API)"
    )

    args = parser.parse_args()

    print("🚀 Week 2: Generate RAG Results")
    print("="*50)
    print(f"🎯 Strategy: {args.strategy}")
    print(f"🧠 Embedder: {args.embedder}")
    if args.model:
        print(f"🤖 Model: {args.model}")
    else:
        print(f"🤖 Model: gemini-2.5-flash (default)")

    try:
        result = run_single_strategy_rag(args.strategy, model=args.model, embedder_type=args.embedder)

        if result and result.get("success", True):
            print("\n🎉 RAG results generated successfully!")
            sys.exit(0)
        else:
            print("\n⚠️  Generation failed. Check logs above.")
            sys.exit(1)

    except Exception as e:
        print(f"\n💥 Fatal error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
