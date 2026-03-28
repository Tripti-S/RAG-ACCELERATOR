# Chunking Strategy

## Strategy Choice
**Hybrid approach:**
 For structured markdown, technical docs, and simple prose: Naive/fixed-size chunking (medium, ~350-400 tokens) with overlap, as these files have clear section boundaries and are mostly uniform.
 For multi-topic, mixed-content, and OCR-extracted text: Semantic chunking (context-aware, ~200-300 tokens) to respect topic shifts and noisy structure.
 For code: No AST chunking needed (corpus is not code-heavy), but parent-child/section-aware chunking is used for educational flow.

## Rationale
This hybrid strategy was chosen to best match the diversity in the corpus, as identified in the chunking analysis and notes. The approach adapts to both structure and semantics, and avoids splitting important context in code or multi-topic files.

## Configuration
- **Chunk size:** 350-400 tokens (naive/structured), 200-300 tokens (semantic/mixed)
- **Overlap:** 50 tokens (naive), 30 tokens (semantic)
- **Strategy-specific settings:**
	- Naive: Markdown headers as boundaries
	- Semantic: Similarity threshold 0.75, adaptive to topic shifts
	- Parent-child: Section-aware for educational flow
- **Embedding model:** all-MiniLM-L6-v2 (384-dim, 512 token limit)
- **Truncation warnings:** 4 chunks exceeded the embedding model's limit (all in outlier documents)

## What You Considered But Didn't Use
- **Pure naive/fixed-size:** Ruled out due to poor handling of topic shifts and mixed content.
- **Pure semantic:** Too slow and unnecessary for uniform/structured docs.
- **AST/code-aware:** Not needed as the corpus is not code-heavy.
- **Recursive/boundary-aware:** Not used as most docs already have clear section headers and naive chunking suffices.

**Observation:**
The hybrid approach provides the best tradeoff between efficiency and context preservation, as confirmed by both the chunking analysis and practical experiments (see notes). It allows for flexibility and can be further tuned if new content types are added in the future.
