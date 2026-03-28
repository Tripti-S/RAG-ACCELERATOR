# Chunking Strategy

## Strategy Choice
**Hybrid approach:**
- Structured markdown, technical docs, and simple prose: Header-aware naive/fixed-size chunking (350–400 tokens) with overlap.
- Multi-topic, mixed-content, and OCR text: Semantic chunking (200–300 tokens) to respect topic shifts.
- Code: No AST chunking (corpus not code-heavy); parent-child/section-aware chunking used to preserve educational flow.

## Rationale
The corpus is predominantly structured educational content with clear section boundaries, but longer documents contain multiple topic shifts. A hybrid approach balances structural consistency with semantic sensitivity. Parent-child chunking preserves conceptual hierarchy (definition → example → application), improving retrieval coherence.

## Configuration
- **Chunk size:** 350–400 tokens (structured), 200–300 tokens (semantic)
- **Overlap:** 50 tokens (~10–15%) naive, 30 tokens (~10%) semantic
- **Strategy-specific settings:**
  - Naive: Markdown headers as boundaries
  - Semantic: Similarity threshold 0.75
  - Parent-child: Section-aware hierarchy
- **Embedding model:** all-MiniLM-L6-v2 (384-dim, 512 token limit)
- **Similarity metric:** Cosine similarity (asymmetric search: short query → longer chunks)
- **Truncation warnings:** 4 (all in outlier long documents)

## What You Considered But Didn't Use
- **Pure naive/fixed-size:** Weak handling of topic shifts in long chapters.
- **Pure semantic:** Unnecessary overhead for well-structured content.
- **AST/code-aware:** Not applicable (no significant code).
- **Recursive-only:** Does not adapt well to semantic drift within long documents.

**Observation:**
The hybrid strategy provides an efficient balance between context preservation, retrieval precision, and computational cost, aligned with the corpus characteristics.