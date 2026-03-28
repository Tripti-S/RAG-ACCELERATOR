# Week 3 Deep Analysis - Judge Reliability

## Evaluation Setup
- Judge model: `gemini-2.5-flash`
- Eval JSON files:
	- `evaluations/eval_results/pairwise_eval_week2_recursive_vs_week3_hybrid_rerank.json`
	- `evaluations/eval_results/pairwise_eval_week3_all_techniques.json`
- Techniques covered across files:
	- Week 2 recursive baseline
	- Week 3 baseline hybrid + rerank
	- Week 3 metadata filter variant
	- Week 3 two-stage routing variant

## Question-by-Question Spot Check

### Q1: Formal definition of independence
- Judge said: Week 3 winner; higher direct-context count (`B_direct_count=9` vs `A_direct_count=7`).
- My manual read: both systems retrieved relevant definitions, but Week 3 top chunks were more concentrated on the exact equation form.
- Agreement: agree.
- What the judge missed: Week 2 had one high-quality definition chunk that was still practically usable.

### Q3: Variance shortcut formula
- Judge said: Week 3 winner; direct contexts strongly favored Week 3 (`9` vs `4`) with lower noise.
- My manual read: Week 3 clearly surfaced formula-first chunks at top ranks; Week 2 contained more tangential derivation context.
- Agreement: agree.
- What the judge missed: almost none in this case; verdict aligns with observed retrieval quality.

### Q7: Linearity of expectation and independence
- Judge said: Week 3 winner, but both techniques had weaker directness (`A_direct_count=3`, `B_direct_count=4`).
- My manual read: this is a harder conceptual question and both pipelines retrieved mixed-quality context; Week 3 was better but not dominant.
- Agreement: partially agree.
- What the judge missed: it under-penalized residual noise because neither side had strong direct hits.

### Q10: Monty Hall error pattern
- Judge said: Week 2 winner (the only Week 2 win in final run).
- My manual read: Week 2 had slightly better direct signal on this question (`A_direct_count=5` vs `B_direct_count=4`).
- Agreement: agree.
- What the judge missed: this edge case suggests question-type sensitivity; reranking is not guaranteed to win every prompt.

## Overall Judge Reliability
- Questions checked: 4 out of 10.
- Agreement rate: 4/4 agree or partially agree.
- Systematic biases found: slight bias toward techniques with more direct hits, even when qualitative usefulness between top chunks is close.
- Rerank handling: generally strong; judge consistently identified top-context precision improvements in Week 3.
- Reliability verdict: reliable enough for directional comparison; still requires manual spot checks on close or conceptual questions.

## Additional Artifact-Level Reliability Checks (All-Techniques File)
Source: `evaluations/eval_results/pairwise_eval_week3_all_techniques.json`

- The structured numeric outputs are complete for all 60 matchups and support aggregate ranking.
- Some reasoning fields contain uncertainty wording (for example "assuming ... noise"), indicating that free-text rationale is less stable than numeric fields.
- Practical implication: use numeric summary metrics (`avg_usefulness`, `avg_relevance`, `noise_chunks_total`, `questions_won`) as primary evidence, and treat rationale text as supporting commentary.

## Prompting Observations
- What worked: requiring per-context verdict plus key quote forced grounded judgments and reduced superficial scoring.
- What did not work: score-only summaries without context-by-context evidence were less trustworthy.
- Evolution from Week 2: Week 3 kept pairwise context judging and expanded to all-techniques comparisons, while retaining manual spot checks for reliability control.
