# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 5: Semantic Cache Threshold Experiment
=============================================

Measures cosine distances between query pairs to find the right cache
distance threshold — the value that determines when two queries are
"close enough" to return a cached answer instead of running the full
RAG pipeline.

The core tradeoff:
- Threshold too low (e.g. 0.02): nearly exact-match only, minimal cache hits
- Threshold too high (e.g. 0.20): catches paraphrases but risks returning
  wrong cached answers for queries that are close but factually different

The dangerous case: "What is the expected value of X?" and "What is the variance of X?"
embed close together (same structure, similar vocabulary) but have entirely
different correct answers. A threshold that matches these is a production bug.

How it works:
1. Define query pairs in categories (paraphrases, dangerous near-misses, unrelated)
2. Embed all queries using Voyage-4-lite (same model as production cache)
3. Compute cosine distance for each pair (same metric as Redis HNSW index)
4. Show which pairs would hit/miss at each candidate threshold
5. Recommend the highest safe threshold (no dangerous matches)

Stack:
- Embeddings: Voyage-4-lite (2048d) via Voyage AI API
- Distance: Cosine distance (1 - cosine_similarity), matches Redis HNSW config
- No Redis or backend required — standalone experiment

Usage:
    python experiments/05_cache_threshold_experiment.py

    # With custom thresholds to test
    python experiments/05_cache_threshold_experiment.py --thresholds 0.03 0.06 0.10 0.15 0.20

Output:
    - Terminal table showing distances and hit/miss per threshold
    - JSON results saved to experiments/results/
"""

import os
import sys
import json
import time
import argparse
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple

from dotenv import load_dotenv

# Path resolution
SCRIPT_DIR = Path(__file__).resolve().parent       # experiments/
WEEK_DIR = SCRIPT_DIR.parent                        # week5_production/
PROJECT_ROOT = WEEK_DIR.parent                      # rag-accelerator-code/


# ---------------------------------------------------------------------------
# Query Pair Definitions
# ---------------------------------------------------------------------------

# Each pair: (query_a, query_b, category, notes)
# Categories:
#   PARAPHRASE      — same question, different words. Cache SHOULD hit.
#   NEAR_MISS       — similar structure but different answer. Cache MUST NOT hit.
#   UNRELATED       — clearly different questions. Cache should miss.
#   BOUNDARY        — subset/superset or borderline cases. Interesting to measure.

QUERY_PAIRS = [
    # --- PARAPHRASE: same question, different wording ---
    (
        "What is Bayes' theorem?",
        "Explain Bayes' theorem",
        "PARAPHRASE",
        "Minimal paraphrase, same intent"
    ),
    (
        "What is Bayes' theorem?",
        "What is Bayes' rule?",
        "PARAPHRASE",
        "Theorem vs rule — same concept"
    ),
    (
        "What is the Central Limit Theorem?",
        "Can you explain what the CLT is?",
        "PARAPHRASE",
        "Full name vs abbreviation"
    ),
    (
        "How do I compute a confidence interval?",
        "What are the steps to calculate a confidence interval?",
        "PARAPHRASE",
        "How-to rephrased"
    ),
    (
        "How does conditional probability work?",
        "Explain how conditional probability functions",
        "PARAPHRASE",
        "Close synonym (work/function)"
    ),

    # --- NEAR_MISS: similar structure, different correct answer ---
    (
        "What is the expected value of a random variable?",
        "What is the variance of a random variable?",
        "NEAR_MISS",
        "Expected value vs variance — related but different answers"
    ),
    (
        "What is a Type I error?",
        "What is a Type II error?",
        "NEAR_MISS",
        "Same structure, opposite statistical errors"
    ),
    (
        "What is the PDF of the normal distribution?",
        "What is the CDF of the normal distribution?",
        "NEAR_MISS",
        "PDF vs CDF — different functions, same distribution"
    ),
    (
        "What is a Poisson distribution?",
        "What is an exponential distribution?",
        "NEAR_MISS",
        "Different distributions — related but distinct"
    ),
    (
        "What is the law of total probability?",
        "What is the law of total expectation?",
        "NEAR_MISS",
        "Similar-sounding laws, different statements"
    ),
    (
        "How do I test a null hypothesis?",
        "How do I construct a confidence interval?",
        "NEAR_MISS",
        "Related inference procedures, different answers"
    ),

    # --- UNRELATED: clearly different topics ---
    (
        "What is Bayes' theorem?",
        "How do I simulate a Monte Carlo estimate?",
        "UNRELATED",
        "Theorem definition vs numerical simulation"
    ),
    (
        "What is the Central Limit Theorem?",
        "What is the law of large numbers?",
        "UNRELATED",
        "CLT vs LLN — different convergence results"
    ),
    (
        "How do I compute a p-value?",
        "What is the Bayes factor?",
        "UNRELATED",
        "Frequentist vs Bayesian inference — different paradigms"
    ),

    # --- BOUNDARY: subset, superset, or edge cases ---
    (
        "What is Bayes' theorem?",
        "What is Bayes' theorem and how is it applied?",
        "BOUNDARY",
        "Superset — broader version of same question"
    ),
    (
        "What distributions are in the exponential family?",
        "Is the Poisson distribution in the exponential family?",
        "BOUNDARY",
        "General vs specific about same topic"
    ),
    (
        "What is Bayes' theorem?",
        "Tell me about Bayes' rule",
        "PARAPHRASE",
        "Question vs command form"
    ),
]


# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

def load_environment() -> dict:
    """Load and validate environment variables for Voyage API."""
    # Try week5 .env first, fall back to project root
    env_file = WEEK_DIR / ".env"
    if not env_file.exists():
        env_file = PROJECT_ROOT / ".env"
    if env_file.exists():
        load_dotenv(env_file)

    voyage_key = os.getenv("VOYAGE_API_KEY")
    if not voyage_key or voyage_key.startswith("your_"):
        raise ValueError(
            "Missing VOYAGE_API_KEY.\n"
            f"Set it in {WEEK_DIR}/.env\n"
            "Get your key from: https://dash.voyageai.com/"
        )

    model = os.getenv("CACHE_EMBED_MODEL", "voyage-4-lite")
    dimension = int(os.getenv("CACHE_EMBED_DIMENSION", "2048"))
    production_threshold = float(os.getenv("CACHE_DISTANCE_THRESHOLD", "0.06"))

    return {
        "voyage_api_key": voyage_key,
        "embed_model": model,
        "embed_dimension": dimension,
        "production_threshold": production_threshold,
    }


# ---------------------------------------------------------------------------
# Embedding
# ---------------------------------------------------------------------------

def embed_queries(queries: List[str], env_config: dict) -> Dict[str, np.ndarray]:
    """
    Embed all unique queries using Voyage API in a single batch call.

    Returns:
        Dict mapping query text -> embedding (numpy array, float32)
    """
    import voyageai

    client = voyageai.Client(api_key=env_config["voyage_api_key"])
    model = env_config["embed_model"]

    print(f"   Embedding {len(queries)} unique queries with {model}...")

    # Voyage API supports batch embedding
    # output_dimension=2048 matches the retrieval pipeline and HNSW index config
    dimension = env_config["embed_dimension"]
    result = client.embed(queries, model=model, output_dimension=dimension)
    embeddings = {}

    for query, embedding in zip(queries, result.embeddings):
        embeddings[query] = np.array(embedding, dtype=np.float32)

    print(f"   Done. Dimension: {len(result.embeddings[0])}")
    return embeddings


# ---------------------------------------------------------------------------
# Distance Computation
# ---------------------------------------------------------------------------

def cosine_distance(a: np.ndarray, b: np.ndarray) -> float:
    """
    Compute cosine distance between two vectors.

    This matches the Redis HNSW COSINE distance metric:
        cosine_distance = 1 - cosine_similarity

    Range:
        0.0  = identical vectors
        1.0  = orthogonal vectors
        2.0  = opposite vectors

    The production cache uses: if distance < threshold -> cache hit.
    """
    similarity = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return float(1.0 - similarity)


def compute_pair_distances(
    pairs: List[Tuple[str, str, str, str]],
    embeddings: Dict[str, np.ndarray],
) -> List[Dict]:
    """
    Compute cosine distance for each query pair.

    Returns:
        List of dicts with pair info and computed distance.
    """
    results = []

    for query_a, query_b, category, notes in pairs:
        dist = cosine_distance(embeddings[query_a], embeddings[query_b])
        results.append({
            "query_a": query_a,
            "query_b": query_b,
            "category": category,
            "notes": notes,
            "cosine_distance": round(dist, 6),
        })

    return results


# ---------------------------------------------------------------------------
# Threshold Analysis
# ---------------------------------------------------------------------------

def analyze_thresholds(
    pair_results: List[Dict],
    thresholds: List[float],
) -> Dict:
    """
    For each threshold, determine which pairs would be cache hits,
    and flag any dangerous matches (NEAR_MISS pairs that hit).

    Returns:
        Dict with per-threshold analysis and recommendation.
    """
    analysis = {}

    for threshold in thresholds:
        hits = []
        misses = []
        dangerous = []

        for pair in pair_results:
            is_hit = pair["cosine_distance"] < threshold

            entry = {
                "query_a": pair["query_a"],
                "query_b": pair["query_b"],
                "category": pair["category"],
                "distance": pair["cosine_distance"],
            }

            if is_hit:
                hits.append(entry)
                if pair["category"] == "NEAR_MISS":
                    dangerous.append(entry)
            else:
                misses.append(entry)

        # Count hits by category
        hit_categories = {}
        for h in hits:
            cat = h["category"]
            hit_categories[cat] = hit_categories.get(cat, 0) + 1

        analysis[str(threshold)] = {
            "threshold": threshold,
            "total_hits": len(hits),
            "total_misses": len(misses),
            "dangerous_hits": len(dangerous),
            "safe": len(dangerous) == 0,
            "hits_by_category": hit_categories,
            "dangerous_details": dangerous,
        }

    # Recommend: highest threshold with zero dangerous hits
    safe_thresholds = [
        t for t in thresholds
        if analysis[str(t)]["dangerous_hits"] == 0
    ]
    recommended = max(safe_thresholds) if safe_thresholds else None

    return {
        "per_threshold": analysis,
        "recommended_threshold": recommended,
        "recommendation_rule": "Highest threshold with zero NEAR_MISS hits",
    }


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------

def print_pair_results(pair_results: List[Dict], production_threshold: float):
    """Print all pair distances, sorted by distance."""
    sorted_pairs = sorted(pair_results, key=lambda p: p["cosine_distance"])

    print(f"\n{'=' * 90}")
    print("QUERY PAIR DISTANCES (sorted by distance, ascending)")
    print(f"{'=' * 90}")
    print(f"   Production threshold: {production_threshold}")
    print(f"   Distance metric: Cosine distance (1 - cosine_similarity)")
    print(f"   Lower = more similar. 0 = identical.")
    print(f"{'─' * 90}")

    # Column headers
    print(f"   {'Dist':>8}  {'Cat':<12}  {'Query A':<30}  {'Query B':<30}")
    print(f"   {'─'*8}  {'─'*12}  {'─'*30}  {'─'*30}")

    for pair in sorted_pairs:
        dist = pair["cosine_distance"]
        cat = pair["category"]
        q_a = pair["query_a"][:28]
        q_b = pair["query_b"][:28]

        # Mark dangerous: near-miss pairs that fall below production threshold
        marker = ""
        if cat == "NEAR_MISS" and dist < production_threshold:
            marker = " << DANGEROUS"
        elif cat == "PARAPHRASE" and dist >= production_threshold:
            marker = " (miss)"

        print(f"   {dist:>8.4f}  {cat:<12}  {q_a:<30}  {q_b:<30}{marker}")

    print(f"{'─' * 90}")


def print_threshold_analysis(threshold_analysis: Dict, thresholds: List[float]):
    """Print the threshold sweep results."""
    print(f"\n{'=' * 90}")
    print("THRESHOLD SWEEP")
    print(f"{'=' * 90}")

    # Count totals by category
    print(f"\n   {'Threshold':>10}  {'Hits':>6}  {'Misses':>8}  {'Dangerous':>10}  {'Safe?':>7}  {'Paraphrase Hits':>16}")
    print(f"   {'─'*10}  {'─'*6}  {'─'*8}  {'─'*10}  {'─'*7}  {'─'*16}")

    per_threshold = threshold_analysis["per_threshold"]

    for t in thresholds:
        data = per_threshold[str(t)]
        safe_str = "YES" if data["safe"] else "NO"
        para_hits = data["hits_by_category"].get("PARAPHRASE", 0)

        print(f"   {t:>10.4f}  {data['total_hits']:>6}  {data['total_misses']:>8}  {data['dangerous_hits']:>10}  {safe_str:>7}  {para_hits:>16}")

    # Recommendation
    rec = threshold_analysis["recommended_threshold"]
    print(f"\n   Recommended threshold: {rec}")
    print(f"   Rule: {threshold_analysis['recommendation_rule']}")

    # Show dangerous details if any threshold has them
    for t in thresholds:
        data = per_threshold[str(t)]
        if data["dangerous_details"]:
            print(f"\n   Dangerous matches at threshold {t}:")
            for d in data["dangerous_details"]:
                print(f"      distance={d['distance']:.4f}  '{d['query_a'][:40]}' vs '{d['query_b'][:40]}'")


def print_category_summary(pair_results: List[Dict]):
    """Print distance statistics per category."""
    categories = {}
    for pair in pair_results:
        cat = pair["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(pair["cosine_distance"])

    print(f"\n{'=' * 90}")
    print("DISTANCE STATISTICS BY CATEGORY")
    print(f"{'=' * 90}")
    print(f"\n   {'Category':<14}  {'Count':>6}  {'Min':>8}  {'Max':>8}  {'Mean':>8}  {'Spread':>8}")
    print(f"   {'─'*14}  {'─'*6}  {'─'*8}  {'─'*8}  {'─'*8}  {'─'*8}")

    for cat in ["PARAPHRASE", "NEAR_MISS", "BOUNDARY", "UNRELATED"]:
        if cat in categories:
            dists = categories[cat]
            print(
                f"   {cat:<14}  {len(dists):>6}  "
                f"{min(dists):>8.4f}  {max(dists):>8.4f}  "
                f"{np.mean(dists):>8.4f}  {max(dists)-min(dists):>8.4f}"
            )

    # The critical gap
    if "PARAPHRASE" in categories and "NEAR_MISS" in categories:
        max_para = max(categories["PARAPHRASE"])
        min_near = min(categories["NEAR_MISS"])
        gap = min_near - max_para

        print(f"\n   Critical gap: {gap:.4f}")
        print(f"   (min NEAR_MISS distance) - (max PARAPHRASE distance)")

        if gap > 0:
            print(f"   Gap is POSITIVE — a safe threshold exists between {max_para:.4f} and {min_near:.4f}")
        else:
            print(f"   Gap is NEGATIVE — paraphrases and near-misses overlap. No perfectly safe threshold.")
            print(f"   You must choose: accept some missed paraphrases or accept some dangerous hits.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_experiment(thresholds: List[float]):
    """Run the full threshold experiment."""
    print("\n" + "=" * 90)
    print("WEEK 5: SEMANTIC CACHE THRESHOLD EXPERIMENT")
    print("=" * 90)

    # Load environment
    env_config = load_environment()
    print(f"\n   Model: {env_config['embed_model']} ({env_config['embed_dimension']}d)")
    print(f"   Production threshold: {env_config['production_threshold']}")
    print(f"   Thresholds to test: {thresholds}")
    print(f"   Query pairs: {len(QUERY_PAIRS)}")

    # Collect unique queries
    unique_queries = list(set(
        [q for pair in QUERY_PAIRS for q in (pair[0], pair[1])]
    ))
    print(f"   Unique queries to embed: {len(unique_queries)}")

    # Embed all queries in one batch
    print(f"\n{'─' * 50}")
    print("1. Embedding Queries")
    print(f"{'─' * 50}")

    start_time = time.time()
    embeddings = embed_queries(unique_queries, env_config)
    embed_time = time.time() - start_time
    print(f"   Embedding time: {embed_time:.1f}s")

    # Compute distances
    print(f"\n{'─' * 50}")
    print("2. Computing Pair Distances")
    print(f"{'─' * 50}")

    pair_results = compute_pair_distances(QUERY_PAIRS, embeddings)
    print(f"   Computed {len(pair_results)} pair distances")

    # Display results
    print_pair_results(pair_results, env_config["production_threshold"])
    print_category_summary(pair_results)

    # Threshold analysis
    print(f"\n{'─' * 50}")
    print("3. Threshold Analysis")
    print(f"{'─' * 50}")

    threshold_analysis = analyze_thresholds(pair_results, thresholds)
    print_threshold_analysis(threshold_analysis, thresholds)

    # Save results
    print(f"\n{'─' * 50}")
    print("4. Saving Results")
    print(f"{'─' * 50}")

    results_dir = SCRIPT_DIR / "results"
    results_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = results_dir / f"cache_threshold_experiment_{timestamp}.json"

    output_data = {
        "experiment": "Semantic Cache Threshold Experiment",
        "model": env_config["embed_model"],
        "dimension": env_config["embed_dimension"],
        "production_threshold": env_config["production_threshold"],
        "thresholds_tested": thresholds,
        "num_pairs": len(pair_results),
        "embedding_time_seconds": round(embed_time, 2),
        "generated_at": datetime.now().isoformat(),
        "pair_results": pair_results,
        "threshold_analysis": {
            "per_threshold": threshold_analysis["per_threshold"],
            "recommended_threshold": threshold_analysis["recommended_threshold"],
            "recommendation_rule": threshold_analysis["recommendation_rule"],
        },
        "category_stats": {},
    }

    # Add category stats to JSON
    categories = {}
    for pair in pair_results:
        cat = pair["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(pair["cosine_distance"])

    for cat, dists in categories.items():
        output_data["category_stats"][cat] = {
            "count": len(dists),
            "min": round(min(dists), 6),
            "max": round(max(dists), 6),
            "mean": round(float(np.mean(dists)), 6),
        }

    with open(output_file, "w") as f:
        json.dump(output_data, f, indent=2)

    print(f"   Results saved: {output_file}")

    # Final summary
    rec = threshold_analysis["recommended_threshold"]
    print(f"\n{'=' * 90}")
    print("EXPERIMENT COMPLETE")
    print(f"{'=' * 90}")
    print(f"   Recommended threshold: {rec}")
    print(f"   Production threshold:  {env_config['production_threshold']}")

    if rec is not None and env_config["production_threshold"] != rec:
        print(f"\n   Current production threshold ({env_config['production_threshold']}) "
              f"differs from recommendation ({rec}).")
        print(f"   Review the pair distances above to decide whether to adjust.")

    return output_data


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Week 5: Semantic cache threshold experiment"
    )
    parser.add_argument(
        "--thresholds",
        type=float,
        nargs="+",
        default=[0.03, 0.05, 0.06, 0.08, 0.10, 0.15, 0.20],
        help="Distance thresholds to test (default: 0.03 0.05 0.06 0.08 0.10 0.15 0.20)"
    )
    args = parser.parse_args()

    try:
        run_experiment(thresholds=sorted(args.thresholds))
    except Exception as e:
        print(f"\nError: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
