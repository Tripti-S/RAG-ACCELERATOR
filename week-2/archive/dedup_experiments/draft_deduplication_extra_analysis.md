# Enhanced Deduplication and Topic Analysis

## Motivation
The initial deduplication logic only removed exact duplicates based on filenames or simple MinHash. However, real-world corpora often contain near-duplicates or repeated topics with different wording, structure, or file names. To address this, we implemented advanced content similarity and topic modeling techniques.

## Methods Used
- **Content Similarity:**
  - Used Sentence Transformers (all-MiniLM-L6-v2) to embed all markdown files.
  - Calculated cosine similarity between document embeddings.
  - Flagged pairs with similarity above 0.90 as near-duplicates.
  - Used fuzzy string matching (Levenshtein ratio) for additional checks.
- **Topic Modeling:**
  - Used TF-IDF vectorization and KMeans clustering to group documents by topic.
  - Flagged clusters with multiple files as potential repeated topics.

## Results
- [To be filled after running enhanced script]

## Impact
- This approach helps remove not just exact duplicates, but also highly similar or repeated-topic documents, improving the quality and diversity of the corpus for downstream RAG and chunking experiments.

## How to Reproduce
- Run `deduplicate_documents.py` with the enhanced logic enabled (see script for details).
- Review the outputs in `outputs/` and this report for flagged duplicates and topic clusters.

---
*This file documents the "extra mile" taken for advanced deduplication and topic analysis beyond the baseline required for the assignment.*
