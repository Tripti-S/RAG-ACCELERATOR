# Chunking Strategy

## Strategy Choice
**Hybrid strategy (evaluated via multiple indexed collections):**

The pipeline supports multiple strategies:
- Naive (small / medium / large)
- Sentence-based
- Recursive
- Semantic
- AST (code-aware)

For this corpus, the primary focus is on:
- Recursive / header-aware chunking for structured educational content.
- Semantic chunking for multi-topic documents.
- Naive medium (baseline comparison).

AST-based chunking is available but not prioritized since the corpus is not code-heavy.

---

## Rationale

The corpus is predominantly structured educational material with clear section boundaries. Recursive chunking preserves logical document hierarchy, while semantic chunking handles topic shifts within long chapters.

Naive chunking variants are indexed to enable controlled comparison across:
- Chunk size sensitivity
- Retrieval quality
- Token truncation behavior

Since the pipeline supports strategy-isolated Qdrant collections, each approach can be evaluated independently for RAG performance.

---

## Configuration

- **Chunk sizes (by strategy):**
  - Naive small: ~200 words
  - Naive medium: ~400 words
  - Naive large: ~800 words
  - Recursive: ~2000 chars / 200 overlap
  - Semantic: adaptive
- **Overlap:** Strategy-dependent (e.g., 25–100 words for naive variants)
- **Embedding model:** BGE-large-en-v1.5 (FastEmbed)
- **Embedding dimension:** 1024
- **Max token limit:** 512 tokens
- **Similarity metric:** Cosine similarity (via Qdrant)
- **Retrieval type:** Asymmetric (short query → longer chunks)
- **Truncation warnings:** Automatically analyzed post-chunking using token estimation

Each strategy creates a separate Qdrant collection for isolated evaluation.

---

## What Was Considered But Not Used as Primary

- AST chunking: Available but not central (corpus not code-dominant).
- Single-strategy indexing: Replaced by multi-strategy experimentation to enable comparative evaluation.
- Fixed-only approach: Expanded to include recursive and semantic for robustness testing.

**Observation:**
The implemented system enables controlled experimentation across chunking strategies, embedding constraints, and truncation analysis, allowing empirical comparison rather than theoretical selection.