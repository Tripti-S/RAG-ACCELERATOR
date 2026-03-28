# Week 2 Checklist Verification — _1

## Verification Sources
- `week2_submission_guidelines.md` (provided checklist)
- `week-2/week2_prequalify.py` run output on current workspace
- `week-2/evaluations/metrics_snapshot_1.json`

## Checklist Status
- [x] `archive/` folder exists
- [x] `.gitingestignore` includes required entries (`archive/`, `rag_results/`, `data/raw/`, `data/processed/`, `*.parquet`, `*.csv`, `*.npy`, `*.bin`, `prequalify.py`, `week2_submission_guidelines.md`)
- [x] `week-2/submission.md` exists and has required sections (per prequalify output)
- [x] `week-2/docs/chunking-analysis.md` exists with required sections
- [x] `week-2/docs/chunking-strategy.md` exists with required sections
- [x] `week-2/docs/iteration-log.md` exists
- [x] `week-2/evaluations/test_questions.json` has 10 questions (within 8–15)
- [x] `week-2/evaluations/eval_results/` has final eval JSON (`final_comparitive_chunk_eval_20260301_211714.json`)
- [x] `week-2/evaluations/week2_comparison.md` exists
- [x] `week-2/evaluations/week2_deep_analysis.md` exists
- [x] `week-2/scripts/` contains Python scripts (15 files in nested folders)
- [~] Week 1 naive index comparison data present but incomplete schema (`naive_rag_results.json` lacks per-question fields)
- [ ] Prequalify script currently exits cleanly (current run crashes at submission txt decode step)

## Prequalify Run Findings (Current)
From latest run of `week-2/week2_prequalify.py`:
1. It reports many PASS checks.
2. It flags `scripts/` as failing because it checks only top-level `scripts/*.py` while your files are nested (e.g., `scripts/strategy/*.py`, `scripts/evaluation/*.py`).
3. It crashes with `UnicodeDecodeError` when reading `tripti_singh_week2_submission.txt` using default encoding.

## Actionable Fixes Before Final Submission
1. **Prequalify script fix**
   - Use UTF-8 when reading submission txt (`read_text(encoding="utf-8", errors="replace")`).
2. **Scripts check fix**
   - Update prequalify `check_has_scripts()` to use recursive glob (`scripts/**/*.py`) instead of top-level-only.
3. **Naive baseline comparability**
   - Regenerate naive RAG results in same schema as strategy RAG files for strict metric deltas.

## Evidence Artifacts
- `evaluations/metrics_snapshot_1.json`
- `evaluations/eval_results/final_comparitive_chunk_eval_20260301_211714.json`
- `evaluations/rag_results/*.json`
- `artifacts/selected_files_manifest.json`
- `week2_prequalify.py` terminal output (latest run)
