def number_of_lines(filename):
    """ Write your code here """
    with open(filename, "r") as f:
        lines = f.readlines()

    return len(lines)


def main():
    print(number_of_lines("test.txt"))  # prints 3
    print(number_of_lines("example.txt"))  # prints 9


if __name__ == "__main__":
    main()
