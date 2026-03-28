# Chunking Analysis (Evidence-Backed) — _1

## Data Sources
- `week-2/artifacts/selected_files_manifest.json`
- `week-2/evaluations/metrics_snapshot_1.json`
- `week-2/evaluations/test_questions.json`

## Content Type Assessment
From `selected_files_manifest.json`:
- Total selected files: **459**
- Content type distribution:
  - `documentation`: **459**

No file in the final selected manifest is tagged as `code`, `table`, or other non-documentation content. This means chunking decisions should be treated as documentation-centric for the selected Week 2 corpus.

## Document Length Distribution (Word Count)
From `metrics_snapshot_1.json` (`manifest.word_stats`), computed over all 459 selected files:
- Shortest document: **36** words
- Longest document: **62,950** words
- Median: **985** words
- Mean: **1,582.5** words
- Standard deviation: **3,958.2** words
- Documents <200 words: **8**
- Documents >1,000 words: **224**
- Documents >2,000 words: **50**
- Missing files during measurement: **0**

## Deduplication Impact
From `selected_files_manifest.json` (`manifest_metadata`):
- Files selected after deduplication: **459**
- Reduction percentage: **0.65%**

The deduplication reduction is small in percentage terms but still provides a documented final selection boundary used for indexing/evaluation.

## Chunking-Relevant Observations (Strictly From Available Evidence)
1. The selected corpus is **entirely labeled as documentation** in the final manifest.
2. The length spread is high (36 to 62,950 words), so a single fixed chunk size is likely to underfit short files and overfit long outliers.
3. A large share of files are long (224 files >1,000 words), supporting boundary-aware or adaptive chunking approaches.
4. Very short files exist (8 files <200 words), where aggressive chunking can add overhead without clear benefit.

## Notes on Limits
- This file does **not** claim code-heavy behavior because current selected-file metadata does not show code content.
- Structural markers (headers/topic shifts) are not quantified here because no direct structural parser output artifact is present in the provided final evaluation set.
