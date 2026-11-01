import json
from decimal import Decimal
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from projects.expense_tracker import load_entries, parse_amount, save_entries, total

ROOT = Path(__file__).resolve().parents[1]


class ExpenseTests(unittest.TestCase):
    def test_amounts_use_decimal_arithmetic(self):
        self.assertEqual(parse_amount("12.5"), Decimal("12.50"))
        self.assertEqual(total([{"label": "A", "amount": "0.10"},
                                {"label": "B", "amount": "0.20"}]), Decimal("0.30"))
        self.assertEqual(total([]), Decimal("0.00"))

    def test_invalid_amounts_are_rejected(self):
        for text in ["-1", "0", "0.001", "abc", "NaN", "Infinity", "1e999"]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                parse_amount(text)

    def test_round_trip_and_missing_ledger(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "nested" / "ledger.json"
            self.assertEqual(load_entries(path), [])
            entries = [{"label": "Café", "amount": "3.50"}]
            save_entries(path, entries)
            self.assertEqual(load_entries(path), entries)
            self.assertEqual(list(path.parent.glob(".expenses-*")), [])

    def test_bad_data_cannot_overwrite_an_existing_ledger(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.json"
            save_entries(path, [{"label": "Lunch", "amount": "5.00"}])
            before = path.read_bytes()
            with self.assertRaises(ValueError):
                save_entries(path, [{"label": " ", "amount": "5.00"}])
            self.assertEqual(path.read_bytes(), before)

    def test_malformed_and_wrong_shape_json(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.json"
            for contents in ["not json", "{}", '[{"label":"x","amount":2}]']:
                path.write_text(contents, encoding="utf-8")
                with self.subTest(contents=contents), self.assertRaises(ValueError):
                    load_entries(path)

    def test_failed_replacement_preserves_the_old_ledger_and_cleans_temporary_file(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.json"
            save_entries(path, [{"label": "Lunch", "amount": "5.00"}])
            before = path.read_bytes()
            with patch("projects.expense_tracker.os.replace", side_effect=OSError("disk error")):
                with self.assertRaises(OSError):
                    save_entries(path, [{"label": "Tea", "amount": "1.00"}])
            self.assertEqual(path.read_bytes(), before)
            self.assertEqual(list(path.parent.glob(".expenses-*")), [])

    def test_cli_persists_and_reports_invalid_input_without_a_traceback(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.json"
            base = [sys.executable, "-m", "projects.expense_tracker", "--file", str(path)]
            result = subprocess.run(base + ["add", "Tea", "1.25"], cwd=ROOT,
                                    capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            result = subprocess.run(base + ["total"], cwd=ROOT, capture_output=True,
                                    text=True, timeout=10)
            self.assertEqual(result.stdout.strip(), "Total: 1.25")
            result = subprocess.run(base + ["add", "Tea", "NaN"], cwd=ROOT,
                                    capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 2)
            self.assertNotIn("Traceback", result.stderr)
            self.assertEqual(len(json.loads(path.read_text(encoding="utf-8"))), 1)
