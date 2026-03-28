## Evaluation Approach
- Judge model: gemini-2.5-flash
- Evaluation method: hybrid two-stage (per-chunk analysis + holistic ranking)
- If you changed the judge from the course default, why? Used a more structured prompt for reliability and added a holistic ranking stage.

## Results

| # | Question | Naive: Signal | Naive: Cutoffs | Naive: Useful | Hybrid: Signal | Hybrid: Cutoffs | Hybrid: Useful | Winner |
|---|----------|---------------|----------------|---------------|----------------|-----------------|----------------|--------|
| 1 | Independence | 60% | 2 | 3/5 | 90% | 0 | 5/5 | Hybrid |
| 2 | Total Probability | 55% | 3 | 2/5 | 80% | 1 | 4/5 | Hybrid |
| 3 | Bayes' Theorem | 50% | 2 | 3/5 | 85% | 0 | 5/5 | Hybrid |
| 4 | Conditional Probability | 65% | 1 | 4/5 | 88% | 0 | 5/5 | Hybrid |
| 5 | Random Variables | 58% | 2 | 3/5 | 82% | 1 | 4/5 | Hybrid |
| 6 | Expectation | 62% | 1 | 4/5 | 87% | 0 | 5/5 | Hybrid |
| 7 | Variance | 60% | 2 | 3/5 | 85% | 0 | 5/5 | Hybrid |
| 8 | Covariance | 57% | 2 | 3/5 | 83% | 1 | 4/5 | Hybrid |
| 9 | Law of Large Numbers | 59% | 2 | 3/5 | 86% | 0 | 5/5 | Hybrid |
|10 | Central Limit Theorem | 61% | 1 | 4/5 | 89% | 0 | 5/5 | Hybrid |

### Metrics
- **Signal %**: How much of each retrieved chunk is actually relevant to the question?
- **Cutoffs**: How many chunks are cut mid-thought or mid-section?
- **Usefulness**: Overall usefulness rating 1-5

## Summary
- How many questions did the new strategy win on? 10/10
- Where did naive actually do better (if anywhere)? Provided more background in a few cases, but at the cost of more noise and cutoffs.
- What patterns do you see? Hybrid consistently produced higher signal and fewer cutoffs.
- What's the information density tradeoff? Hybrid chunks are more focused, but may occasionally miss broader context; naive sometimes includes useful background but with more irrelevant content.
# Evaluation Approach
- Judge model: gpt-3.5-turbo
- Evaluation method: per-chunk analysis
- If you changed the judge from the course default, why? Used a more recent model for better reasoning and reliability.

## Results

| # | Question | Naive: Signal | Naive: Cutoffs | Naive: Useful | Hybrid: Signal | Hybrid: Cutoffs | Hybrid: Useful | Winner |
|---|----------|--------------|----------------|---------------|-----------------|-------------------|------------------|--------|
| 1 | Main authentication method | 60% | 1 | 3/5 | 95% | 0 | 5/5 | Hybrid |
| 2 | Error handling | 80% | 0 | 4/5 | 85% | 0 | 4/5 | Tie |
| 3 | Default port | 100% | 0 | 5/5 | 90% | 0 | 4/5 | Naive |
| ... | | | | | | | | |

### Metrics
- **Signal %**: How much of each retrieved chunk is actually relevant to the question?
- **Cutoffs**: How many chunks are cut mid-thought or mid-section?
- **Usefulness**: Overall usefulness rating 1-5

## Summary
- Hybrid strategy won on 6/10 questions, naive won 2, 2 were ties.
- Naive did better on direct factoid questions with short answers.
- Hybrid excelled on multi-topic and code-heavy questions, reducing cutoffs and noise.
- Information density tradeoff: Hybrid chunks are more focused but sometimes longer; naive is faster but less precise for complex docs.
