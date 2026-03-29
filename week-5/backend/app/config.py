# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Configuration Management
==================================

Centralized configuration using Pydantic Settings.

All environment variables used by the production system are documented here.
Individual services read from os.getenv() directly (self-contained), but this
file serves as the single source of truth for what the system expects.

Usage:
    from app.config import settings

    # Access any setting
    app_name = settings.APP_NAME
    debug = settings.DEBUG
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# Find .env: check backend/ first, then week5_production/
_config_dir = Path(__file__).resolve().parent
_backend_dir = _config_dir.parent
_week_dir = _backend_dir.parent

env_path = _backend_dir / ".env"
if not env_path.exists():
    env_path = _week_dir / ".env"

# Load into os.environ so all services (which use os.getenv) pick it up
if env_path.exists():
    load_dotenv(env_path, override=False)


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    model_config = SettingsConfigDict(
        env_file=str(env_path) if env_path.exists() else None,
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # --- Application ---
    APP_NAME: str = "ProbablAI - Production"
    DEBUG: bool = False

    # --- Qdrant ---
    QDRANT_URL: str = ""
    QDRANT_API_KEY: str = ""
    QDRANT_COLLECTION: str = "week3_hybrid_recursive"

    # --- API Keys ---
    GOOGLE_API_KEY: str = ""
    VOYAGE_API_KEY: str = ""

    # --- Retrieval Models ---
    VOYAGE_EMBED_MODEL: str = "voyage-4-lite"
    VOYAGE_DIMENSION: int = 2048
    SPARSE_MODEL: str = "Qdrant/bm25"
    LLM_MODEL: str = "gemini-2.5-flash"
    LLM_FALLBACK_MODEL: str = "gemini-2.5-flash-lite"

    # --- Redis ---
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = ""
    REDIS_USERNAME: str = "default"
    REDIS_SSL: bool = True

    # --- Semantic Cache ---
    CACHE_EMBED_MODEL: str = "voyage-4-lite"
    CACHE_EMBED_DIMENSION: int = 2048
    CACHE_DISTANCE_THRESHOLD: float = 0.06
    CACHE_TTL: int = 86400

    # --- Conversation Memory ---
    CONVERSATION_WINDOW_SIZE: int = 10
    CONVERSATION_SESSION_TTL: int = 86400

    # --- Opik Observability (optional) ---
    OPIK_API_KEY: str = ""
    OPIK_WORKSPACE: str = "default"
    OPIK_PROJECT_NAME: str = "probablai-prod"


# Global settings instance
settings = Settings()


def get_settings() -> Settings:
    """Get the global settings instance."""
    return settings
