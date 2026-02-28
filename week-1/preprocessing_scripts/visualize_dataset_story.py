from pathlib import Path
from collections import Counter
import json
import matplotlib.pyplot as plt

# ================= CONFIG =================
SCRIPT_DIR = Path(__file__).resolve().parent
WEEK1_DIR = SCRIPT_DIR.parent

PROCESSED_DIR = WEEK1_DIR / "data" / "processed"
OCR_DIR = PROCESSED_DIR / "image_ocr" / "ocr_text"
OUTPUT_DIR = WEEK1_DIR / "analysis" / "analysis_output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ================= INITIALIZE =================
doc_count = 0
token_count = 0
lengths = []

source_distribution = Counter()
topic_counter = Counter()
file_type_distribution = Counter()

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

# ================= PROCESS MAIN DATA =================
for file in PROCESSED_DIR.rglob("*"):
    if file.suffix.lower() not in [".txt", ".md"]:
        continue

    doc_count += 1
    file_type_distribution[file.suffix.lower()] += 1

    text = file.read_text(encoding="utf-8", errors="ignore")
    tokens = text.split()
    token_count += len(tokens)
    lengths.append(len(tokens))

    parts = file.relative_to(PROCESSED_DIR).parts
    if len(parts) > 0:
        source_distribution[parts[0]] += 1

    lower_text = text.lower()
    for keyword in KEYWORDS:
        if keyword in lower_text:
            topic_counter[keyword] += 1

# ================= INCLUDE OCR DATA =================
ocr_count = 0
if OCR_DIR.exists():
    for file in OCR_DIR.rglob("*.txt"):
        ocr_count += 1
        source_distribution["ocr_text"] += 1
        file_type_distribution["ocr_txt"] += 1

# ================= ANALYSIS REPORT =================
analysis_report = {
    "total_documents": doc_count,
    "total_tokens": token_count,
    "average_document_length": sum(lengths) / len(lengths) if lengths else 0,
    "shortest_document": min(lengths) if lengths else 0,
    "longest_document": max(lengths) if lengths else 0,
    "ocr_documents": ocr_count
}

# Probability representation
total_assets = doc_count + ocr_count
probability_distribution = {
    key: value / total_assets if total_assets > 0 else 0
    for key, value in source_distribution.items()
}

analysis_report["probability_distribution"] = probability_distribution

# ================= SAVE JSON =================
with open(OUTPUT_DIR / "analysis_report.json", "w") as f:
    json.dump(analysis_report, f, indent=4)

with open(OUTPUT_DIR / "source_distribution.json", "w") as f:
    json.dump(dict(source_distribution), f, indent=4)

with open(OUTPUT_DIR / "topic_coverage.json", "w") as f:
    json.dump(dict(topic_counter), f, indent=4)

with open(OUTPUT_DIR / "file_type_distribution.json", "w") as f:
    json.dump(dict(file_type_distribution), f, indent=4)

print("✅ JSON reports generated.")

# ================= VISUALIZATIONS =================

# 1️⃣ Source Distribution Pie
if source_distribution:
    plt.figure()
    plt.pie(source_distribution.values(), labels=source_distribution.keys(), autopct="%1.1f%%")
    plt.title("Dataset Source Distribution (Including OCR)")
    plt.savefig(OUTPUT_DIR / "dataset_source_distribution.png")
    plt.show()

# 2️⃣ Topic Coverage
if topic_counter:
    plt.figure()
    plt.bar(topic_counter.keys(), topic_counter.values())
    plt.xticks(rotation=45)
    plt.title("Topic Coverage Across Dataset")
    plt.ylabel("Document Mentions")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "topic_coverage.png")
    plt.show()

# 3️⃣ File Type Distribution
if file_type_distribution:
    plt.figure()
    plt.bar(file_type_distribution.keys(), file_type_distribution.values())
    plt.title("File Type Distribution")
    plt.ylabel("Count")
    plt.savefig(OUTPUT_DIR / "file_type_distribution.png")
    plt.show()

# 4️⃣ Document Length Histogram
if lengths:
    plt.figure()
    plt.hist(lengths, bins=20)
    plt.title("Document Length Distribution")
    plt.xlabel("Token Count")
    plt.ylabel("Number of Documents")
    plt.savefig(OUTPUT_DIR / "document_length_distribution.png")
    plt.show()

print("🚀 Full dataset analytics + OCR integration complete.")
