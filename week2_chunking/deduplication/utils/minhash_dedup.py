# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
MinHash-Based Near-Duplicate Detection
=======================================

Uses MinHash + Locality Sensitive Hashing (LSH) to find near-duplicate documents
based on content similarity, even when filenames differ.

Technique:
- MinHash: Estimate Jaccard similarity efficiently
- LSH: Find candidate duplicates in sub-linear time
- Verification: Calculate actual Jaccard similarity for candidates
"""

import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Set
from collections import defaultdict

try:
    from datasketch import MinHash, MinHashLSH
except ImportError:
    raise ImportError(
        "datasketch is required for MinHash deduplication. "
        "Install with: pip install datasketch"
    )


def create_minhash(text: str, num_perm: int = 128) -> MinHash:
    """
    Create MinHash signature for document content.

    Uses word-level tokenization for simplicity and speed.

    Args:
        text (str): Document text
        num_perm (int): Number of hash permutations (default: 128)
            Higher = more accurate but slower

    Returns:
        MinHash: MinHash signature
    """
    minhash = MinHash(num_perm=num_perm)

    # Tokenize: split on whitespace, lowercase, remove very short words
    words = set(
        word.lower()
        for word in text.split()
        if len(word) >= 3  # Filter out very short words
    )

    # Update MinHash with each unique word
    for word in words:
        minhash.update(word.encode('utf-8'))

    return minhash


def calculate_jaccard_similarity(mh1: MinHash, mh2: MinHash) -> float:
    """
    Calculate Jaccard similarity between two MinHash signatures.

    Args:
        mh1 (MinHash): First MinHash signature
        mh2 (MinHash): Second MinHash signature

    Returns:
        float: Jaccard similarity (0.0 to 1.0)
    """
    return mh1.jaccard(mh2)


def find_near_duplicates_minhash(
    selected_files: Dict[Path, Tuple[Path, str]],
    threshold: float = 0.85,
    num_perm: int = 128
) -> Dict:
    """
    Find near-duplicate documents using MinHash + LSH.

    Process:
    1. Create MinHash signatures for all documents
    2. Build LSH index for fast candidate lookup
    3. For each document, query LSH to find similar documents
    4. Verify similarity and group duplicates
    5. Keep one file from each duplicate group

    Args:
        selected_files (Dict[Path, Tuple[Path, str]]): Files from version dedup
            Format: {filepath: (filepath, selection_reason)}
        threshold (float): Jaccard similarity threshold (default: 0.85)
            0.85 = 85% word overlap
        num_perm (int): Number of MinHash permutations (default: 128)

    Returns:
        Dict: Near-duplicate detection results with structure:
            {
                'selected_files': {filepath: (filepath, reason)},
                'excluded_files': [(filepath, reason, superseded_by)],
                'groups': [group_info_dicts],
                'stats': {
                    'original_count': int,
                    'selected_count': int,
                    'excluded_count': int,
                    'duplicate_groups': int
                },
                'similarity_matrix': np.ndarray (optional)
            }
    """
    print(f"   Threshold: {threshold:.2f} (Jaccard similarity)")
    print(f"   Hash permutations: {num_perm}")

    # Step 1: Create MinHash signatures
    print("   Creating MinHash signatures...")
    minhashes = {}
    file_contents = {}

    for filepath, (_, _) in selected_files.items():
        try:
            text = filepath.read_text(encoding='utf-8', errors='ignore')
            file_contents[filepath] = text
            minhash = create_minhash(text, num_perm=num_perm)
            minhashes[filepath] = minhash
        except Exception as e:
            print(f"   ⚠️  Error reading {filepath.name}: {e}")
            continue

    print(f"   Created {len(minhashes)} MinHash signatures")

    # Step 2: Build LSH index
    print("   Building LSH index...")
    lsh = MinHashLSH(threshold=threshold, num_perm=num_perm)

    for filepath, minhash in minhashes.items():
        # Use filepath as unique key
        lsh.insert(str(filepath), minhash)

    # Step 3: Find duplicate candidates
    print("   Querying LSH for near-duplicates...")
    duplicate_groups = []
    seen = set()
    filepath_to_group = {}

    for filepath, minhash in minhashes.items():
        if filepath in seen:
            continue

        # Query LSH for similar documents
        candidates = lsh.query(minhash)

        if len(candidates) > 1:
            # Found duplicates - convert back to Path objects
            candidate_paths = [Path(c) for c in candidates]

            # Calculate actual Jaccard similarities
            similarities = {}
            for other_path in candidate_paths:
                if other_path != filepath:
                    sim = calculate_jaccard_similarity(
                        minhashes[filepath],
                        minhashes[other_path]
                    )
                    similarities[other_path] = sim

            # Create duplicate group
            group_id = len(duplicate_groups) + 1
            duplicate_groups.append({
                'group_id': group_id,
                'files': [str(p) for p in candidate_paths],
                'similarities': {
                    f"{p1.name} <-> {p2.name}": sim
                    for p2, sim in similarities.items()
                    for p1 in [filepath]
                },
                'method': 'minhash',
                'threshold': threshold
            })

            # Track which files are in which group
            for path in candidate_paths:
                seen.add(path)
                filepath_to_group[path] = group_id

    print(f"   Found {len(duplicate_groups)} near-duplicate groups")

    # Step 4: Select one file from each duplicate group
    # Strategy: Keep the first file (alphabetically) from each group
    final_selected = {}
    excluded_files = []

    # First, add all non-duplicate files
    for filepath, (original_path, reason) in selected_files.items():
        if filepath not in filepath_to_group:
            final_selected[filepath] = (filepath, reason)

    # Then, select one file from each duplicate group
    for group in duplicate_groups:
        group_files = [Path(f) for f in group['files']]

        # Sort alphabetically and keep first
        group_files_sorted = sorted(group_files, key=lambda p: p.name)
        selected_file = group_files_sorted[0]
        excluded = group_files_sorted[1:]

        # Add selected file
        final_selected[selected_file] = (
            selected_file,
            f"selected_from_minhash_group_{group['group_id']}"
        )

        # Track excluded files
        for excluded_file in excluded:
            excluded_files.append((
                excluded_file,
                f"near_duplicate_in_group_{group['group_id']}",
                selected_file.name
            ))

    # Step 5: Calculate statistics
    stats = {
        'original_count': len(selected_files),
        'selected_count': len(final_selected),
        'excluded_count': len(excluded_files),
        'duplicate_groups': len(duplicate_groups)
    }

    print(f"   MinHash duplicate groups: {stats['duplicate_groups']}")
    print(f"   Additional files excluded: {stats['excluded_count']}")

    # Step 6: Create similarity matrix (optional, for analysis)
    similarity_matrix = create_similarity_matrix(minhashes)

    return {
        'selected_files': final_selected,
        'excluded_files': excluded_files,
        'groups': duplicate_groups,
        'stats': stats,
        'similarity_matrix': similarity_matrix
    }


def create_similarity_matrix(minhashes: Dict[Path, MinHash]) -> np.ndarray:
    """
    Create pairwise Jaccard similarity matrix for all documents.

    Useful for visualization and analysis.

    Args:
        minhashes (Dict[Path, MinHash]): MinHash signatures

    Returns:
        np.ndarray: Similarity matrix (n x n)
    """
    file_paths = list(minhashes.keys())
    n = len(file_paths)
    matrix = np.zeros((n, n))

    for i, path1 in enumerate(file_paths):
        for j, path2 in enumerate(file_paths):
            if i <= j:
                sim = calculate_jaccard_similarity(
                    minhashes[path1],
                    minhashes[path2]
                )
                matrix[i][j] = matrix[j][i] = sim

    return matrix


def get_minhash_dedup_summary(result: Dict) -> str:
    """
    Generate human-readable summary of MinHash deduplication results.

    Args:
        result (Dict): Result from find_near_duplicates_minhash()

    Returns:
        str: Formatted summary text
    """
    stats = result['stats']

    summary = f"""
MinHash Near-Duplicate Detection Summary
=========================================

Files processed:     {stats['original_count']}
Files selected:      {stats['selected_count']}
Files excluded:      {stats['excluded_count']}
Reduction:           {stats['excluded_count'] / stats['original_count'] * 100:.1f}%

Duplicate groups:    {stats['duplicate_groups']}

Top similarity pairs:
"""

    # Show highest similarity pairs from each group
    for group in result['groups'][:5]:  # Top 5 groups
        summary += f"\n  Group {group['group_id']}:"
        # Get top 3 similarity pairs
        top_pairs = sorted(
            group['similarities'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:3]

        for pair_name, similarity in top_pairs:
            summary += f"\n    {pair_name}: {similarity:.3f}"

    return summary


def analyze_similarity_distribution(similarity_matrix: np.ndarray) -> Dict:
    """
    Analyze the distribution of document similarities.

    Args:
        similarity_matrix (np.ndarray): Pairwise similarity matrix

    Returns:
        Dict: Statistics about similarity distribution
    """
    # Get upper triangle (excluding diagonal)
    n = similarity_matrix.shape[0]
    upper_triangle = similarity_matrix[np.triu_indices(n, k=1)]

    return {
        'mean': float(np.mean(upper_triangle)),
        'median': float(np.median(upper_triangle)),
        'std': float(np.std(upper_triangle)),
        'min': float(np.min(upper_triangle)),
        'max': float(np.max(upper_triangle)),
        'percentiles': {
            '25th': float(np.percentile(upper_triangle, 25)),
            '50th': float(np.percentile(upper_triangle, 50)),
            '75th': float(np.percentile(upper_triangle, 75)),
            '90th': float(np.percentile(upper_triangle, 90)),
            '95th': float(np.percentile(upper_triangle, 95))
        }
    }
