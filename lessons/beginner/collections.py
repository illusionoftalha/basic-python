"""A list is mutable, a tuple is immutable, a set holds unique values."""


def main():
    languages = ["Python", "Java"]
    languages.append("C")
    location = ("Karachi", "Pakistan")  # Parentheses create a tuple here.
    unique_scores = {80, 90, 80}
    learner = {"name": "Talha", "lessons": len(languages)}
    print("Languages:", ", ".join(languages))
    print("Location:", location[0])
    # Sort a set before printing when you want predictable output.
    print("Unique scores:", sorted(unique_scores))
    print(f"{learner['name']} explored {learner['lessons']} languages.")


if __name__ == "__main__":
    main()
