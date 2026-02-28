# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 2: Chunk Quality Evaluation Viewer
========================================

Streamlit app for viewing LLM-as-judge chunk quality evaluations.
Displays Stage 1 (per-chunk analysis) and Stage 2 (ranking) results
with side-by-side strategy comparison.

Usage:
    streamlit run week2_chunking/experiments/07_chunk_eval_viewer.py
"""

import streamlit as st
import json
from pathlib import Path
from typing import Dict, List

# Path resolution
SCRIPT_DIR = Path(__file__).resolve().parent
WEEK_DIR = SCRIPT_DIR.parent
RAG_RESULTS_DIR = WEEK_DIR / "rag_results"
EVALUATIONS_DIR = WEEK_DIR / "evaluations"

# Page config
st.set_page_config(
    page_title="Week 2: Chunk Quality Evaluation",
    page_icon="🔬",
    layout="wide"
)


def load_evaluation_file(file_path: str) -> Dict:
    """Load evaluation results from JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)


def load_rag_results(strategy: str) -> Dict:
    """Load RAG results for a strategy.

    Uses precise matching to avoid naive_medium matching naive_medium_voyage.
    """
    import re
    pattern = re.compile(rf"rag_results_{re.escape(strategy)}_\d{{8}}_\d{{6}}\.json$")
    files = [f for f in RAG_RESULTS_DIR.iterdir() if f.is_file() and pattern.match(f.name)]
    if not files:
        return None
    latest = sorted(files)[-1]
    with open(latest, 'r') as f:
        return json.load(f)


def get_relevance_icon(signal_pct: int) -> str:
    """Get icon based on signal percentage."""
    if signal_pct >= 80:
        return "🟢"
    elif signal_pct >= 50:
        return "🟡"
    else:
        return "🔴"


def render_summary_row(strategies: List[str], result: Dict):
    """Render Stage 2 ranking summary with equal-height columns."""

    stage2 = result.get("stage2_ranking", {})
    ranking = stage2.get("ranking", {})
    reasoning = stage2.get("reasoning", "")
    key_insight = stage2.get("key_insight", "")

    # Ranking badges
    cols = st.columns(len(strategies))
    for idx, strategy in enumerate(strategies):
        with cols[idx]:
            # Find rank for this strategy
            rank = None
            for r, s in ranking.items():
                if s.lower() == strategy.lower():
                    rank = r
                    break

            if rank == "1st":
                st.success(f"🥇 **{strategy.upper()}** - 1st Place")
            elif rank == "2nd":
                st.warning(f"🥈 **{strategy.upper()}** - 2nd Place")
            elif rank == "3rd":
                st.info(f"🥉 **{strategy.upper()}** - 3rd Place")
            else:
                st.write(f"**{strategy.upper()}**")

    # Reasoning
    if reasoning:
        st.markdown("---")
        st.markdown(f"**Reasoning:** {reasoning}")
    if key_insight:
        st.caption(f"**Key Insight:** {key_insight}")


def render_metrics_row(strategies: List[str], result: Dict):
    """Render Stage 1 summary metrics with equal-height columns."""

    stage1 = result.get("stage1_analyses", {})

    # First row: metrics
    cols = st.columns(len(strategies))
    for idx, strategy in enumerate(strategies):
        with cols[idx]:
            analysis = stage1.get(strategy, {})
            summary = analysis.get("summary", {})

            cut_count = summary.get("cut_mid_answer_count", "?")
            avg_signal = summary.get("avg_signal_pct", "?")
            high_useful = summary.get("high_useful_count", "?")

            st.markdown(f"**{strategy}**")

            m1, m2, m3 = st.columns(3)
            m1.metric("Cuts", cut_count, help="Chunks cut mid-answer")
            m2.metric("Signal", f"{avg_signal}%", help="Avg signal percentage")
            m3.metric("High", high_useful, help="High usefulness count")

    # Second row: assessments in styled boxes (equal height)
    cols = st.columns(len(strategies))
    for idx, strategy in enumerate(strategies):
        with cols[idx]:
            analysis = stage1.get(strategy, {})
            summary = analysis.get("summary", {})
            assessment = summary.get("assessment", "")

            with st.container(height=150):
                st.info(assessment if assessment else "No assessment available")


def render_chunk_analysis_row(strategies: List[str], result: Dict, chunk_idx: int, rag_results: Dict):
    """Render per-chunk analysis with equal-height columns."""

    stage1 = result.get("stage1_analyses", {})

    cols = st.columns(len(strategies))
    for idx, strategy in enumerate(strategies):
        with cols[idx]:
            analysis = stage1.get(strategy, {})
            chunks_data = analysis.get("chunks", {})
            chunk_analysis = chunks_data.get(str(chunk_idx), {})

            # Get actual chunk content from RAG results
            chunk_content = ""
            chunk_file = "unknown"
            chunk_score = 0

            if rag_results.get(strategy):
                question_id = result.get("question_id")
                for r in rag_results[strategy].get("results", []):
                    if r.get("question_id") == question_id:
                        contexts = r.get("retrieved_contexts", [])
                        if chunk_idx <= len(contexts):
                            ctx = contexts[chunk_idx - 1]
                            chunk_content = ctx.get("content", "")
                            chunk_file = Path(ctx.get("metadata", {}).get("file_path", "unknown")).name
                            chunk_score = ctx.get("score", 0)
                        break

            # Analysis values
            cut = chunk_analysis.get("cut_mid_answer", False)
            signal = chunk_analysis.get("signal_pct", 0)
            useful = chunk_analysis.get("useful", "?")
            note = chunk_analysis.get("note", "")

            # Fixed height for chunk header
            cut_icon = "✂️" if cut else "✓"
            signal_icon = get_relevance_icon(signal)
            useful_color = {"high": "🟢", "medium": "🟡", "low": "🔴"}.get(useful, "⚪")

            st.markdown(f"**Chunk {chunk_idx}** {cut_icon} {signal_icon} {useful_color}")
            st.caption(f"{chunk_file} | score: {chunk_score:.3f}")

            # Metrics row
            c1, c2, c3 = st.columns(3)
            c1.caption(f"Cut: {'Yes' if cut else 'No'}")
            c2.caption(f"Signal: {signal}%")
            c3.caption(f"Useful: {useful}")

            # Note (full reasoning)
            if note:
                st.markdown(f"**Analysis:** _{note}_")

            # Content expander
            with st.expander("View content", expanded=False):
                st.text_area(
                    "Content",
                    value=chunk_content,
                    height=200,
                    key=f"chunk_{strategy}_{result.get('question_id')}_{chunk_idx}",
                    disabled=True,
                    label_visibility="collapsed"
                )


def main():
    st.title("🔬 Week 2: Chunk Quality Evaluation Viewer")
    st.caption("LLM-as-judge evaluation: Stage 1 (per-chunk) + Stage 2 (ranking)")

    # Sidebar
    with st.sidebar:
        st.header("📂 Load Evaluation")

        if not EVALUATIONS_DIR.exists():
            st.error("No evaluations directory found")
            st.info("Run 05_chunk_quality_eval.py first")
            return

        eval_files = [f for f in EVALUATIONS_DIR.glob("hybrid_chunk_eval_*.json")]

        if not eval_files:
            st.error("No hybrid chunk evaluation files found")
            st.info("Run 05_chunk_quality_eval.py first")
            return

        eval_file_names = [f.name for f in sorted(eval_files, reverse=True)]
        selected_file = st.selectbox("Evaluation file:", eval_file_names, label_visibility="collapsed")

        if st.button("Load", type="primary", use_container_width=True):
            st.session_state.eval_data = load_evaluation_file(str(EVALUATIONS_DIR / selected_file))
            st.session_state.eval_file = selected_file
            st.session_state.current_question_idx = 0
            st.rerun()

        if 'eval_data' in st.session_state:
            st.markdown("---")
            eval_data = st.session_state.eval_data
            strategies = eval_data.get("strategies", [])

            st.caption(f"**Method:** {eval_data.get('evaluation_method', 'unknown')}")
            st.caption(f"**Model:** {eval_data.get('model', 'Unknown')}")
            st.caption(f"**Questions:** {eval_data.get('questions_evaluated', 0)}")
            st.caption(f"**Strategies:** {', '.join(strategies)}")

            # Ranking tally
            st.markdown("---")
            st.markdown("**🏆 Ranking Tally:**")

            ranking_tally = eval_data.get("ranking_tally", {})
            for strategy in strategies:
                tally = ranking_tally.get(strategy, {})
                first = tally.get("1st", 0)
                second = tally.get("2nd", 0)
                third = tally.get("3rd", 0)
                points = first * 3 + second * 2 + third * 1

                st.markdown(f"**{strategy}**")
                st.caption(f"🥇{first} 🥈{second} 🥉{third} = {points} pts")

            # Winner
            if ranking_tally:
                points_map = {
                    s: ranking_tally.get(s, {}).get("1st", 0) * 3 +
                       ranking_tally.get(s, {}).get("2nd", 0) * 2 +
                       ranking_tally.get(s, {}).get("3rd", 0) * 1
                    for s in strategies
                }
                winner = max(points_map.keys(), key=lambda s: points_map[s])
                st.success(f"**Winner:** {winner}")

    # Main content
    if 'eval_data' not in st.session_state:
        st.info("👈 Load an evaluation file from the sidebar")

        st.markdown("---")
        st.markdown("### How this evaluation works:")
        st.markdown("""
        **Two-Stage LLM-as-Judge Evaluation:**

        **Stage 1: Per-Chunk Analysis** (per strategy)
        - `cut_mid_answer`: Does the chunk cut off content needed to answer THE question?
        - `signal_pct`: What % of the chunk is relevant to THE question?
        - `useful`: Overall usefulness (high/medium/low)

        **Stage 2: Holistic Ranking**
        - Sees ALL Stage 1 analysis + ALL chunks
        - Makes nuanced tradeoff judgments
        - Ranks strategies 1st, 2nd, 3rd

        **The Story:**
        - Small chunks: May have higher signal but risk cut-offs
        - Large chunks: Fewer cut-offs but often diluted signal
        - Medium chunks: Balance both - the sweet spot
        """)
        return

    eval_data = st.session_state.eval_data
    strategies = eval_data.get("strategies", [])
    results = eval_data.get("results", [])

    # Load RAG results for chunk content
    rag_results = {s: load_rag_results(s) for s in strategies}

    if 'current_question_idx' not in st.session_state:
        st.session_state.current_question_idx = 0

    # Navigation
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        if st.button("⬅️ Prev", disabled=st.session_state.current_question_idx == 0, use_container_width=True):
            st.session_state.current_question_idx -= 1
            st.rerun()

    with col2:
        st.markdown(f"<h4 style='text-align: center;'>Question {st.session_state.current_question_idx + 1} / {len(results)}</h4>", unsafe_allow_html=True)

    with col3:
        if st.button("Next ➡️", disabled=st.session_state.current_question_idx >= len(results) - 1, use_container_width=True):
            st.session_state.current_question_idx += 1
            st.rerun()

    # Current result
    current_result = results[st.session_state.current_question_idx]
    question_text = current_result.get("question", "")

    st.markdown("---")
    st.markdown(f"### ❓ {question_text}")
    st.markdown("---")

    # Stage 2: Ranking summary
    st.markdown("## 🏆 Stage 2: Ranking")
    render_summary_row(strategies, current_result)

    st.markdown("---")

    # Stage 1: Summary metrics
    st.markdown("## 📊 Stage 1: Summary Metrics")
    render_metrics_row(strategies, current_result)

    st.markdown("---")

    # Stage 1: Per-chunk analysis
    st.markdown("## 📋 Stage 1: Per-Chunk Analysis")

    # Chunk selector
    chunk_options = list(range(1, 11))
    selected_chunks = st.multiselect(
        "Select chunks to view:",
        options=chunk_options,
        default=[1, 2, 3],
        help="Select which chunks to display side-by-side"
    )

    for chunk_idx in selected_chunks:
        st.markdown(f"---")
        render_chunk_analysis_row(strategies, current_result, chunk_idx, rag_results)


if __name__ == "__main__":
    main()
