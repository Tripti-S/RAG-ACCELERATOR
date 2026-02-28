# Data Quality Notes

Probability RAG System -- Week 1 Corpus Analysis

------------------------------------------------------------------------

## Quantitative Analysis

### 1. Total Documents and Total Size

-   **Total Documents:** 964\
-   **Total Tokens:** 1,724,795\
-   **Average Document Length:** 1,789 tokens

The corpus size is sufficient for semantic retrieval and embedding-based
QA systems.

------------------------------------------------------------------------

### 2. Document Length Distribution

-   **Shortest Document:** 32 tokens\
-   **Longest Document:** 62,950 tokens\
-   **Estimated Median Length:** \~1,300--1,500 tokens

**Observations:**

-   Majority of documents fall within 0--5,000 tokens\
-   Long-tail distribution includes extreme outliers (\>20,000 tokens)\
-   Ultra-long documents (\~60k tokens) require structured chunking\
-   Very short documents (\<50 tokens) may produce weak embeddings

------------------------------------------------------------------------

### 3. Format Breakdown

**By File Type:**

-   `.txt` → 502\
-   `.md` → 462\
-   OCR text → 1,438

**By Content Classification:**

-   Conversational → 20 (0.83%)\
-   Extracted structured text → 482 (20.07%)\
-   Markdown → 462 (19.23%)\
-   OCR text → 1,438 (59.87%)

**Observation:**\
OCR-derived text dominates corpus volume (\~60%), increasing noise risk.

------------------------------------------------------------------------

### 4. Duplicate Count

No explicit duplicate detection results available.

**Risk Level:** Moderate (especially across OCR and extracted content).

Recommendation: Perform cosine similarity deduplication (\>0.95
threshold).

------------------------------------------------------------------------

## Qualitative Analysis

### 1. Well-Covered Topics

High-frequency concepts:

-   Random Variable (570)\
-   Distribution (566)\
-   Expectation (296)

Moderately covered:

-   Bayes (240)\
-   Independence (200)

The corpus strongly emphasizes foundational probability constructs.

------------------------------------------------------------------------

### 2. Sparse or Underrepresented Topics

Lower frequency concepts:

-   Central Limit Theorem (108)\
-   Sample Space (136)\
-   Conditional Probability (144)

Advanced theoretical coverage appears lighter relative to foundational
topics.

------------------------------------------------------------------------

### 3. Structural Quality Observations

**Strengths:**

-   Markdown preserves hierarchy and theorem structure\
-   Extracted text relatively clean\
-   Minimal conversational noise

**Weaknesses:**

-   OCR symbol degradation (σ, integrals, probability notation)\
-   Formatting inconsistencies in OCR content\
-   Potential repeated lecture materials

------------------------------------------------------------------------

### 4. Retrieval Risk Factors

Potential impacts on vector search:

-   Extremely long documents (60k+ tokens)\
-   Very short documents (\<50 tokens)\
-   OCR noise affecting embedding precision\
-   Topic imbalance favoring foundational probability\
-   Possible duplicate material

**Mitigation Strategy:**

-   400-word chunking with 50-word overlap\
-   Separate OCR indexing\
-   Deduplication pass before embedding\
-   Topic distribution monitoring

------------------------------------------------------------------------

## Overall Data Health Assessment

**Strengths:**

-   Large academic corpus\
-   High token density\
-   Structured Markdown presence\
-   Strong foundational topic coverage

**Limitations:**

-   OCR-heavy composition\
-   Topic skew\
-   Potential duplication

**Overall Readiness for Embedding:** High (with preprocessing
safeguards)
