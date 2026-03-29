#!/usr/bin/env python3
"""
Direct Qdrant test - Try to query week3_hybrid_recursive collection
"""

import os
import sys
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import PointIdsList

# Load .env
load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION = "week3_hybrid_recursive"

print("=" * 70)
print("DIRECT QDRANT TEST")
print("=" * 70)
print(f"\nURL: {QDRANT_URL}")
print(f"Collection: {COLLECTION}")

try:
    print("\n1. Connecting to Qdrant...")
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        timeout=10,
        prefer_grpc=False
    )
    print("   ✓ Connected!")
    
    print("\n2. Getting collections...")
    collections = client.get_collections()
    print(f"   Found {len(collections.collections)} collections:")
    for col in collections.collections:
        print(f"   - {col.name}")
    
    # Check if our collection exists
    if not any(c.name == COLLECTION for c in collections.collections):
        print(f"\n   ✗ Collection '{COLLECTION}' NOT FOUND!")
        sys.exit(1)
    
    print(f"\n   ✓ Collection '{COLLECTION}' exists!")
    
    print("\n3. Getting collection info...")
    info = client.get_collection(COLLECTION)
    print(f"   Points count: {info.points_count}")
    print(f"   Vectors size: {info.config.params.vectors}")
    
    print("\n4. Testing simple query with dense vector...")
    # Create a dummy embedding (would be from Voyage in real system)
    dummy_embedding = [0.1] * 2048  # voyage-4-lite has 2048 dimensions
    
    results = client.query_points(
        collection_name=COLLECTION,
        query=dummy_embedding,
        limit=5,
        using="text-dense"
    ).points
    
    print(f"   Retrieved {len(results)} documents")
    for i, result in enumerate(results, 1):
        print(f"\n   Document {i}:")
        print(f"   - Score: {result.score:.4f}")
        print(f"   - ID: {result.id}")
        if result.payload:
            payload = result.payload
            print(f"   - Metadata: {list(payload.keys())}")
            if "source" in payload:
                print(f"   - Source: {payload['source']}")
            if "text" in payload:
                text = payload.get("text", "")
                preview = text[:100] + "..." if len(text) > 100 else text
                print(f"   - Text: {preview}")
    
    print("\n" + "=" * 70)
    print("✓ QDRANT TEST SUCCESSFUL!")
    print("=" * 70)

except Exception as e:
    print(f"\n✗ Error: {type(e).__name__}")
    print(f"   {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
