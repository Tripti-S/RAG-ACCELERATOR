# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Hybrid Retriever with Proper Prefetch Limits
=====================================================

Custom Haystack retriever that fixes QdrantHybridRetriever's prefetch bug.

PROBLEM: Haystack's built-in QdrantHybridRetriever doesn't set explicit prefetch
limits, so Qdrant defaults to ~10-20 docs per vector type instead of requested top_k.

SOLUTION: Use Qdrant native API with explicit prefetch limits on both dense and
sparse queries before RRF fusion.

Retrieval flow:
1. Dense vector prefetch (explicit limit)
2. Sparse vector prefetch (explicit limit)
3. RRF fusion
4. Return top_k results

Adapted from Week 3 (proven in evaluation). No functional changes — this component
is battle-tested across all Week 3 retrieval experiments.
"""

from typing import List, Dict, Any
from haystack import component, Document, default_to_dict, default_from_dict
from qdrant_client import QdrantClient, models


@component
class QdrantHybridRetriever:
    """
    Hybrid retriever using Qdrant's native API with explicit prefetch limits.

    Args:
        url: Qdrant server URL
        api_key: Qdrant API key
        collection_name: Name of the collection
        top_k: Number of documents to return after RRF fusion (default: 50)
        dense_prefetch_limit: Explicit limit for dense prefetch (default: 100)
        sparse_prefetch_limit: Explicit limit for sparse prefetch (default: 100)
    """

    def __init__(
        self,
        url: str,
        api_key: str,
        collection_name: str,
        top_k: int = 50,
        dense_prefetch_limit: int = 100,
        sparse_prefetch_limit: int = 100
    ):
        self.url = url
        self.api_key = api_key
        self.collection_name = collection_name
        self.top_k = top_k  # Output AFTER RRF fusion
        self.dense_prefetch_limit = dense_prefetch_limit  # Dense vector prefetch
        self.sparse_prefetch_limit = sparse_prefetch_limit  # Sparse vector prefetch

        self.client = None

    def warm_up(self):
        """Initialize Qdrant client."""
        if self.client is None:
            self.client = QdrantClient(
                url=self.url,
                api_key=self.api_key,
                prefer_grpc=True,
                timeout=60
            )
            print(f"   Hybrid Retriever ready (Dense:{self.dense_prefetch_limit}, Sparse:{self.sparse_prefetch_limit} -> RRF:{self.top_k})")

    def to_dict(self) -> Dict[str, Any]:
        """Serialize component."""
        return default_to_dict(
            self,
            url=self.url,
            api_key=self.api_key,
            collection_name=self.collection_name,
            top_k=self.top_k,
            dense_prefetch_limit=self.dense_prefetch_limit,
            sparse_prefetch_limit=self.sparse_prefetch_limit
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "QdrantHybridRetriever":
        """Deserialize component."""
        return default_from_dict(cls, data)

    @component.output_types(documents=List[Document])
    def run(
        self,
        query_embedding: List[float],
        query_sparse_embedding: Any
    ) -> Dict[str, Any]:
        """
        Retrieve documents using hybrid search with EXPLICIT prefetch limits.

        Args:
            query_embedding: Dense query embedding
            query_sparse_embedding: Sparse query embedding (SparseEmbedding object)

        Returns:
            Dict with 'documents' key containing retrieved documents
        """
        if self.client is None:
            self.warm_up()

        # Convert sparse embedding to Qdrant format
        sparse_vector = models.SparseVector(
            indices=query_sparse_embedding.indices,
            values=query_sparse_embedding.values
        )

        print(f"   Hybrid retrieval: Dense({self.dense_prefetch_limit}) + Sparse({self.sparse_prefetch_limit}) -> RRF -> {self.top_k} docs")

        # Query with EXPLICIT prefetch limits (THIS IS THE FIX!)
        response = self.client.query_points(
            collection_name=self.collection_name,
            prefetch=[
                # Dense vector prefetch
                models.Prefetch(
                    query=query_embedding,
                    using="text-dense",
                    limit=self.dense_prefetch_limit
                ),
                # Sparse vector prefetch
                models.Prefetch(
                    query=sparse_vector,
                    using="text-sparse",
                    limit=self.sparse_prefetch_limit
                )
            ],
            # Main query: RRF fusion of prefetched results
            query=models.FusionQuery(fusion=models.Fusion.RRF),
            limit=self.top_k,
            with_payload=True
        )

        print(f"   Retrieved {len(response.points)} documents after RRF fusion")

        # Convert to Haystack documents
        documents = []
        for point in response.points:
            # Extract metadata - Qdrant native API returns it nested in 'meta' field
            if 'meta' in point.payload and isinstance(point.payload['meta'], dict):
                metadata = point.payload['meta']
            else:
                # Fallback: extract from top level
                metadata = {k: v for k, v in point.payload.items()
                          if k not in ["content", "blob", "id", "score"]}

            doc = Document(
                id=point.id,
                content=point.payload.get("content", ""),
                meta=metadata,
                score=point.score
            )
            documents.append(doc)

        return {"documents": documents}
