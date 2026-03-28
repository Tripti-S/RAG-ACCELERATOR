# Deduplication script for Week 2 submission
# Adapted from week2_chunking/deduplication/01_deduplicate_documents.py
# All data paths updated to use week-1/data/processed


import argparse
import sys
import os
import json
import shutil
from pathlib import Path
import numpy as np
from collections import defaultdict
from typing import List, Dict, Any
# Enhanced deduplication imports
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from fuzzywuzzy import fuzz
import nltk
nltk.download('punkt', quiet=True)

def parse_args():
	parser = argparse.ArgumentParser(description="Deduplicate documents for RAG pipeline.")
	parser.add_argument('--input-dir', type=str, default='../../week-1/data/processed/markdown',
						help='Input directory containing markdown files')
	parser.add_argument('--output-dir', type=str, default='outputs',
						help='Directory to write deduplication outputs')
	parser.add_argument('--artifacts-dir', type=str, default='../../week-2/artifacts',
						help='Directory to write manifest for cross-week use')
	parser.add_argument('--threshold', type=float, default=0.85,
						help='MinHash similarity threshold for deduplication')
	parser.add_argument('--dry-run', action='store_true',
						help='If set, do not write any files')
	parser.add_argument('--enhanced', action='store_true',
						help='Enable enhanced deduplication and topic analysis')
	return parser.parse_args()

def collect_files(input_dir: Path) -> List[Path]:
	files = list(input_dir.glob('**/*.md'))
	print(f"Collected {len(files)} markdown files from {input_dir}")
	return files

def version_based_deduplication(files: List[Path]) -> Dict[str, Any]:
	# Placeholder for version-based deduplication logic
	# For now, just return all files as unique
	print("Running version-based deduplication (placeholder)")
	return {'unique_files': files, 'duplicates': []}

def minhash_deduplication(files: List[Path], threshold: float) -> Dict[str, Any]:
	# Enhanced: Use embeddings and fuzzy matching for near-duplicate detection
	print(f"Running MinHash/content similarity deduplication with threshold {threshold}")
	texts = []
	for f in files:
		try:
			with open(f, encoding='utf-8') as fh:
				texts.append(fh.read())
		except Exception:
			texts.append("")
	model = SentenceTransformer('all-MiniLM-L6-v2')
	embeddings = model.encode(texts, show_progress_bar=True)
	sim_matrix = cosine_similarity(embeddings)
	n = len(files)
	to_remove = set()
	duplicates = []
	for i in range(n):
		for j in range(i+1, n):
			if sim_matrix[i, j] > threshold:
				# Double-check with fuzzy string match
				fuzz_score = fuzz.ratio(texts[i], texts[j])
				if fuzz_score > 90:
					to_remove.add(j)
					duplicates.append((str(files[i]), str(files[j]), float(sim_matrix[i, j]), fuzz_score))
	unique_files = [f for idx, f in enumerate(files) if idx not in to_remove]
	return {'unique_files': unique_files, 'duplicates': duplicates, 'similarity_matrix': sim_matrix}

def write_selection_manifest(manifest_file: Path, all_files: List[Path], version_result: Dict, minhash_result: Dict):
	manifest = {
		'all_files': [str(f) for f in all_files],
		'version_unique_files': [str(f) for f in version_result['unique_files']],
		'minhash_unique_files': [str(f) for f in minhash_result['unique_files']],
		'duplicates': [str(f) for f in minhash_result['duplicates']]
	}
	with open(manifest_file, 'w') as f:
		json.dump(manifest, f, indent=2)
	print(f"   Selection manifest written: {manifest_file}")

def write_deduplication_report(report_file: Path, all_files: List[Path], version_result: Dict, minhash_result: Dict):
	report = {
		'total_files': len(all_files),
		'version_unique_files': len(version_result['unique_files']),
		'minhash_unique_files': len(minhash_result['unique_files']),
		'duplicates': len(minhash_result['duplicates'])
	}
	with open(report_file, 'w') as f:
		json.dump(report, f, indent=2)
	print(f"   Deduplication report written: {report_file}")

def print_manifest_summary(manifest: Dict):
	print("\nMANIFEST SUMMARY")
	print("-" * 70)
	print(f"   Total files: {len(manifest['all_files'])}")
	print(f"   Version-unique files: {len(manifest['version_unique_files'])}")
	print(f"   MinHash-unique files: {len(manifest['minhash_unique_files'])}")
	print(f"   Duplicates: {len(manifest['duplicates'])}")

def main():
	args = parse_args()
	input_dir = Path(args.input_dir)
	output_dir = Path(args.output_dir)
	artifacts_dir = Path(args.artifacts_dir)

	print("\nSTEP 1: Collecting files")
	print("-" * 70)
	all_files = collect_files(input_dir)

	print("\nSTEP 2: Version-based deduplication")
	print("-" * 70)
	version_result = version_based_deduplication(all_files)


	if args.enhanced:
		print("\nSTEP 3: Enhanced content similarity deduplication")
		print("-" * 70)
		minhash_result = minhash_deduplication(version_result['unique_files'], args.threshold)

		# Topic modeling / clustering
		print("\nSTEP 4: Topic modeling / clustering analysis")
		print("-" * 70)
		# Read all texts again for clustering
		texts = []
		for f in version_result['unique_files']:
			try:
				with open(f, encoding='utf-8') as fh:
					texts.append(fh.read())
			except Exception:
				texts.append("")
		tfidf = TfidfVectorizer(max_features=1000, stop_words='english')
		X = tfidf.fit_transform(texts)
		n_clusters = min(10, max(2, len(texts)//50))
		kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
		labels = kmeans.fit_predict(X)
		clusters = defaultdict(list)
		for idx, label in enumerate(labels):
			clusters[str(label)].append(str(version_result['unique_files'][idx]))
		# Save clusters to file
		with open(output_dir / 'topic_clusters.json', 'w', encoding='utf-8') as f:
			json.dump(clusters, f, indent=2)
		print(f"   Topic clusters written: {output_dir / 'topic_clusters.json'}")
		# Save duplicate pairs to file
		with open(output_dir / 'near_duplicates.json', 'w', encoding='utf-8') as f:
			json.dump(minhash_result['duplicates'], f, indent=2)
		print(f"   Near-duplicates written: {output_dir / 'near_duplicates.json'}")
	else:
		print("\nSTEP 3: MinHash deduplication")
		print("-" * 70)
		minhash_result = minhash_deduplication(version_result['unique_files'], args.threshold)

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
