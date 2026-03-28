# ============================================================================
# The Engineer's RAG Accelerator - Adapted for Capstone Week 2
#
# Streamlit app for HUMAN evaluation of RAG results across chunking strategies.
# Input: week-2/evaluations/rag_results/
# Output: week-2/human_evaluations/
# ============================================================================

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional

import streamlit as st


def resolve_week2_dir() -> Optional[Path]:
	script_dir = Path(__file__).resolve().parent
	for candidate in [script_dir, *script_dir.parents]:
		if (candidate / "evaluations" / "rag_results").exists():
			return candidate
	return None


WEEK2_DIR = resolve_week2_dir()
if WEEK2_DIR is None:
	WEEK2_DIR = Path(__file__).resolve().parent.parent.parent

RAG_RESULTS_DIR = WEEK2_DIR / "evaluations" / "rag_results"
EVALUATIONS_DIR = WEEK2_DIR / "human_evaluations"
EVALUATIONS_DIR.mkdir(parents=True, exist_ok=True)


st.set_page_config(
	page_title="Week 2: Human RAG Evaluation",
	page_icon="📊",
	layout="wide"
)


def load_json(file_path: Path) -> Dict[str, Any]:
	with open(file_path, "r", encoding="utf-8") as f:
		return json.load(f)


def extract_strategy_key(filename: str) -> Optional[str]:
	match = re.match(r"rag_results_(.*?)_\d{8}_\d{6}\.json$", filename)
	if not match:
		return None
	return match.group(1)


def load_latest_rag_by_strategy() -> Dict[str, Dict[str, Any]]:
	if not RAG_RESULTS_DIR.exists():
		return {}

	grouped: Dict[str, List[Path]] = {}
	for file_path in RAG_RESULTS_DIR.glob("rag_results_*.json"):
		strategy_key = extract_strategy_key(file_path.name)
		if not strategy_key:
			continue
		grouped.setdefault(strategy_key, []).append(file_path)

	loaded: Dict[str, Dict[str, Any]] = {}
	for strategy_key, files in grouped.items():
		latest = sorted(files)[-1]
		loaded[strategy_key] = load_json(latest)

	return loaded


def get_question_ids(strategy_payloads: Dict[str, Dict[str, Any]]) -> List[int]:
	if not strategy_payloads:
		return []
	intersection: Optional[set] = None
	for payload in strategy_payloads.values():
		ids = {
			row.get("question_id")
			for row in payload.get("results", [])
			if isinstance(row.get("question_id"), int)
		}
		if intersection is None:
			intersection = ids
		else:
			intersection = intersection.intersection(ids)
	if not intersection:
		return []
	return sorted(intersection)


def get_row_by_qid(payload: Dict[str, Any], question_id: int) -> Optional[Dict[str, Any]]:
	for row in payload.get("results", []):
		if row.get("question_id") == question_id:
			return row
	return None


if "evaluation_data" not in st.session_state:
	st.session_state.evaluation_data = {}
if "current_question_idx" not in st.session_state:
	st.session_state.current_question_idx = 0


st.title("📊 Week 2 Human RAG Evaluation")
st.caption("Compare generated answers across chunking strategies and record manual judgments.")

with st.expander("Paths", expanded=False):
	st.write(f"Week 2 dir: `{WEEK2_DIR}`")
	st.write(f"RAG results dir: `{RAG_RESULTS_DIR}`")
	st.write(f"Human eval dir: `{EVALUATIONS_DIR}`")

strategy_payloads = load_latest_rag_by_strategy()
if not strategy_payloads:
	st.error(f"No RAG results found in: {RAG_RESULTS_DIR}")
	st.stop()

strategy_keys = sorted(strategy_payloads.keys())
question_ids = get_question_ids(strategy_payloads)
if not question_ids:
	st.error("Could not find common question_ids across loaded strategy files.")
	st.stop()

if st.session_state.current_question_idx >= len(question_ids):
	st.session_state.current_question_idx = 0

top_cols = st.columns([2, 1, 1])
with top_cols[0]:
	selected_question_id = st.selectbox(
		"Question",
		options=question_ids,
		index=st.session_state.current_question_idx,
		format_func=lambda qid: f"Q{qid}",
	)
	st.session_state.current_question_idx = question_ids.index(selected_question_id)

with top_cols[1]:
	if st.button("⬅ Previous", use_container_width=True) and st.session_state.current_question_idx > 0:
		st.session_state.current_question_idx -= 1
		st.rerun()

with top_cols[2]:
	if st.button("Next ➡", use_container_width=True) and st.session_state.current_question_idx < len(question_ids) - 1:
		st.session_state.current_question_idx += 1
		st.rerun()

selected_question_id = question_ids[st.session_state.current_question_idx]
reference_row = get_row_by_qid(strategy_payloads[strategy_keys[0]], selected_question_id)

if reference_row is None:
	st.error("Selected question not found in reference strategy payload.")
	st.stop()

st.markdown("### Question")
st.write(reference_row.get("question", "No question text found."))

st.markdown("### Strategy Outputs")
strategy_cols = st.columns(len(strategy_keys))
for index, strategy_key in enumerate(strategy_keys):
	row = get_row_by_qid(strategy_payloads[strategy_key], selected_question_id)
	with strategy_cols[index]:
		st.subheader(strategy_key.capitalize())
		if row is None:
			st.warning("No result for this question.")
			continue
		st.caption(f"Latency: {row.get('query_time_seconds', 'N/A')} s")
		retrieved_contexts = row.get("retrieved_contexts", []) or []
		top_score = retrieved_contexts[0].get("score", "N/A") if retrieved_contexts else "N/A"
		st.caption(f"Top-1 score: {top_score}")
		st.text_area(
			f"Answer ({strategy_key})",
			value=row.get("generated_answer", ""),
			height=280,
			disabled=True,
			key=f"answer_{strategy_key}_{selected_question_id}"
		)

st.divider()
st.markdown("### Human Judgment")

question_eval = st.session_state.evaluation_data.get(selected_question_id, {})

winner = st.selectbox(
	"Best strategy for this question",
	options=["", *strategy_keys],
	index=(["", *strategy_keys].index(question_eval.get("winner", "")) if question_eval.get("winner", "") in ["", *strategy_keys] else 0),
	format_func=lambda value: "Select winner" if value == "" else value.capitalize(),
)

coverage = st.slider(
	"Coverage / completeness (1-5)",
	min_value=1,
	max_value=5,
	value=int(question_eval.get("coverage", 3)),
)

factuality = st.slider(
	"Factual correctness (1-5)",
	min_value=1,
	max_value=5,
	value=int(question_eval.get("factuality", 3)),
)

clarity = st.slider(
	"Clarity (1-5)",
	min_value=1,
	max_value=5,
	value=int(question_eval.get("clarity", 3)),
)

notes = st.text_area(
	"Notes / rationale",
	value=question_eval.get("notes", ""),
	height=120,
)

st.session_state.evaluation_data[selected_question_id] = {
	"winner": winner,
	"coverage": coverage,
	"factuality": factuality,
	"clarity": clarity,
	"notes": notes,
	"question": reference_row.get("question", ""),
}

save_cols = st.columns([1, 1, 2])

with save_cols[0]:
	if st.button("💾 Save Draft", use_container_width=True):
		timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
		output_path = EVALUATIONS_DIR / f"human_eval_draft_{timestamp}.json"
		payload = {
			"saved_at": datetime.now().isoformat(),
			"week2_dir": str(WEEK2_DIR),
			"strategies": strategy_keys,
			"question_ids": question_ids,
			"evaluations": st.session_state.evaluation_data,
		}
		with open(output_path, "w", encoding="utf-8") as f:
			json.dump(payload, f, indent=2)
		st.success(f"Draft saved: {output_path.name}")

with save_cols[1]:
	if st.button("✅ Save Final", use_container_width=True):
		timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
		output_path = EVALUATIONS_DIR / f"human_eval_final_{timestamp}.json"
		completed = len([v for v in st.session_state.evaluation_data.values() if v.get("winner")])
		payload = {
			"saved_at": datetime.now().isoformat(),
			"week2_dir": str(WEEK2_DIR),
			"strategies": strategy_keys,
			"question_ids": question_ids,
			"completed_questions": completed,
			"total_questions": len(question_ids),
			"evaluations": st.session_state.evaluation_data,
		}
		with open(output_path, "w", encoding="utf-8") as f:
			json.dump(payload, f, indent=2)
		st.success(f"Final evaluation saved: {output_path.name}")

with save_cols[2]:
	completed_count = len([v for v in st.session_state.evaluation_data.values() if v.get("winner")])
	st.info(f"Progress: {completed_count}/{len(question_ids)} questions have a selected winner.")
