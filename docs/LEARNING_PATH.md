# Your Python learning path

Run commands from the repository root. Each lesson is independent and uses only
the Python standard library. Try changing a value, predict the output, then run it.

| Step | Lesson | Run | Try next |
|---|---|---|---|
| 1 | [Variables and formatting](../lessons/beginner/variables.py) | `python -m lessons.beginner.variables` | Change the name and lesson count. |
| 2 | [Conditions](../lessons/beginner/conditions.py) | `python -m lessons.beginner.conditions` | Test scores 49, 50, 79 and 80. |
| 3 | [Loops](../lessons/beginner/loops.py) | `python -m lessons.beginner.loops` | Print a different multiplication table. |
| 4 | [Collections](../lessons/beginner/collections.py) | `python -m lessons.beginner.collections` | Add a language and a duplicate score. |
| 5 | [Functions](../lessons/beginner/functions.py) | `python -m lessons.beginner.functions` | Explain why an empty list raises an error. |
| 6 | [Input and output](../lessons/beginner/input_output.py) | `python -m lessons.beginner.input_output --interactive` | Try a blank name. |
| 7 | [Comprehensions](../lessons/intermediate/comprehensions.py) | `python -m lessons.intermediate.comprehensions` | Keep odd numbers instead. |
| 8 | [Exceptions](../lessons/intermediate/exceptions.py) | `python -m lessons.intermediate.exceptions` | Try `0`, `-2` and `3.5`. |
| 9 | [Files](../lessons/intermediate/file_io.py) | `python -m lessons.intermediate.file_io` | Count the lines after reading the file. |
| 10 | [Classes](../lessons/intermediate/objects.py) | `python -m lessons.intermediate.objects` | Borrow the same book twice. |
| 11 | [Generators](../lessons/intermediate/generators.py) | `python -m lessons.intermediate.generators` | Explain the empty second iteration. |
| 12 | [Decorators](../lessons/intermediate/decorators.py) | `python -m lessons.intermediate.decorators` | Decorate a function with keyword arguments. |

## Checkpoints

- After step 4: explain how a list, tuple, set and dictionary differ.
- After step 6: write a small function that accepts input and returns a result.
- After step 9: read a file without depending on the terminal's working directory.
- After step 12: build the [expense tracker](../projects/README.md) and attempt the [exercises](../exercises/README.md).

## Example output

```text
$ python -m lessons.beginner.functions
Average: 80.0

$ python -m lessons.intermediate.generators
Countdown: [3, 2, 1]
An exhausted generator has no more items:
[2, 1]
[]
```

## Original notes

[Python for Beginners](../Python%20for%20Beginners/index.py) and
[Python Advanced](../Python%20Advanced/advanced.py) preserve the original learning
notes. Many snippets are commented out and those files are not the guided lesson
entry points. Some older subjects, such as MySQL, need additional setup and are
outside the dependency-free course. Start with the lessons above.
