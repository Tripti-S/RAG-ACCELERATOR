# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Week 2: Document Deduplication
===============================

Creates a selection manifest of non-duplicate files for indexing.

Two-stage deduplication:
1. Version-based: Keep latest version of spec files (YYYY-MM-DD, draft)
2. MinHash + LSH: Find content-based near-duplicates

Outputs:
- outputs/selected_files_manifest.json (local copy)
- outputs/deduplication_report.json (detailed analysis)
- outputs/similarity_matrix.npy (MinHash similarity matrix)
- artifacts/selected_files_manifest.json (for all chunking scripts)

Usage:
    # Default (threshold=0.85)
    python week2_chunking/deduplication/01_deduplicate_documents.py

    # Custom threshold
    python week2_chunking/deduplication/01_deduplicate_documents.py --threshold 0.90

    # Dry run (no files written)
    python week2_chunking/deduplication/01_deduplicate_documents.py --dry-run
"""

import sys
import numpy as np
from pathlib import Path
from typing import List

# Get absolute paths (works when run from any directory)
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent

# Add utils to path
sys.path.insert(0, str(SCRIPT_DIR))

from utils.version_dedup import deduplicate_by_version
from utils.minhash_dedup import find_near_duplicates_minhash
from utils.manifest_writer import (
    write_selection_manifest,
    write_deduplication_report,
    print_manifest_summary
)


def collect_all_files(data_dir: Path) -> List[Path]:
    """
    Collect all markdown and text files from MCP data directories.

    Scans three subdirectories:
    - curated_mcp_knowledge: Hand-selected documentation
    - mcp_docs_crawled: Official site crawl
    - mcp_python_sdk_filtered: SDK examples and source

    Args:
        data_dir (Path): Data directory path

    Returns:
        List[Path]: List of file paths
    """
    file_paths = []

    subdirs = ['curated_mcp_knowledge', 'mcp_docs_crawled', 'mcp_python_sdk_filtered']

    for subdir in subdirs:
        subdir_path = data_dir / subdir

        if not subdir_path.exists():
            print(f"   Warning: Directory not found: {subdir}")
            continue

        # Collect files by extension
        md_files = list(subdir_path.glob('*.md'))
        txt_files = list(subdir_path.glob('*.txt'))
        py_files = list(subdir_path.glob('*.py'))

        subdir_total = len(md_files) + len(txt_files) + len(py_files)
        print(f"   {subdir}: {subdir_total} files "
              f"({len(md_files)} .md, {len(txt_files)} .txt, {len(py_files)} .py)")

        file_paths.extend(md_files)
        file_paths.extend(txt_files)
        file_paths.extend(py_files)

    return file_paths


def main():
    """Main deduplication workflow."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Deduplicate MCP documentation files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Default deduplication
  python 01_deduplicate_documents.py

  # Higher similarity threshold (stricter deduplication)
  python 01_deduplicate_documents.py --threshold 0.90

  # Preview without writing files
  python 01_deduplicate_documents.py --dry-run
        """
    )

    parser.add_argument(
        '--threshold',
        type=float,
        default=0.85,
        help='MinHash Jaccard similarity threshold (default: 0.85). '
             'Higher = stricter matching'
    )

    parser.add_argument(
        '--num-perm',
        type=int,
        default=128,
        help='Number of MinHash permutations (default: 128). '
             'Higher = more accurate but slower'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview deduplication without writing output files'
    )

    parser.add_argument(
        '--data-dir',
        type=str,
        default=None,
        help='Data directory path (default: data/ at project root)'
    )

    args = parser.parse_args()

    # Header
    print("=" * 70)
    print("WEEK 2: DOCUMENT DEDUPLICATION")
    print("=" * 70)
    print(f"MinHash threshold: {args.threshold:.2f}")
    print(f"Hash permutations: {args.num_perm}")
    print(f"Dry run: {args.dry_run}")
    print("=" * 70)

    # Setup paths (using module-level constants for consistency)
    # Default data dir is at project root
    data_dir = Path(args.data_dir).resolve() if args.data_dir else PROJECT_ROOT / "data"

    # Local outputs directory
    output_dir = SCRIPT_DIR / "outputs"

    # Artifacts directory (for cross-week use)
    artifacts_dir = PROJECT_ROOT / "artifacts"

    if not data_dir.exists():
        print(f"\nError: Data directory not found: {data_dir}")
        print("   Specify with --data-dir /path/to/data")
        sys.exit(1)

    print(f"\nData directory: {data_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Artifacts directory: {artifacts_dir}")

    if not args.dry_run:
        output_dir.mkdir(exist_ok=True)
        artifacts_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: Collect all files
    print(f"\nSTEP 1: Collecting files from {data_dir.name}")
    print("-" * 70)

    all_files = collect_all_files(data_dir)

    if not all_files:
        print("\nError: No files found to process!")
        sys.exit(1)

    print(f"\n   Total files collected: {len(all_files)}")

    # Step 2: Version-based deduplication
    print(f"\nSTEP 2: Version-based deduplication")
    print("-" * 70)

    version_result = deduplicate_by_version(all_files)

    print(f"\n   Version dedup complete:")
    print(f"      Files processed: {version_result['stats']['original_count']}")
    print(f"      Files selected:  {version_result['stats']['selected_count']}")
    print(f"      Files excluded:  {version_result['stats']['excluded_count']}")
    print(f"      Version groups:  {version_result['stats']['version_groups']}")

    # Step 3: MinHash deduplication
    print(f"\nSTEP 3: MinHash near-duplicate detection")
    print("-" * 70)

    minhash_result = find_near_duplicates_minhash(
        version_result['selected_files'],
        threshold=args.threshold,
        num_perm=args.num_perm
    )

    print(f"\n   MinHash dedup complete:")
    print(f"      Files processed: {minhash_result['stats']['original_count']}")
    print(f"      Files selected:  {minhash_result['stats']['selected_count']}")
    print(f"      Files excluded:  {minhash_result['stats']['excluded_count']}")
    print(f"      Duplicate groups: {minhash_result['stats']['duplicate_groups']}")

    # Step 4: Calculate final statistics
    print(f"\nOVERALL DEDUPLICATION RESULTS")
    print("-" * 70)

    total_excluded = (
        version_result['stats']['excluded_count'] +
        minhash_result['stats']['excluded_count']
    )
    final_count = minhash_result['stats']['selected_count']
    reduction_pct = (total_excluded / len(all_files)) * 100 if len(all_files) > 0 else 0

    print(f"   Original files:    {len(all_files)}")
    print(f"   Final selection:   {final_count}")
    print(f"   Total excluded:    {total_excluded}")
    print(f"   Reduction:         {reduction_pct:.1f}%")

    # Step 5: Write outputs
    if args.dry_run:
        print(f"\nDRY RUN: No files written")
        print("-" * 70)
        print("   Would create:")
        print(f"      - {output_dir}/selected_files_manifest.json")
        print(f"      - {output_dir}/deduplication_report.json")
        print(f"      - {output_dir}/similarity_matrix.npy")
        print(f"      - {artifacts_dir}/selected_files_manifest.json")
    else:
        print(f"\nSTEP 4: Writing output files")
        print("-" * 70)

        # Write selection manifest (local copy)
        manifest_file = output_dir / "selected_files_manifest.json"
        write_selection_manifest(
            manifest_file,
            all_files,
            version_result,
            minhash_result
        )

        # Write artifacts manifest (for cross-week use)
        artifacts_manifest_file = artifacts_dir / "selected_files_manifest.json"
        write_selection_manifest(
            artifacts_manifest_file,
            all_files,
            version_result,
            minhash_result
        )
        print(f"   Artifacts manifest: {artifacts_manifest_file}")

        # Write detailed report
        report_file = output_dir / "deduplication_report.json"
        write_deduplication_report(
            report_file,
            all_files,
            version_result,
            minhash_result
        )

        # Save similarity matrix
        similarity_matrix_file = output_dir / "similarity_matrix.npy"
        np.save(similarity_matrix_file, minhash_result['similarity_matrix'])
        print(f"   Similarity matrix saved: {similarity_matrix_file}")

        # Print manifest summary
        import json
        with open(manifest_file, 'r') as f:
            manifest = json.load(f)
        print_manifest_summary(manifest)

    # Step 6: Next steps
    print("\nNEXT STEPS")
    print("-" * 70)

    if args.dry_run:
        print("   1. Review dry run results above")
        print("   2. Adjust --threshold if needed (higher = stricter)")
        print("   3. Run without --dry-run to create manifest")
    else:
        print(f"   1. Review deduplication report:")
        print(f"      {output_dir}/deduplication_report.json")
        print(f"\n   2. The manifest is now available for chunking experiments:")
        print(f"      {artifacts_dir}/selected_files_manifest.json")
        print(f"\n   3. Proceed to chunking experiments (coming in Week 2 Part 2)")

    print("\n" + "=" * 70)
    print("DEDUPLICATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nError: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
