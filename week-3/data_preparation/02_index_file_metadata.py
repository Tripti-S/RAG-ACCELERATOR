import argparse
import json
import os
import sys
import uuid
from pathlib import Path
from typing import Dict

from dotenv import load_dotenv
from haystack import Document
from haystack_integrations.components.embedders.fastembed import FastembedDocumentEmbedder
from haystack_integrations.components.embedders.voyage_embedders import VoyageDocumentEmbedder
from qdrant_client import QdrantClient, models


SCRIPT_DIR = Path(__file__).resolve().parent
WEEK3_DIR = SCRIPT_DIR.parent
PROJECT_ROOT = WEEK3_DIR.parent
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

COLLECTION_NAME = "week3_file_metadata"
VOYAGE_MODEL = "voyage-4-lite"
VOYAGE_DIMENSION = 2048
FASTEMBED_MODEL = "BAAI/bge-small-en-v1.5"
FASTEMBED_DIMENSION = 384
METADATA_FILE = SCRIPT_DIR / "outputs" / "file_metadata.json"
MANIFEST_FILE = ARTIFACTS_DIR / "selected_files_manifest.json"


def load_environment() -> Dict[str, str]:
    load_dotenv(PROJECT_ROOT / ".env")
    required = ["QDRANT_URL", "QDRANT_API_KEY"]
    for key in required:
        if not os.getenv(key):
            raise ValueError(f"Missing {key} in .env")
    return {
        "qdrant_url": os.getenv("QDRANT_URL", ""),
        "qdrant_api_key": os.getenv("QDRANT_API_KEY", ""),
    }


def load_file_metadata() -> Dict[str, Dict]:
    if not METADATA_FILE.exists():
        raise FileNotFoundError(f"Metadata file not found: {METADATA_FILE}")
    data = json.loads(METADATA_FILE.read_text(encoding="utf-8"))
    return data.get("files", {})


def normalize_manifest_entry(path_text: str) -> str:
    normalized_text = path_text.replace("\\", "/")

    if "week-1/data/processed/" in normalized_text:
        suffix = normalized_text.split("week-1/data/processed/", 1)[1]
        fixed = (PROJECT_ROOT / "week-1" / "data" / "processed" / suffix).resolve()
        return str(fixed)

    p = Path(path_text)
    if p.is_absolute():
        return str(p.resolve())
    return str((PROJECT_ROOT / p).resolve())


def get_allowed_files_from_manifest() -> set:
    if not MANIFEST_FILE.exists():
        return set()
    data = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
    allowed = set()
    for entry in data.get("selected_files", []):
        if entry.get("selected"):
            allowed.add(normalize_manifest_entry(entry["filepath"]))
    return allowed


def create_searchable_text(metadata: Dict) -> str:
    parts = []
    if metadata.get("summary"):
        parts.append(metadata["summary"])
    if metadata.get("file_type"):
        parts.append(f"Type: {metadata['file_type']}")
    if metadata.get("content_type"):
        parts.append(f"Content: {metadata['content_type']}")
    concepts = metadata.get("domain_concepts", [])
    if concepts:
        parts.append("Concepts: " + ", ".join(concepts[:20]))
    topics = metadata.get("primary_topics", [])
    if topics:
        parts.append("Topics: " + ", ".join(topics[:20]))
    return " | ".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(description="Index file metadata for Week 3 two-stage routing")
    parser.add_argument("--recreate", action="store_true", help="delete and recreate collection")
    parser.add_argument("--embedder", choices=["fastembed", "voyage"], default="fastembed", help="embedding provider")
    args = parser.parse_args()

    cfg = load_environment()
    file_metadata = load_file_metadata()
    allowed = get_allowed_files_from_manifest()

    if allowed:
        file_metadata = {k: v for k, v in file_metadata.items() if str(Path(k).resolve()) in allowed}

    if not file_metadata:
        raise ValueError("No file metadata entries available to index")

    client = QdrantClient(url=cfg["qdrant_url"], api_key=cfg["qdrant_api_key"])

    exists = any(c.name == COLLECTION_NAME for c in client.get_collections().collections)
    if exists and args.recreate:
        client.delete_collection(COLLECTION_NAME)
        exists = False

    if exists and not args.recreate:
        print(f"Collection already exists: {COLLECTION_NAME}. Use --recreate to rebuild.")
        return

    if args.embedder == "voyage":
        if not os.getenv("VOYAGE_API_KEY"):
            raise ValueError("Missing VOYAGE_API_KEY in .env for --embedder voyage")
        vector_size = VOYAGE_DIMENSION
        embedder = VoyageDocumentEmbedder(model=VOYAGE_MODEL, output_dimension=VOYAGE_DIMENSION)
    else:
        vector_size = FASTEMBED_DIMENSION
        embedder = FastembedDocumentEmbedder(model=FASTEMBED_MODEL)

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
    )

    docs = []
    for file_path, metadata in file_metadata.items():
        docs.append(
            Document(
                id=file_path,
                content=create_searchable_text(metadata),
                meta={
                    "file_path": file_path,
                    "summary": metadata.get("summary", ""),
                    "file_type": metadata.get("file_type", ""),
                    "content_type": metadata.get("content_type", ""),
                    "domain_concepts": metadata.get("domain_concepts", []),
                    "primary_topics": metadata.get("primary_topics", []),
                    "code_examples": metadata.get("code_examples", False),
                    "searchable_keywords": metadata.get("searchable_keywords", []),
                    "can_answer_questions": metadata.get("can_answer_questions", []),
                },
            )
        )

    embedded_docs = embedder.run(documents=docs)["documents"]
    points = []
    for doc in embedded_docs:
        try:
            point_id = str(uuid.UUID(doc.id))
        except ValueError:
            point_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, doc.id))
        points.append(
            models.PointStruct(
                id=point_id,
                vector=doc.embedding,
                payload={
                    "file_path": doc.meta["file_path"],
                    "summary": doc.meta["summary"],
                    "file_type": doc.meta["file_type"],
                    "content_type": doc.meta["content_type"],
                    "domain_concepts": doc.meta["domain_concepts"],
                    "primary_topics": doc.meta["primary_topics"],
                    "code_examples": doc.meta["code_examples"],
                    "searchable_keywords": doc.meta["searchable_keywords"],
                    "can_answer_questions": doc.meta["can_answer_questions"],
                },
            )
        )

    client.upsert(collection_name=COLLECTION_NAME, points=points, wait=True)
    info = client.get_collection(COLLECTION_NAME)
    print(f"Indexed metadata documents: {info.points_count}")
    print(f"Collection: {COLLECTION_NAME}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
