# Week 3 RAG Pipeline Scripts

This folder contains a self-owned Week 3 baseline pipeline implementation (no runtime wrapper into `week3_retrieval`).

## What is implemented

- `01_run_hybrid_rerank_baseline.py`
  - Stage 1: Hybrid retrieval from Qdrant using dense + sparse vectors and RRF fusion.
  - Stage 2: Voyage reranker reduces the candidate set before generation.
  - Generator: Gemini chat model builds final answers from reranked chunks.
  - Output: JSON result file under `week-3/rag_results/` for pairwise evaluation.

- `components/qdrant_hybrid_retriever.py`
  - Custom retriever that uses Qdrant native prefetch + RRF.
  - Sets explicit dense/sparse prefetch limits to keep retrieval behavior consistent.

- `components/voyage_reranker.py`
  - Haystack-compatible reranker component using Voyage API.
  - Includes fallback to top-k original order if reranking call fails.

## Why these defaults

- `collection=week3_hybrid_recursive`
  - Matches the Week 3 indexing script default and avoids overriding prior collections.
- `prefetch_k=50`
  - Keeps a broader candidate pool for reranking.
- `rerank_k=10`
  - Controls context size to reduce prompt noise while preserving recall.
- Dense + sparse retrieval
  - Dense vectors improve semantic match; sparse vectors improve exact-token match.
  - RRF combines both signals without hard weighting.

## Run command

```powershell
uv run python week-3/scripts/rag_pipeline/01_run_hybrid_rerank_baseline.py
```

Optional overrides:

```powershell
uv run python week-3/scripts/rag_pipeline/01_run_hybrid_rerank_baseline.py --collection week3_hybrid_recursive --prefetch-k 50 --rerank-k 10
```

## Required environment variables

- `QDRANT_URL`
- `QDRANT_API_KEY`
- `GOOGLE_API_KEY`
- `VOYAGE_API_KEY`

These are loaded from the project root `.env`.
