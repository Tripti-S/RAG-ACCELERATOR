from pathlib import Path
import hashlib
import json
from collections import defaultdict
from datetime import datetime

# CHANGE THIS if needed
SCRIPT_DIR = Path(__file__).resolve().parent
WEEK1_DIR = SCRIPT_DIR.parent

DATA_ROOT = WEEK1_DIR / "data" / "processed"
LOG_DIR = WEEK1_DIR / "data" / "artifacts"
LOG_DIR.mkdir(exist_ok=True)

def file_hash(path: Path, chunk_size=8192):
    """Compute SHA256 hash of file content."""
    hasher = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()

def scan_duplicates(root: Path):
    hash_map = defaultdict(list)
    processed_files = []

    print("Starting recursive scan...\n")

    for file in root.rglob("*.*"):  # recursive
        if file.is_file():
            print(f"Checking: {file}")
            try:
                h = file_hash(file)
                hash_map[h].append(str(file))
                processed_files.append(str(file))
            except Exception as e:
                print(f"Skipped {file}: {e}")

    duplicates = {h: files for h, files in hash_map.items() if len(files) > 1}

    return processed_files, duplicates


if __name__ == "__main__":
    start_time = datetime.now()

    processed_files, duplicates = scan_duplicates(DATA_ROOT)

    report = {
        "timestamp": start_time.isoformat(),
        "total_files_checked": len(processed_files),
        "duplicate_groups_found": len(duplicates),
        "duplicates": duplicates
    }

    report_path = LOG_DIR / "duplicate_report.json"

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    print("\n===== SCAN COMPLETE =====")
    print(f"Total files checked: {len(processed_files)}")
    print(f"Duplicate groups found: {len(duplicates)}")
    print(f"Report saved to: {report_path}")

    if duplicates:
        print("\n⚠️ DUPLICATES DETECTED — FIX BEFORE PROCEEDING.")
    else:
        print("\n✅ No duplicates found. Safe to continue.")
