# Step 3: Implement and Index

All chunking and indexing scripts are located in:

week-2/scripts/

## Scripts Implemented

- create_chunking_pipeline.py – Defines recursive, semantic, and naive chunking pipelines
- run_naive_indexing.py – Runner for naive chunking
- run_recursive_indexing.py – Runner for recursive chunking
- run_semantic_indexing.py – Runner for semantic chunking
- Supporting preprocessing integrated in pipeline

---

## Important

The Week 1 baseline index was kept intact for comparison.

Each Week 2 strategy indexes into a separate Qdrant collection.

---

# Indexing Comparison

## Week 1 Baseline (Naive Word-Based Chunking)

- Chunking Strategy: Fixed-size word split (400 words, 50 overlap)
- Total Chunk Count: 482
- Average Chunk Size: ~380–400 words
- Embedding Model: BGE-large (1024d)
- Truncation Warnings: None observed
- Indexing Time: Recorded during execution

---

## Week 2 Recursive Chunking

- Chunking Strategy: Recursive character-based splitting (~2000 characters, hierarchical boundaries)
- Total Chunk Count: 2315
- Average Chunk Size: Smaller structured segments
- Embedding Model: BGE-large (1024d)
- Truncation Warnings: None observed
- Indexing Time: Higher than baseline due to increased chunk count

### Observation

Recursive chunking significantly increased chunk count (482 → 2315).

Implications:
- More granular structural splits
- Higher embedding and storage cost
- Potentially more precise retrieval segments
- Increased indexing time

---

## Week 2 Semantic Chunking

- Chunking Strategy: Adaptive semantic boundary detection
- Total Chunk Count: 2792
- Average Chunk Size: Topic-aware variable segments
- Embedding Model: BGE-large (1024d)
- Truncation Warnings: None observed
- Indexing Time: Highest among strategies due to chunk volume

### Observation

Semantic chunking produced the highest chunk count (2792), indicating fine-grained topic segmentation.

Implications:
- Maximum semantic coherence per chunk
- Increased embedding cost
- Higher retrieval precision potential
- Increased storage and indexing time

---

# Comparative Summary

| Strategy   | Chunk Count | Granularity Level | Cost | Retrieval Precision |
|------------|------------|------------------|------|--------------------|
| Naive      | 482        | Fixed-size       | Low  | Moderate |
| Recursive  | 2315       | Structural split | Medium | High |
| Semantic   | 2792       | Topic-aware      | High | Highest potential |

---

# Key Insight

Chunking strategy directly impacts:

- Embedding cost
- Retrieval granularity
- Storage requirements
- Context quality provided to the LLM

Naive chunking is efficient but structure-agnostic.  
Recursive chunking improves structural segmentation but increases chunk count.  
Semantic chunking maximizes topical coherence at the highest computational cost.

This demonstrates the trade-off between efficiency and retrieval precision in RAG system design.