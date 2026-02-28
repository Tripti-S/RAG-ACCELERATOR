# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Selection Manifest Writer
==========================

Creates JSON manifest of selected files for Phase 1 indexing.
Provides audit trail of deduplication decisions.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple


def write_selection_manifest(
    output_file: Path,
    all_files: List[Path],
    version_result: Dict,
    minhash_result: Dict
) -> None:
    """
    Write selection manifest combining version and MinHash deduplication results.

    Args:
        output_file (Path): Output manifest file path
        all_files (List[Path]): Original list of all files scanned
        version_result (Dict): Results from version_based deduplication
        minhash_result (Dict): Results from MinHash deduplication
    """
    # Combine results
    final_selected = minhash_result['selected_files']

    # Build selected files list
    selected_entries = []
    for filepath, (original_path, reason) in final_selected.items():
        # Determine content type
        # SDK .txt files are code (Python SDK converted to .txt for Phase 1 compatibility)
        source_dir = filepath.parent.name
        extension = filepath.suffix.lower()

        if source_dir == "mcp_python_sdk_filtered" and extension == ".txt":
            content_type = "code"
        elif extension == ".py":
            content_type = "code"
        else:
            content_type = "documentation"

        selected_entries.append({
            "filepath": str(filepath),
            "source_dir": source_dir,
            "filename": filepath.name,
            "selected": True,
            "selection_reason": reason,
            "content_type": content_type
        })

    # Build excluded files list
    excluded_entries = []

    # From version dedup
    for filepath, reason, superseded_by in version_result['excluded_files']:
        excluded_entries.append({
            "filepath": str(filepath),
            "source_dir": filepath.parent.name,
            "filename": filepath.name,
            "selected": False,
            "exclusion_reason": reason,
            "superseded_by": superseded_by
        })

    # From MinHash dedup
    for filepath, reason, superseded_by in minhash_result['excluded_files']:
        excluded_entries.append({
            "filepath": str(filepath),
            "source_dir": filepath.parent.name,
            "filename": filepath.name,
            "selected": False,
            "exclusion_reason": reason,
            "superseded_by": superseded_by
        })

    # Combine deduplication groups
    all_groups = version_result['groups'] + minhash_result['groups']

    # Create manifest structure
    manifest = {
        "manifest_metadata": {
            "created_at": datetime.now().isoformat(),
            "deduplication_strategy": "version_based + minhash",
            "total_files_scanned": len(all_files),
            "files_selected": len(final_selected),
            "files_excluded": len(excluded_entries),
            "reduction_percentage": round(
                (len(excluded_entries) / len(all_files)) * 100, 2
            ) if len(all_files) > 0 else 0,
            "version": "phase3_v1",
            "deduplication_stages": {
                "version_based": {
                    "files_processed": version_result['stats']['original_count'],
                    "files_excluded": version_result['stats']['excluded_count'],
                    "groups_found": version_result['stats']['version_groups']
                },
                "minhash": {
                    "files_processed": minhash_result['stats']['original_count'],
                    "files_excluded": minhash_result['stats']['excluded_count'],
                    "groups_found": minhash_result['stats']['duplicate_groups']
                }
            }
        },
        "selected_files": selected_entries,
        "excluded_files": excluded_entries,
        "deduplication_groups": all_groups
    }

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"   ✅ Manifest written: {output_file}")
    print(f"      Selected files: {len(selected_entries)}")
    print(f"      Excluded files: {len(excluded_entries)}")
    print(f"      Reduction: {manifest['manifest_metadata']['reduction_percentage']}%")


def write_deduplication_report(
    output_file: Path,
    all_files: List[Path],
    version_result: Dict,
    minhash_result: Dict
) -> None:
    """
    Write detailed deduplication analysis report.

    Args:
        output_file (Path): Output report file path
        all_files (List[Path]): Original list of all files scanned
        version_result (Dict): Results from version_based deduplication
        minhash_result (Dict): Results from MinHash deduplication
    """
    from .version_dedup import get_version_dedup_summary
    from .minhash_dedup import get_minhash_dedup_summary, analyze_similarity_distribution

    # Generate summaries
    version_summary = get_version_dedup_summary(version_result)
    minhash_summary = get_minhash_dedup_summary(minhash_result)

    # Analyze similarity distribution
    similarity_stats = analyze_similarity_distribution(
        minhash_result['similarity_matrix']
    )

    # Create comprehensive report
    report = {
        "report_metadata": {
            "created_at": datetime.now().isoformat(),
            "total_files_scanned": len(all_files),
            "final_files_selected": len(minhash_result['selected_files']),
            "total_files_excluded": (
                version_result['stats']['excluded_count'] +
                minhash_result['stats']['excluded_count']
            )
        },
        "version_deduplication": {
            "summary": version_summary,
            "statistics": version_result['stats'],
            "duplicate_groups": version_result['groups']
        },
        "minhash_deduplication": {
            "summary": minhash_summary,
            "statistics": minhash_result['stats'],
            "duplicate_groups": minhash_result['groups'],
            "similarity_distribution": similarity_stats
        },
        "file_breakdown": {
            "by_source_directory": get_directory_breakdown(
                all_files,
                minhash_result['selected_files']
            )
        }
    }

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"   ✅ Report written: {output_file}")


def get_directory_breakdown(
    all_files: List[Path],
    selected_files: Dict[Path, Tuple[Path, str]]
) -> Dict:
    """
    Break down file counts by source directory.

    Args:
        all_files (List[Path]): All original files
        selected_files (Dict[Path, Tuple]): Selected files after dedup

    Returns:
        Dict: Directory-wise statistics
    """
    from collections import defaultdict

    dir_stats = defaultdict(lambda: {'total': 0, 'selected': 0, 'excluded': 0})

    # Count all files
    for filepath in all_files:
        dir_name = filepath.parent.name
        dir_stats[dir_name]['total'] += 1

    # Count selected files
    for filepath in selected_files.keys():
        dir_name = filepath.parent.name
        dir_stats[dir_name]['selected'] += 1

    # Calculate excluded
    for dir_name in dir_stats:
        dir_stats[dir_name]['excluded'] = (
            dir_stats[dir_name]['total'] - dir_stats[dir_name]['selected']
        )
        dir_stats[dir_name]['reduction_percentage'] = round(
            (dir_stats[dir_name]['excluded'] / dir_stats[dir_name]['total']) * 100, 2
        ) if dir_stats[dir_name]['total'] > 0 else 0

    return dict(dir_stats)


def load_manifest(manifest_file: Path) -> Dict:
    """
    Load selection manifest from file.

    Args:
        manifest_file (Path): Path to manifest JSON

    Returns:
        Dict: Parsed manifest data

    Raises:
        FileNotFoundError: If manifest doesn't exist
        json.JSONDecodeError: If manifest is invalid JSON
    """
    if not manifest_file.exists():
        raise FileNotFoundError(f"Manifest not found: {manifest_file}")

    with open(manifest_file, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # Validate structure
    required_keys = ['manifest_metadata', 'selected_files', 'excluded_files']
    for key in required_keys:
        if key not in manifest:
            raise ValueError(f"Invalid manifest: missing '{key}' key")

    return manifest


def get_selected_file_paths(manifest: Dict) -> List[str]:
    """
    Extract list of selected file paths from manifest.

    Args:
        manifest (Dict): Loaded manifest data

    Returns:
        List[str]: List of file paths to index
    """
    return [
        entry['filepath']
        for entry in manifest['selected_files']
        if entry['selected']
    ]


def print_manifest_summary(manifest: Dict) -> None:
    """
    Print human-readable summary of manifest.

    Args:
        manifest (Dict): Loaded manifest data
    """
    metadata = manifest['manifest_metadata']

    print("\n" + "=" * 60)
    print("SELECTION MANIFEST SUMMARY")
    print("=" * 60)
    print(f"Created: {metadata['created_at']}")
    print(f"Strategy: {metadata['deduplication_strategy']}")
    print(f"\nFiles scanned:  {metadata['total_files_scanned']}")
    print(f"Files selected: {metadata['files_selected']}")
    print(f"Files excluded: {metadata['files_excluded']}")
    print(f"Reduction:      {metadata['reduction_percentage']}%")

    if 'deduplication_stages' in metadata:
        stages = metadata['deduplication_stages']
        print(f"\nVersion dedup:  -{stages['version_based']['files_excluded']} files "
              f"({stages['version_based']['groups_found']} groups)")
        print(f"MinHash dedup:  -{stages['minhash']['files_excluded']} files "
              f"({stages['minhash']['groups_found']} groups)")

    print("=" * 60 + "\n")
