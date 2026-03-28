Chunking & Embedding Strategy Evaluation
Strategy Choice

A hybrid chunking strategy was selected based on the corpus characteristics.

The corpus is predominantly structured educational content (lecture notes, textbook-style material, technical documentation) with clear headers and hierarchical organization. However, several long documents contain multiple topic shifts, and some OCR-extracted files are less structured.

The selected strategy combines:

Recursive/header-aware chunking (primary strategy) for structured markdown and technical documentation.

Semantic chunking for multi-topic and OCR-extracted documents.

Parent-child hierarchical chunking to preserve educational concept flow.

No AST/code-aware chunking, since the corpus is not code-heavy.

This hybrid approach balances structural awareness with semantic sensitivity.

Rationale

The decision was driven by the corpus analysis.

Most documents:

Have clear markdown headers.

Follow a structured, hierarchical format.

Present educational concepts in a logical progression.

Because of this, recursive/header-aware chunking is appropriate for the majority of files.

However, several long chapters:

Contain multiple conceptual transitions.

Cover distinct subtopics within a single document.

For these, pure fixed-size chunking would risk mixing unrelated concepts. Therefore, semantic chunking is used selectively to detect topic shifts and preserve coherence.

Parent-child chunking was introduced because educational content follows conceptual hierarchies (definition → example → theorem → application). Retrieving isolated fragments could break logical continuity. The hierarchical approach allows retrieval of fine-grained subchunks while retaining access to the broader section context.

AST-based chunking was not used because the corpus does not contain significant code structures that require syntactic preservation.

The strategy aligns with the lesson framework:

Structured documents → recursive

Multi-topic documents → semantic

Mixed corpus → hybrid

Configuration

Chunk size:

350–400 tokens for structured/recursive chunking.

200–300 tokens for semantic chunking.

This size range was chosen because:

It preserves complete conceptual units.

It avoids semantic dilution from overly large chunks.

It reduces fragmentation caused by overly small chunks.

It stays safely within the embedding model’s token limit.

Overlap:

50 tokens for recursive chunks (~10–15% overlap).

30 tokens for semantic chunks (~10% overlap).

Overlap was added to reduce boundary information loss while controlling duplication and embedding cost.

Strategy-specific settings:

Markdown headers used as natural split boundaries.

Semantic similarity threshold set to 0.75.

Very short documents indexed as single chunks.

Extremely long documents split adaptively.

Embedding Strategy

Embedding model:

all-MiniLM-L6-v2

384-dimensional vectors

512 token limit

This model was selected for:

Computational efficiency.

Good semantic performance for medium-scale corpora.

Fast indexing and experimentation.

Similarity metric:

Cosine similarity.

Retrieval mode:

Asymmetric semantic search (short query → longer document chunks).

Asymmetric retrieval is particularly suitable for educational corpora, where user queries are short but require rich contextual grounding.

Truncation and Indexing Observations

Total files after deduplication: 459.

Truncation warnings: 4.

All warnings occurred in outlier long documents.

The selected chunk sizes successfully minimized systematic truncation.

What Was Considered But Not Used

Pure naive/fixed-size chunking was not selected because it does not handle topic shifts well in long, multi-topic documents.

Pure semantic chunking was not selected because it adds computational overhead and is unnecessary for well-structured markdown content.

AST/code-aware chunking was not selected because the corpus is not code-heavy.

Fully recursive-only chunking was not selected because it may not detect semantic drift within long chapters.

Final Assessment

The hybrid strategy was chosen based on empirical corpus analysis rather than default configuration.

It:

Matches the dominant structure of the corpus.

Adapts to multi-topic content.

Preserves educational hierarchy.

Minimizes truncation risk.

Supports effective asymmetric RAG retrieval.

Overall, the approach provides a balanced trade-off between efficiency, semantic integrity, and retrieval performance, and can be further tuned if new content types are introduced.