import re


def add_muls(groups):
    total = 0
    for group in groups:
        cleaned_group: str = group[4:-1]
        split_group = cleaned_group.split(",")
        total += int(split_group[0]) * int(split_group[1])

    return total


def parse_input(file):
    groups = []
    with open(file) as f:
        for line in f:
            mul = re.findall(r"mul\(\d+,\d+\)", line)
            groups = groups + mul
    print(add_muls(groups))


def main():
    parse_input("Day 3/input")


if __name__ == "__main__":
    main()
