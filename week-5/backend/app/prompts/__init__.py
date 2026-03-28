# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Prompts Package — Centralized Prompt Management
=================================================

Re-exports from templates (prompt text) and registry (Opik lifecycle).

Usage:
    from app.prompts import TEMPLATES, CLASSIFICATION_PROMPT, REWRITE_SYSTEM_PROMPT
    from app.prompts import register_prompts, fetch_prompt
"""

from app.prompts.templates import (
    TEMPLATES,
    QUERY_TYPES,
    DEFAULT_QUERY_TYPE,
    CLASSIFICATION_PROMPT,
    REWRITE_SYSTEM_PROMPT,
    TEMPLATE_FACTUAL,
    TEMPLATE_FACTUAL_V2,
    TEMPLATE_HOW_TO,
    TEMPLATE_TROUBLESHOOTING,
    TEMPLATE_CODE_GENERATION,
)
from app.prompts.registry import register_prompts, fetch_prompt

__all__ = [
    # Template constants
    "TEMPLATES",
    "QUERY_TYPES",
    "DEFAULT_QUERY_TYPE",
    "CLASSIFICATION_PROMPT",
    "REWRITE_SYSTEM_PROMPT",
    "TEMPLATE_FACTUAL",
    "TEMPLATE_FACTUAL_V2",
    "TEMPLATE_HOW_TO",
    "TEMPLATE_TROUBLESHOOTING",
    "TEMPLATE_CODE_GENERATION",
    # Registry functions
    "register_prompts",
    "fetch_prompt",
]
