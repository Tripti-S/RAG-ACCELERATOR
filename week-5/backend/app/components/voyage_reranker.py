# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Voyage AI Reranker Component
=====================================

Haystack-compatible reranker using Voyage AI's rerank-2.5 model.
Drop-in replacement for TransformersSimilarityRanker.

Adapted from Week 3 (proven in evaluation). No functional changes —
includes graceful fallback on API failure (returns truncated original
documents rather than crashing the pipeline).
"""

from typing import List, Dict, Any, Optional
from haystack import component, Document
import voyageai
import os


@component
class VoyageReranker:
    """
    Reranker using Voyage AI API.

    Compatible with Haystack pipeline - same interface as TransformersSimilarityRanker.

    Args:
        model: Voyage reranker model (default: "rerank-2.5")
        top_k: Number of documents to return after reranking
        api_key: Voyage API key (reads from VOYAGE_API_KEY env var if not provided)
    """

    def __init__(
        self,
        model: str = "rerank-2.5",
        top_k: int = 10,
        api_key: Optional[str] = None
    ):
        self.model = model
        self.top_k = top_k
        self.api_key = api_key or os.getenv("VOYAGE_API_KEY")
        self.client = None

        if not self.api_key:
            raise ValueError(
                "Voyage API key required. Set VOYAGE_API_KEY environment variable "
                "or pass api_key parameter."
            )

    def warm_up(self):
        """Initialize Voyage client."""
        if self.client is None:
            self.client = voyageai.Client(api_key=self.api_key)
            print(f"   Voyage reranker ready (model: {self.model})")

    @component.output_types(documents=List[Document])
    def run(
        self,
        query: str,
        documents: List[Document],
        top_k: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Rerank documents using Voyage AI.

        Args:
            query: Search query
            documents: List of documents to rerank
            top_k: Override default top_k

        Returns:
            Dict with 'documents' key containing reranked documents
        """
        if self.client is None:
            self.warm_up()

        if not documents:
            return {"documents": []}

        # Use provided top_k or default
        k = top_k if top_k is not None else self.top_k
        k = min(k, len(documents))  # Can't return more than we have

        # Extract document texts for Voyage API
        doc_texts = [doc.content for doc in documents]

        print(f"   Reranking {len(documents)} docs with Voyage (model: {self.model}, top_k: {k})...")

        # Call Voyage rerank API
        try:
            reranking = self.client.rerank(
                query=query,
                documents=doc_texts,
                model=self.model,
                top_k=k
            )
            print(f"   Voyage reranking succeeded")
        except Exception as e:
            print(f"   Voyage reranking failed: {e}")
            # Fallback: return original documents truncated to top_k
            return {"documents": documents[:k]}

        # Reconstruct documents in reranked order with new scores
        reranked_docs = []
        for result in reranking.results:
            original_doc = documents[result.index]

            # Create new document with Voyage relevance score
            reranked_doc = Document(
                id=original_doc.id,
                content=original_doc.content,
                meta=original_doc.meta.copy() if original_doc.meta else {},
                score=result.relevance_score  # Voyage score (0-1 range)
            )
            reranked_docs.append(reranked_doc)

        return {"documents": reranked_docs}
