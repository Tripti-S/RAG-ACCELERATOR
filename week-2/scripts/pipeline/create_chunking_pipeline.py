
# ============================================================================
# The Engineer's RAG Accelerator - Adapted for Capstone Week 2
#
# This script creates a chunking pipeline using the selected strategy.
# Input: week-1/data/processed/
# Output: Qdrant collection for each strategy
# ============================================================================

"""
Week 2: Create Chunking Pipeline with Custom Strategy
====================================================

Generic pipeline builder that accepts any chunking strategy component.
Creates indexing pipeline using:
- File routing → Converters → Joiner → Cleaner → CUSTOM CHUNKER → Embedder → Writer
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from typing import Any, List, Dict

# Path resolution - works when run from any directory
SCRIPT_DIR = Path(__file__).resolve().parent      # scripts/
WEEK2_DIR = SCRIPT_DIR.parent                     # week-2/
PROJECT_ROOT = WEEK2_DIR.parent                   # rag-capstone-week-1/

# Add week-2/scripts to path for strategy imports
sys.path.insert(0, str(SCRIPT_DIR))

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
TOKENS_PER_WORD = 1.3
BGE_MAX_TOKENS = 512

EMBEDDER_CONFIGS = {
	"bge": {
		"name": "BGE-large-en-v1.5 (FastEmbed)",
		"dimension": 1024,
		"max_tokens": 512,
		"type": "fastembed"
	},
    "minilm": {
        "name": "all-MiniLM-L6-v2",
        "dimension": 384,
        "max_tokens": 512,
        "type": "fastembed"
    }
}

def load_environment():
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
	word_count = len(text.split())
	return int(word_count * TOKENS_PER_WORD)

def analyze_chunk_truncation(documents: List[Document], max_tokens: int = BGE_MAX_TOKENS) -> Dict[str, Any]:
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

    config = EMBEDDER_CONFIGS.get(embedder_type)
    if not config:
        raise ValueError(
            f"Unknown embedder type: {embedder_type}. "
            f"Options: {list(EMBEDDER_CONFIGS.keys())}"
        )

    if embedder_type == "bge":
        model_name = "BAAI/bge-large-en-v1.5"
    elif embedder_type == "minilm":
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
    else:
        raise ValueError("Unsupported embedder type")

    embedder = FastembedDocumentEmbedder(
        model=model_name,
        batch_size=batch_size,
        progress_bar=True
    )

    print(f"🚀 Using embedder: {config['name']} "
          f"({config['dimension']}d, {config['max_tokens']} max tokens)")

    return embedder, config["dimension"], config["max_tokens"]

def create_chunking_pipeline(
	chunker_component: Any,
	collection_name: str,
	strategy_name: str,
	metadata_map: dict = None,
	embedder_type: str = "bge"
):
	env_config = load_environment()
	embedder, embedding_dim, max_tokens = create_embedder(
		embedder_type=embedder_type,
		batch_size=env_config['batch_size']
	)
	env_config['embedder_type'] = embedder_type
	env_config['embedding_dimension'] = embedding_dim
	env_config['max_tokens'] = max_tokens
	qdrant_timeout = 60
	print("🔧 Creating Chunking Pipeline...")
	print(f"📊 Strategy: {strategy_name}")
	print(f"🧠 Embedder: {EMBEDDER_CONFIGS[embedder_type]['name']}")
	print(f"🔢 Dimensions: {embedding_dim}")
	print(f"📊 Collection: {collection_name}")
	print(f"⚡ Batch Size: {env_config['batch_size']}")
	print(f"⏱️  Qdrant Timeout: {qdrant_timeout}s")
	print(f"🔧 Creating Qdrant collection: {collection_name}...")
	document_store = QdrantDocumentStore(
		url=env_config["qdrant_url"],
		index=collection_name,
		api_key=Secret.from_env_var("QDRANT_API_KEY"),
		embedding_dim=embedding_dim,
		recreate_index=True,
		return_embedding=True,
		wait_result_from_api=True,
		timeout=qdrant_timeout
	)
	print(f"✅ Qdrant collection created: {collection_name}")
	pipeline = Pipeline()
	pipeline.add_component("file_type_router", FileTypeRouter(
		mime_types=["text/plain", "text/markdown"]
	))
	pipeline.add_component("text_file_converter", TextFileToDocument())
	pipeline.add_component("markdown_converter", MarkdownToDocument())
	pipeline.add_component("document_joiner", DocumentJoiner())
	if metadata_map:
		from metadata_enricher import MetadataEnricher
		pipeline.add_component("metadata_enricher", MetadataEnricher(metadata_map=metadata_map))
	pipeline.add_component("document_cleaner", DocumentCleaner(
		remove_empty_lines=True,
		remove_extra_whitespaces=True,
		remove_repeated_substrings=False
	))
	pipeline.add_component("chunker", chunker_component)
	pipeline.add_component("embedder", embedder)
	pipeline.add_component("document_writer", DocumentWriter(
		document_store=document_store
	))
	print("🔗 Connecting pipeline components...")
	pipeline.connect("file_type_router.text/plain", "text_file_converter.sources")
	pipeline.connect("file_type_router.text/markdown", "markdown_converter.sources")
	pipeline.connect("text_file_converter.documents", "document_joiner.documents")
	pipeline.connect("markdown_converter.documents", "document_joiner.documents")
	if metadata_map:
		pipeline.connect("document_joiner.documents", "metadata_enricher.documents")
		pipeline.connect("metadata_enricher.documents", "document_cleaner.documents")
	else:
		pipeline.connect("document_joiner.documents", "document_cleaner.documents")
	pipeline.connect("document_cleaner.documents", "chunker.documents")
	pipeline.connect("chunker.documents", "embedder.documents")
	pipeline.connect("embedder.documents", "document_writer.documents")
	print(f"✅ Pipeline created for strategy: {strategy_name}")
	print("🚀 Ready to index documents!")
	return pipeline, env_config

if __name__ == "__main__":
	from naive_chunker import NaiveChunker
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
	print("\n🔧 Pipeline components:")
	for i, component_name in enumerate(pipeline.graph.nodes, 1):
		print(f"   {i}. {component_name}")
