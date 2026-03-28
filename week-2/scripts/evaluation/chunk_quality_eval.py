

# ============================================================================
# The Engineer's RAG Accelerator - Adapted for Capstone Week 2
#
# This script evaluates chunk quality for the selected strategy using a hybrid two-stage LLM approach.
# Input: week-2/evaluations/rag_results/
# Output: week-2/evaluations/eval_results/
# ============================================================================

import argparse
import json
import time
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict
import os
from dotenv import load_dotenv
from openai import OpenAI



# Path resolution
SCRIPT_DIR = Path(__file__).resolve().parent
WEEK2_DIR = SCRIPT_DIR.parent.parent
PROJECT_ROOT = WEEK2_DIR.parent
RAG_RESULTS_DIR = WEEK2_DIR / "evaluations" / "rag_results"
EVALUATIONS_DIR = WEEK2_DIR / "evaluations" / "eval_results"
load_dotenv(PROJECT_ROOT / ".env")

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
client = OpenAI()

def load_rag_results(strategy: str) -> Dict:
	import re
	pattern = re.compile(rf"rag_results_{re.escape(strategy)}_\d{{8}}_\d{{6}}\.json$")
	files = [f for f in RAG_RESULTS_DIR.iterdir() if f.is_file() and pattern.match(f.name)]
	if not files:
		raise FileNotFoundError(f"No results found for strategy: {strategy}")
	latest_file = sorted(files)[-1]
	with open(latest_file, 'r') as f:
		return json.load(f)

def call_llm(prompt: str, max_retries: int = 3, use_thinking: bool = False) -> Dict:
	for attempt in range(max_retries):
		try:
			response = client.chat.completions.create(
				model=MODEL_NAME,
				messages=[{"role": "user", "content": prompt}],
				response_format={"type": "json_object"},
				temperature=0.1,
			)

			return json.loads(response.choices[0].message.content)

		except Exception as e:
			if "rate" in str(e).lower() and attempt < max_retries - 1:
				wait_time = (2 ** attempt) * 5
				print(f"Rate limited, retrying in {wait_time}s...")
				time.sleep(wait_time)
			else:
				raise


def build_stage1_prompt(question: str, strategy_name: str, chunks: List[Dict]) -> str:
	prompt = f"""You are analyzing chunk quality for a RAG system.

**THE QUESTION:**
{question}

**STRATEGY:** {strategy_name.upper()}

**CHUNKS TO ANALYZE:**
"""
	for idx, chunk in enumerate(chunks[:10]):
		content = chunk.get("content", "")
		file_path = chunk.get("metadata", {}).get("file_path", "unknown")
		file_name = Path(file_path).name
		score = chunk.get("score", 0)
		prompt += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
**CHUNK {idx + 1}** (file: {file_name}, score: {score:.3f})
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{content}
"""
	prompt += """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**ANALYZE EACH CHUNK FOR THIS QUESTION**

For EACH chunk, assess:

1. **cut_mid_answer** (true/false): Does this chunk cut off content that would help answer THE QUESTION?
   - true: The chunk ends/starts in a way that loses answer-relevant information
   - false: Any cut-off doesn't affect the answer, OR the chunk is complete
   (A structural cut-off that doesn't lose answer content = false)

2. **signal_pct** (0-100): What percentage of this chunk is RELEVANT to answering THE QUESTION?
   - 80-100: Highly focused, almost all content helps answer the question
   - 50-79: Majority relevant, some extra content
   - 20-49: Less than half relevant, lots of unrelated content
   - 0-19: Mostly irrelevant to this question

   BE STRICT: If a chunk has 5 paragraphs but only 1 helps answer the question, that's ~20%.

3. **useful** ("high"/"medium"/"low"): Overall usefulness for answering THIS question

4. **note**: Brief explanation (1 sentence)

**OUTPUT FORMAT (JSON):**

{
  "strategy": "<strategy_name>",
  "chunks": {
	"1": {"cut_mid_answer": true/false, "signal_pct": <0-100>, "useful": "high/medium/low", "note": "<brief>"},
	"2": {...},
	...
	"10": {...}
  },
  "summary": {
	"cut_mid_answer_count": <total>,
	"avg_signal_pct": <average>,
	"high_useful_count": <count with useful=high>,
	"assessment": "<1-2 sentences on this strategy for THIS question>"
  }
}

**BE STRICT:**
- Small chunks: Check if cut-offs lose answer content
- Large chunks: Check signal_pct carefully (often <50% is actually relevant)
"""
	return prompt

def build_stage2_prompt(
	question: str,
	strategies: List[str],
	all_analyses: Dict[str, Dict],
	all_chunks: Dict[str, List[Dict]]
) -> str:
	prompt = f"""You are making a HOLISTIC judgment on which chunking strategy is best.

**THE QUESTION:**
{question}

You have:
1. COMPLETE Stage 1 analysis (per-chunk assessments with full notes)
2. The actual chunks for reference

Your job: Make a NUANCED judgment considering tradeoffs.
"""
	prompt += """
══════════════════════════════════════════════════════════════════════
					STAGE 1 ANALYSIS (COMPLETE)
══════════════════════════════════════════════════════════════════════
"""
	for strategy in strategies:
		analysis = all_analyses.get(strategy, {})
		summary = analysis.get("summary", {})
		chunks_data = analysis.get("chunks", {})
		prompt += f"""
┌──────────────────────────────────────────────────────────────────────
│ STRATEGY: {strategy.upper()}
├──────────────────────────────────────────────────────────────────────
│ SUMMARY:
│   - Cut mid-answer count: {summary.get('cut_mid_answer_count', '?')}
│   - Average signal %: {summary.get('avg_signal_pct', '?')}%
│   - High useful count: {summary.get('high_useful_count', '?')}
│   - Assessment: {summary.get('assessment', 'N/A')}
├──────────────────────────────────────────────────────────────────────
│ PER-CHUNK ANALYSIS:
"""
		for i in range(1, 11):
			c = chunks_data.get(str(i), {})
			if c:
				cut = c.get("cut_mid_answer", False)
				sig = c.get("signal_pct", 0)
				useful = c.get("useful", "?")
				note = c.get("note", "")
				prompt += f"""│
│   Chunk {i}:
│     - cut_mid_answer: {cut}
│     - signal_pct: {sig}%
│     - useful: {useful}
│     - note: {note}
"""
		prompt += "└──────────────────────────────────────────────────────────────────────\n"
	prompt += """
══════════════════════════════════════════════════════════════════════
					ACTUAL CHUNKS (ALL 10 PER STRATEGY)
══════════════════════════════════════════════════════════════════════
"""
	for strategy in strategies:
		chunks = all_chunks.get(strategy, [])
		prompt += f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ {strategy.upper():^68} ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""
		for idx, chunk in enumerate(chunks[:10]):
			content = chunk.get("content", "")
			file_name = Path(chunk.get("metadata", {}).get("file_path", "unknown")).name
			score = chunk.get("score", 0)
			prompt += f"""▼ Chunk {idx + 1} ({file_name}, score: {score:.3f})
{content}

"""
	num_strategies = len(strategies)
	ordinals = ["1st", "2nd", "3rd", "4th", "5th"][:num_strategies]
	ranking_format = ",\n    ".join([f'"{o}": "<strategy_name>"' for o in ordinals])
	prompt += f"""
══════════════════════════════════════════════════════════════════════
						 YOUR JUDGMENT
══════════════════════════════════════════════════════════════════════

**KEY TRADEOFFS TO CONSIDER:**

- Small chunks: May have cut-offs but often HIGHER signal (focused)
- Large chunks: Fewer cut-offs but often LOWER signal (diluted with irrelevant content)
- Medium chunks: May BALANCE both - fewer critical cut-offs, reasonable signal

**CONSIDER:**
- Is a strategy's high signal% more valuable than another's low cut-off count?
- Are the cut-offs actually losing critical answer content, or just structural?
- Which strategy would actually help an LLM answer THIS question better?

**OUTPUT FORMAT (JSON):**

{{
  "ranking": {{
	{ranking_format}
  }},
  "reasoning": "<2-3 sentences explaining your judgment, noting specific tradeoffs>",
  "key_insight": "<What was the deciding factor between the strategies?>"
}}

Rank ALL {num_strategies} strategies. Use the Stage 1 analysis AND the actual chunks to make your judgment.
"""
	return prompt

def run_evaluation(strategies: List[str], test_mode: bool = False):
	print("=" * 70)
	print("HYBRID TWO-STAGE CHUNK QUALITY EVALUATION")
	print("=" * 70)
	print(f"Strategies: {', '.join(strategies)}")
	print(f"Model: {MODEL_NAME}")
	print(f"Stage 1: {len(strategies)} calls per question (per-strategy analysis)")
	print(f"Stage 2: 1 call per question (ranking with full Stage 1 context)")
	if test_mode:
		print("\n🧪 TEST MODE: Only evaluating 1 question")
	print("=" * 70)
	if not RAG_RESULTS_DIR.exists():
		raise FileNotFoundError(f"RAG results directory not found: {RAG_RESULTS_DIR}")

	EVALUATIONS_DIR.mkdir(parents=True, exist_ok=True)
	timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
	print("\n📂 Loading RAG results...")
	all_strategies_results = {}
	for strategy in strategies:
		try:
			results = load_rag_results(strategy)
			all_strategies_results[strategy] = results
			print(f"  ✅ {strategy}: {len(results['results'])} questions")
		except FileNotFoundError as e:
			print(f"  ❌ {strategy}: {e}")
			return
	first_strategy = list(all_strategies_results.values())[0]
	questions = first_strategy["results"]
	if test_mode:
		questions = questions[:1]
	total_calls = len(questions) * (len(strategies) + 1)
	print(f"\n🎯 Evaluating {len(questions)} questions")
	print(f"📊 Total LLM calls: {total_calls}")
	print("=" * 70)
	all_results = []
	ordinals = ["1st", "2nd", "3rd", "4th", "5th"][:len(strategies)]
	ranking_tally = {s: {o: 0 for o in ordinals} for s in strategies}
	for q_idx, question_data in enumerate(questions):
		question_id = question_data["question_id"]
		question_text = question_data["question"]
		print(f"\n{'='*70}")
		print(f"[Question {q_idx+1}/{len(questions)}] {question_text[:60]}...")
		print(f"{'='*70}")
		all_chunks = {}
		for strategy_name, strategy_results in all_strategies_results.items():
			for result in strategy_results["results"]:
				if result["question_id"] == question_id:
					all_chunks[strategy_name] = result["retrieved_contexts"]
					break
		print(f"\n  📋 STAGE 1: Per-strategy analysis (question-centric)")
		all_analyses = {}
		for strategy_name in strategies:
			chunks = all_chunks.get(strategy_name, [])
			print(f"    → Analyzing {strategy_name}...")
			prompt = build_stage1_prompt(question_text, strategy_name, chunks)
			try:
				analysis = call_llm(prompt)
				all_analyses[strategy_name] = analysis
				summary = analysis.get("summary", {})
				print(f"      cut_mid_answer={summary.get('cut_mid_answer_count', '?')}, "
					  f"avg_signal={summary.get('avg_signal_pct', '?')}%, "
					  f"high_useful={summary.get('high_useful_count', '?')}")
			except Exception as e:
				print(f"      ❌ Error: {str(e)}")
				all_analyses[strategy_name] = {"error": str(e)}
		print(f"\n  🏆 STAGE 2: Ranking with full context (thinking enabled)")
		prompt = build_stage2_prompt(question_text, strategies, all_analyses, all_chunks)
		try:
			ranking_result = call_llm(prompt, use_thinking=True)
			ranking = ranking_result.get("ranking", {})
			ranked = []
			for ordinal in ordinals:
				strategy_name = (ranking.get(ordinal) or "").lower()
				ranked.append((ordinal, strategy_name))
				if strategy_name in ranking_tally:
					ranking_tally[strategy_name][ordinal] += 1
			ranking_str = ", ".join([f"{o}: {s}" for o, s in ranked if s])
			print(f"    → {ranking_str}")
			print(f"    → Key insight: {ranking_result.get('key_insight', '')[:80]}...")
			all_results.append({
				"question_id": question_id,
				"question": question_text,
				"stage1_analyses": all_analyses,
				"stage2_ranking": ranking_result
			})
		except Exception as e:
			print(f"    ❌ Error: {str(e)}")
			raise
	output_file = EVALUATIONS_DIR / f"hybrid_chunk_eval_{timestamp}.json"
	output_data = {
		"saved_at": datetime.now().isoformat(),
		"evaluation_method": "hybrid_two_stage",
		"model": MODEL_NAME,
		"strategies": strategies,
		"questions_evaluated": len(questions),
		"results": all_results,
		"ranking_tally": ranking_tally
	}
	with open(output_file, 'w') as f:
		json.dump(output_data, f, indent=2)
	print("\n" + "=" * 70)
	print("EVALUATION COMPLETE")
	print("=" * 70)
	print(f"💾 Saved to: {output_file}")
	print("\n🏆 RANKING TALLY:")
	print("-" * 40)
	num_strategies = len(strategies)
	point_values = {ordinals[i]: num_strategies - i for i in range(len(ordinals))}
	for strategy in strategies:
		tally = ranking_tally[strategy]
		points_earned = sum(tally[o] * point_values[o] for o in ordinals)
		tally_str = " | ".join([f"{o}: {tally[o]}x" for o in ordinals])
		point_scheme = "/".join([str(point_values[o]) for o in ordinals])
		print(f"  {strategy}:")
		print(f"    {tally_str}")
		print(f"    Points ({point_scheme}): {points_earned}")
	points = {s: sum(ranking_tally[s][o] * point_values[o] for o in ordinals)
			  for s in strategies}
	winner = max(points.keys(), key=lambda s: points[s])
	print(f"\n🥇 OVERALL WINNER: {winner} ({points[winner]} points)")
	print("=" * 70)

def main():
	parser = argparse.ArgumentParser(description="Hybrid two-stage chunk quality evaluation")
	parser.add_argument("--strategies", nargs="+", required=True, help="Strategies to compare")
	parser.add_argument("--test", action="store_true", help="Test mode: 1 question only")
	args = parser.parse_args()
	try:
		run_evaluation(strategies=args.strategies, test_mode=args.test)
	except Exception as e:
		print(f"\n❌ Error: {str(e)}")
		import traceback
		traceback.print_exc()
		sys.exit(1)

if __name__ == "__main__":
	main()
