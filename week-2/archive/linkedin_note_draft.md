# LinkedIn Note Drafts: Weekend Build Summary

## Option Story (Week 1 → Week 2 journey)
Over the weekend, I turned my RAG capstone from a solid baseline into a much deeper retrieval engineering project.

**Week 1: what I established**
- Built an end-to-end probability-focused RAG system on a 964-document corpus (~1.7M tokens).
- Set up Qdrant + BGE-large embeddings with a structured chunking baseline (~400-word chunks with overlap).
- Validated strong performance on foundational probability questions (Bayes, CLT, independence, expectation).
- Identified the real bottleneck: when retrieval context is sparse or noisy, generation quality drops.

**Week 1 struggles**
- Fragmented source quality (OCR + textbook + notes) created consistency challenges.
- Baseline retrieval worked well for core definitions but gave limited confidence for harder cross-topic queries.
- Evaluation was mostly qualitative at first, so comparison depth was limited.

**Week 2: what I changed**
- Kept Week 1 naive baseline intact for honest comparison.
- Expanded from one strategy to multi-strategy analysis: recursive, semantic, and hybrid.
- Added deduplication reasoning + manifest traceability to improve corpus control.
- Built stronger evaluation discipline: LLM judging, reliability spot-checks, and manual review support.

**What I learned from Week 1 vs Week 2**
- Fixed-only chunking is efficient, but for educational probability content it can miss concept-to-formula dependencies.
- Recursive chunking gave strong structural coverage and won most often in final rankings.
- Hybrid was rich in context when questions required correlation across related topics, but needed tighter tuning for consistency in formula-heavy cases.
- Better evaluation process changes decisions: it is not only about model quality, it is about judge reliability and traceability.

**Big takeaway**
Week 1 proved the system works. Week 2 proved why a strategy works (or fails) through evidence.

I’m excited to take this into Week 3 with reranking and formula-aware retrieval tuning.

#RAG #LLM #AIEngineering #MLOps #Evaluation #InformationRetrieval #MachineLearning

## Option A (concise)
Weekend project update: I rebuilt my RAG capstone evaluation workflow from a basic baseline into a full multi-strategy experiment pipeline.

What I implemented:
- Baseline continuity with Week 1 naive retrieval for honest comparison
- Recursive, semantic, and hybrid chunking analysis
- Deduplication and corpus-quality controls before indexing
- LLM-based judging plus manual reliability spot-checks
- Traceable artifacts and decision logs for auditability

Key lesson: for probability education content, fixed-only chunking is often too rigid. Recursive structure awareness performed strongly, while hybrid helped in cross-topic context-heavy cases (with tradeoffs in consistency).

Biggest takeaway for me: evaluation quality matters as much as retrieval quality. I focused on proving why decisions were made, not only reporting scores.

#RAG #LLM #InformationRetrieval #MLOps #AIEngineering #DataScience #Evaluation

---

## Option B (detailed)
This weekend I pushed my RAG capstone far beyond baseline requirements and treated it like a real retrieval engineering project.

Instead of stopping at a single chunking strategy, I built and compared multiple approaches (naive baseline, recursive, semantic, and hybrid framing), then tied the results back to artifact-level evidence.

What I focused on:
- Corpus discipline first (dedup reasoning + manifest-backed traceability)
- Strategy comparison instead of single-path assumptions
- LLM-judge outputs with reliability checks, not blind score acceptance
- Human-review support for side-by-side inspection of retrieved context
- Structured documentation of design choices, tradeoffs, and iteration history

What I learned in this domain (probability education):
- Fixed-only chunking is efficient but can miss concept-to-formula context dependencies
- Recursive chunking gave strong structured coverage
- Hybrid can be context-rich when two related topics must be connected, but needs careful tuning for formula precision and consistency
- Better evaluation process leads to better strategy decisions

Most valuable skill I practiced: building a defensible evaluation process that explains not just what won, but why.

#RAG #LLM #AIEngineering #RetrievalAugmentedGeneration #MLOps #PromptEngineering #Evaluation #MachineLearning

---

## Option C (professional story format)
This weekend was a clear reminder that building a working RAG system and building a trustworthy RAG system are two different milestones.

In **Week 1**, I established a strong baseline:
- 964-domain-document corpus (~1.7M tokens)
- End-to-end pipeline with Qdrant + BGE-large embeddings
- Structured chunking baseline and stable outputs on foundational probability questions

But Week 1 also surfaced the challenge: retrieval quality varied with content structure, and qualitative traces alone were not enough to explain tradeoffs confidently.

In **Week 2**, I treated that gap as an engineering problem:
- Preserved baseline for direct comparison
- Implemented and analyzed recursive, semantic, and hybrid chunking paths
- Added dedup/corpus-traceability discipline
- Evaluated with LLM judgement plus reliability checks and manual review patterns

What stood out:
- Recursive performed strongly for structured educational material.
- Hybrid helped when cross-topic context linkage was needed.
- Fixed-only chunking remained efficient but less expressive for concept+formula dependency patterns.

The biggest personal learning: rigorous evaluation design is a feature, not an afterthought.

Week 1 gave me functionality. Week 2 gave me evidence-backed decision making.

#RAG #LLM #AIEngineering #RetrievalAugmentedGeneration #MLOps #Evaluation #DataScience

---

## Optional closing line ideas
- Open to feedback from others building evaluation-first RAG workflows.
- Curious how others validate LLM judges beyond aggregate scores.
- Next step: reranking and formula-aware retrieval tuning.
