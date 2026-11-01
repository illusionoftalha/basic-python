"""Transform and filter a sequence without changing the original."""


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    even_squares = [number ** 2 for number in numbers if number % 2 == 0]
    lengths = {word: len(word) for word in ["Python", "Java", "C"]}
    print("Even squares:", even_squares)
    print("Word lengths:", lengths)
