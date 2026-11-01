"""yield produces one item at a time instead of creating a whole list."""


def countdown(start):
    if type(start) is not int or start < 0:
        raise ValueError("start must be a nonnegative integer")
    while start > 0:
        yield start
        start -= 1


if __name__ == "__main__":
    print("Countdown:", list(countdown(3)))
    print("An exhausted generator has no more items:")
    counter = countdown(2)
    print(list(counter))
    print(list(counter))
