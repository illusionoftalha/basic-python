# Learn Python by running it

[![Python checks](https://github.com/illusionoftalha/basic-python/actions/workflows/check.yml/badge.svg)](https://github.com/illusionoftalha/basic-python/actions/workflows/check.yml)

**12 focused lessons · a practical CLI project · exercises · standard library only**

Start with a short working example, change it, then use the same idea in a small
project. This course is for beginners and learners moving from another language.
You need **Python 3.10+**, a terminal and a text editor. No pip install is needed.

## Quick start

```sh
git clone https://github.com/illusionoftalha/basic-python.git
cd basic-python
python -m lessons.beginner.variables
python -m lessons.beginner.functions
python scripts/check.py
```

On Windows, `py -3` can replace `python`. On macOS/Linux your command may be
`python3`. Always run the module commands from the repository root.

The functions example prints:

```text
Average: 80.0
```

## Pick your next step

| You want to… | Start here |
|---|---|
| Learn from the beginning | [The ordered learning path](docs/LEARNING_PATH.md) |
| Understand a common error | [Troubleshooting](docs/COMMON_ERRORS.md) |
| Practice without copying a solution | [Exercise lab](exercises/README.md) |
| Build something useful | [Expense tracker walkthrough](projects/README.md) |
| Improve an example | [Contribution guide](CONTRIBUTING.md) |

## What you will learn

| Foundations | Next steps |
|---|---|
| Variables, numbers and formatting | Comprehensions |
| Conditions and grade boundaries | Exceptions and input validation |
| For/while loops | UTF-8 text files and context managers |
| Lists, tuples, sets and dictionaries | Classes and object state |
| Functions and return values | Generators and lazy iteration |
| Terminal input and output | Decorators and callable metadata |

Every lesson has a runnable command and a practice task in the learning path.
Examples do not make network requests. The file demo cleans up its temporary
files; interactive input is opt-in with `--interactive`.

## Mini-project: expense tracker

```sh
python -m projects.expense_tracker add "Lunch" 12.50
python -m projects.expense_tracker add "Bus" 2.00
python -m projects.expense_tracker total
```

A new ledger prints `Total: 14.50`. Data goes into the Git-ignored
`data/expenses.json`; repeating the commands adds more entries. The project uses
decimal arithmetic, validates saved data and reports invalid input clearly.
Read the [walkthrough](projects/README.md) before extending it.

## Repository map

```text
lessons/beginner/       Six runnable foundation lessons
lessons/intermediate/   Six lessons building on the foundations
projects/              Expense-tracker CLI and walkthrough
exercises/             Challenges with acceptance examples
tests/                 Standard-library unittest checks
scripts/check.py       Syntax, tests and all lesson demos
docs/                  Learning path and troubleshooting
Python for Beginners/  Original reference notes
Python Advanced/       Original reference notes and optional-integration sketches
```

## Check your work

```sh
python scripts/check.py
# Or run only the unit tests:
python -m unittest discover -s tests -v
```

Tests cover grade boundaries, empty input, generator exhaustion, object state,
decorator behavior, decimal amounts, invalid ledgers and CLI persistence. CI runs
the check on Python 3.10, 3.12 and 3.13 on Ubuntu and Windows.

The original folders preserve earlier notes; many snippets are commented out.
They are not the guided course entry points. Optional MySQL sketches are outside
the dependency-free course.

## License

© 2026 Sheikh Muhammad Talha Bin Khalid. All Rights Reserved.
