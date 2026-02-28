import os
from pathlib import Path
import pdfplumber
from docx import Document

SCRIPT_DIR = Path(__file__).resolve().parent
WEEK1_DIR = SCRIPT_DIR.parent

INPUT_DIR = WEEK1_DIR / "data" / "raw"
TEXT_OUTPUT_DIR = WEEK1_DIR / "data" / "processed" / "extracted_text"

TEXT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def extract_pdf_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
            text += "\n"
    return text


def extract_docx_text(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])


def process_files():
    total = 0

    for root, _, files in os.walk(INPUT_DIR):
        for file in files:
            input_path = Path(root) / file
            relative_path = input_path.relative_to(INPUT_DIR)
            output_path = TEXT_OUTPUT_DIR / relative_path.with_suffix(".txt")

            output_path.parent.mkdir(parents=True, exist_ok=True)

            text = ""

            try:
                if file.lower().endswith(".pdf"):
                    text = extract_pdf_text(input_path)

                elif file.lower().endswith(".docx"):
                    text = extract_docx_text(input_path)

                elif file.lower().endswith((".txt", ".md")):
                    text = input_path.read_text(encoding="utf-8", errors="ignore")

                else:
                    continue

                output_path.write_text(text, encoding="utf-8")
                total += 1
                print("Extracted:", relative_path)

            except Exception as e:
                print("Error processing:", relative_path, e)

    print(f"\n✅ Extraction complete. Files processed: {total}")


if __name__ == "__main__":
    process_files()
