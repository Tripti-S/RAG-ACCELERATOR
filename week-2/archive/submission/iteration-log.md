## Iteration 1: Baseline Naive Chunking
- Configuration: chunk size 1000, overlap 200, embedder: bge-large-en-v1.5
- Result: Avg signal 60%, total cutoffs 17, avg usefulness 3.2/5
- Observation: Many chunks cut mid-thought, lots of irrelevant content.

## Iteration 2: Hybrid Chunking (Semantic + AST)
- Configuration: chunk size 500, overlap 100, embedder: minilm (384d)
- Result: Avg signal 86%, total cutoffs 3, avg usefulness 4.7/5
- Observation: Chunks are more focused, fewer cutoffs, higher information density.

## Final Configuration
- Strategy: Hybrid (Semantic + AST)
- Settings: chunk size 500, overlap 100, embedder: minilm (384d)
- Why this is your stopping point: Further changes produced only marginal improvements (<1% signal gain).

## Lessons Learned
- Surprised by how much chunk size and overlap affect signal and cutoffs.
- Would experiment with even smaller chunks and more overlap if time allowed.
- Still unsure how to best balance context breadth vs. focus for all question types.
# Iteration Log

## Iteration 1: Naive Chunking (Fixed-size)
- Configuration: 350-word chunks, 50-word overlap, all files
- Result: Fast, but topic shifts and code blocks often split mid-section/function. 4 truncation warnings.
- Observation: Naive works for uniform docs, but not for mixed or code-heavy files.

## Iteration 2: Hybrid (Naive + Semantic + AST)
- Configuration: Naive for markdown/prose, semantic for multi-topic/OCR, AST for code-heavy; chunk sizes as in strategy doc
- Result: Better topic and code boundary preservation, fewer cutoffs, improved retrieval quality. Slightly slower processing.
- Observation: Hybrid approach balances speed and quality, especially for noisy or complex files.

## Final Configuration
- Strategy: Hybrid (Naive + Semantic + AST)
- Settings: See chunking-strategy.md for details
- Why this is your stopping point: Further iterations gave marginal (<1%) improvement; current config maximizes quality for effort.

## Lessons Learned
- Surprised by the amount of noise in OCR data and its impact on chunking.
- Would automate chunk type detection for even better results.
- Still unsure how best to handle extremely large outlier docs without losing context.
