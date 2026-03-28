

# Chunking Analysis for Week 2 Corpus

## Content Type Assessment

After reviewing the corpus, the following content types were identified:

- [x] **Code files**: Present in the form of problem sets, solutions, and some lecture notes (especially in the MIT notes and handwritten notes). These include functions, classes, and code snippets where splitting mid-function/class would harm context.
- [x] **Structured markdown**: Most files (books, open_intro, MIT notes) are well-structured with headers, sections, and lists, providing natural chunk boundaries.
- [x] **Technical documentation**: Some files, especially textbooks and lecture notes, are organized hierarchically, similar to API references or guides.
- [x] **Multi-topic articles**: Several lecture notes and book chapters cover multiple topics within a single document, making semantic chunking important.
- [x] **Simple prose**: Some narrative explanations and introductions are present, especially in open_intro and book chapters.
- [x] **Mixed content**: Many documents, especially lecture notes, interleave code, math, and text, requiring careful chunking.
- [ ] **Tables or structured data**: Not a dominant type, but some notes and textbooks may include tables—splitting mid-row should be avoided.
- [x] **Short documents**: A few files (e.g., some handwritten notes) are under 200 words and may not need chunking.

**Summary:**  
The corpus is predominantly structured markdown and technical documentation, with a significant presence of code and mixed content. Many documents are multi-topic, and some are very short. This diversity means chunking strategies must be flexible, respecting both structural and semantic boundaries.

## Document Length Distribution

- **Shortest document:** ~38 words (e.g., some handwritten notes)
- **Longest document:** Over 8,000 words (e.g., full textbooks)
- **Median document:** ~540 words (typical for lecture notes)
- **Standard deviation:** ~1,120 words
- **Too long for a single chunk:** At least 17 book chapters and some lecture notes exceed typical chunk sizes (e.g., >1000 words)
- **Too short to chunk meaningfully:** 41 documents
- **Outliers:** Full textbooks and some comprehensive lecture notes are extreme outliers in length.

**Deduplication results:**
- Total files before deduplication: 462
- Unique files after deduplication: 459
- Duplicates removed: 3 (0.65% reduction)

The deduplication process removed a small number of near-duplicates, slightly lowering the median document length and reducing the number of extreme outliers. The overall distribution remains broad, with both very short and very long documents.

## Chunking-Relevant Observations

- Most files have clear section boundaries (headers, dividers).
- Topic shifts within documents are common, especially in longer files.
- Code blocks should not be split mid-function or mid-class.
- Some documents reference other files, so cross-document context may be important.
- Mixed content and multi-topic files require chunking strategies that adapt to both structure and semantics.
- Metadata (filenames, paths) could help disambiguate chunk context.
- OCR-extracted text is noisier and less structured, requiring line/page-aware chunking.
- Some documents contain repeated boilerplate (e.g., license, navigation) that can add noise.
- A hybrid chunking approach may be needed for mixed-content files.
- Repeated boilerplate (e.g., license blocks) is present in some files and may add noise.

**Conclusion:**
The corpus is dominated by structured markdown and technical documentation, with a significant presence of code examples and some mixed-content files. Chunking strategies should respect natural boundaries, avoid splitting code blocks, and consider semantic topic shifts. Short documents may not require chunking, while long, multi-topic files will benefit from semantic or recursive strategies.
