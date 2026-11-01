"""Names refer to values; Python determines the type of each value."""


def main():
    name = "Talha"                 # str
    completed_lessons = 3           # int
    progress = 3 / 12               # float; / always performs true division
    is_learning = True             # bool
    print(f"{name} completed {completed_lessons} lessons.")
    print(f"Progress: {progress:.0%}; learning: {is_learning}")
    print(f"Next lesson: {completed_lessons + 1}")


if __name__ == "__main__":
    main()
