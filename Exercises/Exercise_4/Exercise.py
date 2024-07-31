import collections
from functools import reduce


def load_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return reduce(lambda x, y: x + y, [l.strip() for l in lines])


def count_letters(filename):
    words = load_file(filename)
    print(f"The count of the letters for the file {filename} is:\n")
    for k, v in sorted(collections.Counter(words).items()):
        if k.isalpha():
            print(f"{k}: {v}")


if __name__ == "__main__":
    count_letters("test.txt")
