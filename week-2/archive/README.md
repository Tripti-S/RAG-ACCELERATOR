# Week 2 Archive Map (Organized)

This folder is a working archive of drafts, references, and exploratory artifacts used during Week 2.

Use this file to answer: Why was this file added?

---

## Folder Layout

- `strategy_reasoning/` → strategy decisions, rationale, early notes
- `comparisons/` → chunk-count and strategy comparison drafts/snapshots
- `dedup_experiments/` → dedup scripts, dependency notes, manifest snapshots
- `tracing_references/` → logging/tracing implementation checklists
- `evaluation_snapshots/` → archived evaluation question variants
- `submission_versions/` → preserved submission writeup variants

---

## File-by-File Purpose Map

| File | Why it was added | Type | Feeds into | Suggested action |
|---|---|---|---|---|
| `strategy_reasoning/active_hybrid_strategy_detailed.md` | Detailed rationale for hybrid chunking and embedding choices, including tradeoffs and thresholds. | active-reference | `week-2/docs/chunking-strategy.md`, evaluation interpretation | Keep as detailed rationale source |
| `strategy_reasoning/scratch_notes_initial.md` | Early brainstorm notes on chunking and embeddings. | legacy-copy | Strategy decision context | Keep as decision history |
| `comparisons/snapshot_chunk_count_comparison.md` | Captures concrete chunk-count comparison across naive/recursive/semantic strategies. | snapshot | `week-2/evaluations/week2_comparison.md`, submission narrative | Keep as evidence snapshot |
| `comparisons/draft_chunking_comparison_template.md` | Generic comparison template with placeholders. | draft-template | Final comparison report structure | Keep as template only |
| `dedup_experiments/script_deduplicate_documents_enhanced.py` | Experimental dedup script with embedding + fuzzy + topic clustering analysis. | active-reference | Dedup workflow ideas, manifest generation pattern | Keep as experimental reference |
| `dedup_experiments/draft_deduplication_extra_analysis.md` | Documents advanced dedup motivation and approach. | draft-template | Optional appendix writeup | Keep as optional supporting note |
| `dedup_experiments/ref_dependencies_extra.md` | Human-readable explanation of extra dependencies for enhanced dedup path. | active-reference | Environment setup notes | Keep; sync with active environment docs if reused |
| `dedup_experiments/requirements_enhanced_dedup.txt` | Extra dependency list for enhanced dedup experiments. | active-reference | Optional experimentation environment | Keep; normalize package lines before production use |
| `dedup_experiments/snapshot_selected_files_manifest.json` | Snapshot manifest of selected corpus files post dedup steps. | snapshot | `week-2/artifacts/selected_files_manifest.json`, indexing scope | Keep for reproducibility |
| `tracing_references/ref_index_strategy_logging.txt` | Checklist for logging/tracing style from strategy index scripts. | active-reference | `week-2/artifacts/walkthrough_traces/*` output conventions | Keep as implementation checklist |
| `evaluation_snapshots/snapshot_test_questions.json` | Archived eval question set variant for retrieval testing. | snapshot | `week-2/evaluations/test_questions.json` | Keep for comparison |
| `submission_versions/legacy_submission_chunking.md` | Submission writeup variant with multi-strategy framing. | legacy-copy | Final submission drafting | Keep best sections, then supersede |
| `submission_versions/legacy_submission_chunking_strategy.md` | Submission writeup variant with hybrid-focused framing. | legacy-copy | Final submission drafting | Merge strongest parts into canonical doc |
| `submission_versions/ref_submission_index_hybrid_tracing.txt` | Reference checklist for adding tracing to hybrid indexing script. | active-reference | `week-2/artifacts/walkthrough_traces/*.txt` generation style | Keep as implementation note |

---

## Rename Traceability (Old → New)

- `chunking-startegy-detailed.md` → `strategy_reasoning/active_hybrid_strategy_detailed.md`
- `notes.md` → `strategy_reasoning/scratch_notes_initial.md`
- `comparision_chunk_count.md` → `comparisons/snapshot_chunk_count_comparison.md`
- `comparison.md` → `comparisons/draft_chunking_comparison_template.md`
- `deduplicate_documents.py` → `dedup_experiments/script_deduplicate_documents_enhanced.py`
- `deduplication_extra_analysis.md` → `dedup_experiments/draft_deduplication_extra_analysis.md`
- `dependencies_extra.md` → `dedup_experiments/ref_dependencies_extra.md`
- `requirements_extra.txt` → `dedup_experiments/requirements_enhanced_dedup.txt`
- `selected_files_manifest.json` → `dedup_experiments/snapshot_selected_files_manifest.json`
- `index_strategy_reference.txt` → `tracing_references/ref_index_strategy_logging.txt`
- `test_questions.json` → `evaluation_snapshots/snapshot_test_questions.json`
- `submission/chunking.md` → `submission_versions/legacy_submission_chunking.md`
- `submission/chunking-strategy.md` → `submission_versions/legacy_submission_chunking_strategy.md`
- `submission/index_hybrid_tracing_reference.txt` → `submission_versions/ref_submission_index_hybrid_tracing.txt`

---

## Canonical Sources to Use Going Forward

When writing final outputs, prefer these canonical locations:

- Strategy narrative: `week-2/docs/chunking-strategy.md`
- Iteration history: `week-2/docs/iteration-log.md`
- Evaluation outputs: `week-2/evaluations/eval_results/` and `week-2/evaluations/rag_results/`
- Trace logs: `week-2/artifacts/walkthrough_traces/`
- Active scripts: `week-2/scripts/`

Archive files are supporting evidence and drafting history, not source-of-truth.
