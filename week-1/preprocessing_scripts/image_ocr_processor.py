import os
from pathlib import Path
import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import json

SCRIPT_DIR = Path(__file__).resolve().parent
WEEK1_DIR = SCRIPT_DIR.parent

RAW_DIR = WEEK1_DIR / "data" / "raw"
OUTPUT_DIR = WEEK1_DIR / "data" / "processed" / "image_ocr"

IMAGE_DIR = OUTPUT_DIR / "extracted_images"
OCR_DIR = OUTPUT_DIR / "ocr_text"

IMAGE_DIR.mkdir(parents=True, exist_ok=True)
OCR_DIR.mkdir(parents=True, exist_ok=True)

metadata_log = []

# If Windows needs explicit path:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def process_pdf(pdf_path):
    doc = fitz.open(pdf_path)

    for page_index in range(len(doc)):
        page = doc[page_index]
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            relative_pdf = pdf_path.relative_to(RAW_DIR)
            image_name = f"{relative_pdf.stem}_page{page_index+1}_img{img_index+1}.{image_ext}"

            image_output_path = IMAGE_DIR / image_name
            image_output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(image_output_path, "wb") as f:
                f.write(image_bytes)

            # OCR
            try:
                image = Image.open(image_output_path)
                ocr_text = pytesseract.image_to_string(image)

                ocr_output_path = OCR_DIR / (image_name + ".txt")
                ocr_output_path.write_text(ocr_text, encoding="utf-8")

                metadata_log.append({
                    "pdf_file": str(relative_pdf),
                    "page": page_index + 1,
                    "image_file": str(image_output_path.name),
                    "ocr_file": str(ocr_output_path.name)
                })

                print(f"OCR extracted: {image_name}")

            except Exception as e:
                print(f"OCR failed for {image_name}: {e}")


def main():
    total_pdfs = 0

    for root, _, files in os.walk(RAW_DIR):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = Path(root) / file
                print(f"Processing PDF: {pdf_path}")
                process_pdf(pdf_path)
                total_pdfs += 1

    # Save metadata
    metadata_path = OUTPUT_DIR / "metadata.json"
    metadata_path.write_text(json.dumps(metadata_log, indent=2), encoding="utf-8")

    print("\n✅ Image OCR extraction complete")
    print(f"PDFs processed: {total_pdfs}")
    print(f"Images extracted: {len(metadata_log)}")


if __name__ == "__main__":
    main()
