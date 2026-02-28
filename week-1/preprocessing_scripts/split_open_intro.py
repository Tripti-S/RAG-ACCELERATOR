import fitz
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
WEEK1_DIR = SCRIPT_DIR.parent

input_pdf = WEEK1_DIR / "data" / "raw" / "open_intro" / "os.pdf"
output_dir = WEEK1_DIR / "data" / "raw" / "open_intro"
output_dir.mkdir(parents=True, exist_ok=True)

doc = fitz.open(input_pdf)

# Adjust page ranges manually after checking TOC
chapters = {
    "probability": (1, 40),
    "random_variables": (41, 90),
    "distributions": (91, 140),
    "clt": (141, 180),
}

for name, (start, end) in chapters.items():
    new_doc = fitz.open()
    new_doc.insert_pdf(doc, from_page=start-1, to_page=end-1)
    new_doc.save(output_dir / f"openintro_chapter_{name}.pdf")

print("Chapters split.")
