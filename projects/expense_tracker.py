"""A local expense ledger using argparse, JSON, pathlib and decimal arithmetic."""

import argparse
import json
import os
from decimal import Decimal, InvalidOperation
from pathlib import Path
from tempfile import NamedTemporaryFile


def parse_amount(text):
    try:
        value = Decimal(text)
        if not value.is_finite() or value <= 0:
            raise ValueError("amount must be positive and finite")
        rounded = value.quantize(Decimal("0.01"))
        if rounded != value:
            raise ValueError("amount cannot contain fractions of a cent")
        return rounded
    except InvalidOperation as error:
        raise ValueError("invalid amount") from error


def validate_entries(entries):
    if not isinstance(entries, list):
        raise ValueError("ledger must contain a JSON list")
    for entry in entries:
        if (not isinstance(entry, dict) or set(entry) != {"label", "amount"}
                or not isinstance(entry["label"], str) or not entry["label"].strip()
                or not isinstance(entry["amount"], str)):
            raise ValueError("each expense needs a nonblank label and a string amount")
        parse_amount(entry["amount"])
    return entries


def load_entries(path):
    if not path.exists():
        return []
    try:
        return validate_entries(json.loads(path.read_text(encoding="utf-8")))
    except json.JSONDecodeError as error:
        raise ValueError("ledger is not valid JSON; repair it before adding entries") from error


def save_entries(path, entries):
    validate_entries(entries)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        # Replace the ledger only after a complete JSON document has been written.
        with NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                prefix=".expenses-", delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(entries, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def total(entries):
    validate_entries(entries)
    return sum((parse_amount(entry["amount"]) for entry in entries), Decimal("0.00"))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path, default=Path("data/expenses.json"))
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="record an expense")
    add.add_argument("label")
    add.add_argument("amount", help="positive decimal amount, e.g. 12.50")
    commands.add_parser("list", help="show expenses")
    commands.add_parser("total", help="sum expenses")
    args = parser.parse_args(argv)
    try:
        entries = load_entries(args.file)
        if args.command == "add":
            entry = {"label": args.label.strip(), "amount": str(parse_amount(args.amount))}
            entries.append(entry)
            save_entries(args.file, entries)
            print(f"Added {entry['amount']}: {entry['label']}")
        elif args.command == "list":
            for entry in entries:
                print(f"{entry['amount']}: {entry['label']}")
            if not entries:
                print("No expenses yet.")
        else:
            print(f"Total: {total(entries):.2f}")
    except (OSError, ValueError) as error:
        parser.exit(2, f"Error: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
