# Chunking Comparison: Week 1 vs Week 2

## Overview
This document compares the chunking approach used in Week 1 (naive baseline) with the advanced chunking strategies implemented in Week 2: Recursive, Semantic, and Hybrid. The comparison covers total chunk count, average chunk size, truncation warnings, and indexing time for each strategy.

---

## 1. Chunking Strategies Compared

- **Week 1 Naive Baseline**: Fixed-size chunking (~400 words, overlap)
- **Week 2 Recursive**: Structure-aware recursive chunking
- **Week 2 Semantic**: Adaptive, similarity-based chunking
- **Week 2 Hybrid**: Combines code/document heuristics and semantic boundaries

---

## 2. Comparison Table

| Strategy         | Total Chunks | Avg Chunk Size | Truncation Warnings | Indexing Time |
|------------------|--------------|----------------|---------------------|--------------|
| Naive Baseline   | [X]          | [Y]            | [Z]                 | [T]          |
| Recursive        | [A]          | [B]            | [C]                 | [D]          |
| Semantic         | [E]          | [F]            | [G]                 | [H]          |
| Hybrid           | [I]          | [J]            | [K]                 | [L]          |

*Replace bracketed values with your actual results after running each pipeline.*

---

## 3. Observations

- **Total Chunk Count**: 
  - Naive baseline produced [X] chunks; advanced strategies produced [A/E/I] chunks, reflecting [more/fewer] but [smaller/larger] segments.
- **Average Chunk Size**: 
  - [Comment on which strategy produced the most/least granular chunks.]
- **Truncation Warnings**: 
  - [Summarize if any strategy led to more chunks exceeding the embedding model limit.]
- **Indexing Time**: 
  - [Note which strategy was fastest/slowest and possible reasons.]

---

## 4. Summary

- The naive baseline provides a simple, uniform segmentation but may cut across logical boundaries.
- Recursive and semantic chunking better preserve document structure and meaning, potentially improving retrieval quality.
- Hybrid chunking aims to balance code/document heuristics with semantic boundaries for optimal chunk quality.
- Use this table and your observations to justify your final strategy choice in your submission.
