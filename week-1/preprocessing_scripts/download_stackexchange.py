import requests
from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).resolve().parent
WEEK1_DIR = SCRIPT_DIR.parent

OUTPUT_DIR = WEEK1_DIR / "data" / "raw" / "stackexchange"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Get top 20 probability questions from API
api_url = "https://api.stackexchange.com/2.3/questions"

params = {
    "order": "desc",
    "sort": "votes",
    "tagged": "probability",
    "site": "stats.stackexchange",
    "pagesize": 20
}

response = requests.get(api_url, params=params)
data = response.json()

question_ids = [item["question_id"] for item in data["items"]]

print(f"Found {len(question_ids)} questions.")

headers = {
    "User-Agent": "Mozilla/5.0"
}

for qid in question_ids:
    url = f"https://stats.stackexchange.com/questions/{qid}"
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        file_path = OUTPUT_DIR / f"se_{qid}.html"
        file_path.write_text(r.text, encoding="utf-8")
        print(f"Downloaded {qid}")
    else:
        print(f"Failed {qid}")

    time.sleep(1)

print("Done.")
