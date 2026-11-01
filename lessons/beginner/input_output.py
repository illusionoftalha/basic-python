"""input returns a string. Interactive input is opt-in for this example."""

import argparse


def greeting(name):
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name cannot be blank")
    return f"Hello, {cleaned}!"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--interactive", action="store_true")
    args = parser.parse_args()
    name = input("Your name: ") if args.interactive else "learner"
    try:
        print(greeting(name))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
