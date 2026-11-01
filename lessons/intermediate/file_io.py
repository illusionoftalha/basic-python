"""Use pathlib, explicit encoding and a disposable directory for this demo."""

from pathlib import Path
from tempfile import TemporaryDirectory


def main():
    with TemporaryDirectory() as directory:
        path = Path(directory) / "days.txt"
        path.write_text("Monday\nTuesday\nWednesday\n", encoding="utf-8")
        days = path.read_text(encoding="utf-8").splitlines()
        print(f"Read {len(days)} days: {', '.join(days)}")
    # The temporary file is removed when the context manager exits.


if __name__ == "__main__":
    main()
