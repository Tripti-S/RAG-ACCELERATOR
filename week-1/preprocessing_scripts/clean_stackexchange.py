from bs4 import BeautifulSoup
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
WEEK1_DIR = SCRIPT_DIR.parent

input_dir = WEEK1_DIR / "data" / "raw" / "stackexchange"
output_dir = WEEK1_DIR / "data" / "processed" / "conversational" / "stackexchange"
output_dir.mkdir(parents=True, exist_ok=True)

for file in input_dir.glob("*.html"):
    html = file.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")

    # Remove unwanted sections
    for tag in soup(["script", "style", "nav", "footer", "aside"]):
        tag.decompose()

    text = soup.get_text(separator="\n")

    # Clean blank lines
    cleaned = "\n".join(line.strip() for line in text.splitlines() if line.strip())

    out_file = output_dir / file.with_suffix(".txt").name
    out_file.write_text(cleaned, encoding="utf-8")

print("StackExchange cleaning complete.")
