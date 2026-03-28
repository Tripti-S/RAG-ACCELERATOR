from __future__ import annotations

import argparse
import json
import os
import time
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from haystack import Pipeline
from haystack.components.builders import ChatPromptBuilder
from haystack.dataclasses import ChatMessage
from haystack_integrations.components.embedders.fastembed import (
    FastembedSparseTextEmbedder,
)
from haystack_integrations.components.embedders.voyage_embedders import VoyageTextEmbedder
from haystack_integrations.components.generators.google_genai import GoogleGenAIChatGenerator

from components.qdrant_hybrid_retriever import QdrantHybridRetriever
from components.voyage_reranker import VoyageReranker


SCRIPT_DIR = Path(__file__).resolve().parent
WEEK3_DIR = SCRIPT_DIR.parents[1]
PROJECT_ROOT = SCRIPT_DIR.parents[2]


def load_env() -> dict[str, str]:
    load_dotenv(PROJECT_ROOT / ".env")

    required = ["QDRANT_URL", "QDRANT_API_KEY", "GOOGLE_API_KEY", "VOYAGE_API_KEY"]
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")

    return {
        "qdrant_url": os.environ["QDRANT_URL"],
        "qdrant_api_key": os.environ["QDRANT_API_KEY"],
        "gemini_model": os.getenv("LLM_MODEL", "gemini-2.5-flash"),
        "voyage_api_key": os.environ["VOYAGE_API_KEY"],
    }


def load_questions() -> list[dict]:
    question_file = PROJECT_ROOT / "artifacts" / "human_eval_questions.json"
    if not question_file.exists():
        raise FileNotFoundError(f"Questions file not found: {question_file}")

    with question_file.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    if not isinstance(payload, dict) or "questions" not in payload:
        raise ValueError("artifacts/human_eval_questions.json must contain a top-level 'questions' field")
    return payload["questions"]


def build_pipeline(
    env: dict[str, str],
    *,
    collection_name: str,
    dense_model: str,
    dense_dimension: int,
    sparse_model: str,
    prefetch_k: int,
    rerank_k: int,
    rerank_model: str,
) -> Pipeline:
    pipeline = Pipeline()

    dense_embedder = VoyageTextEmbedder(model=dense_model, output_dimension=dense_dimension)
    sparse_embedder = FastembedSparseTextEmbedder(model=sparse_model)
    sparse_embedder.warm_up()

    retriever = QdrantHybridRetriever(
        url=env["qdrant_url"],
        api_key=env["qdrant_api_key"],
        collection_name=collection_name,
        top_k=prefetch_k,
        dense_prefetch_limit=100,
        sparse_prefetch_limit=100,
    )
    retriever.warm_up()

    reranker = VoyageReranker(
        model=rerank_model,
        top_k=rerank_k,
        api_key=env["voyage_api_key"],
    )
    reranker.warm_up()

    template = [
        ChatMessage.from_system(
            "You are an assistant for probability and statistics coursework. "
            "Use only the provided context. If context is insufficient, say so clearly."
        ),
        ChatMessage.from_user(
            """Context:
{% for document in documents %}
{{ document.content }}
---
{% endfor %}

Question: {{ question }}"""
        ),
    ]

    pipeline.add_component("dense_embedder", dense_embedder)
    pipeline.add_component("sparse_embedder", sparse_embedder)
    pipeline.add_component("retriever", retriever)
    pipeline.add_component("reranker", reranker)
    pipeline.add_component(
        "prompt_builder",
        ChatPromptBuilder(template=template, required_variables=["documents", "question"]),
    )
    pipeline.add_component("llm", GoogleGenAIChatGenerator(model=env["gemini_model"]))

    pipeline.connect("dense_embedder.embedding", "retriever.query_embedding")
    pipeline.connect("sparse_embedder.sparse_embedding", "retriever.query_sparse_embedding")
    pipeline.connect("retriever.documents", "reranker.documents")
    pipeline.connect("reranker.documents", "prompt_builder.documents")
    pipeline.connect("prompt_builder.prompt", "llm.messages")

    return pipeline


def run_experiment(args: argparse.Namespace) -> Path:
    env = load_env()
    questions = load_questions()
    pipeline = build_pipeline(
        env,
        collection_name=args.collection,
        dense_model=args.dense_model,
        dense_dimension=args.dense_dim,
        sparse_model=args.sparse_model,
        prefetch_k=args.prefetch_k,
        rerank_k=args.rerank_k,
        rerank_model=args.rerank_model,
    )

    output_dir = WEEK3_DIR / "rag_results"
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = output_dir / f"week3_hybrid_rerank_baseline_{timestamp}.json"

    rows: list[dict] = []
    start = time.time()

    for index, q in enumerate(questions, start=1):
        question_text = q.get("user_input") or q.get("question")
        question_id = q.get("question_id", index - 1)
        if not question_text:
            continue

        result = pipeline.run(
            data={
                "dense_embedder": {"text": question_text},
                "sparse_embedder": {"text": question_text},
                "reranker": {"query": question_text},
                "prompt_builder": {"question": question_text},
            },
            include_outputs_from={"reranker", "llm"},
        )

        docs = result["reranker"]["documents"]
        answer = result["llm"]["replies"][0].text if result["llm"]["replies"] else ""

        rows.append(
            {
                "question_id": question_id,
                "user_input": question_text,
                "retrieved_contexts": [
                    {
                        "rank": rank,
                        "score": float(doc.score) if doc.score is not None else 0.0,
                        "content": doc.content,
                        "metadata": {
                            "file_path": (doc.meta or {}).get("file_path", "unknown"),
                            "category": (doc.meta or {}).get("category", "unknown"),
                            "file_type": (doc.meta or {}).get("file_type", "unknown"),
                        },
                    }
                    for rank, doc in enumerate(docs, start=1)
                ],
                "generated_answer": answer,
                "reference_answer": q.get("reference", ""),
                "reference_contexts": q.get("reference_contexts", []),
                "num_contexts_retrieved": len(docs),
            }
        )

    payload = {
        "technique": "Week 3 baseline: hybrid retrieval + reranking",
        "collection": args.collection,
        "dense_model": args.dense_model,
        "dense_dimension": args.dense_dim,
        "sparse_model": args.sparse_model,
        "reranker_model": args.rerank_model,
        "llm_model": env["gemini_model"],
        "prefetch_k": args.prefetch_k,
        "rerank_k": args.rerank_k,
        "questions_processed": len(rows),
        "total_time_seconds": round(time.time() - start, 2),
        "generated_at": datetime.now().isoformat(),
        "results": rows,
    }

    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)

    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run Week 3 hybrid + rerank baseline and generate rag_results JSON."
    )
    parser.add_argument("--collection", default="week3_hybrid_recursive")
    parser.add_argument("--dense-model", default="voyage-4-lite")
    parser.add_argument("--dense-dim", type=int, default=2048)
    parser.add_argument("--sparse-model", default="Qdrant/bm25")
    parser.add_argument("--prefetch-k", type=int, default=50)
    parser.add_argument("--rerank-k", type=int, default=10)
    parser.add_argument("--rerank-model", default="rerank-2.5")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    result_file = run_experiment(args)
    print(f"Saved results to: {result_file}")
