# Week 3 Iteration Log

## Iteration 1: Hybrid Indexing + Baseline Pipeline
- Configuration: indexed `week3_hybrid_recursive` with dense `voyage-4-lite` (`2048d`) + sparse `Qdrant/bm25`; recursive chunking continuity from Week 2.
- Result: successful indexing run with `2315` points and both vector types populated (`dense=true`, `sparse=true`) from `hybrid_indexing_report_20260310_004522.json`.
- Observation: collection is valid for hybrid retrieval + reranking baseline.

## Iteration 2: Final Scored Comparison Run
- Configuration: Week 2 recursive baseline vs Week 3 hybrid+rereank baseline using pairwise judge (`gemini-2.5-flash`).
- Result: Week 3 won `9/10` questions in `pairwise_eval_week2_recursive_vs_week3_hybrid_rerank.json`.
- Observation: reranked hybrid retrieval materially improved directness and reduced noise.

## Iteration 3: Narrowing Paths (Implemented and Scored)
- Configuration: metadata filtering and two-stage file routing evaluated alongside Week 2 recursive and Week 3 baseline hybrid+rereank.
- Result: all-techniques pairwise artifact generated at `week-3/evaluations/eval_results/pairwise_eval_week3_all_techniques.json`.
- Observation: in current runs, narrowing variants underperform baseline hybrid+rereank on aggregate usefulness/relevance/noise metrics.

## Final Configuration
- Pipeline: hybrid + rerank as default evaluated path.
- Settings: dense `voyage-4-lite` (2048d), sparse `Qdrant/bm25`, hybrid candidate set `50`, rerank `10`.
- Stopping rationale: this point gives strong quality gains while keeping implementation and operations manageable.

## Lessons Learned
- Reranking contributes more consistently than narrowing for this corpus.
- Narrowing should only be promoted after it is scored under the same pairwise framework as the baseline.
- CAL tradeoff is real: any extra routing stage must justify additional latency and cost.
