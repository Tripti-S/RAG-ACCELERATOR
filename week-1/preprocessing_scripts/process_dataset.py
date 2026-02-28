import os
import re
from pathlib import Path
import pdfplumber
import fitz  # PyMuPDF
from docx import Document
import pytesseract
from pdf2image import convert_from_path
from PIL import Image


# ================= CONFIG =================
SCRIPT_DIR = Path(__file__).resolve().parent
WEEK1_DIR = SCRIPT_DIR.parent

RAW_DIR = WEEK1_DIR / "data" / "raw"
PROCESSED_DIR = WEEK1_DIR / "data" / "processed"

EXTRACTED_TEXT_DIR = PROCESSED_DIR / "extracted_text"
OCR_TEXT_DIR = PROCESSED_DIR / "ocr_text"
MARKDOWN_DIR = PROCESSED_DIR / "markdown"
CONVERSATIONAL_DIR = PROCESSED_DIR / "conversational"

TEXT_ONLY_FOLDERS = ["stackexchange", "chat", "forum", "transcripts"]

# If needed (Windows)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# ===========================================


def clean_text(text):
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ---------- TEXT EXTRACTION ----------

def extract_pdf_text(pdf_path):
    text = ""

    # Try pdfplumber first
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except:
        pass

    # If empty, try PyMuPDF
    if not text.strip():
        try:
            doc = fitz.open(pdf_path)
            for page in doc:
                text += page.get_text() + "\n"
        except:
            pass

    return text


def ocr_pdf(pdf_path):
    text = ""
    pages = convert_from_path(pdf_path)

    for page in pages:
        text += pytesseract.image_to_string(page)
        text += "\n"

    return text


def extract_docx_text(docx_path):
    doc = Document(docx_path)
    return "\n".join([p.text for p in doc.paragraphs])


# ---------- CLASSIFICATION ----------

def is_conversational(relative_path):
    top_folder = relative_path.parts[0].lower()
    return any(folder in top_folder for folder in TEXT_ONLY_FOLDERS)


def convert_to_markdown(text, title):
    return f"""# {title}

---

{text}

---
"""


# ---------- MAIN PROCESS ----------

def process_dataset():
    total = 0
    ocr_used = 0

    for root, _, files in os.walk(RAW_DIR):
        for file in files:
            input_path = Path(root) / file
            relative_path = input_path.relative_to(RAW_DIR)
            output_txt_path = EXTRACTED_TEXT_DIR / relative_path.with_suffix(".txt")

            output_txt_path.parent.mkdir(parents=True, exist_ok=True)

            text = ""

            print("Processing:", relative_path)

            try:
                # -------- PDF --------
                if file.lower().endswith(".pdf"):
                    text = extract_pdf_text(input_path)

                    if not text.strip():
                        print("  → Using OCR")
                        text = ocr_pdf(input_path)
                        ocr_output = OCR_TEXT_DIR / relative_path.with_suffix(".txt")
                        ocr_output.parent.mkdir(parents=True, exist_ok=True)
                        ocr_output.write_text(text, encoding="utf-8")
                        ocr_used += 1

                # -------- DOCX --------
                elif file.lower().endswith(".docx"):
                    text = extract_docx_text(input_path)

                # -------- TXT / MD --------
                elif file.lower().endswith((".txt", ".md")):
                    text = input_path.read_text(encoding="utf-8", errors="ignore")

                # -------- IMAGE --------
                elif file.lower().endswith((".png", ".jpg", ".jpeg")):
                    image = Image.open(input_path)
                    text = pytesseract.image_to_string(image)
                    ocr_used += 1

                else:
                    continue

                text = clean_text(text)
                output_txt_path.write_text(text, encoding="utf-8")

                # -------- CLASSIFY --------
                if is_conversational(relative_path):
                    conv_path = CONVERSATIONAL_DIR / relative_path.with_suffix(".txt")
                    conv_path.parent.mkdir(parents=True, exist_ok=True)
                    conv_path.write_text(text, encoding="utf-8")
                else:
                    title = input_path.stem.replace("_", " ").title()
                    md_content = convert_to_markdown(text, title)
                    md_path = MARKDOWN_DIR / relative_path.with_suffix(".md")
                    md_path.parent.mkdir(parents=True, exist_ok=True)
                    md_path.write_text(md_content, encoding="utf-8")

                total += 1

            except Exception as e:
                print("  ❌ Error:", e)

    print("\n✅ Processing Complete")
    print("Total files processed:", total)
    print("OCR used on:", ocr_used)


if __name__ == "__main__":
    process_dataset()
