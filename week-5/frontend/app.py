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
import re
import html
from typing import Optional, Dict, Any


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

API_BASE_URL = "https://rag-accelerator.onrender.com"
PORT = os.environ.get("PORT", 8000)

st.set_page_config(
    page_title="ProbablAI | Academic Probability Copilot",
    page_icon="🎲",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Professional theme CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=Fraunces:opsz,wght@9..144,500;9..144,600&display=swap');

    :root {
        --bg: #f4f8f8;
        --surface: #ffffff;
        --ink: #173042;
        --muted: #587283;
        --line: #d2e4e3;
        --brand: #0f7b7b;
        --brand-2: #219e9e;
        --accent: #f08a4b;
        --bot-bg: #f2fcfb;
        --user-bg: #edf7fb;
        --hero-a: #e7f7f5;
        --hero-b: #fff6ec;
    }

    .stApp {
        background:
            radial-gradient(1000px 400px at -10% -20%, var(--hero-a), transparent 70%),
            radial-gradient(900px 380px at 110% -25%, var(--hero-b), transparent 68%),
            linear-gradient(180deg, #f7fbff 0%, var(--bg) 60%, #f1f6fb 100%);
        color: var(--ink);
    }

    /* Force readable text in the main content area */
    .stApp,
    .stApp p,
    .stApp li,
    .stApp label,
    .stApp small,
    .stApp span,
    .stApp div,
    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4 {
        color: var(--ink);
    }

    .stApp a {
        color: #0b6686;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #103344 0%, #0d2a35 100%);
    }

    [data-testid="stSidebar"] * {
        color: #d7e7f2 !important;
    }

    /* Streamlit top header controls: >>, Stop, menu */
    header[data-testid="stHeader"] {
        background: rgba(248, 252, 255, 0.92) !important;
        border-bottom: 1px solid #d8e5ef !important;
        backdrop-filter: blur(4px);
    }

    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"] {
        color: #1d3f55 !important;
    }

    [data-testid="stToolbar"] button,
    [data-testid="stStatusWidget"] button,
    header[data-testid="stHeader"] button,
    button[title="View app menu"],
    button[title="Stop"],
    button[title="Rerun"] {
        background: #ffffff !important;
        color: #1d3f55 !important;
        border: 1px solid #c9dbe8 !important;
    }

    [data-testid="stToolbar"] button:hover,
    [data-testid="stStatusWidget"] button:hover,
    header[data-testid="stHeader"] button:hover,
    button[title="View app menu"]:hover,
    button[title="Stop"]:hover,
    button[title="Rerun"]:hover {
        background: #edf6fd !important;
        color: #0f6e8c !important;
        border-color: #9fc2d8 !important;
    }

    [data-testid="stToolbar"] button svg,
    [data-testid="stStatusWidget"] button svg,
    header[data-testid="stHeader"] button svg {
        fill: currentColor !important;
        stroke: currentColor !important;
        color: inherit !important;
    }

    [data-testid="stSidebar"] button[kind="primary"] {
        background: linear-gradient(135deg, #219e9e, #0f7b7b) !important;
        border: none !important;
        color: #ffffff !important;
    }

    [data-testid="stSidebar"] [data-testid="stButton"] button[kind="secondary"],
    [data-testid="stSidebar"] [data-testid="baseButton-secondary"],
    [data-testid="stSidebar"] [data-baseweb="button"] {
        color: #e6f3fb !important;
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(214, 234, 246, 0.35) !important;
    }

    [data-testid="stSidebar"] .st-emotion-cache-1b2w7b3,
    [data-testid="stSidebar"] .st-emotion-cache-hc3laj,
    [data-testid="stSidebar"] label {
        color: #d7e7f2 !important;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .app-shell {
        border: 1px solid var(--line);
        border-radius: 20px;
        background: linear-gradient(145deg, rgba(255,255,255,0.9), rgba(255,255,255,0.75));
        box-shadow: 0 20px 50px rgba(15, 47, 70, 0.08);
        padding: 16px 18px;
        margin-bottom: 18px;
        backdrop-filter: blur(6px);
    }

    .brand-title {
        font-family: 'Sora', sans-serif;
        font-weight: 800;
        font-size: 1.35rem;
        line-height: 1.2;
        color: var(--ink);
        margin: 0;
        letter-spacing: -0.02em;
    }

    .brand-subtitle {
        font-family: 'Fraunces', serif;
        color: var(--muted);
        font-size: 0.96rem;
        margin-top: 4px;
        margin-bottom: 0;
    }

    .hero-lockup {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 8px 14px;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.72);
        border: 1px solid #d4e4ec;
        box-shadow: 0 8px 24px rgba(16, 52, 68, 0.08);
        margin-bottom: 14px;
    }

    .hero-mark {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 36px;
        height: 36px;
        border-radius: 12px;
        background: linear-gradient(135deg, #219e9e, #0f7b7b);
        color: #ffffff;
        font-size: 1.1rem;
        box-shadow: 0 10px 18px rgba(15, 123, 123, 0.2);
    }

    .hero-kicker {
        font-family: 'Sora', sans-serif;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #255069;
    }

    .badge-row {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 12px;
    }

    .badge {
        font-family: 'Sora', sans-serif;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.03em;
        border-radius: 999px;
        padding: 6px 11px;
        border: 1px solid #c6d8e5;
        color: #1f3e53;
        background: #f5fbff;
    }

    .badge-accent {
        border-color: #ffd1b5;
        background: #fff4ec;
        color: #8a3f28;
    }

    [data-testid="stChatMessage"] {
        border: 1px solid var(--line);
        border-radius: 16px;
        padding: 2px 6px;
        margin-bottom: 10px;
    }

    [data-testid="stChatMessage"][aria-label="Chat message from assistant"] {
        background: linear-gradient(180deg, var(--bot-bg) 0%, #ffffff 100%);
    }

    [data-testid="stChatMessage"][aria-label="Chat message from user"] {
        background: linear-gradient(180deg, var(--user-bg) 0%, #ffffff 100%);
    }

    [data-testid="stChatInputTextArea"] textarea {
        border-radius: 12px !important;
        border: 1px solid #bed2df !important;
        background: #ffffff !important;
        color: var(--ink) !important;
    }

    [data-testid="stChatInputTextArea"] textarea::placeholder {
        color: #6d8292 !important;
    }

    [data-testid="stTextArea"] textarea,
    [data-testid="stTextInput"] input {
        background: #ffffff !important;
        color: var(--ink) !important;
        border: 1px solid #bed2df !important;
    }

    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] summary span,
    [data-testid="stExpanderDetails"] {
        color: var(--ink) !important;
    }

    [data-testid="stButton"] button,
    [data-testid="baseButton-secondary"] {
        color: #143247 !important;
        border-color: #c3d5e2 !important;
        background: #f9fcff !important;
    }

    [data-testid="stButton"] button[kind="primary"],
    [data-testid="baseButton-primary"] {
        background: linear-gradient(135deg, #219e9e, #0f7b7b) !important;
        color: #ffffff !important;
        border: none !important;
    }

    /* Improve readability for top-level tabs / segmented controls if present */
    [data-baseweb="tab"] {
        color: #1c3b50 !important;
    }

    [aria-selected="true"][data-baseweb="tab"] {
        color: #0f6e8c !important;
        font-weight: 600 !important;
    }

    /* Ensure icon-only action buttons (feedback/menu style) stay visible */
    button[title],
    [data-testid="stToolbar"] button,
    [data-testid="stElementToolbar"] button {
        color: #204359 !important;
    }

    .source-card {
        border: 1px solid #d8e6f0;
        border-left: 4px solid var(--brand);
        border-radius: 10px;
        padding: 10px 12px;
        margin: 8px 0;
        background: #fbfdff;
    }

    .source-title {
        font-family: 'Sora', sans-serif;
        font-size: 0.88rem;
        font-weight: 600;
        color: #16354a;
    }

    .source-snippet {
        color: #5b7181;
        font-size: 0.83rem;
        line-height: 1.45;
        margin-top: 6px;
    }

    .welcome-title {
        font-family: 'Fraunces', serif;
        font-size: 2rem;
        line-height: 1.15;
        margin-bottom: 8px;
        letter-spacing: -0.02em;
    }

    .welcome-text {
        font-family: 'Fraunces', serif;
        color: var(--muted);
        font-size: 1.03rem;
        max-width: 680px;
        margin: 0 auto;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Disclaimer below chat input */
    [data-testid="stBottomBlockContainer"]::after {
        content: "ProbablAI is an AI chatbot grounded in curated academic probability resources (MIT, OpenIntro, OCR notes, and course materials). Verify important decisions with primary sources.";
        display: block;
        text-align: center;
        font-size: 0.72rem;
        color: #5f7383;
        padding: 5px 0 9px 0;
    }

    @media (max-width: 640px) {
        .welcome-title {
            font-size: 1.6rem;
        }
        .app-shell {
            border-radius: 14px;
            padding: 12px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Starter suggestions shown on empty state
SUGGESTIONS = [
    {"label": "🎲 Bayes' theorem", "prompt": "What is Bayes' theorem and how is it applied?"},
    {"label": "📊 Central Limit Theorem", "prompt": "Explain the Central Limit Theorem and when it applies."},
    {"label": "📐 Expected value & variance", "prompt": "What is the relationship between expected value, variance, and standard deviation?"},
    {"label": "🐍 Simulate a distribution", "prompt": "Show me Python code to simulate and plot a binomial distribution."},
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
    candidate_urls = [API_BASE_URL]
    # Localhost can resolve inconsistently on some systems; try loopback fallback.
    # if API_BASE_URL == "http://localhost:8000":
    #     candidate_urls.append("http://127.0.0.1:8000")
    # elif API_BASE_URL == "http://127.0.0.1:8000":
    #     candidate_urls.append("http://localhost:8000")
    # for base in candidate_urls:
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=3)
        if response.status_code == 200 and response.json().get("status") == "healthy":
            return True
    except Exception:
        continue
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


def build_feedback_metadata(message: Dict[str, Any], reason: str = "") -> Dict[str, Any]:
    """Build a stable feedback metadata payload with trace/linkage fields."""
    raw = message.get("metadata") or {}
    payload: Dict[str, Any] = dict(raw) if isinstance(raw, dict) else {}

    # Preserve key linkage fields even if upstream metadata shape changes.
    payload.setdefault("trace_id", raw.get("trace_id") if isinstance(raw, dict) else "")
    payload.setdefault("stream_mode", raw.get("stream_mode") if isinstance(raw, dict) else "")
    payload.setdefault("query_type", raw.get("query_type") if isinstance(raw, dict) else "")
    payload.setdefault("cache_hit", raw.get("cache_hit") if isinstance(raw, dict) else None)

    if reason:
        payload["reason"] = reason

    return payload


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
                        # Blinking cursor while streaming
                        message_placeholder.markdown("".join(answer_tokens) + " ▍")

                    elif event_type == "done":
                        metadata = data

                    elif event_type == "error":
                        st.error(f"Something went wrong: {data.get('error', 'Unknown')}")
                        return None

            if answer_tokens:
                # Remove cursor on completion
                message_placeholder.markdown("".join(answer_tokens))
            else:
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
                metadata=build_feedback_metadata(message, reason=reason or ""),
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
                metadata=build_feedback_metadata(message),
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
            metadata=build_feedback_metadata(message),
        )
    elif feedback_value == 0:
        # Thumbs down — flag to open dialog on next rerun
        st.session_state.pending_negative_feedback = message_index


def extract_source_label(metadata: Any) -> str:
    """Extract a clean source label from metadata dict or serialized dict-like string."""
    if isinstance(metadata, dict):
        raw = metadata.get("file_path", "")
    elif isinstance(metadata, str):
        match = re.search(r"file_path=([^;]+)", metadata)
        raw = match.group(1).strip() if match else ""
    else:
        raw = ""

    if not raw:
        return "MIT resource"

    # Return a clean human-readable label: filename without extension, underscores → spaces
    return os.path.splitext(os.path.basename(raw))[0].replace("_", " ")


def display_brand_header():
    """Show branded product header and trust context."""
    st.markdown(
        """
        <div class="app-shell">
            <p class="brand-title">ProbablAI: Academic Probability Copilot</p>
            <p class="brand-subtitle">
                A grounded reasoning copilot for probability and statistics, designed for course study, follow-up exploration, and source-backed answers.
            </p>
            <div class="badge-row">
                <span class="badge">Grounded in MIT + OpenIntro</span>
                <span class="badge">Follow-Up Memory</span>
                <span class="badge badge-accent">Cited Source Excerpts</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


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

        st.caption("Assistant settings")

        st.toggle("Semantic Cache", key="use_cache",
                   help="Cache similar queries for faster responses")
        st.toggle("Stream Responses", key="use_streaming",
                   help="Show responses as they generate")

        st.divider()
        st.caption("Knowledge scope")
        st.write("MIT, OpenIntro, OCR notes, and curated probability/statistics resources")
        st.markdown(
            f'<code style="font-size:0.75rem;background:rgba(255,255,255,0.12);'
            f'color:#b8d8ee;border-radius:6px;padding:3px 8px;border:1px solid rgba(255,255,255,0.15);">'
            f'🔑 {st.session_state.session_id[:14]}...</code>',
            unsafe_allow_html=True,
        )


def display_welcome():
    """Welcome screen with greeting and suggestion chips. Shown only when chat is empty."""
    st.markdown(
        """
        <div style="text-align: center; padding: 56px 0 18px 0;">
            <div class="hero-lockup">
                <span class="hero-mark">🎲</span>
                <span class="hero-kicker">ProbablAI Academic Copilot</span>
            </div>
            <h2 class="welcome-title">
                Your source-grounded probability copilot
            </h2>
            <p class="welcome-text">
                Ask questions, test intuition, and iterate with follow-ups.
                Responses are generated by AI and grounded in indexed academic materials including MIT notes,
                OpenIntro text, and processed course resources, with cited source excerpts attached.
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
                    st.caption(f'🔄 Interpreted as: "{standalone}"')

                # Query type badge (cache-miss only) + cache hit badge
                if metadata.get("cache_hit"):
                    st.caption("🟢 Served from semantic cache")
                elif metadata.get("query_type"):
                    st.caption(f"🔵 Query type: {metadata['query_type']}")

                # Sources — collapsed by default
                contexts = message.get("contexts", [])
                if contexts:
                    _top_score = contexts[0].get("score", 0) if contexts else 0
                    _score_str = f" · top match {_top_score:.2f}" if _top_score else ""
                    with st.expander(f"Sources ({len(contexts)}){_score_str}"):
                        for idx, ctx in enumerate(contexts, start=1):
                            source_label = extract_source_label(ctx.get("metadata", {}))
                            score = ctx.get("score", None)
                            score_pill = (
                                f'<span style="float:right;font-size:0.72rem;background:#e8f4f0;'
                                f'color:#0f7b7b;border:1px solid #b8ddd8;border-radius:999px;'
                                f'padding:1px 7px;font-weight:600;">{score:.2f}</span>'
                                if score is not None else ""
                            )
                            content = ctx.get("content", "")
                            safe_source_name = html.escape(source_label)
                            preview = content[:300] + ("..." if len(content) > 300 else "")
                            safe_preview = html.escape(preview)
                            st.markdown(
                                f"""
                                <div class="source-card">
                                    <div class="source-title">{score_pill}{idx}. {safe_source_name}</div>
                                    <div class="source-snippet">{safe_preview}</div>
                                </div>
                                """,
                                unsafe_allow_html=True,
                            )

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
        st.caption("Tried API endpoint(s):")
        st.code(API_BASE_URL, language="text")
        st.code(f"cd week-5/backend\npython -m uvicorn app.main:app --host {API_BASE_URL} --port {PORT}", language="bash")
        if st.button("Retry connection", use_container_width=True):
            st.rerun()
        st.stop()

    # Sidebar
    display_sidebar()
    display_brand_header()

    # Welcome screen or chat history.
    # Keep suggestion chips visible until the first successful assistant response,
    # so an early backend error doesn't permanently hide the starter prompts.
    _has_response = any(m["role"] == "assistant" for m in st.session_state.messages)
    if not _has_response:
        if st.session_state.messages:
            display_chat_history()   # show any pending user message(s)
        display_welcome()            # chips stay visible until first response
    else:
        display_chat_history()

    # Chat input (or pick up pending query from suggestion chips)
    prompt = st.chat_input("Ask about a theorem, proof idea, distribution, or worked MIT example...")

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
                    # Show rewrite indicator immediately (same timing as streaming path)
                    _meta = result.get("metadata", {})
                    if _meta.get("is_follow_up") and _meta.get("standalone_query"):
                        _sq = _meta["standalone_query"]
                        if _sq and _sq != prompt:
                            st.caption(f'Interpreted as: "{_sq}"')

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
