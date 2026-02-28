# LLM Rate Limits & The $300 Solution

This document explains the rate limit constraints we encountered and how Google Cloud's free credit solves it.

## The Problem

Google's Gemini API free tier has strict rate limits:

| Model | RPM | RPD |
|-------|-----|-----|
| gemini-2.5-flash | 5 | **20** |
| gemini-2.5-flash-lite | 10 | **20** |

**Our workload requires:**
- RAG generation: 8 questions × 7 strategies = 56 requests
- Evaluation (LLM-as-judge): ~150 requests
- **Total: ~200+ requests per full experiment**

With 20 RPD, this is **impossible** on the free tier.

## The Solution: Google Cloud $300 Free Credit

Google Cloud offers **$300 in free credits** for new accounts:

1. Valid for **90 days**
2. **No automatic charges** - you only pay if you explicitly upgrade
3. Credit card required for verification only (not charged)
4. Each student gets their own $300 when they sign up

### Cost Breakdown

| Task | Requests | Est. Cost |
|------|----------|-----------|
| Full Week 2 experiment | ~206 | **~$0.32** |
| Student runs all 7 strategies | ~206 | ~$0.32 |
| 10x experimentation | ~2,060 | ~$3.20 |

**$300 credit = ~900+ full experiment runs**

Your students can experiment freely without worrying about costs.

## Setup Instructions

### 1. Sign Up for Google Cloud

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Sign in with your Google account
3. Accept the $300 free trial offer
4. Add a payment method (for verification - won't be charged)

### 2. Enable Gemini API

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Or search "Gemini API" in Cloud Console
3. Enable the API
4. Create an API key

### 3. Configure Environment

```bash
# .env file
GOOGLE_API_KEY=your_api_key_here
```

### 4. Run Experiments

```bash
# RAG generation
python week2_chunking/experiments/04_generate_rag_results.py naive_medium

# Evaluation
python week2_chunking/experiments/05_evaluate_results.py --strategies naive_small naive_medium naive_large
```

## Rate Limits: Free vs Paid

| Tier | RPM | RPD | Cost |
|------|-----|-----|------|
| Free | 5 | 20 | $0 |
| Pay-as-you-go | 1000+ | Unlimited | ~$0.30/1M input |

With the $300 credit, you're on pay-as-you-go rates but not actually paying.

## Model Pricing (Pay-as-you-go)

| Model | Input | Output |
|-------|-------|--------|
| gemini-2.5-flash | $0.30/1M | $2.50/1M |
| gemini-2.5-flash-lite | $0.10/1M | $0.40/1M |

## Why This Matters for Students

This is a **real-world lesson** in API economics:

1. **Free tiers have limits** - Plan for production from day one
2. **Cloud credits exist** - Most providers offer free trials
3. **Cost estimation matters** - Always estimate token usage before committing

## Advanced: Multi-Provider Support

If you want to add support for multiple LLM providers (Groq, Ollama) for redundancy or local development, see:

`week2_chunking/docs/ADVANCED_multi_provider_llm.md`
