from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from haystack import component
from haystack.dataclasses import ChatMessage
from haystack_integrations.components.generators.google_genai import GoogleGenAIChatGenerator
from qdrant_client import QdrantClient


@component
class LLMFileSelector:
    """Two-stage file selector: broad vector retrieval over file metadata then LLM pruning."""

    def __init__(
        self,
        qdrant_url: str,
        qdrant_api_key: str,
        metadata_collection: str = "week3_file_metadata",
        top_k_broad: int = 50,
        top_k_final: int = 12,
        llm_model: str = "gemini-2.5-flash",
    ) -> None:
        self.qdrant_url = qdrant_url
        self.qdrant_api_key = qdrant_api_key
        self.metadata_collection = metadata_collection
        self.top_k_broad = top_k_broad
        self.top_k_final = top_k_final
        self.llm_model = llm_model
        self.client: QdrantClient | None = None
        self.llm: GoogleGenAIChatGenerator | None = None

    def warm_up(self) -> None:
        if self.client is None:
            self.client = QdrantClient(
                url=self.qdrant_url,
                api_key=self.qdrant_api_key,
                prefer_grpc=True,
                timeout=60,
            )
        if self.llm is None:
            self.llm = GoogleGenAIChatGenerator(model=self.llm_model)

    def _broad_retrieve(self, query_embedding: list[float]) -> list[dict[str, Any]]:
        response = self.client.query_points(
            collection_name=self.metadata_collection,
            query=query_embedding,
            limit=self.top_k_broad,
            with_payload=True,
        )
        rows: list[dict[str, Any]] = []
        for point in response.points:
            payload = point.payload or {}
            fp = str(payload.get("file_path", ""))
            rows.append(
                {
                    "file_path": fp,
                    "filename": Path(fp).name,
                    "summary": str(payload.get("summary", ""))[:280],
                    "file_type": str(payload.get("file_type", "")),
                    "content_type": str(payload.get("content_type", "")),
                    "score": float(point.score) if point.score is not None else 0.0,
                }
            )
        return rows

    def _prune_with_llm(self, query: str, candidates: list[dict[str, Any]]) -> list[str]:
        candidate_block = []
        filename_to_path: dict[str, str] = {}
        for idx, c in enumerate(candidates, start=1):
            filename_to_path[c["filename"]] = c["file_path"]
            candidate_block.append(
                f"{idx}. {c['filename']} | type={c['file_type']} | content={c['content_type']} | score={c['score']:.3f}\n"
                f"summary: {c['summary']}"
            )

        prompt = (
            "Select the most relevant files for answering the user query.\n"
            f"Return ONLY valid JSON array of exactly {self.top_k_final} filenames.\n\n"
            f"Query: {query}\n\nCandidates:\n" + "\n\n".join(candidate_block)
        )
        response = self.llm.run(messages=[ChatMessage.from_user(prompt)])
        text = response["replies"][0].text.strip()
        if text.startswith("```"):
            text = text.strip("`")
            if text.lower().startswith("json"):
                text = text[4:].strip()
        try:
            picked = json.loads(text)
        except Exception:
            return [c["file_path"] for c in candidates[: self.top_k_final]]

        selected: list[str] = []
        for name in picked:
            if isinstance(name, str) and name in filename_to_path:
                selected.append(filename_to_path[name])
        if not selected:
            return [c["file_path"] for c in candidates[: self.top_k_final]]
        return selected[: self.top_k_final]

    @component.output_types(selected_files=list[str])
    def run(self, query: str, query_embedding: list[float]) -> dict[str, list[str]]:
        if self.client is None or self.llm is None:
            self.warm_up()
        candidates = self._broad_retrieve(query_embedding=query_embedding)
        selected = self._prune_with_llm(query=query, candidates=candidates)
        return {"selected_files": selected}
