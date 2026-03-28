from typing import List
from haystack import component, Document

from naive_chunker import NaiveChunker
from semantic_chunker import SemanticChunkerComponent


@component
class HybridChunkerComponent:
    """
    Hybrid chunker:
    - Structured → Naive medium
    - Multi-topic/OCR → Semantic
    """

    def __init__(self):
        self.naive_chunker = NaiveChunker(variant="medium")
        self.semantic_chunker = SemanticChunkerComponent()

    @component.output_types(documents=List[Document])
    def run(self, documents: List[Document]):

        output_docs = []

        for doc in documents:
            content_type = doc.meta.get("content_type", "documentation")

            if content_type in ["multi_topic", "ocr"]:
                result = self.semantic_chunker.run([doc])
            else:
                result = self.naive_chunker.run([doc])

            chunks = result["documents"]

            for chunk in chunks:
                chunk.meta["parent_id"] = doc.id
                chunk.meta["chunking_strategy"] = "hybrid"

            output_docs.extend(chunks)

        return {"documents": output_docs}