"""Check syntax, run unit tests and execute every non-interactive lesson."""

import ast
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
LESSONS = [
    "beginner.variables", "beginner.conditions", "beginner.loops",
    "beginner.collections", "beginner.functions", "beginner.input_output",
    "intermediate.comprehensions", "intermediate.exceptions", "intermediate.file_io",
    "intermediate.objects", "intermediate.generators", "intermediate.decorators",
]


def main():
    sources = []
    for folder in ["lessons", "projects", "tests", "scripts", "Python for Beginners", "Python Advanced"]:
        sources.extend((ROOT / folder).rglob("*.py"))
    for path in sources:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    print(f"Syntax checked {len(sources)} Python files", flush=True)
    subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
                   cwd=ROOT, check=True, timeout=60)
    for lesson in LESSONS:
        print(f"\n--- {lesson} ---", flush=True)
        subprocess.run([sys.executable, "-m", f"lessons.{lesson}"], cwd=ROOT,
                       check=True, timeout=10)
    print(f"\nAll tests and {len(LESSONS)} lesson demos passed.")


if __name__ == "__main__":
    main()
