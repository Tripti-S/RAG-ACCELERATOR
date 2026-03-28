# Conceptual Building (Week 2)

## Objective
Week 2 focused on moving from a baseline RAG pipeline to a more evidence-driven retrieval design by improving three core stages:

1. Corpus quality (deduplication and file selection)
2. Chunking strategy (naive vs recursive vs semantic vs hybrid)
3. Evaluation traceability (comparable outputs, logs, and rationale)

---

## 1) Corpus Preparation and Deduplication Thinking

### Why this mattered
Noisy or repeated documents reduce retrieval quality and inflate index size. Before chunking strategy comparisons, corpus quality needed to be controlled.

### Conceptual decisions
- Start with deterministic dedup foundations (manifest-driven file tracking).
- Explore enhanced dedup ideas (embedding similarity + fuzzy matching + topic clustering) as optional improvements.
- Preserve reproducibility with manifest snapshots.

### Output implications
- Better control of indexing scope.
- Cleaner comparison across chunking strategies.
- Easier traceability between selected corpus and final evaluation outcomes.

---

## 2) Chunking as the Main Experimental Lever

### Baseline reference
Week 1 naive chunking provided a control condition for comparison.

### Week 2 strategy space
- **Naive/fixed-size:** efficient but boundary-agnostic.
- **Recursive:** preserves structural boundaries; increases chunk volume.
- **Semantic:** topic-aware segmentation; often highest chunk volume and cost.
- **Hybrid:** combines structure and semantics for mixed corpus behavior.

### Core tradeoff learned
Chunking is a tradeoff across:
- Retrieval granularity
- Context coherence
- Indexing/storage cost
- Embedding truncation risk

The key conceptual shift was from “pick one chunk size” to “choose strategy based on document behavior and evaluation evidence.”

---

## 3) Embedding and Retrieval Framing

### Reasoning
Embedding choice and chunk design must be aligned:
- Smaller semantic chunks increase precision but also total vectors.
- Larger chunks preserve context but risk dilution or token pressure.
- Asymmetric retrieval (short query to richer chunk context) remains a useful fit for educational corpora.

### Practical implication
Chunking policy cannot be evaluated in isolation; it must be assessed together with embedding limits, retrieval depth (`top_k`), and answer quality signals.

---

## 4) Evaluation and Traceability Discipline

### What was improved
- Strategy-isolated outputs and result files.
- Preserved walkthrough traces for reproducibility.
- Comparable narrative for why one strategy wins per question.

### Why this matters conceptually
A RAG pipeline is only as trustworthy as its experimental trace. Logging and structured result artifacts convert “it seems better” into “it is defensibly better for these reasons.”

---

## 5) What This Built Conceptually

By the end of Week 2, the pipeline moved from implementation-first to evaluation-first:

- From static baseline assumptions → to measurable strategy comparisons.
- From one-size chunking → to context-aware strategy selection.
- From ad-hoc notes → to traceable artifacts linked to decisions.

This forms the foundation for Week 3+: retrieval tuning, reranking, prompt-context optimization, and failure-mode analysis.

---

## Suggested Placement in Main Week 2 Docs

When promoting this file out of archive, place it as:

- `week-2/docs/Conceptual_building.md`

Then link it from:
- `week-2/submission.md`
- `week-2/docs/iteration-log.md`

so the conceptual rationale sits next to experimental outputs.