# Week 2 Deep Analysis — Judge Reliability (Evidence-Backed) — _1

## Evaluation Setup
- Judge model: `gpt-4o-mini`
- Eval JSON file: `eval_results/final_comparitive_chunk_eval_20260301_211714.json`
- Evaluation method: `hybrid_two_stage`

## Spot-Check Method Used Here
This review is constrained to what is present in final artifacts:
1. Stage-1 per-strategy summaries (`avg_signal_pct`, `cut_mid_answer_count`, `high_useful_count`)
2. Stage-2 final ranking (`1st`, `2nd`, `3rd`)
3. Question-level consistency checks (whether ranking aligns with stage summaries)

No extra assumptions were added beyond recorded JSON content.

## Question-by-Question Spot Checks

### Q1
- Stage-1 summary highlights:
  - recursive: signal 63, high_useful 4
  - semantic: signal 54, high_useful 2
  - hybrid: signal 52, high_useful 1
- Stage-2 ranking: 1st=RECURSIVE, 2nd=SEMANTIC, 3rd=HYBRID
- Agreement check: **agree** (ranking aligns with stage summary ordering)

### Q2
- Stage-1 summary highlights:
  - recursive: signal 43, high_useful 1
  - semantic: signal 45, high_useful 0
  - hybrid: signal 48, high_useful 1
- Stage-2 ranking: 1st=RECURSIVE, 2nd=HYBRID, 3rd=SEMANTIC
- Agreement check: **partially agree** (hybrid has highest signal, but recursive ranked first)
- What this suggests: stage-2 likely weighs chunk-level qualitative notes beyond average signal.

### Q3
- Stage-1 summary highlights:
  - recursive: signal 43, high_useful 1
  - semantic: signal 30, high_useful 0
  - hybrid: signal 45, high_useful 3
- Stage-2 ranking: 1st=HYBRID, 2nd=RECURSIVE, 3rd=SEMANTIC
- Agreement check: **agree** (ranking aligns with higher useful-count and signal for hybrid)

### Q4
- Stage-1 summary highlights:
  - recursive: signal 50, high_useful 3
  - semantic: signal 43, high_useful 0
  - hybrid: signal 66, high_useful 4
- Stage-2 ranking: 1st=HYBRID, 2nd=RECURSIVE, 3rd=SEMANTIC
- Agreement check: **agree**

### Q5
- Stage-1 summary highlights:
  - recursive: signal 66, high_useful 3
  - semantic: signal 54, high_useful 3
  - hybrid: signal 66, high_useful 4
- Stage-2 ranking: 1st=HYBRID, 2nd=RECURSIVE, 3rd=SEMANTIC
- Agreement check: **agree** (tie on signal broken by high_useful)

## Overall Judge Reliability (Artifact-Consistency View)
- Questions checked: **5/10**
- Consistency with stage summaries:
  - Full agreement: **4/5**
  - Partial agreement: **1/5**
- Observed behavior:
  1. Stage-2 does not strictly optimize for average signal alone.
  2. Stage-2 appears to use qualitative stage-1 notes and usefulness patterns.
  3. No contradiction where clearly weakest stage-1 profile is ranked first in checked subset.

## Week-1 Naive Baseline Context (Cross-Model Anchor)
From `week-1/traces/traces.json`:
- queries: **5**
- avg latency: **8.468s**
- median latency: **7.97s**
- avg retrieval_count: **5.0**
- avg answer length: **1341.4**

Comparison use in this file:
- Use naive latency/retrieval depth as an operational baseline.
- Use Week-2 stage-1/stage-2 artifacts for quality ranking.
- Avoid direct naive-vs-stage score deltas because naive trace schema has no stage fields (`signal`, `useful`, `cutoffs`, rank).

## Bias/Limitations Found
- Potential weighting ambiguity between `avg_signal_pct` and qualitative chunk notes.
- This reliability check is **internal consistency** against stage-1 summaries; it is not a full manual human read of every retrieved chunk.

## Prompting/Method Observations
- Two-stage setup is auditable because stage-1 and stage-2 artifacts are both saved.
- Reliability improves when stage-2 reasons are read alongside stage-1 summary fields, not just final ranking labels.

## Source Files
- `evaluations/eval_results/final_comparitive_chunk_eval_20260301_211714.json`
- `evaluations/metrics_snapshot_1.json`
- `week-1/traces/traces.json`
