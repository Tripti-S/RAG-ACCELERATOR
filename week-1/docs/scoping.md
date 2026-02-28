# Project Scoping Document

ProbablAI Domain-Constrained RAG for Probability and Statistics Mastery

## IDENTIFY

### What specific problem are you solving?

Working professionals enrolled in an intensive Probability and
Statistics course spend significant time navigating fragmented materials
across textbooks, lecture slides, handwritten notes, and external
resources to clarify core concepts, slowing down learning and exam
preparation.

### Who experiences this problem?

• Executive PG Diploma students in Data Science and AI\
• Mid-career professionals transitioning into analytics roles\
• Senior leaders revisiting statistical foundations\
• Adult learners balancing full-time work with academic study

### Capability Level

L2: Document QA

The system retrieves and answers complex conceptual questions across a
structured academic corpus with source grounding.

### One-Sentence Problem Statement

Working professionals spend 20--30 minutes searching across hundreds of
pages of probability textbooks, lecture slides, and handwritten notes to
clarify foundational concepts needed for coursework and exams.
------------------------------------------------------------------------

## 2. QUALIFY -- Is RAG the Right Approach?

RAG is appropriate because:

• The corpus is too large for prompt-only systems\
• The material is domain-specific and partly proprietary\
• Source attribution matters for academic trust\
• Queries require semantic retrieval


### Is the corpus too large for a single context window?

Yes.

The dataset contains:

• 964 processed documents\
• Over 1.7 million tokens\
• Long documents exceeding 60,000 tokens

This exceeds practical LLM context limits and requires retrieval-based
narrowing.

### Does semantic search add value over keyword matching?

Yes.

Probability questions are conceptual in nature. Semantic search captures
relationships between definitions, theorems, and applied examples that
keyword search would miss.

### Does source attribution matter?

Yes.

In an academic setting, learners require grounded explanations aligned
with course material and traceable references for exam preparation.

### Is the content domain-specific or proprietary?

Yes.

The corpus includes internal course PDFs, instructor-provided notes, and
structured academic lecture materials in addition to public MIT
resources.

Conclusion: RAG is appropriate due to corpus size, semantic retrieval
needs, source grounding requirements, and domain specificity.
Keyword search alone would not solve this problem. Direct prompting
risks hallucination. RAG provides structured retrieval with grounding.

------------------------------------------------------------------------

## 3. DEFINE -- What Does Success Look Like?

### Accuracy

Target: 80%+ conceptually correct responses grounded in source material.

### Latency

Observed average latency approximately 15 seconds for prototype phase.

### Cost

Local embeddings using FastEmbed reduce embedding API cost.

### Coverage

964 processed documents\
1.7M+ tokens\
Multi-source academic integration

------------------------------------------------------------------------

## 4. SCOPE -- Data and Work Required

### How many documents are indexed?

964 processed documents\
1.7M+ total tokens

### What formats are included?

• Markdown files\
• Plain text files\
• OCR-extracted text from PDFs\
• YouTube lecture transcripts\
• Structured academic notes\
• Conversation threads from statquest\

### How often does the data change?

Moderate update frequency:

• Weekly handwritten notes\
• Periodic lecture updates\
• Static textbook sources

### What is the data quality like?

Strengths:

• High-density academic content\
• Structured Markdown preservation\
• Strong foundational concept coverage

Challenges:

• OCR noise\
• Topic imbalance\
• Very long documents requiring chunking

### Who owns the data?

• Internal academic institution for course materials\
• MIT OpenCourseWare for public resources\
• Open-source textbook authors\
• Internet-Conversation-Threads\

------------------------------------------------------------------------

## Nuances and Trade-Offs

Markdown vs Plain Text: Preserved Markdown for semantic hierarchy.

OCR Inclusion: Extracted separately to protect embedding quality.

Chunk Size: Balanced recall and precision using overlapping chunks.

Embedding Model: Selected FastEmbed BGE-large for local reproducibility.

Trace Logging: Implemented programmatic evaluation for reproducibility.

------------------------------------------------------------------------

## Vision

ProbablAI demonstrates how domain-constrained RAG systems can
power structured educational copilots and extend to regulated,
technical, or compliance-heavy domains.

Future enhancements include hybrid OCR integration, user document
uploads, quiz generation, and concept graph visualization.

------------------------------------------------------------------------

End of Scoping Document