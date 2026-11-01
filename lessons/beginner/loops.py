"""range stops before its endpoint; a while loop needs a changing condition."""


def main():
    for number in range(1, 6):
        print(f"3 x {number} = {3 * number}")
    remaining = 3
    while remaining > 0:
        print(f"Countdown: {remaining}")
        remaining -= 1


if __name__ == "__main__":
    main()
