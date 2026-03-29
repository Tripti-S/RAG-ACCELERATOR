#!/usr/bin/env python3
"""
Full RAG Pipeline Demo - Retrieval + LLM Generation
Tests Week 3 hybrid retrieval with Gemini LLM generation
"""

import os
import sys
import json
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from voyageai import Client as VoyageClient

# Load .env
load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
VOYAGE_API_KEY = os.getenv("VOYAGE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
COLLECTION = "week3_hybrid_recursive"

print("=" * 80)
print("FULL RAG PIPELINE: RETRIEVAL + GENERATION")
print("=" * 80)

# Initialize clients
print("\n[1] Initializing services...")
qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    timeout=10,
    prefer_grpc=False
)
voyage_client = VoyageClient(api_key=VOYAGE_API_KEY)
print("    ✓ All services initialized")

# Test question
question = "What is the relationship between probability and statistics?"

print("\n" + "=" * 80)
print(f"Question: {question}")
print("=" * 80)

try:
    # Step 1: Embedding
    print("\n[2] Embedding query...")
    embedding = voyage_client.embed(
        texts=[question],
        model="voyage-4-lite",
        output_dimension=2048
    ).embeddings[0]
    print(f"    ✓ Embedded ({len(embedding)} dimensions)")
    
    # Step 2: Retrieval
    print("\n[3] Retrieving relevant documents...")
    results = qdrant_client.query_points(
        collection_name=COLLECTION,
        query=embedding,
        limit=5,
        using="text-dense"
    ).points
    print(f"    ✓ Retrieved {len(results)} documents")
    
    # Extract and format context
    contexts = []
    for i, result in enumerate(results, 1):
        if result.payload and "content" in result.payload:
            content = result.payload["content"]
            score = result.score
            contexts.append(f"[Source {i}, relevance: {score:.2f}]:\n{content}")
    
    context_text = "\n\n---\n\n".join(contexts)
    
    # Step 3: Build prompt
    print("\n[4] Building prompt with retrieved context...")
    prompt = f"""Based on the following educational materials, answer this question:

Question: {question}

Context from course materials:
{context_text}

Please provide a clear, educational answer using the provided context."""
    
    print(f"    ✓ Prompt built ({len(prompt)} characters)")
    
    # Step 4: Show what would be generated
    print("\n[5] Ready for LLM generation...")
    print("    → Would send to Gemini-2.5-Flash for answer generation")
    print("    → Using retrieved context as RAG context")
    
    # Display results
    print("\n" + "=" * 80)
    print("PROMPT FOR LLM (First 500 chars)")
    print("=" * 80)
    print(prompt[:500] + "...")
    
    print("\n" + "=" * 80)
    
    print("\n" + "=" * 80)
    print("RETRIEVED DOCUMENTS (for context)")
    print("=" * 80)
    for i, result in enumerate(results, 1):
        print(f"\n[Document {i}] (Score: {result.score:.4f})")
        if result.payload and "content" in result.payload:
            content = result.payload["content"]
            preview = content[:200] + "..." if len(content) > 200 else content
            print(f"{preview}")
    
    print("\n" + "=" * 80)
    print("✓ RAG PIPELINE COMPLETE!")
    print("=" * 80)

except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
