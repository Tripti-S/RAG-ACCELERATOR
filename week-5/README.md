# Week 5: Production RAG

This week takes the retrieval pipeline from Week 3 and wraps it in a production system: conversation memory, semantic caching, query routing with type-specific prompts, user feedback collection, and full observability. You will set up the system locally, run it end-to-end, and optionally deploy it to the cloud with Docker.

---

## Module 14: From Demo to Production

### Lesson 5.1: Week 5 Intro + Production Architecture

| Lesson | Title | Type |
|--------|-------|------|
| 5.1a | Week 5 Intro | Watch |
| 5.1b | Production RAG Architecture | Read |

No commands — Lesson 5.1 covers what you will build this week and why each component exists. See the [Architecture diagram](#architecture) below.

### Lesson 5.2: Conversation Memory & Query Rewriting

| Lesson | Title | Type |
|--------|-------|------|
| 5.2a | Conversation Memory & Query Rewriting | Watch |
| 5.2b | Conversation Memory Reference Reading | Read |

Code reference: `backend/app/services/conversation.py` — sliding window memory + conditional query rewriting

### Lesson 5.3: Semantic Caching

| Lesson | Title | Type |
|--------|-------|------|
| 5.3a | Semantic Caching | Watch |
| 5.3b | Semantic Caching Reference Reading | Read |

Code reference: `backend/app/services/semantic_cache.py` — Redis HNSW vector cache

#### Lesson 5.3 — Cache Threshold Experiment

Requires `VOYAGE_API_KEY` in your `.env` file. No Redis or backend needed — standalone experiment.

```bash
# Run the cache threshold experiment (measures cosine distances between query pairs)
python week-5/experiments/cache_threshold_experiment.py

# With custom thresholds to test
python week-5/experiments/cache_threshold_experiment.py --thresholds 0.03 0.06 0.10 0.15 0.20
```

Output: terminal table + JSON results saved to `experiments/results/`.

---

## Module 15: Intelligence Layer

### Lesson 5.4: Query Routing and Classification

| Lesson | Title | Type |
|--------|-------|------|
| 5.4a | Query Routing and Classification | Watch |
| 5.4b | Query Routing Reference Reading | Read |

Code reference: `backend/app/services/query_router.py` — LLM classification + type-specific prompt selection

### Lesson 5.5: RAG Prompt Engineering

| Lesson | Title | Type |
|--------|-------|------|
| 5.5 | RAG Prompt Engineering | Read |

Code reference: `backend/app/prompts/templates.py` — all prompt templates (factual, how-to, troubleshooting, code generation)

### Lesson 5.6: Prompt Lifecycle Management

| Lesson | Title | Type |
|--------|-------|------|
| 5.6 | Prompt Lifecycle Management | Read |

Code reference: `backend/app/prompts/registry.py` — Opik prompt versioning + hot-swap

---

## Module 16: Operations & Ship

### Lesson 5.7: Observability & User Feedback

| Lesson | Title | Type |
|--------|-------|------|
| 5.7a | Observability & User Feedback | Watch |
| 5.7b | Observability & Feedback Reference Reading | Read |

Code reference: `backend/app/main.py` — Opik tracing, feedback endpoint, online evaluation

### Lesson 5.8: Production System Walkthrough

| Lesson | Title | Type |
|--------|-------|------|
| 5.8a | Setup Guide | Read |
| 5.8b | System Design & Project Structure Walkthrough | Watch |
| 5.8c | Backend Services & Query Flow Walkthrough | Watch |
| 5.8d | Frontend, Live Demo & Opik Tracing | Watch |
| 5.8e | Walkthrough Reference Guide | Read |

> **Before watching 5.8b-5.8d:** Complete the setup below (Lesson 5.8a) and start the system so you can follow along with the walkthrough videos. Lesson 5.8e is a companion reference to have open alongside the videos.

**What each walkthrough covers:**
- **5.8b:** `config.py`, `models.py`, project structure, service initialization in `main.py`
- **5.8c:** Full query flow through `main.py` — session handling, query rewriting, cache lookup, classification, retrieval, prompt building, generation, streaming
- **5.8d:** `frontend/app.py`, live demo (cache hits, follow-ups, feedback), Opik traces + prompt library + online evaluation

#### Lesson 5.8a — Environment Setup

```bash
# Copy environment template and fill in your credentials
cp week-5/.env.example week-5/.env
# Edit .env with your API keys — see .env.example for details on each variable
```

#### Lesson 5.8a — Setup Scripts

Run these in order from the project root:

```bash
# 1. Verify Python version, packages, API keys, and service connections
python week-5/setup/01_verify_environment.py

# 2. Verify the Week 3 Qdrant collection has documents
python week-5/setup/02_index_documents.py

# 3. Create Redis cache index and conversation key structures
python week-5/setup/03_setup_redis.py

# 4. Smoke test — runs one query through the full pipeline
python week-5/setup/04_smoke_test.py
```

#### Lesson 5.8a — Start the System

```bash
# Terminal 1: Start the FastAPI backend
cd week-5/backend
python -m app.main
# API at http://localhost:8000
# Docs at http://localhost:8000/docs

# Terminal 2: Start the Streamlit frontend (from project root)
streamlit run week-5/frontend/app.py
# UI at http://localhost:8501
```

### Lesson 5.9: Docker & Cloud Deployment

| Lesson | Title | Type |
|--------|-------|------|
| 5.9 | Docker & Cloud Deployment | Read |

#### Lesson 5.9 — Docker Commands

```bash
# Build and run both services with Docker Compose
cd week-5
docker compose up --build
# Backend: http://localhost:8000
# Frontend: http://localhost:8501

# Stop
docker compose down
```

Cloud deployment to Railway is covered in [`DEPLOY.md`](DEPLOY.md).

### Lesson 5.10: Week 5 Capstone

| Lesson | Title | Type |
|--------|-------|------|
| 5.10 | Week 5 Capstone | Read |

---

## Reference

### Architecture

```
User Query
    |
    v
[Conversation Memory] -- rewrite follow-ups into standalone queries
    |
    v
[Semantic Cache] -- sub-50ms on hit (skip pipeline entirely)
    |  miss
    v
[Query Router] -- classify: FACTUAL | HOW_TO | TROUBLESHOOTING | CODE_GENERATION
    |
    v
[Retrieval Pipeline] -- Dense(100) + Sparse(100) -> RRF(50) -> Voyage Rerank(10)
    |
    v
[Type-Specific Prompt] -- FORMAT section + grounding rules + citations
    |
    v
[Gemini Flash] -- generate answer
    |
    v
[Cache + Store + Respond] -- cache result, store in conversation, return with msg_id
```

### Production Services

| Service | File | What It Does |
|---------|------|--------------|
| **RAG Pipeline** | `services/rag_pipeline.py` | Hybrid (dense + sparse) retrieval with Voyage reranking + Gemini generation |
| **Semantic Cache** | `services/semantic_cache.py` | Redis HNSW vector cache — sub-50ms on similar queries |
| **Conversation Memory** | `services/conversation.py` | Redis-backed sliding window + conditional query rewriting |
| **Query Router** | `services/query_router.py` | LLM-based query classification + type-specific prompt selection |

All services are singletons — initialized once at startup, reused across requests.

### API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/query` | Full RAG pipeline with memory + routing + cache |
| POST | `/query/stream` | SSE streaming version |
| POST | `/feedback` | Store user feedback (thumbs up/down) |
| GET | `/conversation/{session_id}` | Conversation history |
| GET | `/health` | Service health check |
| GET | `/metrics` | Cache stats, latency, feedback summary |

### Models Used

| Component | Model |
|-----------|-------|
| Dense Embeddings | Voyage-4-lite (2048d) |
| Sparse Embeddings | Qdrant/BM25 |
| Reranker | Voyage rerank-2.5 |
| Cache Embeddings | Voyage-4-lite (2048d) |
| LLM (Generation) | Gemini 2.5 Flash |
| LLM (Classification) | Gemini 2.5 Flash |
| LLM (Query Rewriting) | Gemini 2.5 Flash |

### API Keys Required

| Key | Used By | Required |
|-----|---------|----------|
| `QDRANT_URL` + `QDRANT_API_KEY` | RAG pipeline (vector search) | Yes |
| `GOOGLE_API_KEY` | Generation, classification, query rewriting | Yes |
| `VOYAGE_API_KEY` | Dense embeddings, reranking, cache embeddings | Yes |
| `REDIS_HOST` + `REDIS_PASSWORD` | Semantic cache, conversation memory | Yes |
| `OPIK_API_KEY` + `OPIK_WORKSPACE` | Observability tracing | Optional |

### Directory Structure

```
week-5/
├── backend/                         # FastAPI application
│   ├── app/
│   │   ├── main.py                  # Endpoints, streaming, lifecycle
│   │   ├── config.py                # Pydantic settings, env validation
│   │   ├── models.py                # Request/response schemas
│   │   ├── prompts/                 # Centralized prompt management
│   │   │   ├── templates.py         # All prompt text (easy to edit/review)
│   │   │   └── registry.py          # Opik versioning + hot-swap
│   │   ├── services/                # Business logic (singletons)
│   │   │   ├── rag_pipeline.py      # Hybrid + Voyage RAG (async)
│   │   │   ├── semantic_cache.py    # Redis HNSW vector cache
│   │   │   ├── conversation.py      # Sliding window + query rewriting
│   │   │   └── query_router.py      # Classification + prompt selection
│   │   └── components/              # Haystack components
│   │       ├── qdrant_hybrid_retriever.py
│   │       └── voyage_reranker.py
│   ├── Dockerfile
│   └── railway.toml
│
├── frontend/                        # Streamlit chat interface
│   ├── app.py
│   ├── Dockerfile
│   └── railway.toml
│
├── setup/                           # Getting started scripts
│   ├── 01_verify_environment.py     # Check API keys and services
│   ├── 02_index_documents.py        # Verify Week 3 Qdrant collection
│   ├── 03_setup_redis.py            # Create Redis cache index + keys
│   └── 04_smoke_test.py             # End-to-end pipeline test
│
├── experiments/                     # Standalone experiments
│   ├── cache_threshold_experiment.py
│   └── results/                     # Experiment output (JSON)
│
├── walkthrough_traces/              # Walkthrough output artifacts
│
├── docker-compose.yml               # Local Docker deployment
├── DEPLOY.md                        # Railway cloud deployment guide
├── .env.example                     # Environment variable template
└── README.md
```

### Troubleshooting

**"Collection not found" for week3_hybrid_recursive** — The Qdrant collection from Week 3 must exist. Run Week 3 indexing first:
```bash
python week-3/scripts/indexing/01_index_hybrid.py --full
```

**Redis connection refused** — Check your Redis Cloud credentials in `.env`. Ensure `REDIS_HOST`, `REDIS_PORT`, and `REDIS_PASSWORD` are set correctly. Free tier requires `REDIS_SSL=true`.

**"VOYAGE_API_KEY not set"** — Run the environment verification script to check all required keys:
```bash
python week-5/setup/01_verify_environment.py
```

**macOS Qdrant DNS errors** — Uncomment `GRPC_DNS_RESOLVER=native` in your `.env` file. See [root README troubleshooting](../README.md#troubleshooting).

**Opik tracing not appearing** — Opik is optional. Set `OPIK_API_KEY`, `OPIK_WORKSPACE`, and `OPIK_PROJECT_NAME` in `.env` to enable it. Without these, the system runs without tracing.

**Port already in use** — Find and stop the existing process:
```bash
lsof -i :8000 | grep LISTEN
lsof -i :8501 | grep LISTEN
```

**Docker build fails** — Ensure Docker Desktop is installed and running. Docker is only needed for Lesson 5.9 — you can run the system locally without it.
