# Practice lab

Try each exercise before opening the linked reference lesson. Add tests for at
least one boundary case. Keep your own answers in a separate branch or folder.

| Level | Challenge | Acceptance examples | Reference |
|---|---|---|---|
| Beginner | Temperature converter | `0 C -> 32 F`, `100 C -> 212 F`, `-40 C -> -40 F` | [Variables](../lessons/beginner/variables.py) |
| Beginner | FizzBuzz | For 1–15, replace multiples of 3 with Fizz, 5 with Buzz, both with FizzBuzz. | [Loops](../lessons/beginner/loops.py) |
| Beginner | Word counter | Ignore case; `Python python Java` gives Python: 2 and Java: 1. Define how punctuation is handled. | [Collections](../lessons/beginner/collections.py) |
| Beginner | Safe average | Compute the average of a nonempty list; reject an empty list. | [Functions](../lessons/beginner/functions.py) |
| Intermediate | Library shelf | Borrow, return and search books; reject a second borrow. | [Objects](../lessons/intermediate/objects.py) |
| Intermediate | Even-number generator | Yield even values below a limit without constructing a list. | [Generators](../lessons/intermediate/generators.py) |
| Intermediate | Expense categories | Add a category field and report category totals without changing the overall total. Decide how old ledger files migrate. | [Project](../projects/expense_tracker.py) |

## Review your solution

1. Can somebody understand the names without reading every line?
2. What happens with empty input and an invalid value?
3. Are the expected outputs written down?
4. Can your tests run without the network, credentials or personal files?
5. Does `python scripts/check.py` still pass?
