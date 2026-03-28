from pathlib import Path
import runpy


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    target = root / "week-3" / "scripts" / "rag_pipeline" / "03_run_two_stage_routing.py"
    runpy.run_path(str(target), run_name="__main__")


if __name__ == "__main__":
    main()
