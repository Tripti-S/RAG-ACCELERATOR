# ============================================================================
# The Engineer's RAG Accelerator - Adapted for Capstone Week 2
#
# Streamlit app for viewing LLM-as-judge chunk quality evaluations.
# Input: week-2/evaluations/eval_results/
# Output: UI only
# ============================================================================

import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional

import streamlit as st


def resolve_week2_dir() -> Optional[Path]:
	script_dir = Path(__file__).resolve().parent
	for candidate in [script_dir, *script_dir.parents]:
		if (candidate / "evaluations" / "eval_results").exists() and (candidate / "evaluations" / "rag_results").exists():
			return candidate
	return None


WEEK2_DIR = resolve_week2_dir()
if WEEK2_DIR is None:
	WEEK2_DIR = Path(__file__).resolve().parent.parent.parent

RAG_RESULTS_DIR = WEEK2_DIR / "evaluations" / "rag_results"
EVALUATIONS_DIR = WEEK2_DIR / "evaluations" / "eval_results"


st.set_page_config(
	page_title="Week 2: Chunk Quality Evaluation",
	page_icon="🔬",
	layout="wide"
)


def load_json_flexible(file_path: Path) -> Dict[str, Any]:
	text = file_path.read_text(encoding="utf-8")
	cleaned = re.sub(r"^\s*//.*$", "", text, flags=re.MULTILINE)
	cleaned = re.sub(r",\s*([}\]])", r"\1", cleaned)
	return json.loads(cleaned)


def get_strategy_key(strategy_label: str) -> str:
	strategy_lower = (strategy_label or "").lower()
	if "hybrid" in strategy_lower:
		return "hybrid"
	if "semantic" in strategy_lower:
		return "semantic"
	if "recursive" in strategy_lower:
		return "recursive"
	if "naive" in strategy_lower:
		return "naive"
	return strategy_lower.strip().replace(" ", "_")


def load_latest_rag_results(strategy_key: str) -> Optional[Dict[str, Any]]:
	pattern = re.compile(rf"rag_results_{re.escape(strategy_key)}_\d{{8}}_\d{{6}}\.json$")
	if not RAG_RESULTS_DIR.exists():
		return None
	files = [f for f in RAG_RESULTS_DIR.iterdir() if f.is_file() and pattern.match(f.name)]
	if not files:
		return None
	latest = sorted(files)[-1]
	return load_json_flexible(latest)


def summarize_eval_results(results: List[Dict[str, Any]]) -> Dict[str, Any]:
	if not results:
		return {"count": 0, "avg_signal": None, "avg_useful": None, "avg_cutoffs": None}

	signals = [r.get("signal") for r in results if isinstance(r.get("signal"), (int, float))]
	usefuls = [r.get("useful") for r in results if isinstance(r.get("useful"), (int, float))]
	cutoffs = [r.get("cutoffs") for r in results if isinstance(r.get("cutoffs"), (int, float))]

	def avg(values: List[float]) -> Optional[float]:
		return round(sum(values) / len(values), 2) if values else None

	return {
		"count": len(results),
		"avg_signal": avg(signals),
		"avg_useful": avg(usefuls),
		"avg_cutoffs": avg(cutoffs),
	}


st.title("🔬 Week 2 Chunk Quality Evaluation Viewer")
st.caption("Compare strategy-level eval signals with matching RAG retrieval outputs.")

with st.expander("Paths", expanded=False):
	st.write(f"Week 2 dir: `{WEEK2_DIR}`")
	st.write(f"Eval dir: `{EVALUATIONS_DIR}`")
	st.write(f"RAG dir: `{RAG_RESULTS_DIR}`")

if not EVALUATIONS_DIR.exists():
	st.error(f"Evaluation directory not found: {EVALUATIONS_DIR}")
	st.stop()

eval_files = sorted(EVALUATIONS_DIR.glob("*.json"))
if not eval_files:
	st.warning("No evaluation files found in eval_results.")
	st.stop()

selected_eval_file = st.selectbox(
	"Select evaluation file",
	options=eval_files,
	format_func=lambda p: p.name,
)

try:
	eval_data = load_json_flexible(selected_eval_file)
except Exception as exc:
	st.error(f"Failed to load evaluation file: {selected_eval_file.name}")
	st.exception(exc)
	st.stop()

strategy_label = eval_data.get("strategy", "Unknown")
collection = eval_data.get("collection", "Unknown")
results = eval_data.get("results", [])
summary = summarize_eval_results(results)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Strategy", strategy_label)
col2.metric("Collection", collection)
col3.metric("Questions", summary["count"])
col4.metric("Generated At", eval_data.get("generated_at", "N/A"))

col5, col6, col7 = st.columns(3)
col5.metric("Avg Signal", summary["avg_signal"] if summary["avg_signal"] is not None else "N/A")
col6.metric("Avg Useful", summary["avg_useful"] if summary["avg_useful"] is not None else "N/A")
col7.metric("Avg Cutoffs", summary["avg_cutoffs"] if summary["avg_cutoffs"] is not None else "N/A")

st.divider()

if not results:
	st.info("No per-question results found in selected eval file.")
	st.stop()

question_options = [
	(r.get("question_id", idx + 1), r.get("question", "(no question text)"))
	for idx, r in enumerate(results)
]

selected_qid = st.selectbox(
	"Select question",
	options=[qid for qid, _ in question_options],
	format_func=lambda qid: f"Q{qid}: {next((q for qid2, q in question_options if qid2 == qid), '')[:100]}",
)

selected_eval_row = next((r for r in results if r.get("question_id") == selected_qid), results[0])

left, right = st.columns([1, 1])
with left:
	st.subheader("Eval Signals")
	st.markdown(f"**Winner:** {selected_eval_row.get('winner', 'N/A')}")
	st.markdown(f"**Signal:** {selected_eval_row.get('signal', 'N/A')}")
	st.markdown(f"**Useful:** {selected_eval_row.get('useful', 'N/A')}")
	st.markdown(f"**Cutoffs:** {selected_eval_row.get('cutoffs', 'N/A')}")

with right:
	st.subheader("Judge Reasoning")
	st.write(selected_eval_row.get("reasoning", "No reasoning field present."))

st.markdown("### Question")
st.write(selected_eval_row.get("question", "No question text found."))

st.divider()

strategy_key = get_strategy_key(strategy_label)
rag_data = load_latest_rag_results(strategy_key)

if rag_data is None:
	st.warning(f"No matching RAG results file found for strategy key: `{strategy_key}`")
	st.stop()

rag_results = rag_data.get("results", [])
rag_row = next((r for r in rag_results if r.get("question_id") == selected_qid), None)

st.subheader("Matched RAG Output")
st.caption(f"Loaded file pattern: rag_results_{strategy_key}_YYYYMMDD_HHMMSS.json")

if rag_row is None:
	st.info("No matching question in RAG results for selected question id.")
	st.stop()

top_cols = st.columns(3)
top_cols[0].metric("Num Contexts", rag_row.get("num_contexts_retrieved", "N/A"))
top_cols[1].metric("Query Time (s)", rag_row.get("query_time_seconds", "N/A"))
retrieved_contexts = rag_row.get("retrieved_contexts", []) or []
top_cols[2].metric("Top-1 Score", retrieved_contexts[0].get("score", "N/A") if retrieved_contexts else "N/A")

st.markdown("### Generated Answer")
st.write(rag_row.get("generated_answer", "No generated answer found."))

st.markdown("### Retrieved Contexts")
if not retrieved_contexts:
	st.info("No retrieved contexts available.")
else:
	max_rows = st.slider("Contexts to show", min_value=1, max_value=min(10, len(retrieved_contexts)), value=min(5, len(retrieved_contexts)))
	for context in retrieved_contexts[:max_rows]:
		with st.expander(f"Rank {context.get('rank', '?')} | Score {context.get('score', 'N/A')}"):
			metadata = context.get("metadata", {})
			st.markdown(f"**Source:** {metadata.get('file_path', 'N/A')}")
			st.markdown(f"**Chunk Method:** {metadata.get('chunk_method', 'N/A')}")
			st.write(context.get("content", ""))
