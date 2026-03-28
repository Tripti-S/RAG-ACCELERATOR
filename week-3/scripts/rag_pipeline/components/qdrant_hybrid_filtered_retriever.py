from __future__ import annotations

from pathlib import Path
from typing import Any

from haystack import Document, component
from qdrant_client import QdrantClient, models


@component
class QdrantHybridFilteredRetriever:
    """Hybrid retriever with optional payload filtering on category and file path."""

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

    def _build_filter(
        self,
        categories: list[str] | None,
        file_paths: list[str] | None,
    ) -> models.Filter | None:
        conditions: list[models.Condition] = []

        if categories:
            conditions.append(
                models.FieldCondition(
                    key="meta.category",
                    match=models.MatchAny(any=categories),
                )
            )

        if file_paths:
            file_names = [Path(fp).name for fp in file_paths]
            conditions.append(
                models.FieldCondition(
                    key="meta.file_path",
                    match=models.MatchAny(any=file_names),
                )
            )

        if not conditions:
            return None
        return models.Filter(must=conditions)

    @component.output_types(documents=list[Document])
    def run(
        self,
        query_embedding: list[float],
        query_sparse_embedding: Any,
        categories: list[str] | None = None,
        file_paths: list[str] | None = None,
    ) -> dict[str, list[Document]]:
        if self.client is None:
            self.warm_up()

        sparse_vector = models.SparseVector(
            indices=query_sparse_embedding.indices,
            values=query_sparse_embedding.values,
        )
        query_filter = self._build_filter(categories=categories, file_paths=file_paths)

        response = self.client.query_points(
            collection_name=self.collection_name,
            prefetch=[
                models.Prefetch(
                    query=query_embedding,
                    using="text-dense",
                    limit=self.dense_prefetch_limit,
                    filter=query_filter,
                ),
                models.Prefetch(
                    query=sparse_vector,
                    using="text-sparse",
                    limit=self.sparse_prefetch_limit,
                    filter=query_filter,
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
