from pathlib import Path
import shutil
import fitz  # PyMuPDF

SCRIPT_DIR = Path(__file__).resolve().parent
WEEK1_DIR = SCRIPT_DIR.parent

# Adjust this to your actual folder
input_dir = WEEK1_DIR / "data" / "raw" / "mit-notes"

base_output = WEEK1_DIR / "data" / "raw"
transcripts_dir = base_output / "transcripts"
books_dir = base_output / "books"
slides_dir = base_output / "slides_or_notes"
other_dir = base_output / "other"

for d in [transcripts_dir, books_dir, slides_dir, other_dir]:
    d.mkdir(parents=True, exist_ok=True)


def classify_pdf(pdf_path):
    name = pdf_path.name.lower()

    try:
        doc = fitz.open(pdf_path)
        first_page = doc[0].get_text().lower()
    except:
        return "other"

    # 📚 Book detection (strong signal)
    if (
        "introduction to probability" in first_page
        or "bertsekas" in first_page
        or "tsitsiklis" in first_page
        or "chap." in first_page
    ):
        return "book"

    # 🎓 Slide detection
    if (
        "lecture" in first_page
        or "mit opencourseware" in first_page
        or "mitres" in name
    ):
        return "slides"

    # 🗣 Transcript-style detection (long paragraph prose)
    if len(first_page.split()) > 300:
        return "transcript"

    return "other"


for pdf in input_dir.glob("*.pdf"):
    category = classify_pdf(pdf)

    if category == "transcript":
        shutil.copy(pdf, transcripts_dir / pdf.name)
    elif category == "book":
        shutil.copy(pdf, books_dir / pdf.name)
    elif category == "slides":
        shutil.copy(pdf, slides_dir / pdf.name)
    else:
        shutil.copy(pdf, other_dir / pdf.name)

print("Corpus classification complete.")


from collections import Counter

counts = Counter()

for pdf in input_dir.glob("*.pdf"):
    category = classify_pdf(pdf)
    counts[category] += 1

print(counts)
