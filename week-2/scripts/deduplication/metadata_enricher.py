
# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 2: Metadata Enricher Component
====================================

Enriches documents with metadata from deduplication manifest.
Adds content_type (code/documentation) to help downstream components
like the AST chunker detect code files even with .txt extensions.

This component bridges the deduplication phase with the chunking phase,
passing along useful metadata that was computed during deduplication.
"""

import logging
from typing import List, Dict, Any
from pathlib import Path
from haystack import component, Document

logger = logging.getLogger(__name__)


@component
class MetadataEnricher:
	"""
	Enriches documents with metadata from manifest.

	Adds content_type and other metadata fields to documents based on filepath.
	Used to pass manifest metadata through the indexing pipeline.

	This is necessary because:
	1. File converters only see the file, not our manifest
	2. AST chunker needs to know if a .txt file is actually code
	3. We want to preserve source_dir info for debugging
	"""

	def __init__(self, metadata_map: Dict[str, Dict[str, Any]]):
		"""
		Initialize metadata enricher.

		Args:
			metadata_map: Mapping of filepath → metadata dict
						  Example: {"/path/to/file.py": {"content_type": "code", "source_dir": "sdk"}}
		"""
		self.metadata_map = metadata_map

	@component.output_types(documents=List[Document])
	def run(self, documents: List[Document]) -> Dict[str, List[Document]]:
		"""
		Enrich documents with manifest metadata.

		Args:
			documents: Input documents from file converters

		Returns:
			Dict with 'documents' key containing enriched documents
		"""
		enriched_docs = []

		for doc in documents:
			filepath = doc.meta.get("file_path", "")

			# Try to get metadata - first try exact match, then try matching by filename
			extra_meta = self.metadata_map.get(filepath, {})

			if not extra_meta and filepath:
				# Haystack converters might store just filename, not full path
				# Try to find by matching filename at end of manifest paths
				filename = Path(filepath).name

				for full_path, meta in self.metadata_map.items():
					if Path(full_path).name == filename:
						extra_meta = meta
						break

			# Create enriched document
			enriched_doc = Document(
				content=doc.content,
				meta={
					**doc.meta,
					**extra_meta  # Add content_type, source_dir, etc.
				}
			)
			enriched_docs.append(enriched_doc)

		logger.info(f"Enriched {len(enriched_docs)} documents with manifest metadata")
		return {"documents": enriched_docs}
