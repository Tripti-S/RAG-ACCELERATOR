# Week 2 Deep Analysis — Judge Reliability

## Evaluation Setup
- Judge model: gemini-2.5-flash
- Eval JSON file: hybrid_chunk_eval_20260301_123456.json

## Question-by-Question Spot Check

### Q1: State the formal definition of independence between two events.
- **Judge said:** Hybrid strategy is the clear winner due to high signal and minimal cutoffs.
- **My manual read:** Hybrid chunks are focused and relevant, with no critical information lost.
- **Agreement:** agree
- **What the judge missed:** Slightly overrated the usefulness of one chunk with some noise.

### Q2: What is the law of total probability?
- **Judge said:** Naive strategy had more cutoffs, hybrid provided more direct context.
- **My manual read:** Hybrid chunks were more concise, but naive included some useful background.
- **Agreement:** partially agree
- **What the judge missed:** Naive's background chunk was actually helpful for context.

### Q3: Explain Bayes' theorem and its application.
- **Judge said:** Hybrid is best, all chunks highly relevant.
- **My manual read:** Hybrid chunks are indeed highly relevant, but one chunk was redundant.
- **Agreement:** agree
- **What the judge missed:** Did not penalize redundancy in hybrid chunks.

## Overall Judge Reliability
- Questions checked: 3 out of 10
- Agreement rate: 3/3 (2 full, 1 partial)
- Systematic biases found: Slight preference for higher signal, sometimes ignores redundancy or minor noise.
- Is this judge reliable enough for your rubric? yes — generally reliable, but manual spot-checking is still needed for edge cases.

## Prompting Observations
- What worked when using LLMs to analyze results: Clear, structured prompts and explicit criteria improved consistency.
- What didn't work: LLM sometimes missed subtle redundancy or overvalued chunk focus.
- What you'd change about the evaluation approach: Add explicit checks for redundancy and context completeness in the prompt.
# Week 2 Deep Analysis — Judge Reliability

## Evaluation Setup
- Judge model: gpt-3.5-turbo
- Eval JSON file: chunk_eval_hybrid.json

## Question-by-Question Spot Check

### Q1: What is the main authentication method?
- **Judge said:** Hybrid strategy, because the retrieved chunk was more focused and complete.
- **My manual read:** Hybrid chunk included the full authentication section; naive split it mid-way.
- **Agreement:** agree
- **What the judge missed:** Did not mention that naive chunk omitted a key sentence.

### Q2: How does the system handle errors?
- **Judge said:** Tie, both strategies retrieved similar content.
- **My manual read:** Hybrid chunk was more concise, but both contained the answer.
- **Agreement:** partially agree
- **What the judge missed:** Hybrid chunk had less noise, which was not credited.

### Q3: What is the default port?
- **Judge said:** Naive, as it retrieved the correct value directly.
- **My manual read:** Both strategies retrieved the value, but naive was more direct.
- **Agreement:** agree
- **What the judge missed:** Hybrid chunk included extra context, but not needed for this factoid.

## Overall Judge Reliability
- Questions checked: 3 out of 10
- Agreement rate: 2.5/3
- Systematic biases found: Slight preference for longer, more detailed chunks; sometimes ignores noise.
- Is this judge reliable enough for your rubric? Yes, but manual spot-checking is still needed for edge cases.

## Prompting Observations
- What worked when using LLMs to analyze results: Clear, specific prompts about chunk relevance and completeness.
- What didn't work: LLM sometimes overvalues chunk length or ignores minor noise.
- What you'd change about the evaluation approach: Add explicit instructions to penalize noisy or off-topic content.
