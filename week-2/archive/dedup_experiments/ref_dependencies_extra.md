# Enhanced Deduplication Dependencies

This file lists all Python dependencies required for running the enhanced deduplication and topic analysis in week-2/scripts/deduplicate_documents.py.

## Installation Command

To install all dependencies using uv pip, run:

uv pip install -r week-2/scripts/requirements_extra.txt

## requirements_extra.txt

- sentence-transformers
- scikit-learn
- fuzzywuzzy
- nltk
- torch
- numpy
- tqdm

## Notes
- torch is required for sentence-transformers.
- tqdm is used for progress bars.
- numpy is used for array operations and saving similarity matrices.
- nltk is used for tokenization and text preprocessing.

If you encounter issues with torch installation, refer to https://pytorch.org/get-started/locally/ for platform-specific instructions.
