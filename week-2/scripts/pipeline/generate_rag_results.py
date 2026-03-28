
# ============================================================================
# The Engineer's RAG Accelerator - Adapted for Capstone Week 2
#
# This script generates RAG results for the test questions and saves them for evaluation.
# Input: week-1/data/processed/
# Output: week-2/evaluations/rag_results/
# ============================================================================

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# Path resolution - works when run from any directory
SCRIPT_DIR = Path(__file__).resolve().parent      # scripts/
WEEK2_DIR = SCRIPT_DIR.parent                     # week-2/
PROJECT_ROOT = WEEK2_DIR.parent                   # rag-capstone-week-1/
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
RAG_RESULTS_DIR = WEEK2_DIR / "evaluations" / "rag_results"

# Add week-2/scripts to path for imports
sys.path.insert(0, str(SCRIPT_DIR))

# Import RAG pipeline creator
import importlib.util
rag_pipeline_module_path = SCRIPT_DIR / "create_rag_pipeline.py"
spec = importlib.util.spec_from_file_location("create_rag_pipeline", rag_pipeline_module_path)
rag_pipeline_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rag_pipeline_module)
create_rag_pipeline = rag_pipeline_module.create_rag_pipeline
query_rag_pipeline = rag_pipeline_module.query_rag_pipeline
EMBEDDER_CONFIGS = rag_pipeline_module.EMBEDDER_CONFIGS

def load_evaluation_questions(questions_file: str) -> List[Dict]:
	with open(questions_file, 'r') as f:
		data = json.load(f)
	# If the loaded data is a list, return it directly. If it's a dict with 'questions', return that.
	if isinstance(data, list):
		return data
	elif isinstance(data, dict) and "questions" in data:
		return data["questions"]
	else:
		raise ValueError("Questions file must be a list or contain a 'questions' key.")

def generate_results_for_strategy(
	strategy_name: str,
	collection_name: str,
	questions: List[Dict],
	model: str = None
):
	print("\n" + "="*70)
	print(f"📊 GENERATING RESULTS: {strategy_name}")
	print("="*70)
	try:
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
			"dataset": "test_questions",
			"generated_at": datetime.now().isoformat(),
			"results": []
		}
		print(f"\n🤖 Querying with {len(questions)} questions...")
		start_time = time.time()
		for i, q in enumerate(questions, 1):
			question_id = q["id"]
			question_text = q["question"]
			print(f"\n[{i}/{len(questions)}] Question {question_id}: {question_text[:60]}...")
			question_start_time = time.time()
			rag_result = query_rag_pipeline(pipeline, question_text)
			query_time = time.time() - question_start_time
			contexts = []
			for rank, doc in enumerate(rag_result["retrieved_documents"], 1):
				context_meta = {
					"rank": rank,
					"score": doc.score,
					"content": doc.content,
					"metadata": {
						"file_path": doc.meta.get("file_path", "unknown"),
						"source_id": doc.meta.get("source_id"),
						"source_dir": doc.meta.get("source_dir"),
						"content_type": doc.meta.get("content_type"),
						"split_id": doc.meta.get("split_id"),
						"split_idx_start": doc.meta.get("split_idx_start"),
						"_split_overlap": doc.meta.get("_split_overlap"),
						"chunk_method": doc.meta.get("chunk_method", "unknown"),
						"chunk_size": doc.meta.get("chunk_size"),
						"chunk_overlap": doc.meta.get("chunk_overlap"),
						"split_unit": doc.meta.get("split_unit"),
						"detected_language": doc.meta.get("detected_language"),
						"target_size": doc.meta.get("target_size")
					}
				}
				contexts.append(context_meta)
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
			time.sleep(0.5)
		total_time = time.time() - start_time
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
	collection_suffix = f"_{embedder_type}" if embedder_type != "bge" else ""
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
		   "hybrid": {
			   "name": "Hybrid (Semantic + AST)",
			   "collection": "week2_hybrid"
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
	RAG_RESULTS_DIR.mkdir(exist_ok=True)
	print(f"📂 Output directory: {RAG_RESULTS_DIR}")
	questions_file = WEEK2_DIR / "evaluations" / "test_questions.json"
	print(f"📋 Loading questions from: {questions_file}")
	if not questions_file.exists():
		print(f"❌ Questions file not found: {questions_file}")
		print("   Please ensure test_questions.json is in the week-2/evaluations/ directory.")
		return None
	questions = load_evaluation_questions(str(questions_file))
	print(f"✅ Loaded {len(questions)} evaluation questions")
	print("\n" + "="*70)
	print(f"🚀 WEEK 2: GENERATING RAG RESULTS")
	print("="*70)
	print(f"📊 Strategy: {strategy['name']}")
	print(f"❓ Questions: {len(questions)}")
	print(f"📁 Output: {RAG_RESULTS_DIR}")
	results = generate_results_for_strategy(
		strategy_name=strategy["name"],
		collection_name=strategy["collection"],
		questions=questions,
		model=model
	)
	if results.get("success", True):
		timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
		embedder_suffix = f"_{embedder_type}" if embedder_type != "bge" else ""
		output_file = RAG_RESULTS_DIR / f"rag_results_{strategy_key}{embedder_suffix}_{timestamp}.json"
		with open(output_file, 'w') as f:
			json.dump(results, f, indent=2)
		print(f"\n💾 Saved: {output_file.name}")
		print(f"📁 Full path: {output_file}")
		print("\n🎯 Next Steps:")
		print("1. Review JSON file in rag_results/")
		print("2. Run evaluation: python scripts/chunk_quality_eval.py")
		print("3. View results: streamlit run scripts/chunk_eval_viewer.py")
	return results

def main():
	import argparse
	parser = argparse.ArgumentParser(
		description="Generate RAG results for a single chunking strategy"
	)
	parser.add_argument(
		"strategy",
		choices=["naive_small", "naive_medium", "naive_large",
				 "sentence", "recursive", "semantic", "ast_code", "hybrid"],
		help="Chunking strategy to generate results for"
	)
	parser.add_argument(
		"--model",
		type=str,
		default=None,
		help="LLM model to use (default: gemini-2.5-flash)"
	)
	parser.add_argument(
		   "--embedder",
		   choices=["bge", "minilm"],
		   default="bge",
		   help="Embedder used for indexing: bge (FastEmbed) or minilm (MiniLM 384d)"
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
