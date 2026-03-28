# Week 2 Observations

## Scope
These observations summarize comparative behavior across chunking strategies (Naive, Recursive, Semantic, Hybrid) using:
- per-question ranking outcomes,
- chunk quality signals (`signal`, `cutoffs`, `useful`),
- and manual review of selected questions.

---

## Overall Ranking Summary

- **Hybrid** ranked **1st in 8/10** questions.
- **Semantic** ranked **2nd** in most conceptual questions.
- **Recursive** performed best on some structured textbook-style sections.
- **Naive** generally ranked last due to lower signal density.

---

## Strategy Behavior Patterns

| Strategy | Strength | Limitation | Net Observation |
|---|---|---|---|
| Naive | Simple and broad coverage | Large chunks include irrelevant lecture narrative | Lower precision for targeted conceptual retrieval |
| Recursive | Better structural alignment with source hierarchy | Can split equations/explanations across boundaries | Good for structured text, less stable for formula continuity |
| Semantic | Topic-coherent definition grouping | Sometimes pulls slide/OCR artifacts | Strong conceptual retrieval, occasional noise |
| Hybrid | Best balance of relevance and completeness | More complex behavior to tune and monitor | Most consistently useful across evaluated questions |

---

## Manual Judge Reliability Check

Manual review was done for **Q1, Q4, Q7**.

- **Q1:** Judge preference for Hybrid was correct (cleaner formal equation chunk).
- **Q4:** Judge penalized Recursive for cut-mid-answer; manual review confirmed equation splitting.
- **Q7:** Judge preferred Semantic, but manual inspection suggested Recursive had a more direct example; likely slight over-weighting of `signal`.

### Reliability inference
- Judge behavior appears **mostly reliable** for ranking quality.
- Mild bias may exist toward high-signal chunks when directness/completeness trade-offs are close.

---

## Naive Baseline POV

- Naive remains useful as a baseline for speed and simplicity.
- However, for concept-heavy academic queries, naive chunking tends to reduce signal concentration and retrieval precision.
- Compared with Week 2 strategies, naive is best treated as a control condition, not final retrieval strategy.

---

## Practical Conclusion

1. **Primary takeaway:** Hybrid currently gives the strongest overall answer quality.
2. **Close alternative:** Semantic remains a strong default for conceptual questions.
3. **Targeted usage:** Recursive is valuable when document structure is clean and hierarchical.
4. **Baseline role:** Naive should remain for comparison and regression checks.

---

## Next Validation Step

- Re-run full question-set evaluations with identical settings (`top_k`, model, question bank).
- Add a weighted score combining quality (`signal/useful/cutoffs`) and consistency (latency variability).
- Use that combined score to finalize strategy selection for production use.