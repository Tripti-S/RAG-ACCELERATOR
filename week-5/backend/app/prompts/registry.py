# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Opik Prompt Registry — Version Control & Hot-Swap
====================================================

Production prompt lifecycle management through Opik's prompt library.

Two operations:
1. register_prompts() — startup: push current templates to Opik (auto-versions
   if content changed, no-op if unchanged). Creates the baseline in Opik.
2. fetch_prompt()     — runtime: fetch latest version from Opik for each request.
   If someone edited the prompt in Opik UI, next request picks it up automatically
   (hot-swap without redeploy).

Fallback: if Opik is unavailable (not installed, network down, API error),
both functions gracefully fall back to the hardcoded templates in templates.py.
The system always works — Opik adds versioning and hot-swap on top.

Prompt naming convention:
    rag-factual, rag-how-to, rag-troubleshooting, rag-code-generation
"""

from typing import Tuple, Optional, Any

from app.prompts.templates import TEMPLATES

# Opik (optional — no-op if not installed)
try:
    import opik
    from opik import opik_context
    OPIK_AVAILABLE = True
except ImportError:
    OPIK_AVAILABLE = False


# ---------------------------------------------------------------------------
# Prompt name mapping
# ---------------------------------------------------------------------------

# Maps query type (e.g., "FACTUAL") to Opik prompt name (e.g., "rag-factual")
def _prompt_name(query_type: str) -> str:
    return f"rag-{query_type.lower().replace('_', '-')}"


# ---------------------------------------------------------------------------
# Startup: Register prompts in Opik
# ---------------------------------------------------------------------------

def register_prompts() -> None:
    """
    Register all generation templates in Opik's prompt library.

    Called once at startup from QueryRouter.__init__(). For each template:
    - If prompt doesn't exist in Opik → creates it (version 1)
    - If prompt exists with same content → no-op (idempotent)
    - If prompt exists with different content → creates new version (auto-version)

    Skipped silently if Opik is not installed or unavailable.
    """
    if not OPIK_AVAILABLE:
        print("   Opik not available — skipping prompt registration")
        return

    try:
        for query_type, template_text in TEMPLATES.items():
            name = _prompt_name(query_type)
            opik.Prompt(name=name, prompt=template_text)
            print(f"   Registered prompt: {name}")

        print("   All prompts registered in Opik")

    except Exception as e:
        # Registration failure is non-fatal — hardcoded templates still work
        print(f"   Opik prompt registration failed (using hardcoded fallback): {str(e)[:100]}")


# ---------------------------------------------------------------------------
# Runtime: Fetch latest prompt from Opik
# ---------------------------------------------------------------------------

def fetch_prompt(query_type: str) -> Tuple[str, Optional[Any]]:
    """
    Fetch the latest prompt version from Opik for a given query type.

    Returns:
        Tuple of (prompt_text, prompt_object):
        - prompt_text: the system prompt string to use for generation
        - prompt_object: Opik Prompt object for trace linking (None if unavailable)

    If Opik is unavailable or fetch fails, returns the hardcoded template
    from templates.py with prompt_object=None (no trace linking).
    """
    fallback_text = TEMPLATES.get(query_type, TEMPLATES["FACTUAL"])

    if not OPIK_AVAILABLE:
        return fallback_text, None

    try:
        client = opik.Opik()
        name = _prompt_name(query_type)
        prompt_obj = client.get_prompt(name=name)

        if prompt_obj is not None:
            return prompt_obj.prompt, prompt_obj

        # Prompt not found in Opik — use hardcoded
        return fallback_text, None

    except Exception:
        # Fetch failure is non-fatal — use hardcoded template
        return fallback_text, None
