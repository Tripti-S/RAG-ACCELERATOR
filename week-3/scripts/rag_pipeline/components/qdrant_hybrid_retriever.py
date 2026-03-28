from __future__ import annotations

from typing import Any

from haystack import Document, component, default_from_dict, default_to_dict
from qdrant_client import QdrantClient, models


@component
class QdrantHybridRetriever:
    """Hybrid retriever using Qdrant native fusion with explicit prefetch limits."""

    def __init__(
        self,
        url: str,
        api_key: str,
        collection_name: str,
        top_k: int = 50,
        dense_prefetch_limit: int = 100,
        sparse_prefetch_limit: int = 100,
    ) -> None:
        self.url = url
        self.api_key = api_key
        self.collection_name = collection_name
        self.top_k = top_k
        self.dense_prefetch_limit = dense_prefetch_limit
        self.sparse_prefetch_limit = sparse_prefetch_limit
        self.client: QdrantClient | None = None

    def warm_up(self) -> None:
        if self.client is None:
            self.client = QdrantClient(
                url=self.url,
                api_key=self.api_key,
                prefer_grpc=True,
                timeout=60,
            )

    def to_dict(self) -> dict[str, Any]:
        return default_to_dict(
            self,
            url=self.url,
            api_key=self.api_key,
            collection_name=self.collection_name,
            top_k=self.top_k,
            dense_prefetch_limit=self.dense_prefetch_limit,
            sparse_prefetch_limit=self.sparse_prefetch_limit,
        )

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "QdrantHybridRetriever":
        return default_from_dict(cls, data)

    @component.output_types(documents=list[Document])
    def run(
        self,
        query_embedding: list[float],
        query_sparse_embedding: Any,
    ) -> dict[str, list[Document]]:
        if self.client is None:
            self.warm_up()

        sparse_vector = models.SparseVector(
            indices=query_sparse_embedding.indices,
            values=query_sparse_embedding.values,
        )

        response = self.client.query_points(
            collection_name=self.collection_name,
            prefetch=[
                models.Prefetch(
                    query=query_embedding,
                    using="text-dense",
                    limit=self.dense_prefetch_limit,
                ),
                models.Prefetch(
                    query=sparse_vector,
                    using="text-sparse",
                    limit=self.sparse_prefetch_limit,
                ),
            ],
            query=models.FusionQuery(fusion=models.Fusion.RRF),
            limit=self.top_k,
            with_payload=True,
        )

        docs: list[Document] = []
        for point in response.points:
            payload = point.payload or {}
            meta = payload.get("meta") if isinstance(payload.get("meta"), dict) else {}
            docs.append(
                Document(
                    id=str(point.id),
                    content=payload.get("content", ""),
                    meta=meta,
                    score=point.score,
                )
            )
        return {"documents": docs}
