from __future__ import annotations

from pathlib import Path

from haystack import Document, component


@component
class CategoryDocumentFilter:
    """Filter retrieved documents by meta.category without requiring Qdrant payload indexes."""

    @component.output_types(documents=list[Document])
    def run(self, documents: list[Document], categories: list[str] | None = None) -> dict[str, list[Document]]:
        if not categories:
            return {"documents": documents}

        wanted = {c.lower() for c in categories if c}
        if "general" in wanted:
            return {"documents": documents}

        filtered = [d for d in documents if str((d.meta or {}).get("category", "")).lower() in wanted]
        # Fallback to unfiltered docs so downstream generation always has context.
        return {"documents": filtered if filtered else documents}


@component
class FilePathDocumentFilter:
    """Filter retrieved documents by meta.file_path using exact or basename matching."""

    @component.output_types(documents=list[Document])
    def run(self, documents: list[Document], file_paths: list[str] | None = None) -> dict[str, list[Document]]:
        if not file_paths:
            return {"documents": documents}

        exact = {p.strip().lower() for p in file_paths if p and p.strip()}
        names = {Path(p).name.lower() for p in exact}
        filtered: list[Document] = []
        for d in documents:
            doc_path = str((d.meta or {}).get("file_path", "")).strip().lower()
            if not doc_path:
                continue
            if doc_path in exact or Path(doc_path).name.lower() in names:
                filtered.append(d)

        # Fallback to unfiltered docs when selector and retrieval paths do not align.
        return {"documents": filtered if filtered else documents}
