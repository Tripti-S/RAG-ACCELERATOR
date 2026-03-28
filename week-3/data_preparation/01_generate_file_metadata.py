import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from dotenv import load_dotenv
from haystack.dataclasses import ChatMessage
from haystack_integrations.components.generators.google_genai import GoogleGenAIChatGenerator
from tqdm import tqdm


SCRIPT_DIR = Path(__file__).resolve().parent
WEEK3_DIR = SCRIPT_DIR.parent
PROJECT_ROOT = WEEK3_DIR.parent
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

MANIFEST_FILE = ARTIFACTS_DIR / "selected_files_manifest.json"
OUTPUT_FILE = SCRIPT_DIR / "outputs" / "file_metadata.json"
DEFAULT_MODEL = "gemini-2.5-flash"


PROMPT_TEMPLATE = """You are generating metadata for routing in a probability/statistics RAG system.

File path: {file_path}
Content:
{content}

Extract JSON with these fields:
1) summary: 3-5 sentence comprehensive summary
2) file_type: one of ["lecture_notes", "problem_set", "exam", "textbook", "reference", "worked_solution", "other"]
3) domain_concepts: list of all key concepts mentioned (e.g., bayes_rule, conditional_probability, random_variable, expectation, variance, clt, lln, hypothesis_testing, poisson, binomial)
4) content_type: one of ["conceptual", "derivation", "example", "exercise", "solution", "mixed"]
5) primary_topics: 5-15 specific topics covered
6) code_examples: true or false
7) searchable_keywords: 10-20 searchable keywords or phrases
8) can_answer_questions: 3-5 specific questions this file can answer

Return ONLY valid JSON in this exact shape:
{{
  "file_path": "{file_path}",
  "summary": "...",
  "file_type": "lecture_notes|problem_set|exam|textbook|reference|worked_solution|other",
  "domain_concepts": ["..."],
  "content_type": "conceptual|derivation|example|exercise|solution|mixed",
  "primary_topics": ["..."],
  "code_examples": false,
  "searchable_keywords": ["..."],
  "can_answer_questions": ["..."]
}}
"""


def load_environment() -> None:
    load_dotenv(PROJECT_ROOT / ".env")
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("Missing GOOGLE_API_KEY in .env")


def normalize_manifest_path(path_text: str) -> Path:
    normalized_text = path_text.replace("\\", "/")

    if "week-1/data/processed/" in normalized_text:
        suffix = normalized_text.split("week-1/data/processed/", 1)[1]
        fixed = (PROJECT_ROOT / "week-1" / "data" / "processed" / suffix).resolve()
        if fixed.exists():
            return fixed

    p = Path(path_text)
    if p.is_absolute() and p.exists():
        return p
    candidate = (MANIFEST_FILE.parent / p).resolve()
    if candidate.exists():
        return candidate
    candidate2 = (PROJECT_ROOT / p).resolve()
    if candidate2.exists():
        return candidate2
    return p


def get_files_from_manifest(manifest_file: Path) -> List[str]:
    if not manifest_file.exists():
        raise FileNotFoundError(f"Manifest not found: {manifest_file}")
    data = json.loads(manifest_file.read_text(encoding="utf-8"))
    files: List[str] = []
    for entry in data.get("selected_files", []):
        if entry.get("selected"):
            files.append(entry["filepath"])
    return files


def load_existing_metadata(metadata_file: Path) -> Dict[str, Dict]:
    if not metadata_file.exists():
        return {}
    data = json.loads(metadata_file.read_text(encoding="utf-8"))
    return data.get("files", {})


def save_metadata(metadata: Dict[str, Dict], metadata_file: Path) -> None:
    metadata_file.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now().isoformat(),
        "total_files": len(metadata),
        "files": metadata,
    }
    metadata_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def read_content(path: Path, max_chars: int = 30000) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""
    if len(text) > max_chars:
        return text[:max_chars] + "\n\n[... truncated ...]"
    return text


def extract_metadata(llm: GoogleGenAIChatGenerator, file_path: str, content: str, retries: int = 3) -> Dict:
    for attempt in range(retries):
        try:
            prompt = PROMPT_TEMPLATE.format(file_path=file_path, content=content)
            response = llm.run(messages=[ChatMessage.from_user(prompt)])
            text = response["replies"][0].text.strip()
            if text.startswith("```json"):
                text = text[7:]
            if text.startswith("```"):
                text = text[3:]
            if text.endswith("```"):
                text = text[:-3]
            return json.loads(text.strip())
        except Exception as err:
            error_text = str(err)
            if "429" in error_text or "RESOURCE_EXHAUSTED" in error_text or "quota" in error_text.lower():
                retry_after = 20
                match = re.search(r"retry in\s*([\d.]+)s", error_text, flags=re.IGNORECASE)
                if match:
                    retry_after = int(float(match.group(1))) + 2
                print(f"Rate limit hit for {Path(file_path).name}; waiting {retry_after}s before retry")
                time.sleep(retry_after)
                continue

            if attempt == retries - 1:
                return {
                    "file_path": file_path,
                    "summary": f"ERROR: {str(err)[:120]}",
                    "file_type": "other",
                    "domain_concepts": [],
                    "content_type": "mixed",
                    "primary_topics": [],
                    "code_examples": False,
                    "searchable_keywords": ["error"],
                    "can_answer_questions": [],
                }
            time.sleep(2)
    return {
        "file_path": file_path,
        "summary": "ERROR: extraction failed",
        "file_type": "other",
        "domain_concepts": [],
        "content_type": "mixed",
        "primary_topics": [],
        "code_examples": False,
        "searchable_keywords": ["error"],
        "can_answer_questions": [],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate file metadata for Week 3 probability routing")
    parser.add_argument("--files", nargs="+", help="specific file paths")
    parser.add_argument("--missing-only", action="store_true", help="only files not already in output")
    parser.add_argument("--retry-errors", action="store_true", help="re-run only entries whose summary starts with ERROR")
    parser.add_argument("--retry-incomplete", action="store_true", help="re-run entries with ERROR or blank/incomplete metadata")
    parser.add_argument("--limit", type=int, default=0, help="limit number of files for quick test")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help="LLM model")
    parser.add_argument("--checkpoint-every", type=int, default=10, help="save checkpoint every N files")
    parser.add_argument("--sleep-seconds", type=float, default=0.5, help="delay between requests")
    args = parser.parse_args()

    load_environment()

    if args.files:
        file_list = args.files
    else:
        file_list = get_files_from_manifest(MANIFEST_FILE)

    existing = load_existing_metadata(OUTPUT_FILE)
    if args.missing_only:
        file_list = [f for f in file_list if str(normalize_manifest_path(f)) not in existing]

    if args.retry_errors:
        error_keys = {
            k for k, v in existing.items()
            if isinstance(v, dict) and str(v.get("summary", "")).startswith("ERROR:")
        }
        file_list = [f for f in file_list if str(normalize_manifest_path(f)) in error_keys]
        print(f"Retry-errors mode: {len(file_list)} files selected")

    if args.retry_incomplete:
        def is_incomplete(entry: Dict) -> bool:
            summary = str(entry.get("summary", "")).strip()
            topics = entry.get("primary_topics", [])
            keywords = entry.get("searchable_keywords", [])
            concepts = entry.get("domain_concepts", [])
            if summary.startswith("ERROR:"):
                return True
            if summary == "" or summary.lower() in {"n/a", "none"}:
                return True
            if not isinstance(topics, list) or len(topics) == 0:
                return True
            if not isinstance(keywords, list) or len(keywords) == 0:
                return True
            if not isinstance(concepts, list):
                return True
            return False

        incomplete_keys = {
            k for k, v in existing.items()
            if isinstance(v, dict) and is_incomplete(v)
        }
        file_list = [f for f in file_list if str(normalize_manifest_path(f)) in incomplete_keys]
        print(f"Retry-incomplete mode: {len(file_list)} files selected")

    if args.limit and args.limit > 0:
        file_list = file_list[: args.limit]

    print(f"Processing files: {len(file_list)}")
    llm = GoogleGenAIChatGenerator(model=args.model)

    updated = 0
    for index, raw_file in enumerate(tqdm(file_list), start=1):
        abs_path = normalize_manifest_path(raw_file)
        key = str(abs_path)
        if not abs_path.exists():
            continue

        content = read_content(abs_path)
        if not content:
            continue

        metadata = extract_metadata(llm, key, content)
        existing[key] = metadata
        updated += 1

        if index % max(args.checkpoint_every, 1) == 0:
            save_metadata(existing, OUTPUT_FILE)
            print(f"Checkpoint saved: {index}/{len(file_list)}")

        if args.sleep_seconds > 0:
            time.sleep(args.sleep_seconds)

    save_metadata(existing, OUTPUT_FILE)
    print(f"Done. Updated: {updated} | Total stored: {len(existing)}")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
