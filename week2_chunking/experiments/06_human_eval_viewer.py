# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 2: Human Evaluation Viewer
================================

Streamlit app for HUMAN evaluation of RAG results across chunking strategies.
Students use this to manually evaluate and compare retrieval quality.

Features:
- Load multiple strategy results side-by-side
- Rate answer quality (1-5 scale)
- Mark context relevance (relevant/partial/irrelevant)
- Pick best answer per question (comparative evaluation)
- Add comments and notes
- Save/load evaluations
- Track progress

Usage:
    streamlit run week2_chunking/experiments/06_human_eval_viewer.py
"""

import streamlit as st
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List

# Path resolution
SCRIPT_DIR = Path(__file__).resolve().parent      # experiments/
WEEK_DIR = SCRIPT_DIR.parent                       # week2_chunking/
RAG_RESULTS_DIR = WEEK_DIR / "rag_results"
EVALUATIONS_DIR = WEEK_DIR / "human_evaluations"

# Page config
st.set_page_config(
    page_title="Week 2: Human RAG Evaluation",
    page_icon="📊",
    layout="wide"
)

# Initialize session state
if 'evaluation_data' not in st.session_state:
    st.session_state.evaluation_data = {}
if 'current_question_idx' not in st.session_state:
    st.session_state.current_question_idx = 0
if 'loaded_strategies' not in st.session_state:
    st.session_state.loaded_strategies = {}
if 'active_eval_file' not in st.session_state:
    st.session_state.active_eval_file = None


def load_rag_results(file_path: str) -> Dict:
    """Load RAG results from JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)


def find_result_files() -> List[str]:
    """Find all RAG result JSON files."""
    if not RAG_RESULTS_DIR.exists():
        return []

    files = list(RAG_RESULTS_DIR.glob("rag_results_*.json"))
    return sorted([str(f) for f in files])


def save_evaluation(save_path: str):
    """Save current evaluation to JSON."""
    eval_data = {
        "evaluator": "human",
        "saved_at": datetime.now().isoformat(),
        "strategies_evaluated": list(st.session_state.loaded_strategies.keys()),
        "evaluations": st.session_state.evaluation_data
    }

    Path(save_path).parent.mkdir(exist_ok=True)

    with open(save_path, 'w') as f:
        json.dump(eval_data, f, indent=2)

    return save_path


def load_evaluation(load_path: str):
    """Load previously saved evaluation."""
    with open(load_path, 'r') as f:
        eval_data = json.load(f)

    st.session_state.evaluation_data = eval_data.get("evaluations", {})
    st.session_state.active_eval_file = Path(load_path).name

    # Auto-load the strategies that were evaluated
    strategies_evaluated = eval_data.get("strategies_evaluated", [])
    if strategies_evaluated:
        st.session_state.loaded_strategies = {}
        for strategy in strategies_evaluated:
            files = list(RAG_RESULTS_DIR.glob(f"rag_results_{strategy}_*.json"))
            if files:
                latest_file = sorted(files)[-1]
                st.session_state.loaded_strategies[strategy] = load_rag_results(str(latest_file))

    return eval_data


def get_evaluation_key(strategy: str, question_id: int) -> str:
    """Generate unique key for evaluation data."""
    return f"{strategy}_{question_id}"


def calculate_progress() -> float:
    """Calculate evaluation progress percentage."""
    if not st.session_state.loaded_strategies:
        return 0.0

    # Get number of questions from first strategy
    first_strategy = list(st.session_state.loaded_strategies.values())[0]
    num_questions = len(first_strategy.get("results", []))
    num_strategies = len(st.session_state.loaded_strategies)

    total_items = num_strategies * num_questions
    if total_items == 0:
        return 0.0

    evaluated = sum(
        1 for key, data in st.session_state.evaluation_data.items()
        if data.get("answer_rating", 0) > 0
    )

    return (evaluated / total_items) * 100


def render_context_relevance(strategy: str, question_id: int, context_idx: int, context_data: Dict):
    """Render context with relevance selector."""
    eval_key = get_evaluation_key(strategy, question_id)

    # Initialize if not exists
    if eval_key not in st.session_state.evaluation_data:
        st.session_state.evaluation_data[eval_key] = {
            "answer_rating": 0,
            "contexts": {},
            "comments": "",
            "best_answer": False
        }

    context_key = str(context_idx)

    # Ensure contexts dict exists
    if "contexts" not in st.session_state.evaluation_data[eval_key]:
        st.session_state.evaluation_data[eval_key]["contexts"] = {}

    if context_key not in st.session_state.evaluation_data[eval_key]["contexts"]:
        st.session_state.evaluation_data[eval_key]["contexts"][context_key] = "not_evaluated"

    # Extract content and metadata
    context_content = context_data.get("content", "")
    context_metadata = context_data.get("metadata", {})
    file_path = context_metadata.get("file_path", "Unknown")
    score = context_data.get("score", 0.0)

    # Current relevance value
    current_value = st.session_state.evaluation_data[eval_key]["contexts"].get(context_key, "not_evaluated")

    # Color indicator
    colors = {
        "not_evaluated": "⚪",
        "relevant": "🟢",
        "partially_relevant": "🟡",
        "irrelevant": "🔴"
    }

    # Display context header
    st.markdown(f"**Context {context_idx + 1}** {colors[current_value]} - Score: {score:.3f}")
    st.caption(f"📄 {Path(file_path).name}")

    with st.expander(f"View content ({len(context_content)} chars)", expanded=False):
        st.text_area(
            "Content",
            value=context_content,
            height=250,
            key=f"content_{strategy}_{question_id}_{context_idx}",
            label_visibility="collapsed",
            disabled=True
        )

    # Relevance selector
    relevance = st.radio(
        "Relevance",
        options=["not_evaluated", "relevant", "partially_relevant", "irrelevant"],
        index=["not_evaluated", "relevant", "partially_relevant", "irrelevant"].index(current_value),
        horizontal=True,
        key=f"relevance_{strategy}_{question_id}_{context_idx}",
        label_visibility="collapsed"
    )

    st.session_state.evaluation_data[eval_key]["contexts"][context_key] = relevance


def render_strategy_column(strategy_name: str, result: Dict, question_id: int, all_strategies: List[str]):
    """Render evaluation UI for one strategy."""
    eval_key = get_evaluation_key(strategy_name, question_id)

    # Initialize evaluation data
    if eval_key not in st.session_state.evaluation_data:
        st.session_state.evaluation_data[eval_key] = {
            "answer_rating": 0,
            "contexts": {},
            "comments": "",
            "best_answer": False
        }

    # Check if this is marked as best answer
    is_best = st.session_state.evaluation_data[eval_key].get("best_answer", False)

    header = f"📊 {strategy_name}"
    if is_best:
        header += " 🏆"
    st.subheader(header)

    # Display generated answer
    st.markdown("**Generated Answer:**")
    answer = result.get("generated_answer", "")

    with st.container(height=400):
        st.info(answer)

    st.caption(f"{len(answer)} characters | Query time: {result.get('query_time_seconds', 'N/A')}s")

    # Answer quality rating slider
    st.markdown("**Rate Answer Quality:**")
    rating = st.slider(
        "Answer Quality",
        min_value=0,
        max_value=5,
        value=st.session_state.evaluation_data[eval_key].get("answer_rating", 0),
        key=f"rating_{strategy_name}_{question_id}",
        help="0 = Not evaluated, 1 = Poor, 5 = Excellent",
        label_visibility="collapsed"
    )
    st.session_state.evaluation_data[eval_key]["answer_rating"] = rating

    # Display stars
    if rating > 0:
        stars = "⭐" * rating + "☆" * (5 - rating)
        st.caption(f"{stars} ({rating}/5)")
    else:
        st.caption("☆☆☆☆☆ (Not rated)")

    # Mark as best answer checkbox
    best_answer = st.checkbox(
        "🏆 Best Answer",
        value=is_best,
        key=f"best_{strategy_name}_{question_id}",
        help="Check if this is the best answer for this question"
    )

    # If marking as best, unmark others
    if best_answer and not is_best:
        for other_strategy in all_strategies:
            other_key = get_evaluation_key(other_strategy, question_id)
            if other_key in st.session_state.evaluation_data:
                st.session_state.evaluation_data[other_key]["best_answer"] = False
        st.session_state.evaluation_data[eval_key]["best_answer"] = True
    elif not best_answer and is_best:
        st.session_state.evaluation_data[eval_key]["best_answer"] = False

    st.markdown("---")

    # Retrieved contexts
    st.markdown("**Retrieved Contexts (Top 10):**")

    # Context summary
    contexts = result.get("retrieved_contexts", [])
    context_evals = st.session_state.evaluation_data[eval_key].get("contexts", {})

    relevant_count = sum(1 for v in context_evals.values() if v == "relevant")
    partial_count = sum(1 for v in context_evals.values() if v == "partially_relevant")
    irrelevant_count = sum(1 for v in context_evals.values() if v == "irrelevant")

    st.caption(f"🟢 {relevant_count} | 🟡 {partial_count} | 🔴 {irrelevant_count} | ⚪ {10 - relevant_count - partial_count - irrelevant_count}")

    for idx, ctx in enumerate(contexts):
        render_context_relevance(strategy_name, question_id, idx, ctx)
        if idx < len(contexts) - 1:
            st.markdown("---")

    # Comments
    st.markdown("---")
    st.markdown("**Notes/Comments:**")
    comments = st.text_area(
        "Comments",
        value=st.session_state.evaluation_data[eval_key].get("comments", ""),
        key=f"comments_{strategy_name}_{question_id}",
        height=100,
        label_visibility="collapsed",
        placeholder="Add observations, issues, or notes about this answer..."
    )
    st.session_state.evaluation_data[eval_key]["comments"] = comments


def main():
    """Main app."""
    st.title("📊 Week 2: Human RAG Evaluation")
    st.markdown("Evaluate and compare RAG results across different chunking strategies")

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")

        # Find available result files
        result_files = find_result_files()

        if not result_files:
            st.error("No result files found")
            st.info("Run `04_generate_rag_results.py` first")
            return

        # Extract strategy names from filenames
        strategy_options = {}
        for file_path in result_files:
            filename = Path(file_path).name
            parts = filename.replace("rag_results_", "").replace(".json", "").split("_")
            strategy = "_".join(parts[:-2])  # Remove timestamp
            strategy_options[strategy] = file_path

        st.subheader("📁 Select Strategies")
        selected_strategies = st.multiselect(
            "Strategies",
            options=list(strategy_options.keys()),
            default=list(st.session_state.loaded_strategies.keys()) if st.session_state.loaded_strategies else None,
            label_visibility="collapsed"
        )

        if st.button("🔄 Load Strategies", type="primary", use_container_width=True):
            st.session_state.loaded_strategies = {}
            for strategy in selected_strategies:
                file_path = strategy_options[strategy]
                st.session_state.loaded_strategies[strategy] = load_rag_results(file_path)
            st.success(f"Loaded {len(selected_strategies)} strategies")
            st.rerun()

        st.markdown("---")

        # Progress indicator
        if st.session_state.loaded_strategies:
            progress = calculate_progress()
            st.subheader("📈 Progress")
            st.progress(progress / 100)
            st.metric("Evaluated", f"{progress:.0f}%")

        st.markdown("---")

        # Save evaluation
        st.subheader("💾 Save Evaluation")

        if st.session_state.active_eval_file:
            st.info(f"📝 Active: {st.session_state.active_eval_file}")
            default_filename = st.session_state.active_eval_file
        else:
            default_filename = f"human_eval_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        save_filename = st.text_input(
            "Filename:",
            value=default_filename,
            label_visibility="collapsed"
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("💾 Save", type="primary", use_container_width=True):
                save_path = EVALUATIONS_DIR / save_filename
                save_evaluation(str(save_path))
                st.session_state.active_eval_file = save_filename
                st.success("✅ Saved!")
                st.rerun()

        with col2:
            if st.button("📄 New", use_container_width=True):
                new_filename = f"human_eval_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                save_path = EVALUATIONS_DIR / new_filename
                save_evaluation(str(save_path))
                st.session_state.active_eval_file = new_filename
                st.success("✅ Saved as new!")
                st.rerun()

        st.markdown("---")

        # Load evaluation
        st.subheader("📂 Load Evaluation")

        if EVALUATIONS_DIR.exists():
            eval_files = list(EVALUATIONS_DIR.glob("*.json"))
            if eval_files:
                eval_file_names = [f.name for f in sorted(eval_files, reverse=True)]
                selected_eval = st.selectbox("Select:", eval_file_names, label_visibility="collapsed")

                if st.button("📂 Load", use_container_width=True):
                    load_path = EVALUATIONS_DIR / selected_eval
                    loaded_data = load_evaluation(str(load_path))
                    st.success(f"✅ Loaded!")
                    st.rerun()
            else:
                st.info("No saved evaluations yet")
        else:
            st.info("No evaluations directory")

        st.markdown("---")

        # Quick stats
        if st.session_state.evaluation_data:
            st.subheader("📊 Quick Stats")
            total_ratings = [
                d.get("answer_rating", 0)
                for d in st.session_state.evaluation_data.values()
                if d.get("answer_rating", 0) > 0
            ]
            if total_ratings:
                avg_rating = sum(total_ratings) / len(total_ratings)
                st.metric("Avg Rating", f"{avg_rating:.1f}/5")

                best_count = sum(
                    1 for d in st.session_state.evaluation_data.values()
                    if d.get("best_answer", False)
                )
                st.metric("Best Answers Marked", best_count)

    # Main content area
    if not st.session_state.loaded_strategies:
        st.info("👈 Select strategies from the sidebar to begin evaluation")

        st.markdown("---")
        st.markdown("### How to use this tool:")
        st.markdown("""
        1. **Load Strategies**: Select 2-3 chunking strategies to compare
        2. **Rate Answers**: Use the slider (1-5) to rate each answer's quality
        3. **Mark Best**: Check the "Best Answer" box for the winner
        4. **Evaluate Contexts**: Mark each retrieved context as relevant/partial/irrelevant
        5. **Add Notes**: Document your observations
        6. **Save**: Don't forget to save your evaluation!
        """)
        return

    # Get all questions from first strategy
    first_strategy = list(st.session_state.loaded_strategies.values())[0]
    all_questions = first_strategy.get("results", [])

    if not all_questions:
        st.error("No questions found in loaded strategies")
        return

    # Question navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        if st.button("⬅️ Previous", disabled=st.session_state.current_question_idx == 0):
            st.session_state.current_question_idx -= 1
            st.rerun()

    with col2:
        st.markdown(f"### Question {st.session_state.current_question_idx + 1} of {len(all_questions)}")

    with col3:
        if st.button("Next ➡️", disabled=st.session_state.current_question_idx >= len(all_questions) - 1):
            st.session_state.current_question_idx += 1
            st.rerun()

    # Current question
    current_question = all_questions[st.session_state.current_question_idx]
    question_id = current_question.get("question_id", st.session_state.current_question_idx)
    question_text = current_question.get("question", "")

    st.markdown("---")
    st.markdown(f"### ❓ {question_text}")

    # Display metadata
    with st.expander("📋 Question Metadata", expanded=False):
        col1, col2, col3 = st.columns(3)
        col1.metric("Category", current_question.get("category", "N/A"))
        col2.metric("Difficulty", current_question.get("difficulty", "N/A"))
        col3.metric("Content Type", current_question.get("primary_content_type", "N/A"))

    st.markdown("---")

    # Strategy comparison columns
    all_strategy_names = list(st.session_state.loaded_strategies.keys())
    num_strategies = len(all_strategy_names)
    cols = st.columns(num_strategies)

    for idx, (strategy_name, strategy_data) in enumerate(st.session_state.loaded_strategies.items()):
        with cols[idx]:
            # Find matching question
            strategy_results = strategy_data.get("results", [])
            matching_result = None

            for result in strategy_results:
                if result.get("question_id") == question_id:
                    matching_result = result
                    break

            if matching_result:
                render_strategy_column(strategy_name, matching_result, question_id, all_strategy_names)
            else:
                st.warning(f"Question {question_id} not found in {strategy_name}")


if __name__ == "__main__":
    main()
