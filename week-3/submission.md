# Week 3 Capstone Submission

## Student Name(s)
Tripti Singh

## Project Title
ProbablAI - Probability learning RAG model

## Progress Recap
- **Week 1 baseline:** Dense retrieval baseline over processed probability-learning corpus.
- **Week 2 improvement:** Recursive chunking and better corpus preparation produced stronger dense baseline artifacts.
- **Key issue going into Week 3:** Retrieval precision/noise control for mixed conceptual + keyword-heavy probability questions.

## Core Retrieval Failure Mode
Week 2 dense retrieval was reliable for broad semantic similarity, but weaker on keyword-heavy probability queries where exact terms and formula phrases matter. In practice, semantic-only ranking can miss or under-rank exact lexical signals (for example specific rule names, notation, or identifier-like phrasing). With a larger mixed-source corpus, this also increases semantic drift, where loosely related chunks are ranked high while directly useful chunks are buried. The observed impact is lower direct relevance and higher noise in retrieved context sets.

Week 3 addresses this by combining dense semantic embeddings with BM25 sparse retrieval, then applying reranking to refine the final ordering. This architecture preserves semantic coverage, recovers exact-term matches, and improves precision in the top contexts passed to generation.

## Retrieval Assessment Summary
- **Constraint profile:** Quality is prioritized over ultra-low latency; moderate additional retrieval complexity is acceptable.
- **Corpus characteristics:** Heterogeneous corpus with clear topical boundaries and usable metadata; cross-document retrieval is common.
- **Narrowing decision:** Implemented and evaluated. Final default remains hybrid + rerank because narrowing variants underperformed on current scored artifacts.

## Retrieval Configuration
- **Hybrid search:** `voyage-4-lite` (dense) + `Qdrant/bm25` (sparse), Qdrant RRF fusion.
- **Initial retrieval:** top `50` candidates.
- **Reranking:** `rerank-2.5`, rerank to top `10`.
- **Narrowing:** Metadata filtering and two-stage routing were implemented and evaluated.
- **Collection name:** `week3_hybrid_recursive`.
- **Total indexed chunks:** `2315` (`week-3/scripts/indexing/outputs/hybrid_indexing_report_20260310_004522.json`).

Architecture flow:

```text
User Query
	|
	v
Dense Embedding + Sparse BM25 Retrieval
	|
	v
Reciprocal Rank Fusion (Top 50 Candidates)
	|
	v
Voyage Reranker (Top 10 Contexts)
	|
	v
LLM Generation
```

## Evaluation Approach
- **Judge model:** `gemini-2.5-flash`.
- **Method:** Pairwise retrieval-quality evaluation across techniques.
- **Changes from Week 2 or course default:** Expanded from baseline 2-technique comparison to 4-technique comparison, producing 6 pairs across 10 questions (60 matchups).

## Scope and Evidence Policy
This submission reports only measured outcomes from generated artifacts in this repository.

Primary evidence files used:
- `week-3/scripts/indexing/outputs/hybrid_indexing_report_20260310_004522.json`
- `week-3/rag_results/week3_hybrid_rerank_baseline_20260310_010501.json`
- `week-3/rag_results/week3_hybrid_rerank_metadata_filter_results.json`
- `week-3/rag_results/week3_two_stage_routing_results.json`
- `week-3/evaluations/eval_results/pairwise_eval_week3_all_techniques.json`
- `week-3/evaluations/eval_results/pairwise_eval_week2_recursive_vs_week3_hybrid_rerank.json`
- `week-2/evaluations/rag_results/rag_results_recursive_20260301_041934.json`

## Retrieval Setup (Implemented)
- Collection: `week3_hybrid_recursive`
- Dense retrieval: `voyage-4-lite` (`2048` dimensions)
- Sparse retrieval: `Qdrant/bm25`
- Fusion: Qdrant RRF hybrid fusion
- Baseline reranking: `rerank-2.5` from top `50` to top `10`
- Generator model in result artifacts: `gemini-2.5-flash`

Indexing evidence (`week-3/scripts/indexing/outputs/hybrid_indexing_report_20260310_004522.json`):
- `files_processed_this_run`: `459`
- `points_indexed`: `2315`
- `dense_vectors_populated`: `true`
- `sparse_vectors_populated`: `true`

## Techniques Evaluated
Based on `week-3/evaluations/eval_results/pairwise_eval_week3_all_techniques.json`:
- `Recursive (2000c/200)` (Week 2 baseline artifact)
- `Week 3 baseline: hybrid retrieval + reranking`
- `Week 3 hybrid + rerank + metadata filtering`
- `Week 3 two-stage routing + hybrid + reranking`

Evaluation coverage:
- Questions evaluated: `10`
- Technique pairs compared: `6`
- Total pairwise matchups judged: `60`
- Judge model recorded in artifact: `gemini-2.5-flash`

## Results

### A) Four-Technique Pairwise Summary
Source: `week-3/evaluations/eval_results/pairwise_eval_week3_all_techniques.json` (`summary_table`)

| Technique | Avg Usefulness | Avg Relevance | Avg Direct Context Count | Noise Chunks (Total) | Questions Won |
|---|---:|---:|---:|---:|---:|
| Recursive (2000c/200) | 3.833 | 2.250 | 4.500 | 67 | 11 |
| Week 3 baseline: hybrid retrieval + reranking | 4.483 | 3.267 | 6.533 | 23 | 26 |
| Week 3 hybrid + rerank + metadata filtering | 2.667 | 1.700 | 3.400 | 64 | 9 |
| Week 3 two-stage routing + hybrid + reranking | 3.717 | 1.950 | 3.900 | 50 | 14 |

### B) Direct Week 2 vs Week 3 Baseline Comparison
Source: `week-3/evaluations/eval_results/pairwise_eval_week2_recursive_vs_week3_hybrid_rerank.json`

| Metric | Week 2 Recursive | Week 3 Baseline Hybrid+Rerank |
|---|---:|---:|
| Avg usefulness | 3.8 | 4.4 |
| Avg relevance | 2.4 | 3.35 |
| Total noise chunks | 24 | 9 |
| Questions won | 1/10 | 9/10 |

### C) Runtime Evidence Available in Result Artifacts
- Week 2 recursive mean query time from `week-2/evaluations/rag_results/rag_results_recursive_20260301_041934.json`: `11.696s`
- Week 3 baseline total time from `week-3/rag_results/week3_hybrid_rerank_baseline_20260310_010501.json`: `101.11s` across `10` questions, mean `10.111s`
- Metadata-filter and two-stage result artifacts currently record `questions_processed`, but do not include per-question/total runtime fields.

## Evaluation Summary

| Metric | Week 2 (Dense) | Week 3 (Hybrid + Rerank) | Change |
|---|---:|---:|---:|
| Avg usefulness | 3.8 | 4.4 | +0.6 |
| Avg relevance | 2.4 | 3.35 | +0.95 |
| Total noise chunks | 24 | 9 | -15 |
| Questions won | 1/10 | 9/10 | +8/10 |

Interpretation: this evaluation pattern is consistent with hybrid retrieval improving recall by combining semantic and lexical signals, and reranking improving final top-context ordering. The Week 3 baseline achieves higher usefulness/relevance with lower noise than the Week 2 dense baseline. Narrowing strategies were tested in the same run framework, but in current artifacts they are best treated as optional paths rather than default retrieval.

## Findings (Evidence-Backed)
1. Best observed technique in this run set is `Week 3 baseline: hybrid retrieval + reranking`.
It has the highest usefulness (`4.483`), highest relevance (`3.267`), highest direct context count (`6.533`), lowest noise (`23`), and highest wins (`26`) in the 4-technique summary table.

2. In this measured run, narrowing variants underperform the Week 3 baseline.
`metadata filtering` and `two-stage routing` both show lower usefulness/relevance and higher noise than baseline hybrid+rerank.
Likely contributors are: (1) metadata filtering can reduce recall on questions that need cross-document evidence, and (2) file-level routing can misroute multi-concept conceptual questions. This corpus frequently mixes textbook, lecture, and worked-example material for one answer path, so aggressive narrowing can remove useful context diversity. With reranking already improving final precision from a broad candidate pool, additional narrowing did not improve precision enough to offset recall loss in this run.

3. Week 3 baseline remains stronger than Week 2 recursive in the direct two-technique comparison.
Artifact summary reports `9/10` question wins for Week 3 baseline and lower noise (`9` vs `24`).

4. Baseline runtime is slightly lower than Week 2 recursive in available timing fields.
Observed averages are `10.111s` (Week 3 baseline) vs `11.696s` (Week 2 recursive).

## Key Observations
- **What impact did hybrid search have?** In measured comparisons, hybrid+rereank improves aggregate usefulness/relevance and reduces noise versus Week 2 dense baseline.
- **What impact did reranking have?** The strongest overall scores are from the reranked Week 3 baseline in the 4-technique summary (`4.483` usefulness, `3.267` relevance, `23` noise).
- **What impact did narrowing have (if applicable)?** Both narrowing variants were evaluated; in this run set they underperformed baseline hybrid+rereank on aggregate quality metrics.
- **Why did narrowing underperform here?** The most likely explanation is recall loss: probability questions often need context spanning multiple source types, while category/file narrowing restricts candidate diversity early. Two-stage routing also depends on file-level intent selection, which can miss multi-concept conceptual prompts. Since reranking already promotes high-quality chunks from a broader pool, the extra narrowing stage reduced diversity without net precision gain in current artifacts.
- **Where does the system still struggle?** Some question-level edge cases remain (for example the direct Week2-vs-Week3 file still includes one Week 2 win).
- **CAL tradeoff:** Accuracy improves materially with hybrid+rereank; runtime remains acceptable in available measurements (`11.696s` Week 2 vs `10.111s` Week 3 baseline). Extra routing/filter paths add complexity and did not improve quality in current runs.
- **What would you improve next?** Tune/guard narrowing triggers and re-run controlled evaluations only if new metadata/routing quality signals justify added complexity.

## Production Recommendation
Recommended production pipeline:

`Query -> Hybrid Dense + Sparse Retrieval -> RRF Fusion -> Voyage Reranking -> LLM Generation`

This is the best engineering choice for current evidence: it delivers the highest measured relevance and usefulness, the lowest noise in aggregate comparisons, acceptable observed latency in available runtime fields, and reasonable complexity/cost relative to narrowing variants that did not improve quality in this run set.

## Inference and Decision
- Production/default retrieval choice for this repository should remain: `Week 3 baseline: hybrid retrieval + reranking`.
- Narrowing variants are retained as experiments, not default path, because current scored artifacts do not show quality gains over baseline.

## Judge Reliability and Limits
Based on `week-3/evaluations/week3_deep_analysis.md` (manual checks of Q1, Q3, Q7, Q10 on the Week2-vs-Week3 baseline file):
- Agreement status: 4/4 agree or partially agree.
- Noted bias: judge can favor direct-count-heavy outcomes on close conceptual cases.

Additional limitation visible in all-technique eval entries:
- Some reasoning strings include wording such as "assuming ... noise", which indicates occasional judge uncertainty in interpretation even when numeric outputs are returned.

## Final Week 3 Outcome
- Week 3 successfully implemented and evaluated hybrid + reranking and two narrowing variants.
- The strongest measured result in this repository is still the non-narrowed `hybrid + reranking` baseline.
- Submission claims are aligned to generated artifacts listed above, with no additional assumed performance claims.

## Iteration Summary
- **Total iterations:** 3 major iterations documented (hybrid indexing baseline, baseline scored comparison, narrowing experiments with all-techniques scoring).
- **Most impactful change:** Hybrid retrieval plus reranking.
- **Stopping rationale:** Current evidence shows baseline hybrid+rereank is best-performing; narrowing remains experimental until it beats baseline under the same scoring framework.

## Self-Assessment

| Criteria | Score (1-5) | Notes |
|---|---:|---|
| Retrieval analysis depth | 5 | Constraint/corpus/narrowing assessment documented and tied to outcomes. |
| Hybrid implementation quality | 5 | Dense+sparse hybrid indexing validated with `2315` populated points. |
| Reranking integration | 5 | Reranked baseline is implemented and best-performing in measured artifacts. |
| Evaluation thoroughness | 5 | Includes both baseline pairwise and 4-technique pairwise artifacts. |
| Judge reliability check | 4 | Manual spot-checks and limitations documented; still dependent on LLM judge behavior. |
| Documentation clarity | 5 | Docs and submission aligned to artifact-backed findings and decision. |
