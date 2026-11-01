# Project: local expense tracker

Combine functions, validation, exceptions, JSON, files and a command-line interface.
No database, account, external package or network access is needed.

From the repository root:

```sh
python -m projects.expense_tracker add "Lunch" 12.50
python -m projects.expense_tracker add "Bus" 2.00
python -m projects.expense_tracker list
python -m projects.expense_tracker total
```

For a new ledger, the final command prints `Total: 14.50`. The examples write to
`data/expenses.json`, which is ignored by Git. Repeating them adds more entries.
To use another ledger, put the global option before the subcommand:

```sh
python -m projects.expense_tracker --file data/practice.json add "Tea" 1.25
python -m projects.expense_tracker --file data/practice.json total
```

Amounts must be positive, finite decimal values representable in whole cents.
Negative values, `NaN`, and `0.001` are rejected. The tracker uses decimal strings
instead of floating-point amounts. Invalid existing JSON is reported rather than
silently replaced; writes replace the ledger only after a complete new document
is written. This is a single-user exercise, without concurrent-writer locking.

## Read the implementation in this order

1. `parse_amount`: validate a value and convert it to `Decimal`.
2. `validate_entries` and `load_entries`: protect the shape of stored data.
3. `save_entries`: write a complete document before replacement.
4. `total`: combine values using decimal arithmetic.
5. `main`: parse commands and report useful errors.

## Extend it

- Add categories and test that their totals add up to the overall total.
- Add a date and filtering; decide how to read older ledger files.
- Add CSV export using the standard library.
- Implement a budget warning without changing the saved expenses.
