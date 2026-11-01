"""Catch the error you expect; do not hide unrelated programming errors."""


def positive_integer(text):
    value = int(text)
    if value <= 0:
        raise ValueError("value must be positive")
    return value


if __name__ == "__main__":
    for text in ["3", "zero", "-2"]:
        try:
            print(f"Accepted: {positive_integer(text)}")
        except ValueError as error:
            print(f"Cannot use {text!r}: {error}")
