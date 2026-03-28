# Week 3 Context Alignment (Week 1 + Week 2 History)

## Why this file exists
Week 3 code in `week3_retrieval/` is currently MCP-oriented in prompts and metadata assumptions, but this capstone corpus and prior work are probability/statistics-focused. This document captures what was done in Week 1 and Week 2 and defines how Week 3 should be reworked in `week-3/` to stay consistent.

## Week 1: What was built

### Project objective
- Domain-constrained RAG for probability and statistics learning support.
- Sources include MIT notes/transcripts, OpenIntro chapters, textbook content, and processed note material.

### Data pipeline and corpus
- Raw/processed data pipeline was established under `week-1/data/` with layered preprocessing.
- Final reported corpus scale in Week 1 docs: 964 docs and ~1.7M tokens.
- Week 1 retrieval traces were generated for 5 probability questions.

### Week 1 implementation shape
- Indexing pipeline: file routing -> conversion -> cleaning -> chunking -> FastEmbed embeddings -> Qdrant write.
- Baseline chunking used fixed word chunks with overlap in Week 1 scripts.
- RAG query pipeline used embedder + retriever + prompt builder + Gemini generation.

### Key references
- `week-1/submission.md`
- `week-1/docs/scoping.md`
- `week-1/analysis/data_quality_notes.md`
- `week-1/scripts/02_create_pipeline.py`
- `week-1/scripts/03_run_indexing.py`
- `week-1/scripts/04_test_rag_system.py`
- `week-1/scripts/06_run_traces.py`
- `week-1/traces/traces.json`

## Week 2: What changed

### Strategy experimentation focus
- Week 2 moved from single baseline chunking to comparative strategy evaluation.
- Implemented/compared: naive variants, recursive/logical chunking, semantic chunking, and hybrid framing.

### Corpus control
- Dedup + selection manifest workflow created and reused.
- `selected_files_manifest.json` finalized with 459 selected docs and ~0.65% reported reduction.

### Evaluation process
- RAG results generated per strategy with shared test questions.
- Two-stage LLM judge workflow used for comparative quality analysis.
- Final comparison artifact ranked recursive highest in the recorded Week 2 runs.

### Key references
- `week-2/submission.md`
- `week-2/docs/chunking-analysis.md`
- `week-2/docs/chunking-strategy.md`
- `week-2/docs/iteration-log.md`
- `week-2/evaluations/week2_comparison.md`
- `week-2/evaluations/week2_deep_analysis.md`
- `week-2/scripts/deduplication/deduplicate_documents.py`
- `week-2/scripts/Indexing/index_strategy.py`
- `week-2/scripts/pipeline/create_chunking_pipeline.py`
- `week-2/scripts/pipeline/create_rag_pipeline.py`
- `week-2/scripts/pipeline/generate_rag_results.py`
- `week-2/evaluations/eval_results/final_comparitive_chunk_eval_20260301_211714.json`

## Week 3 retrieval reference: what it currently assumes

The reference implementation under `week3_retrieval/` is technically strong but includes MCP-oriented defaults:
- Prompt/system-role text repeatedly says MCP assistant.
- Metadata labels/categories are tuned for MCP implementation concepts.
- Retrieval/evaluation scripts assume a different domain wording than Week 1/2 probability corpus.

## Mismatch to fix before Week 3 finalization

1. Prompt domain mismatch (MCP wording vs probability/statistics intent).
2. Potential metadata category mismatch (MCP taxonomy vs probability taxonomy).
3. Week 3 docs currently contain placeholders and generic findings; they must be replaced with probability-specific run evidence.
4. Evaluation narratives should compare Week 2 probability baseline against Week 3 probability retrieval techniques, not MCP framing.

## Week 3 rework direction (in `week-3/`)

### Keep from `week3_retrieval/`
- Hybrid indexing architecture (dense + sparse + RRF).
- Reranking flow and candidate-depth logic.
- Optional narrowing variants (metadata filter, two-stage file routing).
- Pairwise evaluation scaffolding.

### Adapt for this capstone
- Replace MCP-focused prompt templates with probability/statistics assistant behavior.
- Align category metadata/intent mapping with probability topics (e.g., distributions, expectation, Bayes, CLT, conditional probability, inference/hypothesis testing).
- Ensure Week 3 test questions reuse Week 2 probability question set.
- Regenerate Week 3 results/evaluations from probability corpus and update Week 3 docs with real metrics.

## Execution order for upcoming Week 3 work

1. Prepare artifacts expected by Week 3 scripts from Week 2 data products.
2. Run hybrid indexing on selected probability corpus files.
3. Run technique 1a and 1b first (baseline + rerank).
4. Run optional narrowing techniques (2 and 3) only if useful.
5. Run pairwise evaluation and produce final eval JSON in `week-3/evaluations/eval_results/`.
6. Update `week-3/docs/*`, `week-3/evaluations/*`, and `week-3/submission.md` with probability-grounded findings.

## Practical note
The Week 1 processed corpus is large; for quick debugging, test mode should be used first, then full mode for final evidence runs.
