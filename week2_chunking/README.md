# Week 2: Chunking Strategies

This week explores how different chunking strategies affect RAG quality through hands-on experiments and LLM-as-judge evaluation.

---

## Module 5: Concepts — Chunking, Embeddings, and Data Prep

### Lesson 2.1: Week 2 Intro and Data Preprocessing

| Lesson | Title | Type |
|--------|-------|------|
| 2.1a | Week 2 Intro and Data Quality | Watch |
| 2.1b | Data Quality and Deduplication | Read |

#### Lesson 2.1 — Deduplication Command

```bash
python week2_chunking/deduplication/01_deduplicate_documents.py
```

### Lesson 2.2: Chunking Strategies

| Lesson | Title | Type |
|--------|-------|------|
| 2.2a | Intro to Chunking for RAG | Watch |
| 2.2b | Chunking Strategies Breakdown | Watch |
| 2.2c | Chunking Decision Framework | Watch |
| 2.2d | Chunking Strategies Reference | Read |

### Lesson 2.3: Embeddings and Chunking Connection

| Lesson | Title | Type |
|--------|-------|------|
| 2.3a | Embedding Deep Dive | Watch |
| 2.3b | Embeddings Reference | Read |

---

## Module 6: Size Experiment and Evaluation

### Lesson 2.4: Size Experiment

| Lesson | Title | Type |
|--------|-------|------|
| 2.4a | Size Experiment Walkthrough | Watch |
| 2.4b | Size Experiment How-To Guide | Read |

#### Lesson 2.4 — Size Experiment Commands

```bash
# Index all three sizes
python week2_chunking/experiments/02_index_strategy.py naive_small --full
python week2_chunking/experiments/02_index_strategy.py naive_medium --full
python week2_chunking/experiments/02_index_strategy.py naive_large --full

# Generate RAG results for each
python week2_chunking/experiments/04_generate_rag_results.py naive_small
python week2_chunking/experiments/04_generate_rag_results.py naive_medium
python week2_chunking/experiments/04_generate_rag_results.py naive_large
```

### Lesson 2.5: RAG Evaluation

| Lesson | Title | Type |
|--------|-------|------|
| 2.5a | Intro to RAG Evaluation | Watch |
| 2.5b | LLM-as-a-Judge Deep Dive | Watch |

### Lesson 2.6: Evaluation Walkthrough

| Lesson | Title | Type |
|--------|-------|------|
| 2.6a | Evaluation Walkthrough | Watch |
| 2.6b | Evaluation Walkthrough Guide | Read |

#### Lesson 2.6 — Evaluation Commands

```bash
# Run LLM-as-judge evaluation
python week2_chunking/experiments/05_chunk_quality_eval.py \
    --strategies naive_small naive_medium naive_large

# View results
streamlit run week2_chunking/experiments/06_human_eval_viewer.py
streamlit run week2_chunking/experiments/07_chunk_eval_viewer.py
```

### Lesson 2.7: Voyage Embeddings Upgrade

| Lesson | Title | Type |
|--------|-------|------|
| 2.7 | Voyage Embeddings Upgrade | Read |

#### Lesson 2.7 — Voyage Commands

Add `VOYAGE_API_KEY` to your `.env` file, then:

```bash
# Index with Voyage embeddings
python week2_chunking/experiments/02_index_strategy.py naive_medium --full --embedder voyage

# Generate RAG results
python week2_chunking/experiments/04_generate_rag_results.py naive_medium --embedder voyage

# Compare FastEmbed vs Voyage
python week2_chunking/experiments/05_chunk_quality_eval.py \
    --strategies naive_medium naive_medium_voyage
```

---

## Module 7: Strategy Experiments and Framework

### Lesson 2.8: Strategy Experiments

| Lesson | Title | Type |
|--------|-------|------|
| 2.8a | Strategy Experiments Walkthrough | Watch |
| 2.8b | Strategy Experiments Guide | Read |

#### Lesson 2.8 — Strategy Experiment Commands

```bash
# Index boundary-aware strategies with Voyage
python week2_chunking/experiments/02_index_strategy.py sentence --full --embedder voyage
python week2_chunking/experiments/02_index_strategy.py recursive --full --embedder voyage

# Generate RAG results
python week2_chunking/experiments/04_generate_rag_results.py sentence --embedder voyage
python week2_chunking/experiments/04_generate_rag_results.py recursive --embedder voyage

# Evaluate
python week2_chunking/experiments/05_chunk_quality_eval.py \
    --strategies naive_medium_voyage sentence_voyage recursive_voyage
```

### Lesson 2.9: Chunking Strategy Selection Framework

| Lesson | Title | Type |
|--------|-------|------|
| 2.9 | Chunking Strategy Selection Framework | Read |

### Lesson 2.10: Capstone — Chunking Applied

| Lesson | Title | Type |
|--------|-------|------|
| 2.10 | Capstone — Chunking Strategy Implementation | Read |

#### Capstone Submission Tools

Your submission guidelines and pre-submission validation script are in the `capstone/` folder at the repo root:

- **Guidelines:** [`capstone/week2_submission_guidelines.md`](../capstone/week2_submission_guidelines.md) — full step-by-step walkthrough of what to submit
- **Prequalify script:** [`capstone/week2_prequalify.py`](../capstone/week2_prequalify.py) — run this before submitting to catch structural issues, bloat, and secrets

Copy the prequalify script into your capstone project's `week-2/` directory and run:

```bash
uv run python week-2/prequalify.py
```

---

## Reference

### The 7 Chunking Strategies

| Strategy | Description | Target Size |
|----------|-------------|-------------|
| `naive_small` | Fixed word count | 200 words, 25 overlap |
| `naive_medium` | Fixed word count (baseline) | 400 words, 50 overlap |
| `naive_large` | Fixed word count | 800 words, 100 overlap |
| `sentence` | Sentence boundaries | 6 sentences, 2 overlap |
| `recursive` | Hierarchical (para→sent→word) | 2000 chars, 200 overlap |
| `semantic` | Similarity-based splits | Adaptive |
| `ast_code` | AST parsing for code | 2048 chars (code), 400 words (text) |

### Directory Structure

```
week2_chunking/
├── deduplication/           # Document deduplication (run first)
│   ├── 01_deduplicate_documents.py
│   └── utils/
├── strategies/              # Chunking strategy implementations
│   ├── naive_chunker.py
│   ├── logical_chunker.py
│   ├── semantic_chunker.py
│   └── ast_code_chunker.py
├── experiments/             # Experiment scripts (run in order)
│   ├── 01_create_chunking_pipeline.py
│   ├── 02_index_strategy.py
│   ├── 03_create_rag_pipeline.py
│   ├── 04_generate_rag_results.py
│   ├── 05_chunk_quality_eval.py
│   ├── 06_human_eval_viewer.py
│   └── 07_chunk_eval_viewer.py
├── rag_results/             # Generated RAG results (JSON)
└── evaluations/             # LLM evaluation results (JSON)
```

### Token Truncation Warning

The BGE-large-en-v1.5 embedding model has a 512 token limit:

- `naive_small` (200 words): Fits within limit
- `naive_medium` (400 words): Slight truncation
- `naive_large` (800 words): ~50% truncated

This is intentional — it demonstrates what happens when chunk sizes exceed model constraints.

### Troubleshooting

**"Manifest not found"** — Run deduplication first (Lesson 2.1 command above).

**"Questions file not found"** — Ensure `artifacts/human_eval_questions.json` exists.

**Qdrant DNS issues** — See [root README troubleshooting](../README.md#troubleshooting).
