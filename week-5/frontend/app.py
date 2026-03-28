# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Production Streamlit Chat Frontend
============================================

Clean, user-facing chat interface for the production RAG system.

Features:
- Streamlit native chat components (st.chat_message, st.chat_input, st.feedback)
- Welcome screen with suggestion chips (disappear after first message)
- Conversation memory via session_id
- Real-time streaming responses via SSE
- Query rewrite indicator ("Interpreted as: ...")
- Inline thumbs up/down feedback with detailed dialog on thumbs-down
- Collapsible source citations
- Persistent disclaimer footer
- Minimal sidebar with New Chat + toggles

All developer metrics (cache stats, latency, cost, query type) are
available through the backend /metrics endpoint and Opik traces —
not cluttering the user-facing chat.
"""

import os
import streamlit as st
import requests
import json
import uuid
from typing import Optional, Dict, Any


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

API_BASE_URL = os.environ.get("API_BASE_URL", "http://localhost:8000")

st.set_page_config(
    page_title="ProbablAI",
    page_icon="🎲",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Minimal CSS
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Disclaimer below chat input */
    [data-testid="stBottomBlockContainer"]::after {
        content: "Responses are AI-generated and may contain errors. Please verify important information.";
        display: block;
        text-align: center;
        font-size: 0.7rem;
        color: #888;
        padding: 4px 0 8px 0;
    }
</style>
""", unsafe_allow_html=True)

# Starter suggestions shown on empty state
SUGGESTIONS = [
    {"label": "What is Bayes' theorem?", "prompt": "What is Bayes' theorem and how is it applied?"},
    {"label": "Central Limit Theorem", "prompt": "Explain the Central Limit Theorem and when it applies."},
    {"label": "Expected value & variance", "prompt": "What is the relationship between expected value, variance, and standard deviation?"},
    {"label": "Simulate a distribution", "prompt": "Show me Python code to simulate and plot a binomial distribution."},
]


# ---------------------------------------------------------------------------
# Session State
# ---------------------------------------------------------------------------

def init_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "session_id" not in st.session_state:
        st.session_state.session_id = f"sess_{uuid.uuid4().hex}"
    if "use_cache" not in st.session_state:
        st.session_state.use_cache = True
    if "use_streaming" not in st.session_state:
        st.session_state.use_streaming = True
    if "pending_negative_feedback" not in st.session_state:
        st.session_state.pending_negative_feedback = None
    if "pending_query" not in st.session_state:
        st.session_state.pending_query = None


# ---------------------------------------------------------------------------
# API Helpers
# ---------------------------------------------------------------------------

def check_api_health() -> bool:
    """Check if the backend API is healthy."""
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=3)
        return response.status_code == 200 and response.json().get("status") == "healthy"
    except Exception:
        return False


def send_query(query: str, session_id: str, use_cache: bool) -> Optional[Dict[str, Any]]:
    """Send a standard (non-streaming) query to the backend."""
    try:
        response = requests.post(
            f"{API_BASE_URL}/query",
            json={"query": query, "session_id": session_id, "use_cache": use_cache},
            timeout=120,
        )
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API error: {response.status_code} - {response.text[:200]}")
    except Exception as e:
        st.error(f"Request failed: {str(e)}")
    return None


def send_feedback(session_id: str, msg_id: str, rating: str, query: str, answer: str,
                  comment: str = "", reason: str = "", metadata: Optional[Dict] = None):
    """Send feedback to the backend. Silent on failure."""
    feedback_metadata = metadata or {}
    if reason:
        feedback_metadata["reason"] = reason
    try:
        requests.post(
            f"{API_BASE_URL}/feedback",
            json={
                "session_id": session_id,
                "msg_id": msg_id,
                "rating": rating,
                "query": query,
                "answer": answer,
                "comment": comment,
                "metadata": feedback_metadata,
            },
            timeout=5,
        )
    except Exception:
        pass


def send_streaming_query(query: str, session_id: str, use_cache: bool) -> Optional[Dict[str, Any]]:
    """Send a streaming query and display results in real-time via SSE."""
    try:
        response = requests.post(
            f"{API_BASE_URL}/query/stream",
            json={"query": query, "session_id": session_id, "use_cache": use_cache},
            stream=True,
            headers={"Accept": "text/event-stream"},
            timeout=120,
        )

        if response.status_code != 200:
            st.error(f"API error: {response.status_code}")
            return None

        answer_tokens = []
        contexts = []
        metadata = {}
        event_type = ""
        rewrite_info = None

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Thinking...")

            for line in response.iter_lines():
                if not line:
                    continue

                decoded = line.decode("utf-8")

                if decoded.startswith("event:"):
                    event_type = decoded.split(":", 1)[1].strip()
                elif decoded.startswith("data:"):
                    data_str = decoded.split(":", 1)[1].strip()
                    try:
                        data = json.loads(data_str)
                    except json.JSONDecodeError:
                        continue

                    if event_type == "rewrite":
                        rewrite_info = data

                    elif event_type == "context":
                        contexts.append(data)

                    elif event_type == "token":
                        token = data.get("token", "")
                        answer_tokens.append(token)
                        message_placeholder.markdown("".join(answer_tokens))

                    elif event_type == "done":
                        metadata = data

                    elif event_type == "error":
                        st.error(f"Something went wrong: {data.get('error', 'Unknown')}")
                        return None

            if not answer_tokens:
                message_placeholder.empty()

            # Show rewrite indicator after streaming completes
            if rewrite_info:
                standalone = rewrite_info.get("standalone", "")
                if standalone and standalone != query:
                    st.caption(f'Interpreted as: "{standalone}"')

        # Merge rewrite info into metadata
        if rewrite_info:
            metadata["is_follow_up"] = True
            metadata["standalone_query"] = rewrite_info.get("standalone", "")

        return {
            "answer": "".join(answer_tokens),
            "contexts": contexts,
            "metadata": metadata,
            "session_id": metadata.get("session_id", session_id),
            "msg_id": metadata.get("msg_id", ""),
        }

    except Exception as e:
        st.error(f"Streaming failed: {str(e)}")
        return None


# ---------------------------------------------------------------------------
# Feedback — thumbs up instant, thumbs down opens dialog
# ---------------------------------------------------------------------------

@st.dialog("Help us improve", width="small")
def negative_feedback_dialog(message_index: int):
    """Modal dialog shown after thumbs-down. Skippable via X or ESC."""
    st.write("What went wrong with this response?")

    reason = st.radio(
        "Select a reason:",
        options=[
            "Incorrect or inaccurate",
            "Not helpful or relevant",
            "Didn't follow instructions",
            "Too short or incomplete",
            "Too long or verbose",
            "Other",
        ],
        index=None,
    )

    comment = st.text_area(
        "Additional comments (optional):",
        placeholder="Tell us more about what went wrong...",
        height=100,
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Submit", type="primary", use_container_width=True):
            message = st.session_state.messages[message_index]
            message["feedback"] = "down"
            send_feedback(
                session_id=st.session_state.session_id,
                msg_id=message.get("msg_id", ""),
                rating="down",
                query=message.get("query", ""),
                answer=message.get("content", ""),
                reason=reason or "",
                comment=comment.strip() if comment else "",
                metadata=message.get("metadata"),
            )
            st.rerun()
    with col2:
        if st.button("Skip", use_container_width=True):
            message = st.session_state.messages[message_index]
            message["feedback"] = "down"
            send_feedback(
                session_id=st.session_state.session_id,
                msg_id=message.get("msg_id", ""),
                rating="down",
                query=message.get("query", ""),
                answer=message.get("content", ""),
                metadata=message.get("metadata"),
            )
            st.rerun()


def handle_feedback(message_index: int):
    """Callback: thumbs up records instantly, thumbs down flags for dialog."""
    feedback_value = st.session_state.get(f"feedback_{message_index}")
    if feedback_value is None:
        return

    message = st.session_state.messages[message_index]

    if feedback_value == 1:
        # Thumbs up — record immediately, no dialog
        message["feedback"] = "up"
        send_feedback(
            session_id=st.session_state.session_id,
            msg_id=message.get("msg_id", ""),
            rating="up",
            query=message.get("query", ""),
            answer=message.get("content", ""),
            metadata=message.get("metadata"),
        )
    elif feedback_value == 0:
        # Thumbs down — flag to open dialog on next rerun
        st.session_state.pending_negative_feedback = message_index


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------

def display_sidebar():
    """Minimal sidebar — settings only, no metrics."""
    with st.sidebar:
        if st.button("New Chat", use_container_width=True, type="primary"):
            st.session_state.messages = []
            st.session_state.session_id = f"sess_{uuid.uuid4().hex}"
            st.rerun()

        st.divider()

        st.toggle("Semantic Cache", key="use_cache",
                   help="Cache similar queries for faster responses")
        st.toggle("Stream Responses", key="use_streaming",
                   help="Show responses as they generate")

        st.divider()
        st.caption(f"Session: {st.session_state.session_id[:12]}...")


def display_welcome():
    """Welcome screen with greeting and suggestion chips. Shown only when chat is empty."""
    st.markdown(
        """
        <div style="text-align: center; padding: 80px 0 20px 0;">
            <h2 style="font-weight: 600;">
                What can I help you with?
            </h2>
            <p style="color: #888; font-size: 0.95rem;">
                Ask me anything about probability and statistics — theorems, distributions, inference, and worked examples.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Suggestion chips — 2 rows of 2
    row1 = st.columns(2)
    for i, col in enumerate(row1):
        s = SUGGESTIONS[i]
        with col:
            if st.button(s["label"], key=f"suggestion_{i}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": s["prompt"]})
                st.session_state.pending_query = s["prompt"]
                st.rerun()

    row2 = st.columns(2)
    for i, col in enumerate(row2):
        s = SUGGESTIONS[i + 2]
        with col:
            if st.button(s["label"], key=f"suggestion_{i + 2}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": s["prompt"]})
                st.session_state.pending_query = s["prompt"]
                st.rerun()


def display_chat_history():
    """Render chat history with rewrite indicator, sources, and feedback."""
    for i, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if message["role"] == "assistant":
                metadata = message.get("metadata", {})

                # Rewrite indicator
                standalone = metadata.get("standalone_query")
                if metadata.get("is_follow_up") and standalone:
                    st.caption(f'Interpreted as: "{standalone}"')

                # Sources — collapsed by default
                contexts = message.get("contexts", [])
                if contexts:
                    with st.expander(f"Sources ({len(contexts)})"):
                        for ctx in contexts:
                            file_path = ctx.get("metadata", {}).get("file_path", "unknown")
                            content = ctx.get("content", "")
                            st.markdown(f"**{file_path}**")
                            st.caption(content[:300] + ("..." if len(content) > 300 else ""))
                            st.divider()

                # Inline feedback — thumbs up/down
                msg_id = message.get("msg_id", "")
                if msg_id:
                    existing_feedback = message.get("feedback")
                    st.feedback(
                        "thumbs",
                        key=f"feedback_{i}",
                        disabled=existing_feedback is not None,
                        on_change=handle_feedback,
                        args=[i],
                    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    """Main chat application."""
    init_session_state()

    # Backend health check
    if not check_api_health():
        st.error("**Backend API is offline.**")
        st.code("cd week5_production/backend\npython -m app.main", language="bash")
        st.stop()

    # Sidebar
    display_sidebar()

    # Welcome screen or chat history
    if not st.session_state.messages:
        display_welcome()
    else:
        display_chat_history()

    # Chat input (or pick up pending query from suggestion chips)
    prompt = st.chat_input("Ask a question...")

    # Merge: suggestion chip click sets pending_query (user message already added by chip handler)
    pending = st.session_state.pending_query
    if pending:
        prompt = pending
        st.session_state.pending_query = None

    if prompt:
        # Display user message — only append + render if typed (chips already added it)
        if not pending:
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

        # Get response
        result = None
        if st.session_state.use_streaming:
            result = send_streaming_query(
                prompt, st.session_state.session_id, st.session_state.use_cache
            )
        else:
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    result = send_query(
                        prompt, st.session_state.session_id, st.session_state.use_cache
                    )
                if result:
                    st.markdown(result["answer"])

        # Store assistant response
        if result:
            if result.get("session_id"):
                st.session_state.session_id = result["session_id"]

            st.session_state.messages.append({
                "role": "assistant",
                "content": result["answer"],
                "query": prompt,
                "msg_id": result.get("msg_id", ""),
                "metadata": result.get("metadata", {}),
                "contexts": result.get("contexts", []),
            })

            st.rerun()

    # Open negative feedback dialog if flagged
    if st.session_state.pending_negative_feedback is not None:
        idx = st.session_state.pending_negative_feedback
        st.session_state.pending_negative_feedback = None
        negative_feedback_dialog(idx)


if __name__ == "__main__":
    main()
