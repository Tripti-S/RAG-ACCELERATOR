# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Conversation Memory with Query Rewriting
==================================================

Redis-backed sliding window conversation memory with conditional LLM-powered
query rewriting for multi-turn conversations.

Why conversation memory?
Without memory, every query is independent. Follow-ups like "What about its
configuration?" fail because the system doesn't know what "its" refers to.
Conversation memory stores recent exchanges and rewrites ambiguous queries
into standalone questions suitable for retrieval.

Architecture:
- Redis Lists for sliding window storage (last 10 messages = 5 turns)
- Atomic RPUSH + LTRIM + EXPIRE pipeline for consistent writes
- Conditional query rewriting: skip LLM call when no history (saves latency)
- 24-hour TTL with sliding expiration (refreshes on every interaction)

Rewriting pattern (from LangChain create_history_aware_retriever):
- Only rewrite when conversation history exists
- On first turn: pass query directly (zero LLM overhead)
- On follow-ups: single Gemini Flash call to resolve references
- Example: "What about its config?" -> "What is the MCP protocol configuration?"

Why pass both user + assistant messages to the rewriter?
Assistant responses contain resolved entities the rewriter needs. If user asks
"What is MCP?" and assistant explains it, then user asks "How do I configure it?",
the rewriter needs the assistant's mention of "MCP" to resolve "it".

Redis key schema:
    chat:{session_id}:messages  -> LIST   (sliding window, LTRIM to 10)
    chat:{session_id}:meta      -> HASH   (created_at, last_active, total_messages)

Usage:
    from app.services.conversation import get_conversation_service

    conversation = get_conversation_service()

    # Rewrite follow-up queries using conversation context
    result = await conversation.rewrite_if_needed(query, session_id)
    standalone_query = result["standalone_query"]

    # ... run pipeline with standalone_query ...

    # Store messages AFTER getting the answer
    conversation.add_message(session_id, "user", query)
    conversation.add_message(session_id, "assistant", answer)
"""

import os
import time
import json
import uuid
import asyncio
from typing import Dict, List, Any, Optional

import redis

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

# Haystack LLM for query rewriting (same model as generation — fast and cheap)
from haystack.dataclasses import ChatMessage
from haystack_integrations.components.generators.google_genai import GoogleGenAIChatGenerator

# Rewrite prompt imported from centralized prompt directory (app/prompts/)
from app.prompts import REWRITE_SYSTEM_PROMPT


# ---------------------------------------------------------------------------
# Conversation Service
# ---------------------------------------------------------------------------

class ConversationService:
    """
    Redis-backed conversation memory with conditional query rewriting.

    Stores recent messages in a sliding window per session. When history exists,
    rewrites follow-up queries into standalone questions using a single LLM call.
    Skips the LLM call on first turn (no history = no rewriting needed).

    Session lifecycle:
    - Frontend generates session_id on first load (or "New conversation" click)
    - Backend lazily creates session on first add_message()
    - Session expires after 24h of inactivity (sliding TTL)
    - No thread infrastructure — architecture is thread-ready (session_id = thread_id)
      but UI is single-conversation with "New conversation" button

    Singleton pattern: one service instance across all requests.
    """

    SESSION_PREFIX = "chat:"

    _instance = None
    _initialized = False

    def __new__(cls):
        """Singleton — one conversation service across all requests."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize conversation service: Redis connection, LLM rewriter."""
        if self._initialized:
            return

        print("\n   Initializing conversation service...")

        self._init_config()
        self._init_redis()
        self._init_rewriter()

        self._initialized = True
        print("   Conversation service ready")

    # -------------------------------------------------------------------
    # Initialization
    # -------------------------------------------------------------------

    def _init_config(self):
        """Load conversation configuration from environment."""
        # Redis connection (shared env vars with semantic_cache)
        self.redis_host = os.getenv("REDIS_HOST", "localhost")
        self.redis_port = int(os.getenv("REDIS_PORT", "6379"))
        self.redis_password = os.getenv("REDIS_PASSWORD", "")
        self.redis_username = os.getenv("REDIS_USERNAME", "default")
        self.redis_ssl = os.getenv("REDIS_SSL", "true").lower() == "true"

        # Conversation settings
        self.window_size = int(os.getenv("CONVERSATION_WINDOW_SIZE", "10"))
        self.session_ttl = int(os.getenv("CONVERSATION_SESSION_TTL", "86400"))

        # Rewriter model (same as generation — fast and cheap)
        self.rewriter_model = os.getenv("LLM_MODEL", "gemini-2.5-flash")

        print(f"   Conversation config: window={self.window_size} messages, ttl={self.session_ttl}s")
        print(f"   Rewriter model: {self.rewriter_model}")

    def _init_redis(self):
        """
        Connect to Redis for conversation storage.

        Uses decode_responses=True because conversation data is JSON strings only.
        (Contrast with SemanticCache which uses False for binary embedding vectors.)
        """
        self.redis_client = redis.Redis(
            host=self.redis_host,
            port=self.redis_port,
            username=self.redis_username,
            password=self.redis_password,
            ssl=self.redis_ssl,
            decode_responses=True  # JSON strings only, no binary data
        )

        try:
            self.redis_client.ping()
            print(f"   Redis connected: {self.redis_host}:{self.redis_port}")
        except redis.ConnectionError as e:
            raise ConnectionError(
                f"Cannot connect to Redis at {self.redis_host}:{self.redis_port}. "
                f"Error: {e}"
            )

    def _init_rewriter(self):
        """Initialize the LLM for query rewriting (Gemini Flash)."""
        self.rewriter = GoogleGenAIChatGenerator(model=self.rewriter_model)
        print(f"   Query rewriter ready: {self.rewriter_model}")

    # -------------------------------------------------------------------
    # Session Management
    # -------------------------------------------------------------------

    @staticmethod
    def create_session_id() -> str:
        """
        Generate a new session ID.

        Called by frontend on first load or "New conversation" button click.
        Format: sess_{uuid4_hex} — globally unique, no collisions.
        """
        return f"sess_{uuid.uuid4().hex}"

    def get_history(self, session_id: str) -> List[Dict[str, Any]]:
        """
        Get conversation history for a session.

        Returns the sliding window of recent messages (up to window_size).
        Refreshes the session TTL on read (sliding expiration — active
        conversations persist, inactive ones expire).

        Args:
            session_id: Session identifier

        Returns:
            List of message dicts: [{msg_id, role, content, timestamp}, ...]
            Empty list if session doesn't exist or has expired
        """
        messages_key = f"{self.SESSION_PREFIX}{session_id}:messages"
        raw_messages = self.redis_client.lrange(messages_key, 0, -1)

        # Refresh TTL on read (sliding expiration)
        if raw_messages:
            self.redis_client.expire(messages_key, self.session_ttl)

        return [json.loads(raw) for raw in raw_messages]

    def add_message(
        self,
        session_id: str,
        role: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Add a message to conversation history.

        Atomic Redis pipeline in one round-trip:
        1. RPUSH: append message to list
        2. LTRIM: keep only last window_size messages (sliding window)
        3. EXPIRE: refresh session TTL (sliding expiration)
        4. HSETNX/HSET: update session metadata

        Args:
            session_id: Session identifier
            role: "user" or "assistant"
            content: Message content
            metadata: Optional metadata (query_type, cache_hit, latency, etc.)

        Returns:
            Generated message ID (for linking feedback to specific responses)
        """
        msg_id = f"msg_{uuid.uuid4().hex[:12]}"

        message = {
            "msg_id": msg_id,
            "role": role,
            "content": content,
            "timestamp": time.time(),
        }
        if metadata:
            message["metadata"] = metadata

        messages_key = f"{self.SESSION_PREFIX}{session_id}:messages"
        meta_key = f"{self.SESSION_PREFIX}{session_id}:meta"

        # Atomic pipeline: add + trim window + update meta + refresh TTL
        pipe = self.redis_client.pipeline()
        pipe.rpush(messages_key, json.dumps(message))
        pipe.ltrim(messages_key, -self.window_size, -1)
        pipe.expire(messages_key, self.session_ttl)
        pipe.hsetnx(meta_key, "created_at", str(time.time()))
        pipe.hset(meta_key, "last_active", str(time.time()))
        pipe.hincrby(meta_key, "total_messages", 1)
        pipe.expire(meta_key, self.session_ttl)
        pipe.execute()

        return msg_id

    # -------------------------------------------------------------------
    # Query Rewriting
    # -------------------------------------------------------------------

    @_opik_track(name="rewrite_if_needed")
    async def rewrite_if_needed(
        self,
        query: str,
        session_id: str
    ) -> Dict[str, Any]:
        """
        Conditionally rewrite a query using conversation history.

        Conditional rewriting (LangChain create_history_aware_retriever pattern):
        - No history (first turn): return query as-is, zero LLM overhead
        - History exists (follow-up): rewrite to standalone via single LLM call

        Example:
            Turn 1: "What is MCP?" -> standalone, no rewrite needed
            Turn 2: "How do I configure it?" -> "How do I configure MCP?"
            Turn 3: "Show me an example" -> "Show me an example of MCP configuration"

        Args:
            query: User's latest question (may reference conversation context)
            session_id: Session identifier for history lookup

        Returns:
            Dict with:
                original_query: The raw user query
                standalone_query: Rewritten query (or original if no rewrite)
                is_follow_up: Whether history existed and rewriting was attempted
                history_length: Number of messages in conversation window
        """
        history = self.get_history(session_id)

        # No history = first turn = no rewriting needed (saves one LLM call)
        if not history:
            return {
                "original_query": query,
                "standalone_query": query,
                "is_follow_up": False,
                "history_length": 0,
            }

        # History exists — rewrite using LLM
        try:
            standalone_query = await self._rewrite_query(query, history)

            return {
                "original_query": query,
                "standalone_query": standalone_query,
                "is_follow_up": True,
                "history_length": len(history),
            }

        except Exception as e:
            # Rewrite failure is non-fatal — use original query and continue
            print(f"   Query rewrite failed, using original: {str(e)[:100]}")
            if OPIK_AVAILABLE:
                try:
                    opik_context.update_current_span(metadata={
                        "rewrite_error": str(e)[:200],
                        "fell_back_to_original": True,
                    })
                except Exception:
                    pass
            return {
                "original_query": query,
                "standalone_query": query,
                "is_follow_up": True,
                "history_length": len(history),
            }

    async def _rewrite_query(
        self,
        query: str,
        history: List[Dict[str, Any]]
    ) -> str:
        """
        Rewrite a follow-up query into a standalone question using the LLM.

        Formats conversation history + current query, sends to Gemini Flash
        with rewriting instructions. Returns the standalone version.

        Args:
            query: User's follow-up question
            history: Recent conversation messages from Redis

        Returns:
            Standalone version of the query
        """
        start_time = time.time()

        # Format history as readable conversation text
        history_text = ""
        for msg in history:
            role = "User" if msg["role"] == "user" else "Assistant"
            history_text += f"{role}: {msg['content']}\n"

        messages = [
            ChatMessage.from_system(REWRITE_SYSTEM_PROMPT),
            ChatMessage.from_user(
                f"Chat History:\n{history_text}\n"
                f"Latest Question: {query}\n\n"
                f"Rewrite the latest question as a standalone question:"
            )
        ]

        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(
            None,
            lambda: self.rewriter.run(messages=messages)
        )

        standalone = result["replies"][0].text.strip()
        elapsed = time.time() - start_time

        # Fallback if LLM returns empty
        if not standalone:
            standalone = query

        print(f"   Query rewritten ({elapsed:.2f}s): '{query[:40]}' -> '{standalone[:40]}'")

        return standalone

    # -------------------------------------------------------------------
    # Health & Info
    # -------------------------------------------------------------------

    def is_healthy(self) -> bool:
        """Check if Redis connection is operational."""
        try:
            self.redis_client.ping()
            return True
        except Exception:
            return False

    def get_session_info(self, session_id: str) -> Optional[Dict[str, Any]]:
        """
        Get metadata about a conversation session.

        Useful for monitoring and the metrics endpoint.

        Args:
            session_id: Session identifier

        Returns:
            Dict with created_at, last_active, total_messages.
            None if session doesn't exist or has expired.
        """
        meta_key = f"{self.SESSION_PREFIX}{session_id}:meta"
        meta = self.redis_client.hgetall(meta_key)

        if not meta:
            return None

        return {
            "session_id": session_id,
            "created_at": float(meta.get("created_at", 0)),
            "last_active": float(meta.get("last_active", 0)),
            "total_messages": int(meta.get("total_messages", 0)),
        }


# ---------------------------------------------------------------------------
# Singleton accessor
# ---------------------------------------------------------------------------

_conversation_service: Optional[ConversationService] = None


def get_conversation_service() -> ConversationService:
    """
    Get or create the global conversation service instance.

    Singleton ensures we initialize the Redis connection and LLM rewriter
    exactly once across all requests.
    """
    global _conversation_service
    if _conversation_service is None:
        _conversation_service = ConversationService()
    return _conversation_service
