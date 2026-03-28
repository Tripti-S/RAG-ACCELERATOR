# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.

"""
Week 2: Logical Boundary Chunking Strategies
=============================================

Chunking that respects logical text boundaries rather than
arbitrary word counts.

Strategies:
- Sentence-based: Split by sentences, target ~6 sentences, 2 sentence overlap
- Recursive: Hierarchical splitting (paragraphs → sentences → words), target ~400 words

Key Insight:
These strategies never split mid-sentence, preserving grammatical
completeness. Recursive chunking additionally tries to keep paragraphs
together when possible.
"""

from typing import List, Dict, Literal
from haystack import component, Document
from haystack.components.preprocessors import DocumentSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter


@component
class SentenceChunker:
	"""
	Haystack component for sentence-based chunking.

	Respects sentence boundaries, preventing mid-sentence splits.
	Target size ~6 sentences with 2-sentence overlap for context continuity.

	Best for: Prose content where sentence-level coherence matters.
	"""

	def __init__(self):
		"""Initialize sentence-based chunker."""
		# Haystack's sentence splitter
		self.splitter = DocumentSplitter(
			split_by="sentence",
			split_length=6,    # 6 sentences (avg ~120 words)
			split_overlap=2    # 2 sentence overlap for context
		)

	def warm_up(self):
		"""Warm up the internal splitter."""
		self.splitter.warm_up()

	@component.output_types(documents=List[Document])
	def run(self, documents: List[Document]) -> Dict[str, List[Document]]:
		"""
		Split documents by sentence boundaries.

		Args:
			documents: List of documents to chunk

		Returns:
			Dictionary with "documents" key containing chunked documents
		"""
		result = self.splitter.run(documents=documents)

		# Add chunk metadata
		for doc in result["documents"]:
			doc.meta["chunk_method"] = "sentence_based"
			doc.meta["split_unit"] = "sentence"
			doc.meta["target_sentences"] = 6
			doc.meta["sentence_overlap"] = 2

		return result


@component
class RecursiveChunker:
	"""
	Haystack component for recursive character-based chunking.

	Uses hierarchical splitting: tries to split on larger separators first
	(paragraphs), then moves to smaller ones (sentences, words) if needed.
	This preserves natural document structure better than naive chunking.

	Separator hierarchy: \n\n (paragraphs) → \n (lines) → . (sentences) → space (words)

	Best for: Well-structured documents with clear paragraph boundaries.
	"""

	def __init__(self):
		"""Initialize recursive chunker."""
		# LangChain's RecursiveCharacterTextSplitter
		# Tries separators in order: \n\n (paragraphs), \n (lines), . (sentences), space (words)
		self.splitter = RecursiveCharacterTextSplitter(
			chunk_size=2000,      # ~400 words (avg 5 chars/word)
			chunk_overlap=200,    # ~40 words overlap
			length_function=len,  # Measure by characters
			separators=["\n\n", "\n", ". ", " ", ""]  # Try in this order
		)

	def warm_up(self):
		"""Warm up method (no-op for LangChain splitter)."""
		pass

	@component.output_types(documents=List[Document])
	def run(self, documents: List[Document]) -> Dict[str, List[Document]]:
		"""
		Split documents using recursive character splitting.

		Args:
			documents: List of documents to chunk

		Returns:
			Dictionary with "documents" key containing chunked documents
		"""
		chunked_docs = []

		for doc in documents:
			# Use LangChain recursive splitter
			chunks = self.splitter.split_text(doc.content)

			# Convert to Haystack Documents
			for i, chunk_text in enumerate(chunks):
				chunk_doc = Document(
					content=chunk_text,
					meta={
						**doc.meta,  # Preserve original metadata
						"chunk_method": "recursive",
						"split_unit": "recursive_char",
						"chunk_size": 2000,
						"chunk_overlap": 200,
						"chunk_index": i,
						"original_doc_id": doc.id
					}
				)
				chunked_docs.append(chunk_doc)

		return {"documents": chunked_docs}


@component
class LogicalChunker:
	"""
	Unified component that can use either sentence or recursive chunking.
	"""

	def __init__(self, strategy: Literal["sentence", "recursive"] = "sentence"):
		"""
		Initialize logical chunker with strategy.

		Args:
			strategy: "sentence" or "recursive"
		"""
		if strategy not in ["sentence", "recursive"]:
			raise ValueError(f"Invalid strategy '{strategy}'. Must be: sentence or recursive")

		self.strategy = strategy

		if strategy == "sentence":
			self.chunker = SentenceChunker()
		else:
			self.chunker = RecursiveChunker()

	def warm_up(self):
		"""Warm up the internal chunker."""
		self.chunker.warm_up()

	@component.output_types(documents=List[Document])
	def run(self, documents: List[Document]) -> Dict[str, List[Document]]:
		"""
		Split documents using selected logical boundary strategy.

		Args:
			documents: List of documents to chunk

		Returns:
			Dictionary with "documents" key containing chunked documents
		"""
		return self.chunker.run(documents=documents)


def create_sentence_chunker() -> SentenceChunker:
	"""Factory function for sentence-based chunker."""
	return SentenceChunker()


def create_recursive_chunker() -> RecursiveChunker:
	"""Factory function for recursive chunker."""
	return RecursiveChunker()


if __name__ == "__main__":
	"""Test logical chunkers with sample text."""

	# Create sample document with paragraphs
	paragraphs = [
		"This is the first paragraph. It has multiple sentences. Each sentence adds information. The paragraph discusses a concept.",
		"This is the second paragraph. It continues the discussion. New ideas are introduced here. The text flows naturally.",
		"Third paragraph arrives. It builds on previous content. More details emerge. Context deepens."
	]
	sample_text = "\n\n".join(paragraphs)
	sample_doc = Document(content=sample_text, meta={"source": "test"})

	# Test sentence chunker
	print(f"{'='*60}")
	print(f"Testing Sentence-Based Chunker")
	print(f"{'='*60}")

	sent_chunker = SentenceChunker()
	sent_result = sent_chunker.run(documents=[sample_doc])
	sent_chunks = sent_result["documents"]

	print(f"Number of chunks: {len(sent_chunks)}")
	if sent_chunks:
		print(f"First chunk metadata: {sent_chunks[0].meta}")
		print(f"First chunk preview: {sent_chunks[0].content[:100]}...")

	# Test recursive chunker
	print(f"\n{'='*60}")
	print(f"Testing Recursive Chunker")
	print(f"{'='*60}")

	rec_chunker = RecursiveChunker()
	rec_result = rec_chunker.run(documents=[sample_doc])
	rec_chunks = rec_result["documents"]

	print(f"Number of chunks: {len(rec_chunks)}")
	if rec_chunks:
		print(f"First chunk metadata: {rec_chunks[0].meta}")
		print(f"First chunk preview: {rec_chunks[0].content[:100]}...")
