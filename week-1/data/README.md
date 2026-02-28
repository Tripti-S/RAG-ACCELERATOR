# Data Engineering & Corpus Documentation

ProbablAI -- Week 1 Data Layer

This document explains:

1.  Where the data came from\
2.  How it was extracted\
3.  What preprocessing was applied\
4.  What was filtered out and why\
5.  Final corpus statistics\
6.  The layered ingestion design

Raw data lives in:

week-1/data/raw/

Processed data lives in:

week-1/data/processed/

These directories are excluded from submission due to size, but fully
documented here.

------------------------------------------------------------------------

## 1. Data Sources

The corpus was intentionally diversified to improve robustness,
grounding, and conceptual coverage.

### Academic Core

• MIT 6.041 Probability Lectures & Transcripts\
• MIT 18.05 (Spring 2022) -- Lectures, Exams, Problem Sets\
• OpenIntro Statistics -- Probability chapters\
• Probability textbooks (digital PDF)

### Community & Applied Knowledge

• StackExchange Probability Tag -- Top-voted Q&A threads\
• StatQuest-style discussions

### Internal / Manual Collection

• Handwritten lecture notes (scanned PDFs)\
• Instructor-provided course PDFs\
• Slide decks (PPT / PDF format)

This multi-source strategy improved conceptual depth, applied framing,
and phrasing diversity.

------------------------------------------------------------------------

## 2. Data Extraction Methods

### PDF Extraction

Tools used:

• pdfplumber\
• PyMuPDF (fallback)

Strategy:

• Attempt structured text extraction\
• If extraction length suspiciously small → trigger OCR

------------------------------------------------------------------------

### OCR Pipeline

Tools:

• pytesseract\
• pdf2image\
• OpenCV

OCR was:

• Triggered conditionally\
• Stored separately\
• Not embedded initially

Reason: Mathematical OCR introduces symbol distortion. Separation
preserves embedding quality.

------------------------------------------------------------------------

### HTML Extraction

Tools:

• BeautifulSoup\
• requests

Steps:

• Removed navigation menus\
• Removed scripts and styling\
• Extracted semantic text blocks\
• Converted HTML → clean TXT

------------------------------------------------------------------------

### YouTube Transcript Extraction

Command used:

python -m yt_dlp --write-auto-subs --skip-download --sub-lang en
--convert-subs srt --yes-playlist PLAYLIST_URL

Post-processing:

• Converted SRT → plain text\
• Removed timestamps\
• Normalized formatting

------------------------------------------------------------------------

### MIT Filtering Strategy

Filtering command example:

Get-ChildItem -File \| Where-Object {
($_.Name -match "pset|exam|lec") -and ($\_.Extension -ne ".zip") }

Purpose:

• Avoid redundancy\
• Exclude irrelevant materials\
• Keep high-signal academic content

------------------------------------------------------------------------

## 3. Preprocessing Pipeline

Layered transformation:

RAW\
↓\
extracted_text (format normalization)\
↓\
markdown (structured academic content)\
conversational (cleaned Q&A/chat)\
↓\
INDEX THIS

------------------------------------------------------------------------

### extracted_text

• Normalize formats\
• Convert PDF/HTML/DOCX → text\
• Separate OCR content

------------------------------------------------------------------------

### markdown

• Preserve headings\
• Preserve theorem/definition structure\
• Enable structure-aware chunking

------------------------------------------------------------------------

### conversational

• Clean StackExchange threads\
• Remove signatures and unrelated comments\
• Retain Q&A structure

------------------------------------------------------------------------

## 4. Additional Preprocessing Steps

### Duplicate Detection

• Removed repeated documents\
• Eliminated near-identical copies\
• Prevented embedding redundancy

### Large Book Splitting

• Split large PDFs by topic/section\
• Prevented multi-topic contamination\
• Improved retrieval relevance

### Noise Removal

Removed:

• Lock files\
• Config files\
• Navigation elements\
• HTML headers/footers\
• Empty OCR outputs

### Metadata Enrichment

• Added source labels\
• Preserved file_path\
• Maintained folder hierarchy

------------------------------------------------------------------------

## 5. Final Corpus Statistics

Documents processed: 964\
Total tokens: \~1.7M\
OCR-derived files: 1,438 intermediate outputs\
Longest document: \~62k tokens

Format breakdown:

• Markdown\
• TXT\
• OCR text\
• Transcripts

------------------------------------------------------------------------

## 6. Value Added Through Preprocessing

This data layer demonstrates:

• Strategic dataset curation\
• Layered ingestion architecture\
• Conditional OCR handling\
• Structure-aware chunking\
• Noise filtering discipline\
• Reproducible processing scripts


------------------------------------------------------------------------

End of Data Documentation
