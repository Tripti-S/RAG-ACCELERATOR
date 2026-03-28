
# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 2: Naive Word-Based Chunking Strategies
=============================================

Three variants of simple word-based chunking to demonstrate
the impact of chunk size on retrieval quality.

Variants:
- small: 200 words, 25 overlap (~1000 chars) - high precision, low context
- medium: 400 words, 50 overlap (~2000 chars) - balanced baseline
- large: 800 words, 100 overlap (~4000 chars) - more context, diluted relevance

Key Insight:
These are "naive" because they split purely on word count without
considering sentence boundaries, paragraphs, or semantic units.
This makes them a useful baseline for comparing smarter strategies.
"""

from typing import List, Dict, Literal
from haystack import component, Document
from haystack.components.preprocessors import DocumentSplitter


@component
class NaiveChunker:
	"""
	Haystack component for naive word-based chunking.

	Simple fixed-size chunking without considering semantic boundaries,
	sentence structure, or content type. Pure word-count based splitting.

	This is the simplest approach and serves as our baseline.
	"""

	def __init__(self, variant: Literal["small", "medium", "large"] = "medium"):
		"""
		Initialize naive chunker with size variant.

		Args:
			variant: Size variant - "small" (200w), "medium" (400w), or "large" (800w)
		"""
		# Define chunk sizes and overlap for each variant
		sizes = {
			"small": (200, 25),    # ~260 tokens, fits BGE-large
			"medium": (400, 50),   # ~520 tokens, slight truncation risk
			"large": (800, 100)    # ~1040 tokens, will be truncated by BGE-large
		}

		if variant not in sizes:
			raise ValueError(f"Invalid variant '{variant}'. Must be: small, medium, or large")
		self.variant = variant
		self.chunk_size, self.overlap = sizes[variant]

		# Create Haystack DocumentSplitter
		self.splitter = DocumentSplitter(
			split_by="word",
			split_length=self.chunk_size,
			split_overlap=self.overlap
		)

	def warm_up(self):
		"""Warm up the internal splitter."""
		self.splitter.warm_up()

	@component.output_types(documents=List[Document])
	def run(self, documents: List[Document]) -> Dict[str, List[Document]]:
		"""
		Split documents using naive word-based chunking.

		Args:
			documents: List of documents to chunk

		Returns:
			Dictionary with "documents" key containing chunked documents
		"""
		# Run Haystack splitter
		result = self.splitter.run(documents=documents)

		# Add chunk metadata to each document
		for doc in result["documents"]:
			doc.meta["chunk_method"] = f"naive_{self.variant}"
			doc.meta["chunk_size"] = self.chunk_size
			doc.meta["chunk_overlap"] = self.overlap

		return result


def create_naive_chunker(variant: str = "medium") -> NaiveChunker:
	"""
	Factory function to create a naive chunker.

	Args:
		variant: "small", "medium", or "large"

	Returns:
		Configured NaiveChunker instance
	"""
	return NaiveChunker(variant=variant)


if __name__ == "__main__":
	"""Test the naive chunker with sample text."""

	# Create sample document
	sample_text = " ".join([f"Word{i}" for i in range(500)])  # 500 words
	sample_doc = Document(content=sample_text, meta={"source": "test"})

	# Test each variant
	for variant in ["small", "medium", "large"]:
		print(f"\n{'='*60}")
		print(f"Testing Naive Chunker - {variant.upper()}")
		print(f"{'='*60}")

		chunker = NaiveChunker(variant=variant)
		result = chunker.run(documents=[sample_doc])

		chunks = result["documents"]
		print(f"Original document: 500 words")
		print(f"Chunk size: {chunker.chunk_size} words")
		print(f"Chunk overlap: {chunker.overlap} words")
		print(f"Number of chunks created: {len(chunks)}")

		# Show first chunk metadata
		if chunks:
			print(f"\nFirst chunk metadata:")
			print(f"  - chunk_method: {chunks[0].meta.get('chunk_method')}")
			print(f"  - chunk_size: {chunks[0].meta.get('chunk_size')}")
			print(f"  - chunk_overlap: {chunks[0].meta.get('chunk_overlap')}")

			# Count words in first chunk
			first_chunk_words = len(chunks[0].content.split())
			print(f"  - actual words in first chunk: {first_chunk_words}")
