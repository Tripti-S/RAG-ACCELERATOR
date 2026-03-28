# Inference: Week 2 Strategy Evaluation (Recursive, Semantic, Hybrid) + Week 1 Naive POV

## Definition (What “Inference” Means Here)
In this document, **inference** means: conclusions derived by combining retrieval/evaluation evidence across artifacts, not from a single run or one metric.

Specifically, conclusions are based on:
1. Week 2 `eval_results` (human/heuristic quality signals: `signal`, `cutoffs`, `useful`, `winner`)
2. Week 2 `rag_results` (retrieval behavior and runtime: scores, contexts, latency)
3. Week 1 `traces/traces.json` (naive baseline retrieval/latency behavior)

---

## Data Sources Used
- `week-2/evaluations/eval_results/recursive_chunk_eval_20260301_123456.json`
- `week-2/evaluations/eval_results/semantic_chunk_eval_20260301_123456.json`
- `week-2/evaluations/eval_results/hybrid_chunk_eval_20260301_123456.json`
- `week-2/evaluations/rag_results/rag_results_recursive_20260301_041934.json`
- `week-2/evaluations/rag_results/rag_results_semantic_20260301_042330.json`
- `week-2/evaluations/rag_results/rag_results_hybrid_20260301_111809.json`
- `week-1/traces/traces.json`
- Supporting chunk-count context: `week-2/archive/comparisons/snapshot_chunk_count_comparison.md`

---

## Quantitative Summary (from `rag_results`)

| Strategy | Questions | Avg Latency (s) | Median Latency (s) | Max Latency (s) | Avg Top-1 Score | Avg Context Score | Avg Contexts Retrieved | Avg Answer Length |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Recursive | 10 | 11.696 | 12.345 | 15.780 | 0.7953 | 0.7729 | 10.0 | 2272.0 |
| Semantic | 10 | 9.151 | 8.565 | 16.970 | 0.7979 | 0.7742 | 10.0 | 1774.4 |
| Hybrid | 10 | 20.641 | 13.075 | 91.580 | 0.6676 | 0.5745 | 10.0 | 2292.3 |

### Direct observations
- **Semantic is fastest on average and median latency** among Week 2 strategies.
- **Recursive and Semantic retrieval scores are very close** (`top1` and overall context score).
- **Hybrid shows runtime instability** (large max-latency outlier at `91.58s`) and lower retrieval score averages in this run.

---

## Quality Signals (from `eval_results` files)

Using the available quality fields in the eval artifacts (`signal`, `cutoffs`, `useful`), the directional trend in sampled entries is:

- **Hybrid:** highest `signal` and `useful`, lowest `cutoffs` in shown samples.
- **Semantic:** middle performance; generally focused but with some overlap/cutoff mentions.
- **Recursive:** lower signal than hybrid/semantic in shown samples; more cutoff/noise indications.

### Important caveat
The three `eval_results` files are partially templated/abbreviated (contain `// ... more questions ...`), so these quality comparisons should be treated as **directional**, not final benchmark totals.

---

## Week 1 Naive POV (Baseline Contrast)

From `week-1/traces/traces.json`:
- Queries: `5`
- Avg latency: `8.468s`
- p95 latency (small sample): `9.39s`
- Avg retrieved contexts: `5.0`
- Avg answer length: `1341.4`

### Naive vs Week 2 interpretation
1. **Speed/throughput:** Naive baseline appears latency-efficient in this small trace sample.
2. **Depth of retrieval:** Week 2 strategies consistently retrieve `top_k=10` contexts (vs ~5 in Week 1 traces), increasing grounding breadth but with added latency/cost.
3. **Chunking tradeoff context:**
   - Naive chunking (fixed-size) is cheaper and simpler.
   - Recursive/Semantic increase granularity and context precision potential.
   - Supporting snapshot shows scale jump in chunk volume (`482` naive → `2315` recursive → `2792` semantic), explaining heavier indexing/retrieval workloads.

---

## Consolidated Inference

1. **If objective is stable speed + strong retrieval scores in current runs, Semantic is the strongest Week 2 candidate.**
2. **Recursive is close to Semantic on relevance scores, but not faster.**
3. **Hybrid has strong directional quality signals in eval snippets, but current rag runtime/score aggregates indicate instability and mismatch that should be investigated before declaring it best.**
4. **Naive remains a useful operational baseline** (fast, simple), but with less retrieval depth and lower expected context precision for complex questions.

---

## Recommended Next Validation Step
To finalize strategy selection with high confidence:
1. Regenerate **full** (non-templated) eval files for all 10 questions.
2. Re-run each strategy with same model + same `top_k` + same question set.
3. Report final decision on combined metrics: quality (`signal/useful/cutoffs`) + latency consistency + retrieval scores.

Current evidence supports **Semantic as default production candidate**, with **Hybrid as a candidate for targeted tuning experiments**.