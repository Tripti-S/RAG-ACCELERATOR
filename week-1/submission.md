# Week 1 Capstone Submission

## Student Name

Tripti Singh

## Project Title

ProbablAI: A Domain-Constrained RAG System for Academic Concept Mastery

## Problem Statement

Working professionals enrolled in advanced probability and statistics
courses struggle with fragmented, heterogeneous study material across
textbooks, lecture slides, notes, and transcripts; this project
consolidates that material into a structured, searchable,
source-grounded RAG knowledge base.

------------------------------------------------------------------------

## Data Overview

-   **Corpus size:** 964 documents, \~1.7M total tokens\
-   **Data sources:** MIT lecture notes, OpenIntro textbook material,
    academic probability resources, processed OCR notes\
-   **Formats:** Markdown (.md), text (.txt), OCR-extracted text\
-   **Domain:** Probability theory and foundational statistics

------------------------------------------------------------------------

## Data Curation Summary

-   **Extraction method:** PDF extraction via pdfplumber and PyMuPDF;
    OCR processed separately\
-   **Preprocessing steps:** Text normalization, whitespace cleanup,
    metadata preservation, Markdown structure retention\
-   **Key decisions:**
    -   Preserved Markdown hierarchy for semantic chunk alignment\
    -   Isolated OCR content to reduce embedding noise\
    -   Removed extremely short documents (\<50 tokens) where
        appropriate\
    -   Applied structured chunking for long documents

------------------------------------------------------------------------

## Pipeline Configuration

-   **Vector database:** Qdrant\
-   **Collection name:** probability_rag_week1\
-   **Embedding model:** BAAI/bge-large-en-v1.5 (1024 dimensions)\
-   **Chunk strategy:** Structured chunking (\~400-word segments with
    overlap)\
-   **LLM:** Gemini 2.5 Flash\
-   **Documents indexed:** 964 documents (producing chunked embeddings)

------------------------------------------------------------------------

## Trace Summary

Five evaluation queries were executed across conceptual and
definition-based prompts.

Patterns observed: - High retrieval quality for foundational definitions
(Bayes, CLT, expectation, independence). - Strong alignment when corpus
contains dense academic explanations. - Retrieval occasionally returns
multiple chunks from the same source when topic coverage is
concentrated. - System performs best on well-covered, formula-driven
questions.

  -------------------------------------------------------------------------
  Query           Retrieval               Answer            Notes
  --------------- ----------------------- ----------------- ---------------
  Explain Bayes   Good                    Good              Highly covered
  theorem                                                   concept in
                                                            corpus

  Conditional     Good                    Good              Retrieved
  probability                                               direct worked
  example                                                   example

  Independence    Good                    Good              Exact formula
  definition                                                retrieved

  Central Limit   Good                    Good              Strong
  Theorem                                                   theoretical
                                                            coverage

  Define          Good                    Good              Retrieved
  expectation                                               discrete +
                                                            continuous
                                                            cases
  -------------------------------------------------------------------------

------------------------------------------------------------------------

## Observations

### What types of queries work well?

-   Definition-based questions\
-   Formula-driven conceptual prompts\
-   Foundational probability topics\
-   Worked examples present in textbook material

### What types of queries struggle?

-   Meta-level critique questions\
-   Model failure or assumption-based analysis\
-   Highly advanced theoretical edge cases\
-   Topics sparsely represented in corpus

### Is the issue retrieval or generation?

Most issues are retrieval-related when content coverage is sparse.
Generation performs well when provided accurate chunks.

### What would you improve first?

-   Add more balanced coverage for advanced theoretical topics\
-   Improve deduplication across OCR and extracted materials\
-   Implement retrieval score analysis and dynamic top-k tuning\
-   Add evaluation metrics beyond qualitative traces

------------------------------------------------------------------------

## Self-Assessment

  -----------------------------------------------------------------------
  Criteria                Score (1-5)                    Notes
  ----------------------- ------------------------------ ----------------
  Problem scoping clarity 5                              Clear
                                                         educational use
                                                         case

  Data sourcing and       5                              Structured,
  curation                                               multi-source
                                                         corpus

  Pipeline is functional  5                              End-to-end RAG
                                                         working

  Trace quality and depth 4                              Strong but can
                                                         include more
                                                         failure cases

  Observations and        5                              Clear patterns
  analysis                                               and improvement
                                                         roadmap
  -----------------------------------------------------------------------

------------------------------------------------------------------------
