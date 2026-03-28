# Week 2 Capstone Submission

## Student Name(s)
Tripti Singh

## Project Title
RAG Capstone: Probability QA

## Week 1 Recap
- **Corpus:** Final Week-2 selected corpus contains **459** documents (`manifest_metadata.files_selected` in `artifacts/selected_files_manifest.json`).
- **Week 1 baseline performance:** Artifact-level baseline available in `week-1/traces/traces.json` shows 5 tracked queries, avg latency **8.468s**, avg retrieval_count **5.0**.
- **Key issue identified:** Need strategy comparison with higher-quality retrieval alignment while preserving stable runtime.
- **What Week 1 established:** A reliable baseline for foundational probability QA (definitions/formula-centric prompts) and a reproducible trace format.
- **Why Week 2 was needed:** Week-1 traces were strong but small-sample and schema-limited for multi-strategy quality deltas, so a broader judged evaluation was required.

## Chunking Analysis Summary
- **Dominant content types:** `documentation` only in selected-file manifest (**459/459**).
- **Document length distribution:** min **36**, max **62,950**, median **985**, stdev **3,958.2** words.
- **Key chunking consideration:** Wide length variance and long-tail outliers (224 files >1,000 words, 50 >2,000 words).
- **Deduplication results:** files selected **459**, reduction **0.65%**.

## Strategy Choice
- **Strategy:** Provisional winner by final eval artifact: **recursive**.
- **Rationale:** In final judge output (`final_comparitive_chunk_eval_20260301_211714.json`), recursive is ranked 1st on **6/10** questions.
- **Decision logic:** Recursive was selected as final because it performed best on overall judged wins, while still staying close to semantic on retrieval relevance (`top1_avg` gap 0.0026).
- **Configuration:** See implementation scripts and corresponding RAG artifacts (`scripts/Indexing/index_hybrid.py`, `scripts/pipeline/create_chunking_pipeline.py`).
- **Embedding model:**
  - recursive/semantic artifacts: `BGE-large-en-v1.5 (FastEmbed)` (1024-d)
  - hybrid artifact: `all-MiniLM-L6-v2` (384-d)
- **New collection name:** `week2_recursive` (for recursive artifact run)
- **Total chunks:** **N/A in final eval JSON** (chunk-count table not emitted in this artifact)
- **Truncation warnings:** **N/A in final eval JSON**

## Evaluation Approach
- **Judge model:** `gpt-4o-mini`
- **Method:** `hybrid_two_stage`
- **Changes from course default:** Not inferred beyond what is explicitly in artifact metadata.

## Evaluation Summary

| Metric | Naive Baseline | New Strategy (Recursive) | Change |
|--------|---------------|---------------------------|--------|
| Avg signal % | N/A (not available in comparable naive artifact) | 54.2 | N/A |
| Total/Avg cutoffs | N/A | 0.1 avg cut-mid-answer count | N/A |
| Avg usefulness | N/A | 2.7 avg high-useful count | N/A |
| Questions won | N/A vs recursive not available | recursive 1st on 6/10 | N/A |

### Cross-Strategy Outcome Snapshot (Week 2)
| Strategy | 1st-place wins (10 Q) | Avg signal % | Avg cut-mid count | Avg high-useful count | Avg latency (s) | Avg top-1 score |
|---|---:|---:|---:|---:|---:|---:|
| recursive | 6 | 54.2 | 0.1 | 2.7 | 11.696 | 0.7953 |
| semantic | 1 | 46.4 | 0.0 | 1.5 | 9.151 | 0.7979 |
| hybrid | 3 | 51.6 | 0.0 | 2.1 | 20.641 | 0.6676 |

Interpretation: semantic is fastest and slightly higher on top-1 retrieval score, but recursive wins most often on final judged answer quality/usefulness in this run set.

### Week-1 Trace Baseline (Operational Comparison)
| Baseline source | Queries | Avg latency (s) | Median latency (s) | Avg retrieved contexts | Avg answer length |
|---|---:|---:|---:|---:|---:|
| `week-1/traces/traces.json` | 5 | 8.468 | 7.97 | 5.0 | 1341.4 |

Interpretation: Week-1 naive baseline is faster in this small trace sample and retrieves fewer contexts on average (5 vs Week-2 `top_k=10` strategy runs), while Week-2 comparison artifacts provide richer quality ranking fields.

Additional strategy ranking context:
- hybrid 1st on 3/10
- semantic 1st on 1/10
- recursive on 6/10

### Evidence-Based Tradeoff Summary
- **Recursive:** Best overall judged outcome; balanced relevance and runtime.
- **Semantic:** Best speed profile and near-parity relevance; fewer final wins in judged outputs.
- **Hybrid:** Context-rich behavior in selected questions, but high runtime variability (max **91.58s**) and lower average top-1 score in captured artifacts.

## Judge Reliability Assessment
- **Spot-checked questions:** 1–5 (artifact consistency check)
- **Agreement with manual review:** Internal stage1/stage2 consistency: 4 full + 1 partial agreement in checked subset.
- **Judge weaknesses found:** Stage-2 weighting is not strictly tied to average signal; qualitative notes influence ranking.
- **Reliability conclusion:** Judge output is usable for directional ranking across strategies, but should be paired with retrieval/runtime metrics before final production decisions.

## Key Observations
- **Where did the new strategy help most?** Recursive improved judged answer quality consistency on the mixed set of factoid/analytical/conceptual questions.
- **Where did it not help (or hurt)?** Pure speed did not correlate with final judged ranking; semantic was faster but less frequently ranked first.
- **What's the information density tradeoff?** Higher context granularity/coverage can improve judged usefulness, but may increase runtime and operational cost.
- **Domain insight (Probability QA):** Formula-grounded educational prompts benefit from boundary-aware chunks, while cross-topic explanatory prompts can benefit from hybrid-style context linking.
- **What would you improve next?** Generate a fully comparable naive artifact (same schema) to complete baseline-vs-strategy deltas; then run a controlled re-eval with equal embedding family across all strategies.

## Iteration Summary
- **Total evidenced runs:** 4 major timestamped artifacts (recursive RAG, semantic RAG, hybrid RAG, final eval).
- **Most impactful change:** Running a final two-stage multi-strategy judge pass enabled direct strategy ranking.
- **Stopping rationale:** Final 10-question ranked eval artifact exists and supports evidence-backed write-up.

## Risks and Limits (Explicit)
- Naive baseline artifact is not schema-compatible with Week-2 strategy eval fields, so strict metric deltas are partially unavailable.
- Week-1 trace baseline uses 5 queries, while Week-2 final comparison uses 10 questions; baseline interpretation is operational, not directly equivalent scoring.
- Hybrid run used a different embedding family/dimension than recursive/semantic in captured artifacts, so part of variance may include embedding effects in addition to chunking effects.

## Self-Assessment

| Criteria | Score (1-5) | Notes |
|----------|-------------|-------|
| Chunking analysis depth | 4 | Backed by manifest + measured length stats |
| Strategy selection rationale | 4 | Uses final ranking artifact rather than assumptions |
| Evaluation thoroughness | 4 | Full 10-question multi-strategy eval artifact present |
| Judge reliability check | 4 | Internal consistency spot-check documented |
| Iteration quality | 4 | Multiple timestamped strategy runs captured |
| Documentation clarity | 4 | `_1` docs separate evidence-backed version from earlier drafts |

## Sources Used
- `evaluations/metrics_snapshot_1.json`
- `evaluations/eval_results/final_comparitive_chunk_eval_20260301_211714.json`
- `evaluations/rag_results/rag_results_recursive_20260301_041934.json`
- `evaluations/rag_results/rag_results_semantic_20260301_042330.json`
- `evaluations/rag_results/rag_results_hybrid_20260301_111809.json`
- `evaluations/rag_results/naive_rag_results.json`
- `artifacts/selected_files_manifest.json`
- `week-1/traces/traces.json`
