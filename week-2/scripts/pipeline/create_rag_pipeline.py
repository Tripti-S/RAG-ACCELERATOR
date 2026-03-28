# This script creates a RAG pipeline for evaluation.
# Update input/output paths to use week-1/data/processed/ as the data source.
# ...existing code from week2_chunking/experiments/03_create_rag_pipeline.py will be adapted here...
# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 2: Create RAG Query Pipeline
==================================

Creates RAG pipeline for querying any Week 2 chunking strategy collection.
Keeps retrieval settings constant across all strategies for fair comparison.

Pipeline:
- Query Embedder (FastEmbed/Voyage) → Retriever (Qdrant) → Prompt Builder → Generator (Gemini)

Embedder auto-detection:
- Collections ending with '_voyage' use Voyage text embedder
- All other collections use FastEmbed (BGE)

Prerequisites:
- Google Cloud account with $300 free credit (covers entire course)
- GOOGLE_API_KEY in .env
- VOYAGE_API_KEY in .env (for Voyage embeddings)

Adapted from phase2_chunking/03_create_rag_pipeline.py
"""

import os
from pathlib import Path
from dotenv import load_dotenv

from haystack import Pipeline
from haystack.components.builders import ChatPromptBuilder
from haystack.dataclasses import ChatMessage
from haystack_integrations.components.embedders.fastembed import FastembedTextEmbedder
from haystack_integrations.components.retrievers.qdrant import QdrantEmbeddingRetriever
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore
from haystack_integrations.components.generators.google_genai import GoogleGenAIChatGenerator
from haystack.utils import Secret


# Path resolution - works when run from any directory
SCRIPT_DIR = Path(__file__).resolve().parent      # scripts/
WEEK2_DIR = SCRIPT_DIR.parent                     # week-2/
PROJECT_ROOT = WEEK2_DIR.parent                   # rag-capstone-week-2/

# Default model - Gemini 2.5 Flash (best balance of speed/quality/cost)
DEFAULT_MODEL = "gemini-2.5-flash"

# Embedder configurations (must match 01_create_chunking_pipeline.py)
EMBEDDER_CONFIGS = {
    "bge": {
        "name": "BGE-large-en-v1.5 (FastEmbed)",
        "dimension": 1024,
        "type": "fastembed"
    },
    "minilm": {
        "name": "all-MiniLM-L6-v2",
        "dimension": 384,
        "type": "fastembed"
    },
    "voyage": {
        "name": "Voyage-4-lite (API)",
        "model": "voyage-4-lite",
        "dimension": 2048,
        "type": "voyage"
    }
}


def detect_embedder_from_collection(collection_name: str) -> str:
    """Auto-detect embedder type from collection name suffix."""
    if collection_name.endswith("_voyage"):
        return "voyage"
    return "bge"


def create_text_embedder(embedder_type: str = "bge"):
    """
    Factory function to create the appropriate text embedder for queries.

    Args:
        embedder_type: "bge" for FastEmbed BGE, "voyage" for Voyage API

    Returns:
        Tuple[text_embedder_component, dimension]
    """
    config = EMBEDDER_CONFIGS.get(embedder_type)
    if not config:
        raise ValueError(f"Unknown embedder type: {embedder_type}")

    if embedder_type == "voyage":
        from haystack_integrations.components.embedders.voyage_embedders import VoyageTextEmbedder
        embedder = VoyageTextEmbedder(
            model=config["model"],
            output_dimension=config["dimension"],
        )
        print(f"🚀 Using Voyage text embedder: {config['model']} ({config['dimension']}d)")
    else:
        # Use correct model for each embedder type
        if embedder_type == "minilm":
            model_name = "sentence-transformers/all-MiniLM-L6-v2"
        else:
            model_name = os.getenv("FASTEMBED_MODEL", "BAAI/bge-large-en-v1.5")
        embedder = FastembedTextEmbedder(
            model=model_name,
            progress_bar=False
        )
        print(f"🚀 Using FastEmbed text embedder: {config['name']}")

    return embedder, config["dimension"]


def load_environment():
    """Load environment variables from .env file."""
    env_path = PROJECT_ROOT / ".env"
    load_dotenv(env_path)

    required_vars = [
        "QDRANT_URL",
        "QDRANT_API_KEY",
        "GOOGLE_API_KEY",
        "FASTEMBED_MODEL",
        "EMBEDDING_DIMENSION"
    ]

    for var in required_vars:
        if not os.getenv(var):
            raise ValueError(f"Missing required environment variable: {var}")

    return {
        "qdrant_url": os.getenv("QDRANT_URL"),
        "qdrant_api_key": os.getenv("QDRANT_API_KEY"),
        "google_api_key": os.getenv("GOOGLE_API_KEY"),
        "fastembed_model": os.getenv("FASTEMBED_MODEL", "BAAI/bge-large-en-v1.5"),
        "embedding_dimension": int(os.getenv("EMBEDDING_DIMENSION", "1024")),
    }


def create_rag_pipeline(collection_name: str, model: str = None, embedder_type: str = None):
    """
    Create RAG pipeline for querying a specific collection.

    Args:
        collection_name: Qdrant collection to query
        model: Gemini model to use (default: gemini-2.5-flash)
        embedder_type: "bge" or "voyage" (auto-detected from collection name if None)

    Returns:
        Pipeline: Configured RAG pipeline
        dict: Environment configuration
    """
    env_config = load_environment()
    model = model or DEFAULT_MODEL


    # Force hybrid collection to always use minilm embedder (384d)
    if collection_name == "week2_hybrid":
        embedder_type = "minilm"
    elif embedder_type is None:
        embedder_type = detect_embedder_from_collection(collection_name)

    print(f"🔧 Creating RAG pipeline for collection: {collection_name}")
    print(f"🧠 Embedder: {EMBEDDER_CONFIGS[embedder_type]['name']}")

    # Get embedding dimension for this embedder
    embedding_dim = EMBEDDER_CONFIGS[embedder_type]["dimension"]

    # Create Qdrant document store (connect to existing)
    document_store = QdrantDocumentStore(
        url=env_config["qdrant_url"],
        index=collection_name,
        api_key=Secret.from_env_var("QDRANT_API_KEY"),
        embedding_dim=embedding_dim,
        recreate_index=False,  # Connect to existing
        return_embedding=False,
        wait_result_from_api=True
    )
    doc_count = document_store.count_documents()
    print(f"✅ Connected to Qdrant - {doc_count} documents")

    # Create RAG pipeline
    pipeline = Pipeline()

    # 1. Query Embedder - must match embedder used for indexing
    text_embedder, _ = create_text_embedder(embedder_type)
    # Only warm up FastEmbed embedder (Voyage doesn't need/have warm_up)
    if embedder_type == "bge":
        print("   Warming up text embedder...")
        text_embedder.warm_up()
    pipeline.add_component("text_embedder", text_embedder)

    # Update env_config with embedder info
    env_config['embedder_type'] = embedder_type
    env_config['embedding_dimension'] = embedding_dim

    # 2. Retriever - retrieve top 10 chunks (consistent across all strategies)
    pipeline.add_component(
        "retriever",
        QdrantEmbeddingRetriever(
            document_store=document_store,
            top_k=10  # Fixed retrieval count for fair comparison
        )
    )

    # 3. Chat Prompt Builder - RAG prompt template
    template = [
        ChatMessage.from_system("You are an expert assistant for the Model Context Protocol (MCP). Use the provided context to answer questions about MCP implementation and concepts. Provide accurate, practical answers based on the context."),
        ChatMessage.from_user("""Context:
{% for document in documents %}
{{ document.content }}
---
{% endfor %}

Question: {{ question }}""")
    ]

    pipeline.add_component(
        "prompt_builder",
        ChatPromptBuilder(template=template, required_variables=["documents", "question"])
    )

    # 4. LLM Generator - Gemini
    pipeline.add_component(
        "llm",
        GoogleGenAIChatGenerator(model=model)
    )

    # Connect pipeline
    pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
    pipeline.connect("retriever.documents", "prompt_builder.documents")
    pipeline.connect("prompt_builder.prompt", "llm.messages")

    print(f"✅ RAG pipeline created for: {collection_name}")
    print(f"🤖 Model: {model}")

    # Add model to config for reference
    env_config["model"] = model

    return pipeline, env_config


def query_rag_pipeline(pipeline: Pipeline, question: str):
    """
    Query RAG pipeline with a question.

    Args:
        pipeline: Configured RAG pipeline
        question: User question

    Returns:
        dict: Query results with answer and retrieved contexts
    """
    result = pipeline.run(
        data={
            "text_embedder": {"text": question},
            "prompt_builder": {"question": question}
        },
        include_outputs_from={"retriever", "llm"}
    )

    # Extract results
    answer = result["llm"]["replies"][0].text if result["llm"]["replies"] else ""
    retrieved_docs = result["retriever"]["documents"]

    return {
        "question": question,
        "answer": answer,
        "retrieved_documents": retrieved_docs,
        "num_retrieved": len(retrieved_docs)
    }


def main():
    """Test RAG pipeline creation with CLI args."""
    import argparse
    parser = argparse.ArgumentParser(description="Create RAG pipeline for a Qdrant collection.")
    parser.add_argument("--collection", type=str, required=True, help="Qdrant collection name to query")
    parser.add_argument("--embedder", type=str, choices=list(EMBEDDER_CONFIGS.keys()), default=None, help="Embedder type to use (bge, minilm, voyage). If not set, auto-detect from collection name.")
    parser.add_argument("--model", type=str, default=None, help="Gemini model to use (default: gemini-2.5-flash)")
    args = parser.parse_args()

    try:
        pipeline, env_config = create_rag_pipeline(
            collection_name=args.collection,
            model=args.model,
            embedder_type=args.embedder
        )

        print("\n" + "="*60)
        print("📋 RAG PIPELINE TEST")
        print("="*60)
        print(f"✅ Pipeline created successfully")
        print(f"🧠 Embedder: {EMBEDDER_CONFIGS[env_config['embedder_type']]['name']}")
        print(f"🔢 Dimensions: {env_config['embedding_dimension']}")
        print(f"🤖 Model: {env_config['model']}")
        print(f"📊 Components: {len(pipeline.graph.nodes)}")

        print("\n🔧 Pipeline components:")
        for i, component_name in enumerate(pipeline.graph.nodes, 1):
            print(f"   {i}. {component_name}")

    except Exception as e:
        print(f"❌ Pipeline creation failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
