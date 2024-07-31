import random


def coin_tosses(n):
    return [random.randint(0, 1) for x in range(n)]


def count(tosses):
    count_one = sum(tosses)
    return (count_one, len(tosses) - count_one)


def percentage(count_of_tosses):
    (h, t) = count_of_tosses
    return (round(100 * h / (h + t), 2), round(100 * t / (h + t), 2))


def main():
    x = input("How many coin tosses would you like to simulate?\n")
    tosses = coin_tosses(int(x))
    count_tosses = count(tosses)
    percentage_tosses = percentage(count_tosses)

    (h, t) = count_tosses
    print(f"\nNo. of Heads: {h}")
    print(f"No. of Tails: {t}")

    (ph, pt) = percentage_tosses
    print(f"\n%   of Heads: {ph}")
    print(f"%   of Tails: {pt}")


if __name__ == "__main__":
    main()
