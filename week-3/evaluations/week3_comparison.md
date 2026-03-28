# Week 3 vs Week 2 Comparison

## Evaluation Approach
- Judge model: `gemini-2.5-flash`
- Evaluation method: pairwise retrieval quality comparison across techniques.
- Input set: same Week 2 evaluation questions reused for consistency.
- Source-of-truth eval files:
	- `week-3/evaluations/eval_results/pairwise_eval_week2_recursive_vs_week3_hybrid_rerank.json`
	- `week-3/evaluations/eval_results/pairwise_eval_week3_all_techniques.json`

Coverage from all-techniques artifact:
- Questions: `10`
- Technique pairs: `6`
- Pairwise matchups judged: `60`

## Results

### All-Techniques Aggregate (Primary Week 3 Experiment)

| Technique | Avg Usefulness | Avg Relevance | Avg Direct Context Count | Noise Chunks (Total) | Questions Won |
|---|---:|---:|---:|---:|---:|
| Recursive (2000c/200) | 3.833 | 2.250 | 4.500 | 67 | 11 |
| Week 3 baseline: hybrid retrieval + reranking | 4.483 | 3.267 | 6.533 | 23 | 26 |
| Week 3 hybrid + rerank + metadata filtering | 2.667 | 1.700 | 3.400 | 64 | 9 |
| Week 3 two-stage routing + hybrid + reranking | 3.717 | 1.950 | 3.900 | 50 | 14 |

Inference from aggregate table:
- Week 3 baseline hybrid+rereank is best in this run set across all summary metrics and win count.

### Direct Week 2 vs Week 3 Baseline Detail

| # | Question | W2: Useful | W2: Relevant | W2: Noise | W3 Hybrid+Rerank: Useful | W3: Relevant | W3: Noise | Winner |
|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Independence definition formula | 4.0/5 | 3.5/5 | 2 | 4.5/5 | 4.5/5 | 1 | W3 |
| 2 | Bayes rule + denominator | 5.0/5 | 2.5/5 | 0 | 5.0/5 | 3.0/5 | 0 | W3 |
| 3 | Variance shortcut formula | 3.0/5 | 2.0/5 | 4 | 5.0/5 | 4.5/5 | 0 | W3 |
| 4 | Law of total probability -> Bayes | 3.5/5 | 2.5/5 | 3 | 5.0/5 | 4.5/5 | 0 | W3 |
| 5 | Independence vs conditional independence | 5.0/5 | 1.5/5 | 0 | 4.5/5 | 2.0/5 | 1 | W3 |
| 6 | Binomial limiting conditions | 4.0/5 | 3.5/5 | 2 | 4.5/5 | 4.5/5 | 0 | W3 |
| 7 | Linearity of expectation | 2.5/5 | 1.5/5 | 5 | 3.0/5 | 2.0/5 | 3 | W3 |
| 8 | Geometric memoryless property | 3.0/5 | 2.0/5 | 4 | 4.0/5 | 3.0/5 | 2 | W3 |
| 9 | E[X\|Y] vs E[X\|sigma(Y)] | 4.5/5 | 2.5/5 | 1 | 5.0/5 | 3.5/5 | 0 | W3 |
| 10 | Monty Hall common error | 3.5/5 | 2.5/5 | 3 | 3.5/5 | 2.0/5 | 2 | W2 |

Aggregate summary (from final pairwise JSON):
- Avg usefulness: W2 `3.8/5` vs W3 `4.4/5`
- Avg relevance (directness): W2 `2.4/5` vs W3 `3.35/5`
- Total noise chunks: W2 `24` vs W3 `9`
- Questions won: W2 `1/10` vs W3 `9/10`

## Impact Analysis
- Hybrid + rerank impact: in both comparison artifacts, this configuration shows higher usefulness and relevance with lower noise than Week 2 recursive baseline.
- Metadata-filter narrowing impact: underperformed baseline in this run (`2.667` usefulness, `1.700` relevance, `64` noise).
- Two-stage routing impact: improved over metadata filter on most aggregate metrics but still underperformed baseline (`3.717` usefulness, `1.950` relevance, `50` noise).
- Failure analysis for narrowing variants: current evidence is consistent with recall loss from early restriction. Many probability questions in this set require cross-document context (definitions, formulas, and examples from different sources), and category/file constraints can drop useful chunks before reranking. Two-stage routing adds dependency on file-level intent selection, which can misroute multi-concept conceptual prompts. Because reranking already improves precision from a broad candidate pool, narrowing did not produce a net gain in this run.

## CAL Tradeoff
- Cost: reranker and extra routing/filter stages add API and pipeline complexity versus Week 2 recursive.
- Accuracy: best measured quality is from Week 3 baseline hybrid+rereank (top scores in all-techniques summary).
- Latency (available artifacts): Week 2 recursive mean `11.696s`; Week 3 baseline total `101.11s` for 10 questions (mean `10.111s`).

## Summary
- Week 3 baseline hybrid+rereank is the strongest measured approach in this repository.
- Week 2 recursive remains competitive on selected prompts (for example Q10 in direct baseline comparison).
- In this run set, narrowing variants did not beat baseline; they remain experimental paths rather than default retrieval strategy.
