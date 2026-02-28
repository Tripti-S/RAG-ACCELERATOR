import fitz
import pytesseract
from pdf2image import convert_from_path
from pathlib import Path
import cv2
import numpy as np
import re

# Set Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

SCRIPT_DIR = Path(__file__).resolve().parent
WEEK1_DIR = SCRIPT_DIR.parent

RAW_DIR = WEEK1_DIR / "data" / "raw"
PROCESSED_DIR = WEEK1_DIR / "data" / "processed" / "extracted_text"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def clean_text(text):
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_text_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text


def ocr_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    text = ""
    for page in pages:
        img = np.array(page)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text += pytesseract.image_to_string(gray)
    return text


for pdf in RAW_DIR.rglob("*.pdf"):
    print(f"Processing {pdf}")

    # Preserve folder structure
    relative_path = pdf.relative_to(RAW_DIR)
    output_path = PROCESSED_DIR / relative_path.with_suffix(".txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    text = extract_text_pdf(pdf)

    if len(text.strip()) < 200:
        print("  → OCR fallback")
        text = ocr_pdf(pdf)

    if len(text.strip()) > 100:
        text = clean_text(text)
        output_path.write_text(text, encoding="utf-8")

print("Recursive preprocessing complete.")
