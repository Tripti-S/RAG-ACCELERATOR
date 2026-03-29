#!/usr/bin/env python3
"""
Test Week 3 Hybrid Retrieval with a real query using Voyage embeddings
"""

import os
import sys
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from voyageai import Client as VoyageClient

# Load .env
load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
VOYAGE_API_KEY = os.getenv("VOYAGE_API_KEY")
COLLECTION = "week3_hybrid_recursive"

print("=" * 80)
print("WEEK 3 HYBRID RETRIEVAL TEST")
print("=" * 80)

# Initialize clients
print("\n1. Initializing clients...")
qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    timeout=10,
    prefer_grpc=False
)
voyage_client = VoyageClient(api_key=VOYAGE_API_KEY)
print("   ✓ Clients initialized")

# Test queries
test_queries = [
    "What is probability?",
    "How do I calculate variance?",
    "Explain Bayes' theorem",
]

for query_text in test_queries:
    print("\n" + "-" * 80)
    print(f"Query: '{query_text}'")
    print("-" * 80)
    
    try:
        # Get dense embedding from Voyage with full dimension
        print(f"\n2. Embedding query with Voyage...")
        embedding = voyage_client.embed(
            texts=[query_text],
            model="voyage-4-lite",
            output_dimension=2048  # Match the collection's expected dimension
        ).embeddings[0]
        print(f"   ✓ Embedding obtained ({len(embedding)} dimensions)")
        
        # Query Qdrant
        print(f"\n3. Querying Qdrant with hybrid search...")
        results = qdrant_client.query_points(
            collection_name=COLLECTION,
            query=embedding,
            limit=3,
            using="text-dense"
        ).points
        
        print(f"   ✓ Retrieved {len(results)} documents\n")
        
        for i, result in enumerate(results, 1):
            print(f"   [{i}] Score: {result.score:.4f}")
            
            # Extract content
            if result.payload:
                payload = result.payload
                if "content" in payload:
                    content = payload["content"]
                    preview = content[:150] + "..." if len(content) > 150 else content
                    print(f"       Content: {preview}")
                if "meta" in payload:
                    meta = payload["meta"]
                    if isinstance(meta, dict):
                        if "source" in meta:
                            print(f"       Source: {meta['source']}")
                        if "file_name" in meta:
                            print(f"       File: {meta['file_name']}")
            print()
    
    except Exception as e:
        print(f"   ✗ Error: {e}")

print("\n" + "=" * 80)
print("✓ WEEK 3 RETRIEVAL TEST COMPLETE!")
print("=" * 80)
