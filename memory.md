# ProbablAI — RAG Capstone Project Memory

**Goal:** Build a production-grade RAG system for probability/statistics learning, targeted at working professionals in fast-paced courses.  
**Author:** Tripti Singh | **Date:** March 25, 2026  
**Core Stack:** Haystack 2.x, Qdrant, Voyage AI, Gemini 2.5 Flash, FastAPI, Streamlit

---

## Week 1 — Foundation & Data Curation

- Assembled a **964-document corpus** (~1.7M tokens) from MIT lecture notes, OpenIntro stats, OCR-processed handwritten notes, StackExchange threads, and YouTube transcripts.
- Built an **end-to-end baseline RAG pipeline**: ingest → chunk → embed → Qdrant index → retrieve → generate.
- Embeddings: **BAAI/bge-large-en-v1.5** (1024-d via FastEmbed); chunking: markdown-aware (~400 words + 50-word overlap).
- **5 traced queries** evaluated qualitatively; ~8.5s avg latency, avg 5 retrieved contexts.
- Identified limitations: OCR noise, no numeric eval scale, topic skew toward foundational concepts.

**Key scripts:** `week-1/scripts/01_setup_qdrant.py`, `02_create_pipeline.py`, `03_run_indexing.py`, `04_test_rag_system.py`, `05_interactive_rag.py`  
**Key artifacts:** `week-1/traces/traces.json`, `week-1/docs/scoping.md`, `week-1/analysis/data_quality_notes.md`

---

## Week 2 — Chunking Strategy Optimization

- Deduplicated corpus: **964 → 459 documents** (65% reduction via MinHash), manifest tracked in `artifacts/selected_files_manifest.json`.
- Compared 4 chunking strategies across 10 test questions using **GPT-4o-mini as judge**.

| Strategy | Avg Usefulness | Questions Won |
|---|---|---|
| **Recursive** ✓ **Selected** | 2.7 | **6/10** |
| Hybrid | 2.1 | 3/10 |
| Semantic | 1.5 | 1/10 |
| Week 1 Baseline | — | baseline |

- **Winner:** Recursive chunking — structure/boundary-aware, best consistency; aligns with document hierarchy and formula-to-context dependencies.
- Recursive latency: 11.696s; Semantic: 9.151s; Hybrid: 20.641s

**Key scripts:** `week-2/scripts/indexing/index_hybrid.py`, `pipeline/create_chunking_pipeline.py`, `evaluation/`, `deduplication/`  
**Key artifacts:** `week-2/submission.md`, `week-2/Design_Implementation_Details.md`, `week-2/Experimentation_Details.md`, `week-2/evaluations/`

---

## Week 3 — Hybrid Retrieval + Reranking

### Architecture
```
Query → Dense (Voyage 4-lite, 2048-d) + Sparse (BM25)
  → Qdrant Hybrid RRF (top 50)
  → Voyage Rerank 2.5 (top 10)
  → Gemini 2.5 Flash Generation
```

- **459 documents → 2,315 chunks** indexed (collection: `week3_hybrid_recursive`)
- Indexing report: `week-3/scripts/indexing/outputs/hybrid_indexing_report_20260310_004522.json`
- Also experimented with metadata category filtering and two-stage routing (both rejected — too aggressive, hurt diversity).

### 4-Technique Pairwise Evaluation (60 matchups, 10 questions)

| Technique | Avg Usefulness | Avg Relevance | Questions Won |
|---|---|---|---|
| **Hybrid + Rerank** ✓ **Selected** | **4.48** | **3.27** | **26/60** |
| Two-Stage Routing + Hybrid + Rerank | 3.72 | 1.95 | 14/60 |
| Week 2 Recursive (baseline) | 3.83 | 2.25 | 11/60 |
| Hybrid + Rerank + Metadata Filter | 2.67 | 1.70 | 9/60 |

### Direct Week 2 vs Week 3 Comparison
- Week 3 wins **9/10** questions directly
- Noise reduction: 67 → 23 chunks (−66%)
- Usefulness: 3.8 → 4.4 (+0.6)
- Relevance: 2.4 → 3.35 (+0.95)
- Latency: 11.7s → ~10.1s (improved)

**Key artifacts:**
- `week-3/evaluations/eval_results/pairwise_eval_week2_recursive_vs_week3_hybrid_rerank.json`
- `week-3/evaluations/eval_results/pairwise_eval_week3_all_techniques.json`
- `week-3/rag_results/` — 4 technique result JSONs
- `week-3/docs/retrieval-analysis.md`, `week-3/docs/retrieval-strategy.md`

**Key scripts:** `week-3/scripts/01_index_hybrid.py`, `02_run_hybrid_rerank_baseline.py`, `03_run_metadata_filter.py`, `04_run_two_stage_routing.py`, `05_evaluate_pairwise.py`

---

## Week 5 — Production System

### Backend (FastAPI)
- **Core RAG pipeline:** Qdrant hybrid retrieval + Voyage reranking (`backend/app/services/rag_pipeline.py`)
- **Conversation memory:** Sliding window with conditional query rewriting (`backend/app/services/conversation.py`)
- **Semantic caching:** Redis-backed HNSW vector cache, cosine threshold 0.06 (`backend/app/services/semantic_cache.py`)
- **Query routing:** LLM classifier → type-specific prompt templates (factual, how-to, conceptual, code) (`backend/app/services/query_router.py`)
- **Prompt management:** Opik-based versioning, registry pattern (`backend/app/prompts/`)
- **Observability:** Opik tracing + `/feedback` endpoint for user ratings

### Frontend (Streamlit)
- Chat interface with streaming responses, conversation history, and feedback buttons (`frontend/app.py`)

### Infrastructure
- **Docker Compose:** Backend :8000, Frontend :8501
- **Deployment:** Railway.app (frontend public, backend internal network)
- **Setup scripts:** `setup/01_verify_environment.py`, `02_index_documents.py`, `03_setup_redis.py`, `04_smoke_test.py`

---

## Overall Progression

```
Week 1: Baseline RAG (dense only, naive chunking, 964 docs, ~8.5s)
  ↓
Week 2: Recursive chunking wins; corpus deduped to 459 docs, 11.7s
  ↓
Week 3: Hybrid (dense+sparse) + Voyage reranking; 9/10 Q improvement, ~10.1s
  ↓
Week 5: Full production app — caching, routing, memory, observability, Railway deploy
```

## Important Notes
- `.env` file is at root: `c:\Users\singhtripti\rag-capstone-week-2\.env`
- Scripts referencing PROJECT_ROOT must use `SCRIPT_DIR.parents[2]` to resolve `.env` correctly
- Active venv: `.venv/` at project root
- Qdrant collection name for Week 3: `week3_hybrid_recursive` (2,315 points)
