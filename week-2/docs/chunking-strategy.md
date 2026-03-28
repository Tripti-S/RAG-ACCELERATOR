# Chunking Strategy

## Data Sources
- `week-2/evaluations/metrics_snapshot_1.json`
- `week-2/evaluations/eval_results/final_comparitive_chunk_eval_20260301_211714.json`
- `week-2/evaluations/rag_results/rag_results_recursive_20260301_041934.json`
- `week-2/evaluations/rag_results/rag_results_semantic_20260301_042330.json`
- `week-2/evaluations/rag_results/rag_results_hybrid_20260301_111809.json`
- `week-2/scripts/strategy/logical_chunker.py`
- `week-2/scripts/strategy/semantic_chunker.py`
- `week-2/scripts/strategy/hybrid_chunker.py`
- `week-2/scripts/strategy/naive_chunker.py`
- `week-2/scripts/Indexing/index_hybrid.py`
- `week-2/archive/comparisons/snapshot_chunk_count_comparison.md`

## Strategy Choice
- Selected final strategy: **recursive** (`week2_recursive`).
- Final judge artifact ranks recursive 1st on **6/10** questions (hybrid 3/10, semantic 1/10).
- Evaluation setup used `gpt-4o-mini` with `hybrid_two_stage` (from metrics snapshot).

## Rationale
The corpus evidence in Week 2 is documentation-heavy (459/459 selected files), with very wide length spread (36 to 62,950 words). This creates a boundary problem for fixed-only chunking: short docs do not need aggressive splitting, while long docs can lose coherence if split arbitrarily.

Recursive chunking was selected because it is boundary-aware and preserves structure better on long technical/educational text. In this project, it provided the strongest overall judged outcome while keeping retrieval relevance close to semantic.

Why not choose fastest strategy only:
- Semantic had faster average latency (**9.151s**) and slightly higher top-1 score (**0.7979**),
- but recursive achieved better final judged wins (6/10), which was the primary decision criterion for answer quality.

Why not choose hybrid as final:
- Hybrid showed useful context-linking behavior in some cases,
- but artifact-level runtime variance was high (max latency **91.58s**) with lower average top-1 score (**0.6676**) in this run set.

## Configuration

### Implemented chunkers (code-level facts)
- **Naive baseline (`NaiveChunker`, medium variant):** 400 words, 50 overlap (`scripts/strategy/naive_chunker.py`).
- **Recursive (`RecursiveChunker`):** `chunk_size=2000` chars, `chunk_overlap=200` chars, separators `"\n\n", "\n", ". ", " ", ""` (`scripts/strategy/logical_chunker.py`).
- **Semantic (`SemanticChunkerComponent`):** breakpoint type `percentile`, amount `95`, boundary model `sentence-transformers/all-MiniLM-L6-v2` (`scripts/strategy/semantic_chunker.py`).
- **Hybrid (`HybridChunkerComponent`):** routes `multi_topic`/`ocr` to semantic, otherwise naive-medium (`scripts/strategy/hybrid_chunker.py`).

### Embedding model settings
- Recursive/Semantic RAG artifacts: `BGE-large-en-v1.5 (FastEmbed)`, 1024 dimensions.
- Hybrid RAG artifact: `all-MiniLM-L6-v2`, 384 dimensions.

### Collections used
- `week2_recursive`
- `week2_semantic`
- `week2_hybrid`
- Week-1 baseline reference from trace artifact: `week-1/traces/traces.json`

### Chunk-count evidence (from archive comparison snapshot)
- Naive baseline: **482** chunks
- Recursive: **2315** chunks
- Semantic: **2792** chunks

### Truncation warnings
- The final evaluation JSON does not contain per-strategy truncation counts.
- Truncation analysis utilities exist in pipeline code (`create_chunking_pipeline.py`), but no unified truncation table is emitted in final evaluation artifacts.

## What Was Considered But Not Used
- **Naive-only as final:** efficient baseline, but not boundary-aware for long mixed-concept documents.
- **Semantic as final:** strong speed/top-1 in this run set, but fewer judged wins (1/10).
- **Hybrid as final:** useful for cross-topic linkage, but high latency variability and lower top-1 average in captured artifacts.

## Strategy Outcome Summary
| Strategy | 1st-place wins (10 Q) | Avg latency (s) | Avg top-1 score |
|---|---:|---:|---:|
| recursive | 6 | 11.696 | 0.7953 |
| semantic | 1 | 9.151 | 0.7979 |
| hybrid | 3 | 20.641 | 0.6676 |

Decision rule used: prioritize final judged answer quality outcome across the shared 10-question set, while documenting runtime/retrieval tradeoffs explicitly.
