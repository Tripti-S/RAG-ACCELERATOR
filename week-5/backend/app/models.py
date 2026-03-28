# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: API Request/Response Models
=====================================

Pydantic V2 models for the FastAPI backend.

Defines the contract between frontend and backend. Every request and response
is validated and documented through these schemas.
"""

from typing import Dict, List, Any, Optional
from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Query Models
# ---------------------------------------------------------------------------

class QueryRequest(BaseModel):
    """Request model for /query and /query/stream endpoints."""
    query: str = Field(..., min_length=1, max_length=2000, description="User's question")
    session_id: Optional[str] = Field(None, description="Session ID for conversation memory")
    use_cache: bool = Field(True, description="Whether to check semantic cache first")


class ContextItem(BaseModel):
    """A single retrieved context chunk in the response."""
    rank: int
    score: float
    content: str
    metadata: Dict[str, Any]


class QueryResponse(BaseModel):
    """Response model for /query endpoint."""
    answer: str
    contexts: List[ContextItem]
    metadata: Dict[str, Any]
    session_id: str = Field(..., description="Session ID (generated if not provided)")
    msg_id: str = Field(..., description="Message ID for linking feedback")


# ---------------------------------------------------------------------------
# Feedback Models
# ---------------------------------------------------------------------------

class FeedbackRequest(BaseModel):
    """Request model for /feedback endpoint."""
    session_id: str = Field(..., description="Session identifier")
    msg_id: str = Field(..., description="Message ID of the rated response")
    rating: str = Field(..., pattern="^(up|down)$", description="Thumbs up or down")
    query: str = Field(..., description="The query that was answered")
    answer: str = Field(..., description="The answer that was rated")
    comment: Optional[str] = Field(None, max_length=1000, description="Optional user comment")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Query metadata (type, cache_hit, etc.)")


class FeedbackResponse(BaseModel):
    """Response model for /feedback endpoint."""
    status: str
    feedback_key: str


# ---------------------------------------------------------------------------
# Conversation Models
# ---------------------------------------------------------------------------

class ConversationMessage(BaseModel):
    """A single message in conversation history."""
    msg_id: str
    role: str
    content: str
    timestamp: float
    metadata: Optional[Dict[str, Any]] = None


class ConversationResponse(BaseModel):
    """Response model for /conversation/{session_id} endpoint."""
    session_id: str
    messages: List[ConversationMessage]
    session_info: Optional[Dict[str, Any]] = None


# ---------------------------------------------------------------------------
# Monitoring Models
# ---------------------------------------------------------------------------

class HealthResponse(BaseModel):
    """Response model for /health endpoint."""
    status: str
    timestamp: float
    components: Dict[str, str]


class MetricsResponse(BaseModel):
    """Response model for /metrics endpoint."""
    total_requests: int
    avg_latency_ms: float
    total_cost_usd: float
    cache_stats: Dict[str, Any]
