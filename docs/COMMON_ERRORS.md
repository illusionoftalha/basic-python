# Common Python mistakes

## Nothing happens when I run a file

Lines beginning with `#` are comments. The original notes contain commented
snippets; the files under `lessons/` are executable examples.

## `python` is not found

Install Python and reopen your terminal. On Windows try `py --version` and replace
`python` with `py -3` in the commands. On macOS/Linux try `python3 --version`.

## `ModuleNotFoundError: No module named lessons`

Run the `python -m lessons...` commands from the repository root, the directory
containing `README.md` and `lessons/`.

## Input looks numeric but arithmetic fails

`input()` returns text. Convert it using `int()` or `float()` and catch
`ValueError` for input that cannot be converted. Do not use `eval()` on user input.

## A tuple changes when I edit it

`[1, 2]` is a list. `(1, 2)` is a tuple, and `(1,)` is a one-item tuple. Tuples
cannot have their items reassigned, though a mutable object inside a tuple can change.

## A string method seems to do nothing

Strings are immutable. `name.upper()` returns another string; use
`name = name.upper()` or `print(name.upper())` to use that result. This works in
VS Code and other terminals alike.

## I get a file-not-found error

A relative path starts at the process's current working directory, not
automatically at the script. The file lesson uses a temporary directory; for
project-owned resources use `Path(__file__).resolve().parent` as the base.

## My decimal total is surprising

Binary floating-point cannot represent every decimal fraction exactly. The
expense tracker accepts decimal strings and uses `Decimal` for cent amounts.
Avoid constructing its amounts from floats.
