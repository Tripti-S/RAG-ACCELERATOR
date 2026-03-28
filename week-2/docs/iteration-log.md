# Iteration Log (Evidence-Backed) — _1

## Data Sources
- `week-2/evaluations/rag_results/rag_results_recursive_20260301_041934.json`
- `week-2/evaluations/rag_results/rag_results_semantic_20260301_042330.json`
- `week-2/evaluations/rag_results/rag_results_hybrid_20260301_111809.json`
- `week-2/evaluations/eval_results/final_comparitive_chunk_eval_20260301_211714.json`
- `week-2/evaluations/metrics_snapshot_1.json`

## Iteration 1: Recursive Evaluation Run
- Artifact timestamp: `2026-03-01T04:17:32.419552`
- File: `rag_results_recursive_20260301_041934.json`
- Result summary (from `metrics_snapshot_1.json`):
  - Questions: 10
  - Avg latency: 11.696s
  - Top-1 avg score: 0.7953
- Observation: Strong relevance score profile with moderate runtime.

## Iteration 2: Semantic Evaluation Run
- Artifact timestamp: `2026-03-01T04:21:54.058140`
- File: `rag_results_semantic_20260301_042330.json`
- Result summary:
  - Questions: 10
  - Avg latency: 9.151s
  - Top-1 avg score: 0.7979
- Observation: Fastest average latency and slightly strongest top-1 score in this run set.

## Iteration 3: Hybrid Evaluation Run
- Artifact timestamp: `2026-03-01T11:14:38.485978`
- File: `rag_results_hybrid_20260301_111809.json`
- Result summary:
  - Questions: 10
  - Avg latency: 20.641s
  - Max latency: 91.58s
  - Top-1 avg score: 0.6676
- Observation: Runtime variability/outlier present; lower top-1 average in this captured run.

## Iteration 4: Final Multi-Strategy Judge Pass
- Artifact timestamp: `2026-03-01T21:27:39.377615`
- File: `eval_results/final_comparitive_chunk_eval_20260301_211714.json`
- Evaluation method: `hybrid_two_stage`
- Judge model: `gpt-4o-mini`
- 1st-place tally over 10 questions:
  - recursive: 6
  - hybrid: 3
  - semantic: 1

## Current Stopping Point (Evidence-Based)
- Final artifact exists with full 10-question ranking across the three strategies.
- Recursive has the highest first-place frequency in the final judge output.
- Additional runs may still be useful, but current artifacts are sufficient to produce a justified Week 2 comparison package.

## Lessons Learned (From Artifacts)
1. Retrieval quality and runtime do not always align; semantic is faster while recursive wins more judge rankings in this final set.
2. Hybrid shows high variance in runtime in the captured run set (max 91.58s).
3. Keeping timestamped run artifacts enables reproducible audit of strategy evolution.
