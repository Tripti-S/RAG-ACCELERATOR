# Week 2 Comparison (Evidence-Backed) — _1

## Evaluation Approach
- Judge model: `gpt-4o-mini`
- Evaluation method: `hybrid_two_stage`
- Final eval JSON: `eval_results/final_comparitive_chunk_eval_20260301_211714.json`
- Strategy set evaluated: `recursive`, `semantic`, `hybrid`

## Per-Question Comparison (From Final Eval JSON)
| # | Question (short) | Recursive: Signal | Recursive: Cutoffs | Recursive: Useful | Semantic: Signal | Semantic: Cutoffs | Semantic: Useful | Hybrid: Signal | Hybrid: Cutoffs | Hybrid: Useful | Winner |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Independence definition equation | 63 | 0 | 4 | 54 | 0 | 2 | 52 | 0 | 1 | RECURSIVE |
| 2 | Bayes rule + denominator role | 43 | 0 | 1 | 45 | 0 | 0 | 48 | 0 | 1 | RECURSIVE |
| 3 | Variance shortcut formula | 43 | 0 | 1 | 30 | 0 | 0 | 45 | 0 | 3 | HYBRID |
| 4 | LTP to Bayes derivation | 50.0 | 0 | 3 | 43 | 0 | 0 | 66 | 0 | 4 | HYBRID |
| 5 | Independence vs conditional independence | 66 | 0 | 3 | 54 | 0 | 3 | 66 | 0 | 4 | HYBRID |
| 6 | Binomial to Poisson limits | 60.5 | 0 | 4 | 61 | 0 | 5 | 48 | 0 | 3 | RECURSIVE |
| 7 | Linearity of expectation | 57 | 1 | 1 | 38 | 0 | 2 | 52 | 0 | 1 | RECURSIVE |
| 8 | Geometric memoryless property | 54.5 | 0 | 3 | 43 | 0 | 1 | 40 | 0 | 3 | RECURSIVE |
| 9 | E[X\|Y] vs E[X\|Y=y] | 56 | 0 | 2 | 53 | 0 | 1 | 56 | 0 | 1 | SEMANTIC |
| 10 | Monty Hall misconception | 49 | 0 | 5 | 43 | 0 | 1 | 43 | 0 | 0 | RECURSIVE |

## Strategy-Level Results (From Final Eval JSON)

### Stage-2 Ranking Outcome (10 questions)
| Strategy | 1st | 2nd | 3rd |
|---|---:|---:|---:|
| recursive | 6 | 3 | 1 |
| hybrid | 3 | 3 | 4 |
| semantic | 1 | 4 | 5 |

### Stage-1 Aggregate Signals (avg across 10 questions)
| Strategy | Avg signal % | Avg cut-mid-answer count | Avg high-useful count |
|---|---:|---:|---:|
| recursive | 54.2 | 0.1 | 2.7 |
| hybrid | 51.6 | 0.0 | 2.1 |
| semantic | 46.4 | 0.0 | 1.5 |

## RAG Runtime/Top-1 Context Metrics (From RAG JSONs)
| Strategy | Avg latency (s) | Median latency (s) | Max latency (s) | Avg top-1 score |
|---|---:|---:|---:|---:|
| recursive | 11.696 | 12.345 | 15.78 | 0.7953 |
| semantic | 9.151 | 8.565 | 16.97 | 0.7979 |
| hybrid | 20.641 | 13.075 | 91.58 | 0.6676 |

## Week-1 Naive Baseline (From `week-1/traces/traces.json`)
| Baseline | Queries | Avg latency (s) | Median latency (s) | Avg retrieved contexts | Avg answer length |
|---|---:|---:|---:|---:|---:|
| naive_week1_trace | 5 | 8.468 | 7.97 | 5.0 | 1341.4 |

Naive trace file does not contain `top1` relevance scores or judge ranking fields, so those columns remain unavailable for strict side-by-side scoring.

## Naive Baseline Status
A strict naive-vs-strategy metric comparison is **not fully available** in current final artifacts:
- `rag_results/naive_rag_results.json` contains only:
  - `documents_written: 2384`
- It does not include per-question retrieval contexts, latency, or answer quality fields required for side-by-side metric comparison.

Week-1 baseline trace evidence available in `week-1/traces/traces.json`:
- queries: 5
- avg latency: 8.468s
- avg retrieval_count: 5.0

## Summary (Strictly Data-Backed)
1. Final judge ranking favors **recursive** overall (6/10 first-place).
2. **Semantic** is fastest by average latency and has the highest top-1 score average in the available RAG runs.
3. **Hybrid** shows larger runtime variability in captured artifacts (max 91.58s) and lower top-1 score average in this run set.
4. A complete naive metric comparison requires regenerating naive results in the same schema as current per-strategy RAG JSONs.

## Source Files
- `evaluations/metrics_snapshot_1.json`
- `evaluations/eval_results/final_comparitive_chunk_eval_20260301_211714.json`
- `evaluations/rag_results/rag_results_recursive_20260301_041934.json`
- `evaluations/rag_results/rag_results_semantic_20260301_042330.json`
- `evaluations/rag_results/rag_results_hybrid_20260301_111809.json`
- `evaluations/rag_results/naive_rag_results.json`
- `week-1/traces/traces.json`
