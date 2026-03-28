"""
Week 3 hybrid indexing script.

Creates a Qdrant collection with:
- Dense vectors: semantic embeddings (Voyage by default; BGE optional)
- Sparse vectors: BM25 sparse embeddings

Data source:
- Uses selected files from artifacts/selected_files_manifest.json
- Uses optimized chunking lineage from Week 2 (recursive chunking), not Week 1 naive chunking

Usage:
  python week-3/scripts/indexing/01_index_hybrid.py --test
  python week-3/scripts/indexing/01_index_hybrid.py --full
  python week-3/scripts/indexing/01_index_hybrid.py --full --dense-model bge
    python week-3/scripts/indexing/01_index_hybrid.py --full --recreate
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional

from dotenv import load_dotenv
from haystack import Pipeline, component, Document
from haystack.components.converters import MarkdownToDocument, TextFileToDocument
from haystack.components.joiners import DocumentJoiner
from haystack.components.preprocessors import DocumentCleaner
from haystack.components.routers import FileTypeRouter
from haystack.components.writers import DocumentWriter
from haystack.utils import Secret
from haystack_integrations.components.embedders.fastembed import (
    FastembedDocumentEmbedder,
    FastembedSparseDocumentEmbedder,
)
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore
from qdrant_client import QdrantClient


SCRIPT_DIR = Path(__file__).resolve().parent
WEEK3_DIR = SCRIPT_DIR.parents[1]  # week-3/
PROJECT_ROOT = WEEK3_DIR.parent
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
DEFAULT_MANIFEST_FILE = ARTIFACTS_DIR / "selected_files_manifest.json"
WEEK2_MANIFEST_FILE = PROJECT_ROOT / "week-2" / "artifacts" / "selected_files_manifest.json"

# Reuse Week 2 strategy code without modifying week-2 files.
WEEK2_STRATEGY_DIR = PROJECT_ROOT / "week-2" / "scripts" / "strategy"
sys.path.insert(0, str(WEEK2_STRATEGY_DIR))

# Reuse Week 3 metadata mapping as reference.
REF_METADATA_DIR = PROJECT_ROOT / "week3_retrieval" / "indexing"
sys.path.insert(0, str(REF_METADATA_DIR))

from metadata.metadata_schema import match_file_to_category  # type: ignore
from logical_chunker import RecursiveChunker  # type: ignore


COLLECTION_NAME = "week3_hybrid_recursive"
SPARSE_MODEL = "Qdrant/bm25"
OUTPUT_DIR = SCRIPT_DIR / "outputs"

DENSE_CONFIGS: Dict[str, Dict[str, object]] = {
    "voyage": {
        "name": "voyage-4-lite",
        "dimension": 2048,
        "kind": "voyage",
    },
    "bge": {
        "name": "BAAI/bge-large-en-v1.5",
        "dimension": 1024,
        "kind": "fastembed",
    },
}


def _normalize_path(path_text: str) -> str:
    return str(Path(path_text).resolve())


def _resolve_manifest_file_path(path_text: str, manifest_path: Path) -> Path:
    """Resolve manifest file paths robustly across different run directories."""
    raw = Path(path_text)
    if raw.is_absolute():
        return raw

    # Common cases in this repo use relative paths emitted from different working dirs.
    candidates = [
        (PROJECT_ROOT / raw).resolve(),
        (manifest_path.parent / raw).resolve(),
        raw.resolve(),
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    # Fall back to first deterministic candidate for clear error logging upstream.
    return candidates[0]


def load_environment(dense_model_key: str) -> Dict[str, str]:
    load_dotenv(PROJECT_ROOT / ".env")

    required = ["QDRANT_URL", "QDRANT_API_KEY"]
    if dense_model_key == "voyage":
        required.append("VOYAGE_API_KEY")

    for var in required:
        if not os.getenv(var):
            raise ValueError(f"Missing required environment variable: {var}")

    return {
        "qdrant_url": os.getenv("QDRANT_URL", ""),
        "qdrant_api_key": os.getenv("QDRANT_API_KEY", ""),
    }


def load_manifest(manifest_path: Path) -> dict:
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def select_files_from_manifest(manifest_path: Path, test_mode: bool) -> Tuple[List[str], Dict[str, Dict[str, str]]]:
    manifest = load_manifest(manifest_path)

    selected_entries = [e for e in manifest.get("selected_files", []) if e.get("selected", True)]
    if not selected_entries:
        raise ValueError("No selected files found in manifest")

    if test_mode:
        code_entries = [e for e in selected_entries if e.get("content_type") == "code"]
        doc_entries = [e for e in selected_entries if e.get("content_type") != "code"]
        if code_entries:
            selected_entries = code_entries[:5] + doc_entries[:5]
        else:
            # Docs-only corpus fallback: keep a meaningful test sample size.
            selected_entries = doc_entries[:10]

    file_paths = [str(_resolve_manifest_file_path(e["filepath"], manifest_path)) for e in selected_entries]
    metadata_map: Dict[str, Dict[str, str]] = {}
    for e in selected_entries:
        abs_key = str(_resolve_manifest_file_path(e["filepath"], manifest_path))
        metadata_map[abs_key] = {
            "content_type": str(e.get("content_type", "documentation")),
            "source_dir": str(e.get("source_dir", "")),
            "selection_reason": str(e.get("selection_reason", "")),
        }

    print(f"Manifest selected files: {manifest.get('manifest_metadata', {}).get('files_selected', 'unknown')}")
    print(f"Files to process in this run: {len(file_paths)}")
    return file_paths, metadata_map


@component
class Week3MetadataEnricher:
    """Adds file-level metadata and category labels to each chunk."""

    def __init__(self, metadata_map: Dict[str, Dict[str, str]]):
        self.metadata_map = metadata_map

    @component.output_types(documents=List[Document])
    def run(self, documents: List[Document]) -> Dict[str, List[Document]]:
        enriched: List[Document] = []
        for doc in documents:
            raw_path = (
                doc.meta.get("file_path")
                or doc.meta.get("source_path")
                or doc.meta.get("path")
                or ""
            )
            file_path = _normalize_path(str(raw_path)) if raw_path else ""
            extra = self.metadata_map.get(file_path, {})

            if file_path.endswith(".py"):
                file_type = "code"
            elif file_path.endswith(".md"):
                file_type = "markdown"
            else:
                file_type = "text"

            doc.meta.update(
                {
                    "file_path": file_path,
                    "file_type": file_type,
                    "category": match_file_to_category(file_path),
                    "content_type": extra.get("content_type", "documentation"),
                    "source_dir": extra.get("source_dir", ""),
                    "selection_reason": extra.get("selection_reason", ""),
                }
            )
            enriched.append(doc)
        return {"documents": enriched}


def build_dense_embedder(dense_model_key: str):
    dense_conf = DENSE_CONFIGS[dense_model_key]
    if dense_conf["kind"] == "voyage":
        # Lazy import to avoid loading Voyage/transformers stack when using BGE.
        from haystack_integrations.components.embedders.voyage_embedders import VoyageDocumentEmbedder

        return VoyageDocumentEmbedder(
            model=str(dense_conf["name"]),
            output_dimension=int(dense_conf["dimension"]),
        )
    return FastembedDocumentEmbedder(
        model=str(dense_conf["name"]),
        batch_size=32,
        progress_bar=True,
    )


def create_pipeline(
    qdrant_url: str,
    qdrant_api_key: str,
    collection_name: str,
    dense_model_key: str,
    metadata_map: Dict[str, Dict[str, str]],
    recreate_index: bool,
) -> Pipeline:
    dense_conf = DENSE_CONFIGS[dense_model_key]

    document_store = QdrantDocumentStore(
        url=qdrant_url,
        index=collection_name,
        api_key=Secret.from_token(qdrant_api_key),
        embedding_dim=int(dense_conf["dimension"]),
        recreate_index=recreate_index,
        return_embedding=True,
        use_sparse_embeddings=True,
        wait_result_from_api=True,
        timeout=120,
    )

    pipeline = Pipeline()
    pipeline.add_component("file_type_router", FileTypeRouter(mime_types=["text/plain", "text/markdown"]))
    pipeline.add_component("text_converter", TextFileToDocument())
    pipeline.add_component("md_converter", MarkdownToDocument())
    pipeline.add_component("joiner", DocumentJoiner())
    pipeline.add_component(
        "cleaner",
        DocumentCleaner(
            remove_empty_lines=True,
            remove_extra_whitespaces=True,
            remove_repeated_substrings=False,
        ),
    )

    # Week 2 winning chunking strategy reused directly.
    pipeline.add_component("chunker", RecursiveChunker())
    pipeline.add_component("metadata_enricher", Week3MetadataEnricher(metadata_map=metadata_map))
    pipeline.add_component("dense_embedder", build_dense_embedder(dense_model_key))
    pipeline.add_component("sparse_embedder", FastembedSparseDocumentEmbedder(model=SPARSE_MODEL, progress_bar=True))
    pipeline.add_component("writer", DocumentWriter(document_store=document_store))

    pipeline.connect("file_type_router.text/plain", "text_converter.sources")
    pipeline.connect("file_type_router.text/markdown", "md_converter.sources")
    pipeline.connect("text_converter.documents", "joiner.documents")
    pipeline.connect("md_converter.documents", "joiner.documents")
    pipeline.connect("joiner.documents", "cleaner.documents")
    pipeline.connect("cleaner.documents", "chunker.documents")
    pipeline.connect("chunker.documents", "metadata_enricher.documents")
    pipeline.connect("metadata_enricher.documents", "dense_embedder.documents")
    pipeline.connect("dense_embedder.documents", "sparse_embedder.documents")
    pipeline.connect("sparse_embedder.documents", "writer.documents")

    return pipeline


def write_run_report(
    *,
    manifest_file: str,
    collection_name: str,
    dense_model_name: str,
    dense_dimension: int,
    sparse_model: str,
    mode: str,
    manifest_selected_files: Optional[int],
    files_processed: int,
    docs_written: int,
    elapsed_seconds: float,
    points_indexed: int,
    expected_points: Optional[int],
    dense_vectors_populated: bool,
    sparse_vectors_populated: bool,
    sample_metadata_fields: List[str],
) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = OUTPUT_DIR / f"hybrid_indexing_report_{timestamp}.json"

    report = {
        "run_timestamp": timestamp,
        "collection_name": collection_name,
        "vector_configuration": {
            "dense_model": dense_model_name,
            "dense_dimension": dense_dimension,
            "sparse_model": sparse_model,
        },
        "chunking": {
            "strategy": "recursive",
            "source": "week-2/scripts/strategy/logical_chunker.py::RecursiveChunker",
        },
        "inputs": {
            "manifest_file": str(manifest_file),
            "manifest_selected_files": manifest_selected_files,
            "files_processed_this_run": files_processed,
            "mode": mode,
        },
        "outputs": {
            "documents_written": docs_written,
            "elapsed_seconds": round(elapsed_seconds, 3),
            "points_indexed": points_indexed,
            "expected_points": expected_points,
            "point_count_matches_expected": (
                None if expected_points is None else points_indexed == expected_points
            ),
            "dense_vectors_populated": dense_vectors_populated,
            "sparse_vectors_populated": sparse_vectors_populated,
            "sample_metadata_fields": sample_metadata_fields,
        },
        "notes": [
            "Week 3 hybrid re-indexes because sparse BM25 vectors must be materialized in collection points.",
            "Week 2 dense-only collections cannot serve full dense+sparse hybrid retrieval without re-indexing.",
        ],
    }

    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report_path


def _detect_vector_population(point) -> Tuple[bool, bool]:
    dense_present = False
    sparse_present = False

    vectors = getattr(point, "vector", None)
    if isinstance(vectors, dict):
        for val in vectors.values():
            if isinstance(val, list) and len(val) > 0:
                dense_present = True
            if hasattr(val, "indices") and hasattr(val, "values"):
                sparse_present = True
            if isinstance(val, dict) and "indices" in val and "values" in val:
                sparse_present = True
    elif isinstance(vectors, list) and len(vectors) > 0:
        dense_present = True

    sparse_vectors = getattr(point, "sparse_vector", None)
    if sparse_vectors:
        sparse_present = True

    return dense_present, sparse_present


def verify_collection(
    qdrant_url: str,
    qdrant_api_key: str,
    collection_name: str,
    expected_points: Optional[int],
) -> None:
    client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key)
    info = client.get_collection(collection_name=collection_name)
    points_count = int(getattr(info, "points_count", 0) or 0)

    print("\n--- Index Verification ---")
    print(f"Collection: {collection_name}")
    print(f"Points indexed: {points_count}")
    if expected_points is not None:
        if points_count == expected_points:
            print(f"Point count check: PASS (matches expected {expected_points})")
        else:
            print(f"Point count check: WARN (expected {expected_points}, got {points_count})")

    points, _ = client.scroll(
        collection_name=collection_name,
        limit=1,
        with_vectors=True,
        with_payload=True,
    )
    if not points:
        print("Vector presence check: WARN (no points found)")
        return {
            "points_indexed": points_count,
            "dense_vectors_populated": False,
            "sparse_vectors_populated": False,
            "sample_metadata_fields": [],
        }

    dense_ok, sparse_ok = _detect_vector_population(points[0])
    print(f"Dense vectors populated: {'YES' if dense_ok else 'NO'}")
    print(f"Sparse vectors populated: {'YES' if sparse_ok else 'NO'}")

    payload = getattr(points[0], "payload", {}) or {}
    payload_keys = sorted(payload.keys())
    print(f"Metadata fields indexed (sample): {', '.join(payload_keys[:12])}")

    return {
        "points_indexed": points_count,
        "dense_vectors_populated": dense_ok,
        "sparse_vectors_populated": sparse_ok,
        "sample_metadata_fields": payload_keys[:12],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Week 3 hybrid indexing (dense + BM25 sparse)")
    parser.add_argument("--collection", default=COLLECTION_NAME, help="Qdrant collection name")
    parser.add_argument("--dense-model", choices=list(DENSE_CONFIGS.keys()), default="voyage")
    parser.add_argument(
        "--manifest",
        type=str,
        default=None,
        help="Optional path to selected_files_manifest.json",
    )
    parser.add_argument("--test", action="store_true", help="Index small balanced sample")
    parser.add_argument("--full", action="store_true", help="Index full selected manifest")
    parser.add_argument("--expected-points", type=int, default=None, help="Optional expected point count for validation")
    parser.add_argument("--recreate", action="store_true", help="Recreate collection before indexing (destructive for that collection)")
    args = parser.parse_args()

    test_mode = not args.full
    if args.full and args.test:
        raise ValueError("Use only one of --test or --full")

    dense_conf = DENSE_CONFIGS[args.dense_model]
    env = load_environment(args.dense_model)
    if args.manifest:
        manifest_file = Path(args.manifest)
    elif WEEK2_MANIFEST_FILE.exists():
        manifest_file = WEEK2_MANIFEST_FILE
    else:
        manifest_file = DEFAULT_MANIFEST_FILE

    manifest = load_manifest(manifest_file)
    files_to_process, metadata_map = select_files_from_manifest(manifest_file, test_mode=test_mode)

    print("\n=== Week 3 Hybrid Indexing ===")
    print(f"Collection: {args.collection}")
    print(f"Dense model: {dense_conf['name']} ({dense_conf['dimension']}d)")
    print(f"Sparse model: {SPARSE_MODEL}")
    print("Chunker: recursive (Week 2 winner)")
    print("Chunking lineage: Week 2 optimized, non-naive")
    print(f"Mode: {'TEST' if test_mode else 'FULL'}")

    pipeline = create_pipeline(
        qdrant_url=env["qdrant_url"],
        qdrant_api_key=env["qdrant_api_key"],
        collection_name=args.collection,
        dense_model_key=args.dense_model,
        metadata_map=metadata_map,
        recreate_index=args.recreate,
    )

    start = time.time()
    result = pipeline.run(data={"file_type_router": {"sources": files_to_process}})
    elapsed = time.time() - start
    docs_written = int(result.get("writer", {}).get("documents_written", 0))

    print("\n=== Indexing Complete ===")
    print(f"Documents/chunks written: {docs_written}")
    print(f"Elapsed seconds: {elapsed:.2f}")

    verification = verify_collection(
        qdrant_url=env["qdrant_url"],
        qdrant_api_key=env["qdrant_api_key"],
        collection_name=args.collection,
        expected_points=args.expected_points,
    )

    report_file = write_run_report(
        manifest_file=str(manifest_file),
        collection_name=args.collection,
        dense_model_name=str(dense_conf["name"]),
        dense_dimension=int(dense_conf["dimension"]),
        sparse_model=SPARSE_MODEL,
        mode="TEST" if test_mode else "FULL",
        manifest_selected_files=manifest.get("manifest_metadata", {}).get("files_selected"),
        files_processed=len(files_to_process),
        docs_written=docs_written,
        elapsed_seconds=elapsed,
        points_indexed=int(verification["points_indexed"]),
        expected_points=args.expected_points,
        dense_vectors_populated=bool(verification["dense_vectors_populated"]),
        sparse_vectors_populated=bool(verification["sparse_vectors_populated"]),
        sample_metadata_fields=list(verification["sample_metadata_fields"]),
    )
    print(f"Run report: {report_file}")


if __name__ == "__main__":
    main()
