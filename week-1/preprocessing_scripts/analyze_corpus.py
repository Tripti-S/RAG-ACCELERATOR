from pathlib import Path
from collections import Counter
import json
import re

SCRIPT_DIR = Path(__file__).resolve().parent
WEEK1_DIR = SCRIPT_DIR.parent

PROCESSED_DIR = WEEK1_DIR / "data" / "processed"
OUTPUT_DIR = WEEK1_DIR / "analysis" / "analysis_output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

doc_count = 0
token_count = 0
lengths = []
source_distribution = Counter()
topic_counter = Counter()

KEYWORDS = [
    "conditional probability",
    "bayes",
    "independence",
    "central limit theorem",
    "random variable",
    "distribution",
    "sample space",
    "expectation"
]

for file in PROCESSED_DIR.rglob("*.txt"):
    doc_count += 1
    text = file.read_text(encoding="utf-8", errors="ignore")
    tokens = text.split()
    token_count += len(tokens)
    lengths.append(len(tokens))

    # Extract source name (first folder after processed/)
    parts = file.relative_to(PROCESSED_DIR).parts
    if len(parts) > 0:
        source = file.relative_to(PROCESSED_DIR).parts[0]
        source_distribution[source] += 1


    lower_text = text.lower()
    for keyword in KEYWORDS:
        if keyword in lower_text:
            topic_counter[keyword] += 1

analysis_report = {
    "total_documents": doc_count,
    "total_tokens": token_count,
    "average_document_length": sum(lengths) / len(lengths) if lengths else 0,
    "shortest_document": min(lengths) if lengths else 0,
    "longest_document": max(lengths) if lengths else 0
}

with open(OUTPUT_DIR / "analysis_report.json", "w") as f:
    json.dump(analysis_report, f, indent=4)

with open(OUTPUT_DIR / "source_distribution.json", "w") as f:
    json.dump(source_distribution, f, indent=4)

with open(OUTPUT_DIR / "topic_coverage.json", "w") as f:
    json.dump(topic_counter, f, indent=4)

print("Analysis reports generated.")
