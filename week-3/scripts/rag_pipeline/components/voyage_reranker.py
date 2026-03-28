from __future__ import annotations

import os
from typing import Any

import voyageai
from haystack import Document, component


@component
class VoyageReranker:
    """Rerank retrieved chunks using Voyage rerank API."""

    def __init__(
        self,
        model: str = "rerank-2.5",
        top_k: int = 10,
        api_key: str | None = None,
    ) -> None:
        self.model = model
        self.top_k = top_k
        self.api_key = api_key or os.getenv("VOYAGE_API_KEY")
        if not self.api_key:
            raise ValueError("VOYAGE_API_KEY is required for Voyage reranking.")
        self.client: voyageai.Client | None = None

    def warm_up(self) -> None:
        if self.client is None:
            self.client = voyageai.Client(api_key=self.api_key)

    @component.output_types(documents=list[Document])
    def run(
        self,
        query: str,
        documents: list[Document],
        top_k: int | None = None,
    ) -> dict[str, Any]:
        if self.client is None:
            self.warm_up()

        if not documents:
            return {"documents": []}

        k = min(top_k or self.top_k, len(documents))
        doc_texts = [doc.content for doc in documents]

        try:
            response = self.client.rerank(
                query=query,
                documents=doc_texts,
                model=self.model,
                top_k=k,
            )
        except Exception:
            return {"documents": documents[:k]}

        reranked: list[Document] = []
        for item in response.results:
            source_doc = documents[item.index]
            reranked.append(
                Document(
                    id=source_doc.id,
                    content=source_doc.content,
                    meta=dict(source_doc.meta or {}),
                    score=float(item.relevance_score),
                )
            )
        return {"documents": reranked}
