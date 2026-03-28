# Week 3 Retrieval Strategy

## Hybrid Configuration

- Dense embedding model: `voyage-4-lite`
- Dense dimensions: `2048`
- Sparse model: `Qdrant/bm25`
- Fusion method: Reciprocal Rank Fusion (RRF) inside Qdrant hybrid retrieval
- Collection: `week3_hybrid_recursive`
- Candidate retrieval setup: dense prefetch `100`, sparse prefetch `100`, fused candidate set `top_k=50` for rerank pipeline

## Hybrid Indexing Evidence

- Indexing script: `week-3/scripts/indexing/01_index_hybrid.py`
- Data source for indexing: `week-2/artifacts/selected_files_manifest.json` (selected Week 2 corpus lineage; no Week 1 naive chunk path)
- Chunking used during indexing: recursive chunking reused from Week 2 (`week-2/scripts/strategy/logical_chunker.py::RecursiveChunker`)
- Collection name and vector configuration:
	- Collection: `week3_hybrid_recursive`
	- Dense vector: `voyage-4-lite` (`2048d`)
	- Sparse vector: `Qdrant/bm25`
- Point count validation:
	- Source report: `week-3/scripts/indexing/outputs/hybrid_indexing_report_20260310_004522.json`
	- `points_indexed`: `2315`
	- `dense_vectors_populated`: `true`
	- `sparse_vectors_populated`: `true`
- Dense and sparse population checks:
	- Verified in report outputs (`dense_vectors_populated=true`, `sparse_vectors_populated=true`)
- Metadata indexed alongside chunks:
	- Stored under `meta` payload with source-derived fields from the manifest and indexing pipeline

### Week 2 -> Week 3 Change Rationale

- Embedding model changed from Week 2 recursive artifact (`BGE-large-en-v1.5`) to `voyage-4-lite` for the Week 3 hybrid baseline.
- Why: Week 3 focuses on hybrid + rerank retrieval quality and uses a stronger dense model before reranking.
- What stayed consistent: selected corpus lineage and recursive chunking continuity from Week 2.

## Reranking Configuration

- Reranker model: `Voyage rerank-2.5`
- Reranking depth: rerank from `50` hybrid candidates to top `10`
- LLM generation model: `gemini-2.5-flash`
- Why this setup: hybrid retrieval improves recall for mixed keyword+semantic queries, and reranking improves precision in the final context window sent to generation.

## Narrowing Decision

- Narrowing techniques were implemented and evaluated in this repository.
- Technique 2: metadata category filtering before reranking.
- Technique 3: two-stage file routing (`50 -> 12` files) before reranking.
- Output artifacts:
	- `week-3/rag_results/week3_hybrid_rerank_metadata_filter_results.json`
	- `week-3/rag_results/week3_two_stage_routing_results.json`
- Scored comparison artifact:
	- `week-3/evaluations/eval_results/pairwise_eval_week3_all_techniques.json`

## Measured Outcomes Across Techniques

From `week-3/evaluations/eval_results/pairwise_eval_week3_all_techniques.json` (`summary_table`):

| Technique | Avg Usefulness | Avg Relevance | Avg Direct Context Count | Noise Chunks (Total) | Questions Won |
|---|---:|---:|---:|---:|---:|
| Recursive (2000c/200) | 3.833 | 2.250 | 4.500 | 67 | 11 |
| Week 3 baseline: hybrid retrieval + reranking | 4.483 | 3.267 | 6.533 | 23 | 26 |
| Week 3 hybrid + rerank + metadata filtering | 2.667 | 1.700 | 3.400 | 64 | 9 |
| Week 3 two-stage routing + hybrid + reranking | 3.717 | 1.950 | 3.900 | 50 | 14 |

Evidence-backed inference:
- The highest-quality measured configuration in this run set is the non-narrowed Week 3 baseline (`hybrid + reranking`).
- Narrowing variants are retained as experimental paths, but they are not selected as default because they underperform baseline on usefulness, relevance, direct context count, and noise.

## Pipeline Architecture Summary

Primary baseline pipeline:

`Query -> Dense embed + Sparse embed -> Hybrid RRF (top 50) -> Voyage rerank (top 10) -> LLM generation`

Narrowing variants:

1. `Query -> Intent mapper -> Metadata-filtered hybrid (top 50) -> Voyage rerank (top 10) -> LLM generation` (available design path; not part of final scored run)
2. `Query -> LLM file selector (top 50 broad -> top 12 files) -> File-filtered hybrid (top 50) -> Voyage rerank (top 10) -> LLM generation` (implemented and evaluated)
