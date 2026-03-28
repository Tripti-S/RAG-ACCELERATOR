from __future__ import annotations

import argparse
import json
import os
import re
import time
from itertools import combinations
from pathlib import Path

from dotenv import load_dotenv
from haystack.dataclasses import ChatMessage
from haystack_integrations.components.generators.google_genai import GoogleGenAIChatGenerator


SCRIPT_DIR = Path(__file__).resolve().parent
WEEK3_DIR = SCRIPT_DIR.parents[1]
PROJECT_ROOT = SCRIPT_DIR.parents[2]


def load_env() -> None:
    load_dotenv(PROJECT_ROOT / ".env")
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("Missing GOOGLE_API_KEY")


def _latest_file(pattern: str, folder: Path) -> Path:
    files = sorted(folder.glob(pattern))
    if not files:
        raise FileNotFoundError(f"No files matching {pattern} in {folder}")
    return files[-1]


def load_results(path: Path) -> tuple[str, dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    tech = data.get("technique") or data.get("strategy") or path.stem
    return str(tech), data


def get_question_text(row: dict) -> str:
    return row.get("user_input") or row.get("question") or ""


def build_prompt(question: str, tech_a: str, ctx_a: list[dict], tech_b: str, ctx_b: list[dict]) -> str:
    def block(prefix: str, contexts: list[dict]) -> str:
        lines = []
        for i, c in enumerate(contexts[:10], start=1):
            score = float(c.get("score", 0.0))
            text = str(c.get("content", ""))[:1800]
            lines.append(f"[{prefix}{i}] score={score:.3f}\n{text}\n")
        return "\n".join(lines)

    return f"""You are evaluating retrieval quality for one question.

Question:
{question}

Technique A: {tech_a}
{block('A', ctx_a)}

Technique B: {tech_b}
{block('B', ctx_b)}

For each technique, compute from the 10 contexts:
- useful_total: number of contexts that are useful for answering this question (0-10)
- direct_count: number of contexts with direct answer value (0-10)
- noise_count: number of contexts that are irrelevant/noise (0-10)

Then choose winner_code = "A" or "B".

Return ONLY valid JSON:
{{
  "A_useful_total": <int>,
  "B_useful_total": <int>,
  "A_direct_count": <int>,
  "B_direct_count": <int>,
  "A_noise_count": <int>,
  "B_noise_count": <int>,
  "winner_code": "A or B",
  "reasoning": "short reason"
}}
"""


def call_judge(prompt: str, model: str = "gemini-2.5-flash", retries: int = 3) -> dict:
    generator = GoogleGenAIChatGenerator(
        model=model,
        generation_kwargs={"temperature": 0.1, "response_mime_type": "application/json"},
    )
    for i in range(retries):
        try:
            resp = generator.run(messages=[ChatMessage.from_user(prompt)])
            txt = resp["replies"][0].text.strip()
            start = txt.find("{")
            end = txt.rfind("}")
            if start >= 0 and end >= 0:
                txt = txt[start : end + 1]
            txt = re.sub(r",(\s*[}\]])", r"\1", txt)
            return json.loads(txt)
        except Exception as exc:
            if i == retries - 1:
                raise
            wait = 5 * (i + 1)
            if "429" in str(exc) or "RESOURCE_EXHAUSTED" in str(exc):
                time.sleep(wait + 15)
            else:
                time.sleep(wait)
    return {}


def main() -> None:
    parser = argparse.ArgumentParser(description="Pairwise eval across Week 3 all techniques")
    parser.add_argument("--model", default="gemini-2.5-flash")
    args = parser.parse_args()

    load_env()

    week2_file = _latest_file("rag_results_recursive_*.json", PROJECT_ROOT / "week-2" / "evaluations" / "rag_results")
    week3_baseline = _latest_file("week3_hybrid_rerank_baseline_*.json", WEEK3_DIR / "rag_results")
    meta_file = WEEK3_DIR / "rag_results" / "week3_hybrid_rerank_metadata_filter_results.json"
    two_stage_file = WEEK3_DIR / "rag_results" / "week3_two_stage_routing_results.json"
    for p in [meta_file, two_stage_file]:
        if not p.exists():
            raise FileNotFoundError(f"Missing required result file: {p}")

    technique_files = [week2_file, week3_baseline, meta_file, two_stage_file]
    techniques: list[str] = []
    data_map: dict[str, dict] = {}
    source_files: dict[str, str] = {}
    for p in technique_files:
        name, data = load_results(p)
        techniques.append(name)
        data_map[name] = data
        source_files[name] = str(p.resolve())

    base_rows = next(iter(data_map.values()))["results"]
    pairs = list(combinations(techniques, 2))
    evaluations: dict[str, dict] = {}
    win_counts = {t: 0 for t in techniques}

    aggregate = {
        t: {"usefulness": [], "relevance": [], "direct": [], "noise": []}
        for t in techniques
    }

    for row in base_rows:
        qid = row.get("question_id")
        qtext = get_question_text(row)
        for ta, tb in pairs:
            ra = next((r for r in data_map[ta]["results"] if r.get("question_id") == qid), None)
            rb = next((r for r in data_map[tb]["results"] if r.get("question_id") == qid), None)
            if not ra or not rb:
                continue
            prompt = build_prompt(qtext, ta, ra.get("retrieved_contexts", []), tb, rb.get("retrieved_contexts", []))
            judged = call_judge(prompt=prompt, model=args.model)

            a_use = int(judged.get("A_useful_total", 0))
            b_use = int(judged.get("B_useful_total", 0))
            a_dir = int(judged.get("A_direct_count", 0))
            b_dir = int(judged.get("B_direct_count", 0))
            a_noise = int(judged.get("A_noise_count", 0))
            b_noise = int(judged.get("B_noise_count", 0))
            winner_code = str(judged.get("winner_code", "")).upper()
            winner = ta if winner_code == "A" else tb if winner_code == "B" else "unclear"
            if winner in win_counts:
                win_counts[winner] += 1

            aggregate[ta]["usefulness"].append(a_use / 2)
            aggregate[tb]["usefulness"].append(b_use / 2)
            aggregate[ta]["relevance"].append(a_dir / 2)
            aggregate[tb]["relevance"].append(b_dir / 2)
            aggregate[ta]["direct"].append(a_dir)
            aggregate[tb]["direct"].append(b_dir)
            aggregate[ta]["noise"].append(a_noise)
            aggregate[tb]["noise"].append(b_noise)

            key = f"q{qid}_{ta}_vs_{tb}"
            evaluations[key] = {
                "question_id": qid,
                "question": qtext,
                "technique_a": ta,
                "technique_b": tb,
                "winner": winner,
                "winner_code": winner_code,
                "metrics": {
                    "A_usefulness_score": a_use / 2,
                    "B_usefulness_score": b_use / 2,
                    "A_relevance_score": a_dir / 2,
                    "B_relevance_score": b_dir / 2,
                    "A_direct_context_count": a_dir,
                    "B_direct_context_count": b_dir,
                    "A_noise_chunks": a_noise,
                    "B_noise_chunks": b_noise,
                },
                "reasoning": judged.get("reasoning", ""),
            }

    summary = {}
    for t, m in aggregate.items():
        n_use = len(m["usefulness"]) or 1
        n_rel = len(m["relevance"]) or 1
        n_noise = len(m["noise"]) or 1
        summary[t] = {
            "avg_usefulness": round(sum(m["usefulness"]) / n_use, 3),
            "avg_relevance": round(sum(m["relevance"]) / n_rel, 3),
            "avg_direct_context_count": round(sum(m["direct"]) / (len(m["direct"]) or 1), 3),
            "noise_chunks_total": int(sum(m["noise"])),
            "noise_chunks_avg": round(sum(m["noise"]) / n_noise, 3),
            "questions_won": int(win_counts[t]),
        }

    output = {
        "evaluation_type": "pairwise_retrieval_week3_all_techniques",
        "model": args.model,
        "techniques": techniques,
        "source_files": source_files,
        "pairs_compared": pairs,
        "questions_evaluated": len(base_rows),
        "evaluations": evaluations,
        "summary_table": summary,
    }

    out_path = WEEK3_DIR / "evaluations" / "eval_results" / "pairwise_eval_week3_all_techniques.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")

    print("\nFinal Summary Table")
    print("technique | avg usefulness | avg relevance | noise | questions won")
    for t in techniques:
        s = summary[t]
        print(
            f"{t} | {s['avg_usefulness']:.3f} | {s['avg_relevance']:.3f} | "
            f"{s['noise_chunks_total']} | {s['questions_won']}"
        )
    print(f"\nSaved evaluation to: {out_path}")


if __name__ == "__main__":
    main()
