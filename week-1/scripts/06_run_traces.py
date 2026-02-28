import time
import importlib.util
from pathlib import Path


# --------------------------------------------------
# Load pipeline factory dynamically
# --------------------------------------------------
def _load_create_complete_rag_pipeline():
    script_dir = Path(__file__).resolve().parent
    module_path = script_dir / "04_test_rag_system.py"

    spec = importlib.util.spec_from_file_location("test_rag_system", module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from: {module_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    factory = getattr(module, "create_complete_rag_pipeline", None)
    if not callable(factory):
        raise ImportError(
            "Function create_complete_rag_pipeline not found in 04_test_rag_system.py"
        )
    return factory


create_complete_rag_pipeline = _load_create_complete_rag_pipeline()


# --------------------------------------------------
# Complex / Higher-Level Queries
# --------------------------------------------------
TEST_QUERIES = [
    "Explain how Bayesian updating works in a multi-stage experiment.",
    "Compare the Central Limit Theorem and the Law of Large Numbers with formal guarantees.",
    "Explain the mathematical definition of conditional independence.",
    "Derive the expectation formula for a continuous random variable from its probability density function.",
    "Under what modeling assumptions can Bayesian updating produce misleading results?"
]


# --------------------------------------------------
# Main Trace Runner
# --------------------------------------------------
def run_traces():
    print("🚀 Creating RAG pipeline...")
    pipeline = create_complete_rag_pipeline()

    output_dir = Path("week-1/traces")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "trace.md"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Week 1 Trace Report\n\n")

        for i, query in enumerate(TEST_QUERIES, 1):
            print(f"\nRunning Query {i}: {query}")

            start_time = time.time()

            result = pipeline.run(
                {
                    "text_embedder": {"text": query},
                    "prompt_builder": {"question": query}
                },
                include_outputs_from={"retriever", "llm"}
            )

            latency = round(time.time() - start_time, 2)

            retrieved_docs = result["retriever"]["documents"]
            replies = result["llm"]["replies"]

            full_answer = replies[0].text if replies else "No answer generated."

            # --------------------------------------------------
            # Write to markdown
            # --------------------------------------------------
            f.write(f"## Query {i}: {query}\n\n")
            f.write(f"**Question:** {query}\n\n")

            f.write("**Retrieved Chunks:**\n")

            if not retrieved_docs:
                f.write("No chunks retrieved.\n")
            else:
                for j, doc in enumerate(retrieved_docs, 1):
                    source = Path(doc.meta.get("file_path", "Unknown")).name
                    score = getattr(doc, "score", 0.0)
                    preview = doc.content[:80].replace("\n", " ")
                    f.write(
                        f"{j}. {source} (score: {score:.4f}) - {preview}\n"
                    )

            f.write("\n**Generated Answer:**\n")
            f.write(full_answer + "\n\n")

            f.write("**Assessment:**\n")
            f.write("- Retrieval quality: \n")
            f.write("- Answer quality: \n")
            f.write("- Was the right context retrieved? \n")
            f.write("- If not, what was missing?\n\n")
            f.write("---\n\n")

            print(f"✅ Completed (Latency: {latency}s)")

    print("\n🎉 Trace generation complete!")
    print(f"📄 Saved to: {output_file}")


if __name__ == "__main__":
    run_traces()
