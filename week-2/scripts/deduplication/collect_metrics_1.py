import json
import statistics
from pathlib import Path
from collections import Counter, defaultdict

root = Path(r"C:/Users/singhtripti/rag-capstone-week-2")
week2 = root / "week-2"


def read_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


questions = read_json(week2 / "evaluations/test_questions.json")
q_count = len(questions)
q_types = Counter(q.get("type", "unknown") for q in questions)

eval_file = week2 / "evaluations/eval_results/hybrid_chunk_eval_20260301_211714.json"
eval_data = read_json(eval_file)
results = eval_data.get("results", [])

stage1 = defaultdict(lambda: {"signal": [], "cutoffs": [], "high_useful": []})
for row in results:
    analyses = row.get("stage1_analyses", {})
    for strategy, analysis in analyses.items():
        summary = analysis.get("summary", {})
        if isinstance(summary.get("avg_signal_pct"), (int, float)):
            stage1[strategy]["signal"].append(summary["avg_signal_pct"])
        if isinstance(summary.get("cut_mid_answer_count"), (int, float)):
            stage1[strategy]["cutoffs"].append(summary["cut_mid_answer_count"])
        if isinstance(summary.get("high_useful_count"), (int, float)):
            stage1[strategy]["high_useful"].append(summary["high_useful_count"])

stage1_avg = {}
for strategy, vals in stage1.items():
    stage1_avg[strategy] = {
        "avg_signal_pct": round(sum(vals["signal"]) / len(vals["signal"]), 2) if vals["signal"] else None,
        "avg_cut_mid_answer_count": round(sum(vals["cutoffs"]) / len(vals["cutoffs"]), 2) if vals["cutoffs"] else None,
        "avg_high_useful_count": round(sum(vals["high_useful"]) / len(vals["high_useful"]), 2) if vals["high_useful"] else None,
    }

first_place = Counter()
rank_counts = defaultdict(Counter)
for row in results:
    ranking = row.get("stage2_ranking", {}).get("ranking", {})
    for ordinal, strategy in ranking.items():
        if strategy:
            s = strategy.lower()
            rank_counts[s][ordinal] += 1
    first = ranking.get("1st")
    if first:
        first_place[first.lower()] += 1


def rag_stats(path: Path):
    data = read_json(path)
    rows = data.get("results", [])
    latencies = [r.get("query_time_seconds") for r in rows if isinstance(r.get("query_time_seconds"), (int, float))]
    top1_scores = []
    for row in rows:
        ctx = row.get("retrieved_contexts", []) or []
        if ctx and isinstance(ctx[0].get("score"), (int, float)):
            top1_scores.append(ctx[0]["score"])
    return {
        "questions": len(rows),
        "lat_avg": round(sum(latencies) / len(latencies), 3) if latencies else None,
        "lat_median": round(statistics.median(latencies), 3) if latencies else None,
        "lat_max": round(max(latencies), 3) if latencies else None,
        "top1_avg": round(sum(top1_scores) / len(top1_scores), 4) if top1_scores else None,
    }


rag = {
    "recursive": rag_stats(week2 / "evaluations/rag_results/rag_results_recursive_20260301_041934.json"),
    "semantic": rag_stats(week2 / "evaluations/rag_results/rag_results_semantic_20260301_042330.json"),
    "hybrid": rag_stats(week2 / "evaluations/rag_results/rag_results_hybrid_20260301_111809.json"),
}

traces = read_json(root / "week-1/traces/traces.json")
trace_lat = [t.get("latency_seconds") for t in traces if isinstance(t.get("latency_seconds"), (int, float))]
trace_ret = [t.get("retrieval_count") for t in traces if isinstance(t.get("retrieval_count"), (int, float))]
trace_ans = [t.get("answer_length") for t in traces if isinstance(t.get("answer_length"), (int, float))]
week1_trace = {
    "queries": len(traces),
    "lat_avg": round(sum(trace_lat) / len(trace_lat), 3) if trace_lat else None,
    "lat_median": round(statistics.median(trace_lat), 3) if trace_lat else None,
    "retrieval_count_avg": round(sum(trace_ret) / len(trace_ret), 2) if trace_ret else None,
    "answer_length_avg": round(sum(trace_ans) / len(trace_ans), 1) if trace_ans else None,
}

manifest = read_json(week2 / "artifacts/selected_files_manifest.json")
meta = manifest.get("manifest_metadata", {})
selected_files = manifest.get("selected_files", [])
content_types = Counter(x.get("content_type", "unknown") for x in selected_files)

word_counts = []
missing = 0
for entry in selected_files:
    rel = entry.get("filepath", "")
    normalized = rel.replace("\\", "/")
    if normalized.startswith("../../"):
        candidate = (root / normalized.replace("../../", "")).resolve()
    else:
        candidate = (week2 / normalized).resolve()

    if candidate.exists() and candidate.is_file():
        text = candidate.read_text(encoding="utf-8", errors="ignore")
        word_counts.append(len(text.split()))
    else:
        missing += 1

word_stats = {
    "count_measured": len(word_counts),
    "missing": missing,
    "min": min(word_counts) if word_counts else None,
    "max": max(word_counts) if word_counts else None,
    "median": round(statistics.median(word_counts), 1) if word_counts else None,
    "mean": round(statistics.mean(word_counts), 1) if word_counts else None,
    "stdev": round(statistics.pstdev(word_counts), 1) if len(word_counts) > 1 else None,
    "lt_200": sum(1 for w in word_counts if w < 200),
    "gt_1000": sum(1 for w in word_counts if w > 1000),
    "gt_2000": sum(1 for w in word_counts if w > 2000),
}

ignore_lines = (week2 / ".gitingestignore").read_text(encoding="utf-8").splitlines()
ignore_set = {line.strip() for line in ignore_lines if line.strip() and not line.strip().startswith("#")}
required_ignore = [
    "archive/",
    "rag_results/",
    "data/raw/",
    "data/processed/",
    "*.parquet",
    "*.csv",
    "*.npy",
    "*.bin",
    "prequalify.py",
    "week2_submission_guidelines.md",
]
ignore_status = {entry: (entry in ignore_set) for entry in required_ignore}

snapshot = {
    "questions": {"count": q_count, "types": dict(q_types)},
    "eval": {
        "file": eval_file.name,
        "model": eval_data.get("model"),
        "method": eval_data.get("evaluation_method"),
        "strategies": eval_data.get("strategies"),
        "questions_evaluated": eval_data.get("questions_evaluated"),
        "first_place": dict(first_place),
        "rank_counts": {k: dict(v) for k, v in rank_counts.items()},
        "stage1_avg": stage1_avg,
    },
    "rag": rag,
    "week1_trace": week1_trace,
    "manifest": {
        "files_selected": meta.get("files_selected"),
        "reduction_percentage": meta.get("reduction_percentage"),
        "content_types": dict(content_types),
        "word_stats": word_stats,
    },
    "ignore_status": ignore_status,
}

out_path = week2 / "evaluations" / "metrics_snapshot_1.json"
out_path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
print(out_path)
