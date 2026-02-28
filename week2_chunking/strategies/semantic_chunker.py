# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 2: Semantic Chunking Strategy
===================================

Chunks based on semantic similarity rather than fixed boundaries.
Uses LangChain's SemanticChunker to detect natural topic transitions.

How It Works:
1. Embed each sentence individually
2. Compare consecutive sentence embeddings
3. Split where similarity drops (topic transition detected)

Key Features:
- Adaptive chunk sizes based on content coherence
- Uses lightweight embeddings (MiniLM) for boundary detection
- Final chunks still embedded with bge-large-en-v1.5 for storage

Important Limitations:
- Double embedding cost (once for chunking, once for storage)
- Fails on uniform content (no topic transitions = huge chunks)
- Poor on code (syntax similarity ≠ semantic similarity)
- Unpredictable chunk sizes
"""

from typing import List, Dict
from haystack import component, Document

# LangChain imports for semantic chunking
from langchain_text_splitters import RecursiveCharacterTextSplitter
try:
    from langchain_huggingface import HuggingFaceEmbeddings
except ImportError:
    from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker


@component
class SemanticChunkerComponent:
    """
    Haystack component for semantic-based chunking using LangChain.

    Uses embeddings to detect semantic boundaries and split text
    where topic transitions occur naturally.

    Note: The embeddings_model here is ONLY for detecting chunk boundaries.
    The final chunks are re-embedded with bge-large-en-v1.5 during indexing.
    """

    def __init__(
        self,
        embeddings_model: str = "sentence-transformers/all-MiniLM-L6-v2",
        breakpoint_threshold_type: str = "percentile",
        breakpoint_threshold_amount: float = 95
    ):
        """
        Initialize semantic chunker.

        Args:
            embeddings_model: Model for semantic similarity (internal use only)
            breakpoint_threshold_type: "percentile", "standard_deviation", or "interquartile"
            breakpoint_threshold_amount: Threshold value (e.g., 95 for 95th percentile)

        Note: embeddings_model is ONLY for chunking boundary detection.
              Final chunks are embedded with bge-large-en-v1.5 during indexing.
        """
        # Create embeddings for semantic similarity detection
        # Using lightweight model for chunking (not for final storage)
        self.embeddings = HuggingFaceEmbeddings(
            model_name=embeddings_model,
            model_kwargs={'device': 'cpu'}
        )

        # Create LangChain semantic chunker
        self.chunker = SemanticChunker(
            embeddings=self.embeddings,
            breakpoint_threshold_type=breakpoint_threshold_type,
            breakpoint_threshold_amount=breakpoint_threshold_amount
        )

        self.breakpoint_type = breakpoint_threshold_type
        self.threshold_amount = breakpoint_threshold_amount

    @component.output_types(documents=List[Document])
    def run(self, documents: List[Document]) -> Dict[str, List[Document]]:
        """
        Split documents using semantic chunking.

        Args:
            documents: List of documents to chunk

        Returns:
            Dictionary with "documents" key containing chunked documents
        """
        chunked_docs = []

        for doc in documents:
            # Use LangChain semantic chunker
            chunks = self.chunker.split_text(doc.content)

            # Convert to Haystack Documents (filter empty chunks)
            chunk_index = 0
            for chunk_text in chunks:
                # Skip empty or whitespace-only chunks
                if not chunk_text or not chunk_text.strip():
                    continue

                chunk_doc = Document(
                    content=chunk_text,
                    meta={
                        **doc.meta,  # Preserve original metadata
                        "chunk_method": "semantic",
                        "breakpoint_type": self.breakpoint_type,
                        "threshold_amount": self.threshold_amount,
                        "chunk_index": chunk_index,
                        "original_doc_id": doc.id
                    }
                )
                chunked_docs.append(chunk_doc)
                chunk_index += 1

        return {"documents": chunked_docs}


def create_semantic_chunker(
    breakpoint_threshold_type: str = "percentile",
    breakpoint_threshold_amount: float = 95
) -> SemanticChunkerComponent:
    """
    Factory function to create semantic chunker.

    Args:
        breakpoint_threshold_type: Threshold type for semantic breaks
        breakpoint_threshold_amount: Threshold value

    Returns:
        Configured SemanticChunkerComponent
    """
    return SemanticChunkerComponent(
        breakpoint_threshold_type=breakpoint_threshold_type,
        breakpoint_threshold_amount=breakpoint_threshold_amount
    )


if __name__ == "__main__":
    """Test semantic chunker with sample text."""

    # Create sample document with topic shifts
    sample_text = """
    Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources.
    MCP provides a standardized way to connect AI models to various contexts and tools.
    The protocol defines clear interfaces for context providers and consumers.

    FastMCP is a Python library that makes it easy to build MCP servers.
    You can create a server with just a few lines of code using decorators.
    The library handles all the protocol complexity for you.
    FastMCP supports tools, resources, and prompts out of the box.

    Security is crucial when building MCP servers.
    Always validate inputs before processing them.
    Use environment variables for sensitive configuration.
    Implement proper authentication and authorization.
    Follow the principle of least privilege.
    """

    sample_doc = Document(content=sample_text, meta={"source": "test"})

    print(f"{'='*60}")
    print(f"Testing Semantic Chunker")
    print(f"{'='*60}")

    chunker = SemanticChunkerComponent()
    result = chunker.run(documents=[sample_doc])

    chunks = result["documents"]
    print(f"\nOriginal text: {len(sample_text)} characters")
    print(f"Number of semantic chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i+1} ---")
        print(f"Length: {len(chunk.content)} chars")
        print(f"Metadata: {chunk.meta}")
        print(f"Preview: {chunk.content[:100]}...")
