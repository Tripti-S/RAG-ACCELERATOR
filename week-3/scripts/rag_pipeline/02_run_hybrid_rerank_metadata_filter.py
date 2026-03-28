from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from haystack import Pipeline
from haystack.components.builders import ChatPromptBuilder
from haystack.dataclasses import ChatMessage
from haystack_integrations.components.embedders.fastembed import FastembedSparseTextEmbedder
from haystack_integrations.components.embedders.voyage_embedders import VoyageTextEmbedder
from haystack_integrations.components.generators.google_genai import GoogleGenAIChatGenerator

SCRIPT_DIR = Path(__file__).resolve().parent
WEEK3_DIR = SCRIPT_DIR.parents[1]
PROJECT_ROOT = SCRIPT_DIR.parents[2]

if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from components.document_filters import CategoryDocumentFilter
from components.qdrant_hybrid_retriever import QdrantHybridRetriever
from components.voyage_reranker import VoyageReranker


def load_env() -> dict[str, str]:
    load_dotenv(PROJECT_ROOT / ".env")
    required = ["QDRANT_URL", "QDRANT_API_KEY", "GOOGLE_API_KEY", "VOYAGE_API_KEY"]
    missing = [k for k in required if not os.getenv(k)]
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
    return {
        "qdrant_url": os.environ["QDRANT_URL"],
        "qdrant_api_key": os.environ["QDRANT_API_KEY"],
        "voyage_api_key": os.environ["VOYAGE_API_KEY"],
        "llm_model": os.getenv("LLM_MODEL", "gemini-2.5-flash"),
    }


def load_questions() -> list[dict]:
    p = PROJECT_ROOT / "artifacts" / "human_eval_questions.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    return data["questions"]


def map_query_to_categories(query: str) -> list[str]:
    q = query.lower()
    categories: list[str] = []
    if any(k in q for k in ["bayes", "probability", "independence", "conditional"]):
        categories.append("probability_rules")
    if any(k in q for k in ["distribution", "binomial", "poisson", "geometric", "normal"]):
        categories.append("distributions")
    if not categories:
        categories.append("general")
    return categories


def build_pipeline(env: dict[str, str]) -> Pipeline:
    pipe = Pipeline()
    pipe.add_component("dense", VoyageTextEmbedder(model="voyage-4-lite", output_dimension=2048))
    sparse = FastembedSparseTextEmbedder(model="Qdrant/bm25")
    sparse.warm_up()
    pipe.add_component("sparse", sparse)
    retriever = QdrantHybridRetriever(
        url=env["qdrant_url"],
        api_key=env["qdrant_api_key"],
        collection_name="week3_hybrid_recursive",
        top_k=50,
        dense_prefetch_limit=100,
        sparse_prefetch_limit=100,
    )
    retriever.warm_up()
    pipe.add_component("retriever", retriever)
    pipe.add_component("category_filter", CategoryDocumentFilter())
    reranker = VoyageReranker(model="rerank-2.5", top_k=10, api_key=env["voyage_api_key"])
    reranker.warm_up()
    pipe.add_component("reranker", reranker)

    template = [
        ChatMessage.from_system("Use only provided context to answer probability/statistics questions."),
        ChatMessage.from_user(
            """Context:
{% for document in documents %}
{{ document.content }}
---
{% endfor %}

Question: {{ question }}"""
        ),
    ]
    pipe.add_component("prompt", ChatPromptBuilder(template=template, required_variables=["documents", "question"]))
    pipe.add_component("llm", GoogleGenAIChatGenerator(model=env["llm_model"]))
    pipe.connect("dense.embedding", "retriever.query_embedding")
    pipe.connect("sparse.sparse_embedding", "retriever.query_sparse_embedding")
    pipe.connect("retriever.documents", "category_filter.documents")
    pipe.connect("category_filter.documents", "reranker.documents")
    pipe.connect("reranker.documents", "prompt.documents")
    pipe.connect("prompt.prompt", "llm.messages")
    return pipe


def main() -> None:
    env = load_env()
    questions = load_questions()
    pipe = build_pipeline(env)
    out_rows: list[dict] = []

    for idx, q in enumerate(questions, start=1):
        text = q.get("user_input") or q.get("question")
        if not text:
            continue
        categories = map_query_to_categories(text)
        result = pipe.run(
            data={
                "dense": {"text": text},
                "sparse": {"text": text},
                "category_filter": {"categories": categories},
                "reranker": {"query": text},
                "prompt": {"question": text},
            },
            include_outputs_from={"reranker", "llm"},
        )
        docs = result["reranker"]["documents"]
        answer = result["llm"]["replies"][0].text if result["llm"]["replies"] else ""
        out_rows.append(
            {
                "question_id": q.get("question_id", idx - 1),
                "user_input": text,
                "retrieved_contexts": [
                    {
                        "rank": r,
                        "score": float(d.score) if d.score is not None else 0.0,
                        "content": d.content,
                        "metadata": {
                            "file_path": (d.meta or {}).get("file_path", "unknown"),
                            "category": (d.meta or {}).get("category", "unknown"),
                            "file_type": (d.meta or {}).get("file_type", "unknown"),
                        },
                    }
                    for r, d in enumerate(docs, start=1)
                ],
                "generated_answer": answer,
                "reference_answer": q.get("reference", ""),
                "reference_contexts": q.get("reference_contexts", []),
                "num_contexts_retrieved": len(docs),
            }
        )

    payload = {
        "technique": "Week 3 hybrid + rerank + metadata filtering",
        "collection": "week3_hybrid_recursive",
        "dense_model": "voyage-4-lite",
        "dense_dimension": 2048,
        "sparse_model": "Qdrant/bm25",
        "reranker_model": "rerank-2.5",
        "llm_model": env["llm_model"],
        "prefetch_k": 50,
        "rerank_k": 10,
        "questions_processed": len(out_rows),
        "results": out_rows,
    }

    out_file = WEEK3_DIR / "rag_results" / "week3_hybrid_rerank_metadata_filter_results.json"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Saved results to: {out_file}")


if __name__ == "__main__":
    main()
