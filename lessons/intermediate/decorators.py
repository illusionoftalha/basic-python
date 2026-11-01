"""A decorator wraps a callable; wraps preserves its name and documentation."""

from functools import wraps


def announce(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")
        return function(*args, **kwargs)
    return wrapper


@announce
def add(left, right):
    """Add two numbers and return the result."""
    return left + right


if __name__ == "__main__":
    print("Result:", add(2, right=3))
