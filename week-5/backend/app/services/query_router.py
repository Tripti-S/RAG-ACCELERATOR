# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Query Router — Classification + Prompt Templates
==========================================================

Classifies user queries into types and selects specialized prompt templates.

Why query routing?
A single monolithic prompt can't optimize for all query types. "What is MCP?"
needs a concise factual answer. "How do I create an MCP server?" needs numbered steps.
"MCP server connection refused" needs cause-diagnosis-fix structure.
Different queries need different instructions. That's query routing.

Architecture:
- One Gemini Flash call to classify query into 4 types
- Type-specific prompt template with tailored FORMAT section
- Three-tier insufficient context handling per template

Query types (4):
- FACTUAL: Direct facts, definitions, values -> concise 1-3 sentence answers
- HOW_TO: Procedures, setup instructions -> numbered steps
- TROUBLESHOOTING: Errors, failures, debugging -> cause/diagnosis/fix structure
- CODE_GENERATION: Code requests, implementations -> runnable code with imports

Why 4 types not 6?
Comparison and Conceptual are natural extensions students can add. 4 types makes
the teaching point ("different queries need different prompts") without overwhelming.

Sources: Nirant Kasliwal RAG query types, NVIDIA RAG Blueprint, Anthropic prompt
patterns, kapa.ai RAG best practices, Stack AI prompt engineering guide.

Usage:
    from app.services.query_router import get_query_router

    router = get_query_router()

    # Classify query
    classification = await router.classify(query)

    # Build type-specific prompt
    prompt_messages = router.build_prompt(query, contexts, classification["category"])

    # Generate with pipeline (which accepts prompt_messages)
    answer = await pipeline.generate(query, contexts, prompt_messages)
"""

import os
import json
import time
import asyncio
from typing import Dict, List, Any, Optional

from haystack import Document
from haystack.dataclasses import ChatMessage
from haystack_integrations.components.generators.google_genai import GoogleGenAIChatGenerator

# Opik tracing (optional — no-op decorator if not installed)
try:
    import opik
    from opik import opik_context
    _opik_track = opik.track
    OPIK_AVAILABLE = True
except ImportError:
    def _opik_track(**kwargs):
        def _noop(func):
            return func
        return _noop
    OPIK_AVAILABLE = False

# Prompts imported from centralized prompt directory (app/prompts/)
from app.prompts import (
    TEMPLATES, QUERY_TYPES, DEFAULT_QUERY_TYPE,
    CLASSIFICATION_PROMPT,
    register_prompts, fetch_prompt,
)


# ---------------------------------------------------------------------------
# Query Router
# ---------------------------------------------------------------------------

class QueryRouter:
    """
    Query classification and prompt template selection.

    Two responsibilities:
    1. classify(): Determine query type via LLM (FACTUAL, HOW_TO, etc.)
    2. build_prompt(): Select template + format contexts into ChatMessage list

    The build_prompt() method is synchronous (just string formatting).
    classify() is async (LLM call).

    Singleton pattern: one router instance across all requests.
    """

    _instance = None
    _initialized = False

    def __new__(cls):
        """Singleton — one router instance across all requests."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize router: LLM for classification."""
        if self._initialized:
            return

        print("\n   Initializing query router...")

        self._init_config()
        self._init_llm()
        self._init_prompts()

        self._initialized = True
        print("   Query router ready")

    # -------------------------------------------------------------------
    # Initialization
    # -------------------------------------------------------------------

    def _init_config(self):
        """Load router configuration from environment."""
        self.llm_model = os.getenv("LLM_MODEL", "gemini-2.5-flash")

        print(f"   Router config: model={self.llm_model}")

    def _init_llm(self):
        """Initialize the LLM for classification."""
        self.llm = GoogleGenAIChatGenerator(model=self.llm_model)
        print(f"   Router LLM ready: {self.llm_model}")

    def _init_prompts(self):
        """Register prompt templates in Opik for versioning and hot-swap."""
        register_prompts()

    # -------------------------------------------------------------------
    # Classification
    # -------------------------------------------------------------------

    @_opik_track(name="classify")
    async def classify(self, query: str) -> Dict[str, Any]:
        """
        Classify a query into one of 4 types using a single LLM call.

        Args:
            query: User's question

        Returns:
            Dict with:
                category: One of FACTUAL, HOW_TO, TROUBLESHOOTING, CODE_GENERATION
                confidence: LLM's confidence score (0.0-1.0)
        """
        start_time = time.time()

        messages = [
            ChatMessage.from_system(CLASSIFICATION_PROMPT),
            ChatMessage.from_user(query)
        ]

        try:
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(
                None,
                lambda: self.llm.run(messages=messages)
            )

            raw_text = result["replies"][0].text.strip()
            classification = self._parse_json_response(raw_text)

            category = classification.get("category", DEFAULT_QUERY_TYPE).upper()
            confidence = float(classification.get("confidence", 0.5))

            # Validate category
            if category not in QUERY_TYPES:
                category = DEFAULT_QUERY_TYPE
                confidence = 0.0

            elapsed = time.time() - start_time
            print(f"   Query classified: {category} (confidence={confidence:.2f}, {elapsed:.2f}s)")

            return {"category": category, "confidence": confidence}

        except Exception as e:
            print(f"   Classification failed, defaulting to {DEFAULT_QUERY_TYPE}: {str(e)[:100]}")
            if OPIK_AVAILABLE:
                try:
                    opik_context.update_current_span(metadata={
                        "classification_error": str(e)[:200],
                        "defaulted_to": DEFAULT_QUERY_TYPE,
                    })
                except Exception:
                    pass
            return {"category": DEFAULT_QUERY_TYPE, "confidence": 0.0}

    # -------------------------------------------------------------------
    # Prompt Building
    # -------------------------------------------------------------------

    def build_prompt(
        self,
        query: str,
        contexts: List[Document],
        query_type: str
    ) -> List[ChatMessage]:
        """
        Build a ChatMessage list using the type-specific prompt template.

        Fetches the latest prompt version from Opik (hot-swap without redeploy).
        Falls back to hardcoded templates if Opik is unavailable.
        Links the prompt version to the current Opik trace for prompt-to-trace
        traceability.

        Args:
            query: User's question (standalone — already rewritten if follow-up)
            contexts: Retrieved Document objects from retrieval pipeline
            query_type: One of FACTUAL, HOW_TO, TROUBLESHOOTING, CODE_GENERATION

        Returns:
            List[ChatMessage] ready for the generator
        """
        # Fetch latest prompt from Opik (falls back to hardcoded if unavailable)
        system_prompt, prompt_obj = fetch_prompt(query_type)

        # Link prompt version to current Opik trace (prompt-to-trace traceability)
        if prompt_obj is not None and OPIK_AVAILABLE:
            try:
                opik_context.update_current_trace(prompts=[prompt_obj])
            except Exception:
                pass

        # Format contexts with chunk IDs for citation
        context_text = self._format_contexts(contexts)

        return [
            ChatMessage.from_system(system_prompt),
            ChatMessage.from_user(
                f"CONTEXT:\n{context_text}\n\n"
                f"QUESTION: {query}"
            )
        ]

    def _format_contexts(self, contexts: List[Document]) -> str:
        """
        Format Document objects into numbered context text for prompts.

        Each context gets a [chunk_id] that the LLM uses for citations.
        Includes source metadata so the LLM knows where information came from.

        Args:
            contexts: Retrieved Document objects

        Returns:
            Formatted context string with numbered chunks
        """
        if not contexts:
            return "(No relevant context found.)"

        parts = []
        for i, doc in enumerate(contexts, 1):
            file_path = doc.meta.get("file_path", "unknown")
            category = doc.meta.get("category", "unknown")
            parts.append(
                f"[{i}] (source: {file_path}, type: {category})\n{doc.content}"
            )

        return "\n\n".join(parts)

    # -------------------------------------------------------------------
    # Internal helpers
    # -------------------------------------------------------------------

    @staticmethod
    def _parse_json_response(text: str) -> Dict[str, Any]:
        """
        Parse JSON from LLM response, handling common formatting issues.

        LLMs sometimes wrap JSON in markdown code blocks or add extra text.
        This method strips common wrappers and attempts to parse.

        Args:
            text: Raw LLM response text

        Returns:
            Parsed dict, or empty dict if parsing fails
        """
        # Strip markdown code blocks if present
        cleaned = text.strip()
        if cleaned.startswith("```"):
            # Remove opening ```json or ``` and closing ```
            lines = cleaned.split("\n")
            lines = [l for l in lines if not l.strip().startswith("```")]
            cleaned = "\n".join(lines).strip()

        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            # Try to find JSON object in the text
            start = cleaned.find("{")
            end = cleaned.rfind("}") + 1
            if start >= 0 and end > start:
                try:
                    return json.loads(cleaned[start:end])
                except json.JSONDecodeError:
                    pass
            return {}


# ---------------------------------------------------------------------------
# Singleton accessor
# ---------------------------------------------------------------------------

_query_router: Optional[QueryRouter] = None


def get_query_router() -> QueryRouter:
    """
    Get or create the global query router instance.

    Singleton ensures we initialize the classification LLM exactly once
    across all requests.
    """
    global _query_router
    if _query_router is None:
        _query_router = QueryRouter()
    return _query_router
