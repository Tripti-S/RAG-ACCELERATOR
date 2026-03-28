# ============================================================================
# The Engineer's RAG Accelerator - Course Code
# Copyright (c) 2026 NeoSage. All rights reserved.
#
# This code is provided exclusively for enrolled students of the RAG Accelerator
# course. It may not be shared, redistributed, or used to create derivative works.
# See the Course Access Policy for full terms.
# ============================================================================

"""
Version-Based Deduplication
============================

Handles deduplication of versioned MCP documentation files.
Keeps the latest version when multiple versions of the same file exist.

Supported version patterns:
- Date-based: modelcontextprotocol_io_specification_2025-06-18_architecture.md
- Draft: modelcontextprotocol_io_specification_draft_architecture.md
"""

import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional
from collections import defaultdict


def extract_version_info(filename: str) -> Tuple[str, Optional[datetime]]:
    """
    Extract base name and version date from filename.

    Args:
        filename (str): Filename to parse

    Returns:
        Tuple[str, Optional[datetime]]: (base_name, version_date)
            - base_name: Filename with version replaced by placeholder
            - version_date: Parsed date or None if no version found

    Examples:
        >>> extract_version_info("spec_2025-06-18_arch.md")
        ("spec_VERSION_arch.md", datetime(2025, 6, 18))

        >>> extract_version_info("spec_draft_arch.md")
        ("spec_VERSION_arch.md", datetime.min)

        >>> extract_version_info("no_version.md")
        ("no_version.md", None)
    """
    # Pattern 1: Date-based version (YYYY-MM-DD)
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
    if date_match:
        try:
            version_date = datetime.strptime(date_match.group(1), '%Y-%m-%d')
            # Replace date with placeholder to create base name
            base_name = re.sub(r'_\d{4}-\d{2}-\d{2}_', '_VERSION_', filename)
            return base_name, version_date
        except ValueError:
            # Invalid date format, treat as no version
            pass

    # Pattern 2: Draft version (lowest priority - keep stable versions instead)
    if '_draft_' in filename.lower():
        base_name = re.sub(r'_draft_', '_VERSION_', filename, flags=re.IGNORECASE)
        return base_name, datetime.min  # Draft = lowest priority

    # No version pattern found
    return filename, None


def deduplicate_by_version(file_paths: List[Path]) -> Dict:
    """
    Deduplicate files by keeping only the latest version of each base file.

    Process:
    1. Group files by base name (version-agnostic)
    2. For each group, keep the file with the latest version date
    3. Track which files were kept and which were excluded

    Args:
        file_paths (List[Path]): List of file paths to deduplicate

    Returns:
        Dict: Deduplication results with structure:
            {
                'selected_files': {filename: (filepath, reason)},
                'excluded_files': [(filepath, reason, superseded_by)],
                'groups': [group_info_dicts],
                'stats': {
                    'original_count': int,
                    'selected_count': int,
                    'excluded_count': int,
                    'version_groups': int
                }
            }
    """
    print("   Grouping files by base name...")

    # Group files by base name
    version_groups = defaultdict(list)

    for filepath in file_paths:
        base_name, version_date = extract_version_info(filepath.name)
        version_groups[base_name].append((filepath, version_date))

    # Process each group
    selected_files = {}
    excluded_files = []
    dedup_groups = []

    print(f"   Found {len(version_groups)} unique base names")

    for base_name, versions in version_groups.items():
        if len(versions) == 1:
            # No duplicates - keep the file
            filepath, version_date = versions[0]
            selected_files[filepath] = (filepath, "no_duplicates_found")
        else:
            # Multiple versions - keep latest
            # Sort by version date (None < valid dates < datetime.max)
            versions_sorted = sorted(
                versions,
                key=lambda x: x[1] if x[1] is not None else datetime.min,
                reverse=True  # Latest first
            )

            latest_filepath, latest_date = versions_sorted[0]

            # Format version for display
            if latest_date == datetime.min:
                version_str = "draft"
            elif latest_date:
                version_str = latest_date.strftime('%Y-%m-%d')
            else:
                version_str = "unknown"

            # Keep latest version
            selected_files[latest_filepath] = (
                latest_filepath,
                f"latest_version_{version_str}"
            )

            # Track excluded versions
            for filepath, version_date in versions_sorted[1:]:
                if version_date == datetime.min:
                    excluded_version_str = "draft"
                elif version_date:
                    excluded_version_str = version_date.strftime('%Y-%m-%d')
                else:
                    excluded_version_str = "unknown"

                excluded_files.append((
                    filepath,
                    f"superseded_by_version_{version_str}",
                    latest_filepath.name
                ))

            # Store group info
            dedup_groups.append({
                'group_id': len(dedup_groups) + 1,
                'base_name': base_name,
                'files': [str(fp) for fp, _ in versions_sorted],
                'versions': [
                    vd.strftime('%Y-%m-%d') if vd and vd not in (datetime.min, None)
                    else ('draft' if vd == datetime.min else 'unknown')
                    for _, vd in versions_sorted
                ],
                'selected': str(latest_filepath),
                'method': 'version_based',
                'file_count': len(versions)
            })

    # Calculate statistics
    stats = {
        'original_count': len(file_paths),
        'selected_count': len(selected_files),
        'excluded_count': len(excluded_files),
        'version_groups': len(dedup_groups)
    }

    print(f"   Version groups with duplicates: {stats['version_groups']}")
    print(f"   Files excluded: {stats['excluded_count']}")

    return {
        'selected_files': selected_files,
        'excluded_files': excluded_files,
        'groups': dedup_groups,
        'stats': stats
    }


def get_version_dedup_summary(result: Dict) -> str:
    """
    Generate human-readable summary of version deduplication results.

    Args:
        result (Dict): Result from deduplicate_by_version()

    Returns:
        str: Formatted summary text
    """
    stats = result['stats']

    summary = f"""
Version-Based Deduplication Summary
====================================

Files processed:     {stats['original_count']}
Files selected:      {stats['selected_count']}
Files excluded:      {stats['excluded_count']}
Reduction:           {stats['excluded_count'] / stats['original_count'] * 100:.1f}%

Version groups found: {stats['version_groups']}

Top duplicate groups:
"""

    # Show top 5 groups by file count
    top_groups = sorted(
        result['groups'],
        key=lambda g: g['file_count'],
        reverse=True
    )[:5]

    for group in top_groups:
        summary += f"\n  {group['base_name'][:60]}..."
        summary += f"\n    Versions: {', '.join(group['versions'])}"
        summary += f"\n    Selected: {group['selected'].split('/')[-1]}\n"

    return summary
