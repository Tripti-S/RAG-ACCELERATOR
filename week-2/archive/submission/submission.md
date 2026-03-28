# Week 2 Capstone Submission

## Student Name(s)
Tripti Singh

## Project Title
RAG Capstone: Probability QA

## Week 1 Recap
- **Corpus:** 120 docs, probability/statistics domain
- **Week 1 baseline performance:** Retrieval often included irrelevant or cut-off chunks; signal was low.
- **Key issue identified:** Needed to improve chunk relevance and reduce mid-thought cutoffs.

## Chunking Analysis Summary
- **Dominant content types:** Textbook chapters, problem sets, lecture notes
- **Document length distribution:** Median 8 pages, range 1-40, some very long outliers
- **Key chunking consideration:** Many documents have logical section breaks; preserving these improves chunk focus
- **Deduplication results:** 12 duplicate files removed (10% reduction)

## Strategy Choice
- **Strategy:** Hybrid (Semantic + AST)
- **Rationale:** Combines semantic and code-aware chunking for best focus and context
- **Configuration:** chunk size 500, overlap 100, AST splitting enabled
- **Embedding model:** minilm (sentence-transformers/all-MiniLM-L6-v2, 384d)
- **New collection name:** week2_hybrid
- **Total chunks:** 1983 (Week 1 baseline: 2100)
- **Truncation warnings:** 2 chunks truncated, minimal impact

## Evaluation Approach
- **Judge model:** gemini-2.5-flash
- **Method:** Hybrid two-stage (per-chunk analysis + holistic ranking)
- **Changes from course default:** Added explicit redundancy and context checks in prompt

## Evaluation Summary

| Metric | Naive Baseline | New Strategy | Change |
|--------|---------------|--------------|--------|
| Avg signal % | 59% | 86% | +27% |
| Total cutoffs | 17 | 3 | -14 |
| Avg usefulness | 3.3 | 4.7 | +1.4 |
| Questions won | 0 | 10 | +10 |

## Judge Reliability Assessment
- **Spot-checked questions:** 1, 2, 3
- **Agreement with manual review:** High, with minor caveats on redundancy
- **Judge weaknesses found:** Sometimes overrates chunk focus, misses redundancy

## Key Observations
- **Where did the new strategy help most?** Reduced cutoffs, higher signal, more focused answers
- **Where did it not help (or hurt)?** Occasionally missed useful background context
- **What's the information density tradeoff?** Smaller, focused chunks = higher signal, but risk missing broader context
- **What would you improve next?** Experiment with dynamic chunk sizes and more context-aware splitting

## Iteration Summary
- **Total iterations:** 2
- **Most impactful change:** Switching to hybrid chunking with minilm embedder
- **Stopping rationale:** Further changes gave only marginal improvements

## Self-Assessment

| Criteria | Score (1-5) | Notes |
|----------|-------------|-------|
| Chunking analysis depth | 5 | Detailed corpus review |
| Strategy selection rationale | 5 | Data-driven, justified |
| Evaluation thoroughness | 5 | Multi-stage, spot-checked |
| Judge reliability check | 5 | Manual and LLM spot-checks |
| Iteration quality | 5 | Multiple, well-documented |
| Documentation clarity | 5 | All sections complete |
# Week 2 Capstone Submission

## Student Name(s)
Tripti Singh

## Project Title
RAG Capstone Corpus Analysis

## Week 1 Recap
- **Corpus:** 462 documents, technical and educational domain (markdown, code, OCR text)
- **Week 1 baseline performance:** Naive chunking worked for simple docs but failed on multi-topic and code-heavy files; frequent cutoffs and noisy retrieval.
- **Key issue identified:** Improve retrieval quality, reduce cut-off chunks, and handle mixed/complex content types.

**Extra Deduplication/Topic Analysis:**
  - Enhanced deduplication now uses content similarity (embeddings + fuzzy matching) and topic modeling (TF-IDF + KMeans) to flag near-duplicates and repeated topics.
  - See docs/deduplication_extra_analysis.md for details and results.
- **Dominant content types:** Structured markdown, technical docs, code examples, OCR-extracted text
- **Document length distribution:** Median 540 words, range 38–8,200, 2 extreme outliers
- **Key chunking consideration:** Topic shifts, code structure, and noisy OCR data require hybrid chunking
- **Deduplication results:**
  - Total files processed: 462
  - Unique files after deduplication: 459
  - Duplicates removed: 3 (0.65% reduction)

## Strategy Choice
- **Strategy:** Hybrid (Naive + Semantic + AST)
- **Rationale:** Hybrid approach preserves topic and code boundaries, handles noisy OCR, and improves retrieval for complex docs.
- **Configuration:** chunk size 350/200/400, overlap 50/30/0, see chunking-strategy.md
- **Embedding model:** all-MiniLM-L6-v2 (384-dim, 512 token limit)
- **New collection name:** capstone_hybrid
- **Total chunks:** 2,140 (Week 1 baseline: 2,320)
- **Truncation warnings:** 4 (all in outlier docs, minimal impact)

## Evaluation Approach
- **Judge model:** gpt-3.5-turbo
- **Method:** per-chunk analysis
- **Changes from course default:** Used a more recent model for improved reliability

## Evaluation Summary

| Metric | Naive Baseline | Hybrid Strategy | Change |
|--------|---------------|-----------------|--------|
| Avg signal % | 78% | 89% | +11% |
| Total cutoffs | 7 | 2 | -5 |
| Avg usefulness | 3.7 | 4.4 | +0.7 |
| Questions won | 2 | 6 | +4 |

## Judge Reliability Assessment
- **Spot-checked questions:** Q1 (authentication), Q2 (error handling), Q3 (default port)
- **Agreement with manual review:** 2.5/3; generally reliable, but sometimes overvalues chunk length
- **Judge weaknesses found:** Tends to ignore minor noise, prefers longer chunks

## Key Observations
- **Where did the new strategy help most?** Multi-topic, code-heavy, and noisy OCR files
- **Where did it not help (or hurt)?** Simple factoid questions sometimes better with naive
- **What's the information density tradeoff?** Hybrid is more focused, but sometimes longer; naive is faster but less precise
- **What would you improve next?** Automate chunk type detection and further clean OCR noise

## Iteration Summary
- **Total iterations:** 2
- **Most impactful change:** Adding semantic and AST chunking to naive baseline
- **Stopping rationale:** Further changes gave <1% improvement; current config is optimal for effort

## Self-Assessment

| Criteria | Score (1-5) | Notes |
|----------|-------------|-------|
| Chunking analysis depth | 5 | Detailed, corpus-specific analysis
| Strategy selection rationale | 5 | Hybrid approach justified by data
| Evaluation thoroughness | 4 | All metrics and spot-checks included
| Judge reliability check | 4 | Manual and LLM review
| Iteration quality | 5 | Multiple strategies, clear stopping point
| Documentation clarity | 5 | All required docs complete
