# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 2: Create Chunking Pipeline with Custom Strategy
======================================================

Generic pipeline builder that accepts any chunking strategy component.
Creates indexing pipeline using:
- File routing → Converters → Joiner → Cleaner → CUSTOM CHUNKER → Embedder → Writer

This allows us to test different chunking strategies while keeping
everything else constant (same embeddings, same storage, same data).
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from typing import Any, List, Dict

# Path resolution - works when run from any directory
SCRIPT_DIR = Path(__file__).resolve().parent      # experiments/
WEEK_DIR = SCRIPT_DIR.parent                       # week2_chunking/
PROJECT_ROOT = WEEK_DIR.parent                     # rag-workshop-classroom/

# Add week2_chunking to path for strategy imports
sys.path.insert(0, str(WEEK_DIR))

# Haystack core imports
from haystack import Pipeline, Document
from haystack.components.converters import MarkdownToDocument, TextFileToDocument
from haystack.components.preprocessors import DocumentCleaner
from haystack.components.routers import FileTypeRouter
from haystack.components.joiners import DocumentJoiner
from haystack.components.writers import DocumentWriter

# FastEmbed import
from haystack_integrations.components.embedders.fastembed import FastembedDocumentEmbedder

# Qdrant import
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore
from haystack.utils import Secret


# Token estimation constants for truncation warning
# BGE-large uses BERT tokenizer: ~1.3 tokens per word for English
TOKENS_PER_WORD = 1.3
BGE_MAX_TOKENS = 512
VOYAGE_MAX_TOKENS = 32000  # Voyage-4-lite supports 32K tokens


# Embedder configurations
EMBEDDER_CONFIGS = {
    "bge": {
        "name": "BGE-large-en-v1.5 (FastEmbed)",
        "dimension": 1024,
        "max_tokens": 512,
        "type": "fastembed"
    },
    "voyage": {
        "name": "Voyage-4-lite (API)",
        "model": "voyage-4-lite",
        "dimension": 2048,
        "max_tokens": 32000,
        "type": "voyage"
    }
}


def load_environment():
    """Load environment variables for Qdrant connection."""
    # Load from project root .env
    env_path = PROJECT_ROOT / ".env"
    load_dotenv(env_path)

    required_vars = [
        "QDRANT_URL",
        "QDRANT_API_KEY",
        "FASTEMBED_MODEL",
        "EMBEDDING_DIMENSION"
    ]

    for var in required_vars:
        if not os.getenv(var):
            raise ValueError(f"Missing required environment variable: {var}")

    return {
        "qdrant_url": os.getenv("QDRANT_URL"),
        "qdrant_api_key": os.getenv("QDRANT_API_KEY"),
        "fastembed_model": os.getenv("FASTEMBED_MODEL", "BAAI/bge-large-en-v1.5"),
        "embedding_dimension": int(os.getenv("EMBEDDING_DIMENSION", "1024")),
        "batch_size": int(os.getenv("FASTEMBED_BATCH_SIZE", "32"))
    }


def estimate_tokens(text: str) -> int:
    """
    Estimate token count for text.

    Uses word count × 1.3 as approximation for BERT tokenizers.
    This is conservative - actual token count may be slightly higher.
    """
    word_count = len(text.split())
    return int(word_count * TOKENS_PER_WORD)


def analyze_chunk_truncation(documents: List[Document], max_tokens: int = BGE_MAX_TOKENS) -> Dict[str, Any]:
    """
    Analyze how many chunks would be truncated by the embedding model.

    Args:
        documents: List of chunked documents
        max_tokens: Maximum tokens the embedding model accepts (default: 512 for BGE)

    Returns:
        Dict with truncation statistics
    """
    truncated_count = 0
    total_tokens_lost = 0
    max_chunk_tokens = 0
    token_counts = []

    for doc in documents:
        tokens = estimate_tokens(doc.content)
        token_counts.append(tokens)
        max_chunk_tokens = max(max_chunk_tokens, tokens)

        if tokens > max_tokens:
            truncated_count += 1
            total_tokens_lost += (tokens - max_tokens)

    avg_tokens = sum(token_counts) / len(token_counts) if token_counts else 0

    return {
        "total_chunks": len(documents),
        "truncated_count": truncated_count,
        "truncation_percentage": (truncated_count / len(documents) * 100) if documents else 0,
        "total_tokens_lost": total_tokens_lost,
        "max_chunk_tokens": max_chunk_tokens,
        "avg_chunk_tokens": avg_tokens,
        "model_max_tokens": max_tokens
    }


def print_truncation_warning(stats: Dict[str, Any], strategy_name: str, embedder_type: str = "bge"):
    """
    Print a clear warning about token truncation.

    Args:
        stats: Truncation statistics from analyze_chunk_truncation
        strategy_name: Name of the chunking strategy
        embedder_type: Type of embedder being used
    """
    config = EMBEDDER_CONFIGS.get(embedder_type, EMBEDDER_CONFIGS["bge"])

    if stats["truncated_count"] == 0:
        print(f"\n✅ Token Limit Check: All {stats['total_chunks']} chunks within {stats['model_max_tokens']} token limit")
        print(f"   Max chunk: {stats['max_chunk_tokens']} tokens | Avg: {stats['avg_chunk_tokens']:.0f} tokens")
        return

    print(f"\n⚠️  TOKEN TRUNCATION WARNING - {strategy_name}")
    print(f"   {'='*55}")
    print(f"   Embedding model limit: {stats['model_max_tokens']} tokens ({config['name']})")
    print(f"   ")
    print(f"   Chunks exceeding limit: {stats['truncated_count']}/{stats['total_chunks']} ({stats['truncation_percentage']:.1f}%)")
    print(f"   Total tokens truncated: ~{stats['total_tokens_lost']}")
    print(f"   Largest chunk: ~{stats['max_chunk_tokens']} tokens (exceeds by ~{stats['max_chunk_tokens'] - stats['model_max_tokens']})")
    print(f"   Average chunk: ~{stats['avg_chunk_tokens']:.0f} tokens")
    print(f"   ")
    print(f"   Impact: Content beyond {stats['model_max_tokens']} tokens will NOT be embedded.")
    print(f"   {'='*55}")


def create_embedder(embedder_type: str = "bge", batch_size: int = 32):
    """
    Factory function to create the appropriate embedder.

    Args:
        embedder_type: "bge" for FastEmbed BGE, "voyage" for Voyage API
        batch_size: Batch size for embedding

    Returns:
        Tuple[embedder_component, dimension, max_tokens]
    """
    config = EMBEDDER_CONFIGS.get(embedder_type)
    if not config:
        raise ValueError(f"Unknown embedder type: {embedder_type}. Options: {list(EMBEDDER_CONFIGS.keys())}")

    if embedder_type == "voyage":
        from haystack_integrations.components.embedders.voyage_embedders import VoyageDocumentEmbedder
        embedder = VoyageDocumentEmbedder(
            model=config["model"],
            output_dimension=config["dimension"],
        )
        print(f"🚀 Using Voyage embedder: {config['model']} ({config['dimension']}d, {config['max_tokens']} max tokens)")
    else:
        # Default: BGE via FastEmbed
        embedder = FastembedDocumentEmbedder(
            model=os.getenv("FASTEMBED_MODEL", "BAAI/bge-large-en-v1.5"),
            batch_size=batch_size,
            progress_bar=True,
            parallel=None
        )
        print(f"🚀 Using FastEmbed embedder: {config['name']} ({config['dimension']}d, {config['max_tokens']} max tokens)")

    return embedder, config["dimension"], config["max_tokens"]


def create_chunking_pipeline(
    chunker_component: Any,
    collection_name: str,
    strategy_name: str,
    metadata_map: dict = None,
    embedder_type: str = "bge"
):
    """
    Create indexing pipeline with custom chunking strategy.

    Args:
        chunker_component: Haystack @component for chunking
        collection_name: Qdrant collection name
        strategy_name: Human-readable strategy name for logging
        metadata_map: Optional filepath → metadata mapping from manifest
        embedder_type: "bge" for FastEmbed BGE, "voyage" for Voyage API

    Returns:
        Pipeline: Configured indexing pipeline
        dict: Environment configuration (extended with embedder info)
    """
    env_config = load_environment()

    # Create embedder using factory
    embedder, embedding_dim, max_tokens = create_embedder(
        embedder_type=embedder_type,
        batch_size=env_config['batch_size']
    )

    # Update env_config with actual embedder settings
    env_config['embedder_type'] = embedder_type
    env_config['embedding_dimension'] = embedding_dim
    env_config['max_tokens'] = max_tokens

    # Use longer timeout for larger vectors (2048d voyage vs 1024d bge)
    qdrant_timeout = 120 if embedder_type == "voyage" else 60

    print("🔧 Creating Chunking Pipeline...")
    print(f"📊 Strategy: {strategy_name}")
    print(f"🧠 Embedder: {EMBEDDER_CONFIGS[embedder_type]['name']}")
    print(f"🔢 Dimensions: {embedding_dim}")
    print(f"📊 Collection: {collection_name}")
    print(f"⚡ Batch Size: {env_config['batch_size']}")
    print(f"⏱️  Qdrant Timeout: {qdrant_timeout}s")

    # Create Qdrant document store
    print(f"🔧 Creating Qdrant collection: {collection_name}...")
    document_store = QdrantDocumentStore(
        url=env_config["qdrant_url"],
        index=collection_name,
        api_key=Secret.from_env_var("QDRANT_API_KEY"),
        embedding_dim=embedding_dim,  # Use dimension from embedder factory
        recreate_index=True,  # Fresh collection for each strategy
        return_embedding=True,
        wait_result_from_api=True,
        timeout=qdrant_timeout
    )
    print(f"✅ Qdrant collection created: {collection_name}")

    # Create the pipeline
    pipeline = Pipeline()

    # 1. File Type Router
    pipeline.add_component("file_type_router", FileTypeRouter(
        mime_types=["text/plain", "text/markdown"]
    ))

    # 2. Document Converters
    pipeline.add_component("text_file_converter", TextFileToDocument())
    pipeline.add_component("markdown_converter", MarkdownToDocument())

    # 3. Document Joiner
    pipeline.add_component("document_joiner", DocumentJoiner())

    # 4. Metadata Enricher (if manifest metadata provided)
    if metadata_map:
        from strategies.metadata_enricher import MetadataEnricher
        pipeline.add_component("metadata_enricher", MetadataEnricher(metadata_map=metadata_map))

    # 5. Document Cleaner
    pipeline.add_component("document_cleaner", DocumentCleaner(
        remove_empty_lines=True,
        remove_extra_whitespaces=True,
        remove_repeated_substrings=False
    ))

    # 6. CUSTOM CHUNKER - this is what makes each pipeline unique!
    pipeline.add_component("chunker", chunker_component)

    # 7. Document Embedder - configurable (BGE via FastEmbed or Voyage API)
    pipeline.add_component("embedder", embedder)

    # 8. Document Writer
    pipeline.add_component("document_writer", DocumentWriter(
        document_store=document_store
    ))

    # Connect components
    print("🔗 Connecting pipeline components...")

    # Route files by type
    pipeline.connect("file_type_router.text/plain", "text_file_converter.sources")
    pipeline.connect("file_type_router.text/markdown", "markdown_converter.sources")

    # Join documents
    pipeline.connect("text_file_converter.documents", "document_joiner.documents")
    pipeline.connect("markdown_converter.documents", "document_joiner.documents")

    # Process documents (with optional metadata enrichment)
    if metadata_map:
        pipeline.connect("document_joiner.documents", "metadata_enricher.documents")
        pipeline.connect("metadata_enricher.documents", "document_cleaner.documents")
    else:
        pipeline.connect("document_joiner.documents", "document_cleaner.documents")

    pipeline.connect("document_cleaner.documents", "chunker.documents")

    # Generate embeddings and write
    pipeline.connect("chunker.documents", "embedder.documents")
    pipeline.connect("embedder.documents", "document_writer.documents")

    print(f"✅ Pipeline created for strategy: {strategy_name}")
    print("🚀 Ready to index documents!")

    return pipeline, env_config


def main():
    """Test pipeline creation with naive medium chunker."""
    from strategies.naive_chunker import NaiveChunker

    try:
        # Test with naive medium chunker
        chunker = NaiveChunker(variant="medium")
        pipeline, env_config = create_chunking_pipeline(
            chunker_component=chunker,
            collection_name="week2_test_naive_medium",
            strategy_name="Naive Medium (400w)"
        )

        print("\n" + "="*60)
        print("📋 PIPELINE CREATION TEST")
        print("="*60)
        print(f"✅ Pipeline created successfully")
        print(f"📊 Components: {len(pipeline.graph.nodes)}")
        print(f"🔗 Connections: {len(pipeline.graph.edges)}")

        # List components
        print("\n🔧 Pipeline components:")
        for i, component_name in enumerate(pipeline.graph.nodes, 1):
            print(f"   {i}. {component_name}")

    except Exception as e:
        print(f"❌ Pipeline creation failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
