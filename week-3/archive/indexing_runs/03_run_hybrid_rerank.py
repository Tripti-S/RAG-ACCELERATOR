from pathlib import Path
import runpy


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    target = root / "week3_retrieval" / "experiments" / "01b_generate_hybrid_results.py"
    runpy.run_path(str(target), run_name="__main__")


if __name__ == "__main__":
    main()
