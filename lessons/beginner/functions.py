"""Return a result so callers can reuse it instead of only printing it."""


def average(values):
    if not values:
        raise ValueError("at least one value is required")
    return sum(values) / len(values)


if __name__ == "__main__":
    scores = [70, 80, 90]
    print(f"Average: {average(scores):.1f}")
