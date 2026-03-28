# Week 2 Value-Add Report: Design Considerations

It highlights design decisions, experimentation, and evidence-backed outcomes.


## 2 What is Added
### A. Multi-Strategy Architecture
 I implemented and analyzed:
- **Naive baseline**   Week 1 continuity
- **Recursive strategy**
- **Semantic strategy**
- **Hybrid framing** for mixed behavior

This enabled cross-strategy evaluation rather than one-shot reporting.

### B. Corpus Engineering + Dedup Thinking
I treated corpus quality as a first-class system component:
- Manifest-driven corpus selection and traceability
- Dedup experimentation and analysis notes
- Preservation of reproducibility artifacts

This reduced noise in strategy comparison and made evaluation conclusions more defensible.

### C. Evaluation Reliability 
I added a reliability process:
- Stage-level interpretation   `signal`, `useful`, `cutoffs`
- Cross-checking judge outcomes against strategy-level behavior
- Explicit limitations when schema mismatch prevented strict direct deltas

This moved the project from "judge says X" to "judge says X and we verified where/why that holds."

### D. Human + LLM Review Workflow
I implemented evaluation support for both machine and manual review:
- LLM-based scoring/evaluation pipeline artifacts
- Human review workflow/viewer logic for direct comparative reads

This increases confidence in the evaluation process and supports stakeholder auditability.

### E. Archive-Driven Design Documentation
Instead of losing experiments, I organized and mapped archive material into purposeful categories:
- Strategy reasoning
- Comparison snapshots
- Dedup experiments
- Tracing references
- Evaluation snapshots
- Submission versions

This preserves design history and makes decision provenance explicit.

---

## 3 Baseline vs Value-Add Matrix

| Area | Baseline expectation | What I delivered |
|---|---|---|
| Strategy scope | One strategy + baseline mention | Naive + Recursive + Semantic + Hybrid reasoning |
| Corpus handling | Basic preparation | Deduplication logic, manifest traceability, corpus-quality controls |
| Evaluation | Single final judge output | Multi-artifact evaluation + reliability interpretation + manual-review support |
| Comparison depth | Summary table | Strategy-by-strategy runtime/relevance/ranking synthesis with caveats |
| Documentation | Required docs only | Structured archive map + conceptual synthesis + stakeholder-facing reasoning |
| Reproducibility | Minimal | Timestamped artifacts, trace files, and explicit source mapping |

---

## 4 Why These Design Choices Were Necessary for This Domain   Probability Education
The corpus is educational probability material with:
- hierarchical explanation flow,
- concept-to-formula dependencies,
- examples tied to surrounding context,
- topic transitions within long documents.

### Domain implication
A fixed chunking policy alone is often insufficient because educational questions may require:
- local formula precision, and
- broader explanatory context.

This is why the project explored recursive, semantic, and hybrid behavior rather than forcing a single naive design.

---

## 5 Key Findings from Experiments and Analysis

### Finding 1: Fixed/naive is efficient but less expressive for complex educational retrieval
- Week 1 traces provide a useful operational baseline   speed + stable retrieval count.
- However, naive schema is not fully comparable to Week 2 strategy artifacts for deep quality scoring.

### Finding 2: Recursive performs strongly for structured educational coverage
- Final ranking artifacts favored **recursive** most often.
- Recursive aligns well with structured markdown/section boundaries and complete conceptual coverage.

### Finding 3: Semantic improves topical separation where sections are mixed
- Semantic behavior is useful when topic shifts occur within long chapters.
- It can improve focus but introduces extra chunking/indexing complexity.

### Finding 4: Hybrid showed contextual richness but uneven behavior
- Hybrid reasoning remains strong when correlation across two related topics is needed.
- In observed runs, hybrid had variability and did not dominate every metric.
- Practical observation from this project: hybrid can be context-rich, but formula-centric precision may still require stricter boundary control and targeted tuning.

### Finding 5: Evaluation quality depends on process, not just model choice
- Using `gpt-4o-mini` judge with multi-strategy artifacts helped ranking decisions.
- Reliability improved when stage outputs were interpreted with manual spot-check logic.

---

## 6 What This Demonstrates to Stakeholders
it is a **full experimental evaluation effort** with:
- structured decision-making,
- strategy iteration,
- engineering implementation,
- evidence traceability,
- and explicit discussion of tradeoffs/limits.

In short:  I optimized for **evaluation credibility** and **design clarity**.

---

## 7 Evidence and Design Provenance   Where Details Live

### Final evidence artifacts
- `week-2/evaluations/metrics_snapshot_1.json`
- `week-2/evaluations/eval_results/final_comparitive_chunk_eval_20260301_211714.json`
- `week-2/evaluations/rag_results/rag_results_recursive_20260301_041934.json`
- `week-2/evaluations/rag_results/rag_results_semantic_20260301_042330.json`
- `week-2/evaluations/rag_results/rag_results_hybrid_20260301_111809.json`
- `week-1/traces/traces.json`

### Design discussions and rationale history
- `week-2/archive/Conceptual_building.md`
- `week-2/archive/strategy_reasoning/active_hybrid_strategy_detailed.md`
- `week-2/archive/comparisons/snapshot_chunk_count_comparison.md`
- `week-2/archive/dedup_experiments/`
- `week-2/archive/README.md`

### Submission-facing synthesized docs
- `week-2/submission_1.md`
- `week-2/evaluations/week2_comparison_1.md`
- `week-2/evaluations/week2_deep_analysis_1.md`
- `week-2/docs/chunking-analysis_1.md`
- `week-2/docs/chunking-strategy_1.md`
- `week-2/docs/iteration-log_1.md`

---

## 8 Final Position
For this probability-focused educational corpus, the evidence supports:
- avoiding simplistic fixed-only chunking as the sole strategy,
- using recursive structure-awareness as a strong default foundation,
- applying hybrid/semantic reasoning when cross-topic conceptual linkage is required,
- and keeping evaluation reliability checks as a mandatory part of decision making.

This is the value added beyond baseline compliance.
