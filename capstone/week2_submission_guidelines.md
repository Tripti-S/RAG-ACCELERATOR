# Week 2 Capstone Submission Guidelines

This document walks you through everything you need to submit for your Week 2 capstone deliverable. Follow it step by step.

---

## Before You Start: Clean Up Your Working Directory

Week 2 generates a lot of intermediate files — multiple RAG results from different strategies, evaluation runs, deduplication artifacts, scratch experiments. Before structuring your submission, separate your final work from your scratch work.

### Create an Archive Folder

In your `week-2/` directory, create an `archive/` folder and move anything that isn't part of your final submission into it:

```
week-2/
├── archive/                           # Scratch pad — NOT part of submission
│   ├── early_experiment_results/      # First attempts, abandoned strategies
│   ├── old_eval_runs/                 # Evaluation runs you iterated past
│   └── notes.md                       # Rough notes, scratch thinking
├── ... (your final deliverables)
```

This keeps your working directory clean and ensures gitingest only picks up what matters.

### Update Your .gitingestignore

Before running gitingest, make sure your `.gitingestignore` **inside `week-2/`** includes:

```
# week-2/.gitingestignore
archive/
rag_results/
data/raw/
data/processed/
*.parquet
*.csv
*.npy
*.bin
prequalify.py
week2_submission_guidelines.md
```

This excludes your scratch work, raw RAG result JSONs (200-400KB each — too large), data files, binary artifacts (like similarity matrices from deduplication), and the submission tooling itself. Note that `eval_results/` is **not** excluded — your final evaluation JSON is kept as grading evidence. Gitingest runs from the `week-2/` subdirectory, so it only captures what's inside that directory.

---

## Your Week 2 Directory Structure

Your capstone repo should now have a `week-2/` directory alongside your existing `week-1/`:

```
my-capstone/
├── week-1/                            # Your Week 1 submission (keep as-is)
└── week-2/
    ├── submission.md                  # Required: your submission document
    ├── docs/
    │   ├── chunking-analysis.md       # Required: corpus analysis through a chunking lens
    │   ├── chunking-strategy.md       # Required: strategy choice, rationale, configuration
    │   └── iteration-log.md           # Required: what you tried, what happened, what you changed
    ├── scripts/                        # Required: your adapted chunking and indexing scripts
    │   ├── [chunking script(s)]       # Your chunking implementation(s)
    │   └── [indexing script(s)]       # Your indexing with new strategy
    ├── evaluations/
    │   ├── test_questions.json        # Required: 8-15 test questions
    │   ├── eval_results/              # Required: your FINAL LLM judge output (kept for grading)
    │   │   └── chunk_eval_[strategies].json
    │   ├── rag_results/               # Your raw RAG outputs (excluded from submission)
    │   ├── week2_comparison.md        # Required: your analysis of results
    │   └── week2_deep_analysis.md     # Required: judge reliability deep-dive
    ├── archive/                        # Your scratch pad (excluded from submission)
    └── .gitingestignore               # Required: tells gitingest what to skip
```

**Note on scripts:** You don't have to follow the exact script numbering from the course (e.g., `06_chunk_with_strategy.py`). Name them in a way that makes sense for your project. The requirement is that your chunking and indexing code is present and functional.

---

## Step 1: Analyze Your Corpus Through a Chunking Lens

Create `week-2/docs/chunking-analysis.md` with:

### Content Type Assessment

Go through your corpus and identify what you're working with:
- [ ] Code files (functions, classes, imports — splitting mid-function kills context)
- [ ] Structured markdown (headers, sections, lists — natural boundary points)
- [ ] Technical documentation (API references, guides — often hierarchical)
- [ ] Multi-topic articles (topic shifts within a single document — semantic boundaries matter)
- [ ] Simple prose (blog posts, narratives — more forgiving to chunk naively)
- [ ] Mixed content (code + text interleaved — needs different treatment for each)
- [ ] Tables or structured data (splitting a table mid-row loses meaning)
- [ ] Short documents (under 200 words — may not need chunking at all)

Don't just check boxes — explain what you found. If your corpus is 80% structured markdown with some code examples, say that. If you have documents that mix three content types, call that out — it matters for your strategy choice.

### Document Length Distribution

- Shortest document: [X words/chars]
- Longest document: [X words/chars]
- Median document: [X words/chars]
- Standard deviation or spread
- How many documents are "too long" for a single chunk?
- How many are "too short" to chunk meaningfully?
- Are there extreme outliers? What are they?

If you ran deduplication in Week 2, include what you found: how many duplicates, what reduction percentage, and whether that changed the distribution.

### Chunking-Relevant Observations

What about your data specifically matters for chunking? This is where your analysis gets unique to your corpus:

- Are there natural section boundaries (headers, dividers, `---` separators)?
- Do topics shift within documents? How often?
- Is there code that shouldn't be split mid-function or mid-class?
- Are there documents where context at the beginning matters for understanding the end?
- Do your documents reference each other? (Cross-document context that chunking destroys)
- Is there metadata (filenames, paths, categories) that could help disambiguate chunks?
- Are there repeated boilerplate sections (navbars, footers, license blocks) that add noise?

The point isn't to answer every question — it's to demonstrate you've looked at your data with chunking in mind and identified the characteristics that should drive your strategy.

---

## Step 2: Select and Document Your Strategy

Create `week-2/docs/chunking-strategy.md` with:

### Strategy Choice

Which strategy did you select? Options include (but aren't limited to):
- Fixed-size / naive (with size variants: small, medium, large)
- Sliding window with overlap
- Recursive / boundary-aware (splits on headers, paragraphs, sentences)
- Semantic (groups by topic similarity)
- AST / code-aware (respects code structure)
- Hybrid (different strategies for different content types in your corpus)

If your corpus has mixed content types, you might use different strategies for different parts — that's a valid approach. Document it.

### Rationale

Why this strategy for your corpus? Connect your choice back to your analysis from Step 1. Reference the decision framework from Lesson 2.11 as a starting point, but your data may suggest a different path:
- CODE-heavy → AST
- STRUCTURED DOCS → Recursive
- MULTI-TOPIC → Semantic
- UNIFORM DOCS → Recursive
- MIXED → Consider hybrid or the dominant content type

If you diverged from the framework, explain why. The "why" matters more than the choice.

### Configuration

- Chunk size: [X tokens/words/chars] and why you picked this size
- Overlap: [X tokens/words/chars] ([Y]%) and why this overlap
- Strategy-specific settings: [e.g., separators for recursive, similarity threshold for semantic, language for AST]
- Embedding model: [model name] and its token limit
- Did you see truncation warnings during indexing? How many chunks exceeded the embedding model's limit?

### What You Considered But Didn't Use

Briefly: what other strategies did you evaluate, and why did you rule them out? This shows your decision-making process.

---

## Step 3: Implement and Index

Place your chunking and indexing scripts in `week-2/scripts/`.

**What must be here:**
- Script(s) that chunk your corpus using your chosen strategy
- Script(s) that index those chunks into a Qdrant collection
- Any preprocessing or deduplication scripts you adapted

**Important:** Keep your Week 1 naive index intact. You need both collections for comparison.

Your new collection should have a different name from Week 1 (e.g., `my_project_recursive` vs `my_project_baseline`).

After indexing, document in your strategy doc:
- Total chunk count (Week 1 naive: [X] → Week 2 strategy: [Y])
- Average chunk size
- Truncation warnings (how many chunks exceeded embedding model limit)
- Indexing time

---

## Step 4: Create Test Questions

Create `week-2/evaluations/test_questions.json` with 8-15 test questions you know the answers to. Mix three types:

- **Factoid** (3-5): Questions with a specific, verifiable answer. "What port does the server run on?"
- **Analytical** (3-5): Questions requiring synthesis across information. "How does authentication differ between v1 and v2?"
- **Conceptual** (2-5): Questions about understanding or explanation. "Why does the system use event sourcing?"

Pick questions that genuinely test different retrieval scenarios. Include at least 1-2 questions you expect your system to struggle with.

**You'll reuse these same questions in Week 3**, so invest time in picking good ones.

---

## Step 5: Generate RAG Results

Run your test questions against both your Week 1 naive index and your Week 2 strategy index. Save the RAG results (retrieved chunks + generated answers) for each strategy.

Place the output files in `week-2/evaluations/rag_results/`:

```
evaluations/rag_results/
├── rag_results_naive_baseline.json      # Week 1 pipeline results
└── rag_results_[your_strategy].json     # Week 2 pipeline results
```

If you tested multiple strategies before settling on your final one, include those results too — they're evidence of experimentation.

---

## Step 6: Evaluate — But Don't Trust Your Judge Blindly

This is the most important part of Week 2. You're not just comparing numbers — you're learning whether your evaluation itself is reliable.

### Run Your LLM Judge

Use the evaluation approach from the course (or adapt it) to compare your strategies. Save evaluation outputs in `week-2/evaluations/eval_results/`.

**You don't have to use the same LLM judge from the course.** If you want to use a different model, a different prompt structure, or a different evaluation rubric — that's on the table. What matters is that your evaluation is reliable for your data and your questions. If you change the judge, document why.

### Deep Evaluate Your Judge's Output

**This is critical.** Don't just take the LLM judge's scores at face value. Your final eval JSON is included in your submission — we can see what the judge said. Your job is to show you actually checked whether the judge was right.

Create `week-2/evaluations/week2_deep_analysis.md` with:

1. Pick 3-5 questions where the judge gave strong opinions (clear winner)
2. Read the actual retrieved chunks and generated answers yourself
3. For each: Does the judge's assessment match what you see? Where does it diverge?
4. Look for cases where the judge missed something, overrated noisy chunks, or got the ranking wrong

**Tip:** You can use Claude (or another LLM) to help you analyze the raw results — but the quality of that analysis depends entirely on how you prompt it. What you ask the model to look for, how you structure the comparison, what criteria you emphasize — that's your judgment call, and it's part of what we grade. The prompting intuition you build here is an important skill.

```markdown
# Week 2 Deep Analysis — Judge Reliability

## Evaluation Setup
- Judge model: [what you used]
- Eval JSON file: [filename of the eval result you're analyzing]

## Question-by-Question Spot Check

### Q[X]: [question text]
- **Judge said:** [winner, reasoning summary]
- **My manual read:** [what you actually see in the chunks]
- **Agreement:** [agree / partially agree / disagree]
- **What the judge missed:** [specific observation]

### Q[Y]: [question text]
...

## Overall Judge Reliability
- Questions checked: [X out of Y]
- Agreement rate: [X/Y]
- Systematic biases found: [e.g., favors longer chunks, ignores noise, etc.]
- Is this judge reliable enough for your rubric? [yes/no and why]

## Prompting Observations
- What worked when using LLMs to analyze results: [observations]
- What didn't work: [observations]
- What you'd change about the evaluation approach: [observations]
```

### Write Your Comparison

Create `week-2/evaluations/week2_comparison.md`:

```markdown
## Evaluation Approach
- Judge model: [what you used]
- Evaluation method: [per-chunk analysis, pairwise, etc.]
- If you changed the judge from the course default, why?

## Results

| # | Question | Naive: Signal | Naive: Cutoffs | Naive: Useful | Strategy: Signal | Strategy: Cutoffs | Strategy: Useful | Winner |
|---|----------|--------------|----------------|---------------|-----------------|-------------------|------------------|--------|
| 1 | [short] | X% | Y | Z/5 | X% | Y | Z/5 | [N/S/Tie] |
| ... | | | | | | | | |

### Metrics
- **Signal %**: How much of each retrieved chunk is actually relevant to the question?
- **Cutoffs**: How many chunks are cut mid-thought or mid-section?
- **Usefulness**: Overall usefulness rating 1-5

## Summary
- How many questions did the new strategy win on?
- Where did naive actually do better (if anywhere)?
- What patterns do you see?
- What's the information density tradeoff?
```

---

## Step 7: Iterate and Log

Create `week-2/docs/iteration-log.md` documenting your experiments:

```markdown
## Iteration 1: [What you tried]
- Configuration: [settings]
- Result: [what happened — include specific numbers]
- Observation: [what you learned]

## Iteration 2: [What you changed and why]
- Configuration: [settings]
- Result: [what happened]
- Observation: [what you learned]

## Final Configuration
- Strategy: [name]
- Settings: [final params]
- Why this is your stopping point: [explanation]

## Lessons Learned
- [What surprised you]
- [What you'd do differently]
- [What you still don't know]
```

Stop iterating when improvements become marginal (1-2 points) or scores plateau.

---

## Step 8: Write Your Submission Document

Create `week-2/submission.md` using the exact template below. Every section is required.

```markdown
# Week 2 Capstone Submission

## Student Name(s)
[Full name of each team member, one per line]

## Project Title
[Same project as Week 1]

## Week 1 Recap
- **Corpus:** [brief — X docs, Y domain]
- **Week 1 baseline performance:** [your honest summary from Week 1 observations]
- **Key issue identified:** [what you wanted to improve — retrieval? noise? cut-off chunks?]

## Chunking Analysis Summary
- **Dominant content types:** [what your corpus mostly contains]
- **Document length distribution:** [short summary — median, range, outliers]
- **Key chunking consideration:** [the most important thing about your data for chunking]
- **Deduplication results:** [if applicable — files removed, reduction %]

## Strategy Choice
- **Strategy:** [name]
- **Rationale:** [1-2 sentences on why this strategy for your data]
- **Configuration:** chunk size [X], overlap [Y], [other settings]
- **Embedding model:** [model name and dimension]
- **New collection name:** [name]
- **Total chunks:** [count] (Week 1 baseline: [count])
- **Truncation warnings:** [count and impact]

## Evaluation Approach
- **Judge model:** [what you used]
- **Method:** [per-chunk analysis, pairwise, hybrid, etc.]
- **Changes from course default:** [if any, and why]

## Evaluation Summary

| Metric | Naive Baseline | New Strategy | Change |
|--------|---------------|--------------|--------|
| Avg signal % | | | |
| Total cutoffs | | | |
| Avg usefulness | | | |
| Questions won | | | |

## Judge Reliability Assessment
- **Spot-checked questions:** [which ones]
- **Agreement with manual review:** [summary]
- **Judge weaknesses found:** [if any]

## Key Observations
- **Where did the new strategy help most?** [Your observations]
- **Where did it not help (or hurt)?** [Your observations]
- **What's the information density tradeoff?** [Smaller chunks = more precise but less context, etc.]
- **What would you improve next?** [Your thinking on what to tackle in Week 3]

## Iteration Summary
- **Total iterations:** [count]
- **Most impactful change:** [what made the biggest difference]
- **Stopping rationale:** [why you stopped where you did]

## Self-Assessment

| Criteria | Score (1-5) | Notes |
|----------|-------------|-------|
| Chunking analysis depth | | |
| Strategy selection rationale | | |
| Evaluation thoroughness | | |
| Judge reliability check | | |
| Iteration quality | | |
| Documentation clarity | | |
```

---

## Step 9: Generate and Validate Your Submission

From your capstone repo root (the directory that contains `week-2/`):

```bash
uv run gitingest week-2/ -o firstname_lastname_week2_submission.txt
```

This only captures files inside `week-2/`. Make sure your `archive/`, prequalify script, and guidelines doc are in `.gitingestignore` so they don't bloat the output.

Then run the prequalify check:

```bash
uv run python week-2/prequalify.py
```

Fix any issues it flags before submitting.

---

## Step 10: Submit

1. Go to the **#capstone** channel on Discord.
2. Upload your `.txt` file and tag **@Nocto**:

```
@Nocto Week 2 submission
```

3. Nocto will validate and confirm receipt. An instructor will review and provide feedback.

---

## Grading Rubric

| Criteria | Weight | What we look for |
|----------|--------|-----------------|
| **Chunking Analysis** | 20% | Corpus analyzed through chunking lens, content types identified, distribution documented, observations specific to your data |
| **Strategy Selection** | 15% | Clear rationale tied to analysis, configuration documented, alternatives considered |
| **Evaluation Quality** | 25% | 8-15 test questions, honest comparison with metrics, patterns identified |
| **Judge Reliability** | 15% | Evidence of checking the judge's work against raw results, awareness of evaluation limitations, prompting quality |
| **Iteration & Documentation** | 15% | Multiple iterations attempted, changes justified, stopping point explained |
| **Improvement Over Baseline** | 10% | Evidence of meaningful comparison with Week 1, clear observations about what changed |

This is about the process of systematic experimentation and learning to evaluate your own evaluations, not about getting the "best" chunking strategy. Show your thinking.

---

## Checklist Before Submitting

- [ ] `archive/` folder created for scratch work
- [ ] `.gitingestignore` includes: `archive/`, `rag_results/`, `data/`, `*.npy`, `*.bin`, `prequalify.py`, `week2_submission_guidelines.md`
- [ ] `week-2/submission.md` is complete (all sections filled)
- [ ] `week-2/docs/chunking-analysis.md` has content types, distribution, and corpus-specific observations
- [ ] `week-2/docs/chunking-strategy.md` has strategy, rationale, configuration, and alternatives considered
- [ ] `week-2/docs/iteration-log.md` documents at least 2 iterations
- [ ] `week-2/evaluations/test_questions.json` has 8-15 questions
- [ ] `week-2/evaluations/eval_results/` has your FINAL LLM judge output JSON (kept for grading)
- [ ] `week-2/evaluations/week2_comparison.md` has per-question comparison and summary
- [ ] `week-2/evaluations/week2_deep_analysis.md` has judge reliability spot-check with specific questions
- [ ] `week-2/scripts/` contains your chunking and indexing scripts
- [ ] Week 1 naive index is still intact for comparison
- [ ] Prequalify script passes with no errors
