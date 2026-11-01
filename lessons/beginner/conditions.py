"""Use ordered branches to turn a score into a grade."""


def grade(score):
    """Accept an integer from 0 to 100, including both boundaries."""
    if type(score) is not int or not 0 <= score <= 100:
        raise ValueError("score must be an integer between 0 and 100")
    if score >= 80:
        return "A"
    if score >= 70:
        return "B"
    if score >= 60:
        return "C"
    if score >= 50:
        return "D"
    return "F"


if __name__ == "__main__":
    for result in [100, 80, 69, 50, 0]:
        print(f"{result}: {grade(result)}")
