# Week 3 Retrieval Analysis

## Constraint Assessment

- Latency budget: under 10 seconds is acceptable for interactive use and evaluation workflows.
- Cost budget: low to moderate; additional retrieval steps are acceptable when they produce clear quality gains.
- Accuracy criticality: high/costly; wrong answers on this learning corpus can mislead concept understanding and downstream implementation decisions.
- Query volume: under 100 queries/day; quality can be prioritized over high-throughput optimization.


## Corpus Assessment

- Heterogeneity: yes. `week-1/data/processed` contains mixed modalities and formats: `3962` files total across markdown/text/OCR and images (`.txt 1940`, `.md 462`, `.jpeg 969`, `.png 469`, `.jpx 121`, plus metadata JSON).
- Domain boundaries: clear. Folder structure separates source domains such as `mit-notes-2018`, `mit-notes-2022`, `HandwrittenLecNotes`, `open_intro`, `books`, and `stackexchange`.
- Metadata quality: usable. The OCR pipeline includes structured metadata (`week-1/data/processed/image_ocr/metadata.json`) with `pdf_file`, `page`, `image_file`, and `ocr_file` mappings, which supports traceability and filtering.
- Query patterns: mixed. Corpus composition supports both keyword-heavy lookups (formula terms, chapter/lecture labels, StackExchange phrasing) and conceptual questions (lecture notes + textbook explanations).
- Cross-document needs: common. Useful answers often require combining textbook context, lecture notes/transcripts, and OCR-derived content from handwritten notes.

Note on scope: `week3_retrieval/` is reference-only. Final Week 3 decisions are based on `week-3/` implementation/evaluation artifacts built on this Week 1/2 data lineage.

## Narrowing Assessment

| Criterion | Your Answer | Points Toward Narrowing? |
|---|---|---|
| Corpus is heterogeneous | Yes | Yes |
| Domain boundaries are clear | Yes | Yes |
| Quality metadata exists or can be generated | Yes | Yes |
| Accuracy is critical | Yes | Yes |
| Latency budget is flexible | Yes | Yes |
| Cost budget is flexible | Partial (low/moderate) | Partial |

Assessment: this is `5 Yes + 1 Partial`, so narrowing is worth testing.

Final Week 3 decision:
- Narrowing should be evaluated as an optional enhancement path.
- Hybrid + rerank remains the default baseline because it offers strong quality gains with lower complexity.
- Narrowing is not forced for every query due to added latency/cost and over-filtering risk on multi-source questions.
