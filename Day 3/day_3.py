import re


def add_muls(groups):
    total = 0
    do_state = True
    for group in groups:
        if group == "do()":
            do_state = True
            continue
        elif group == "don't()":
            do_state = False
            continue

        cleaned_group: str = group[4:-1]
        split_group = cleaned_group.split(",")
        if do_state:
            total += int(split_group[0]) * int(split_group[1])

    return total


def parse_input(file):

    find_groups = r"(mul\(\d{0,3},\d{0,3}\)|do\(\)|don't\(\))"

    with open(file) as f:
        content = f.read()
        groups = re.findall(find_groups, content)

    print(add_muls(groups))


def main():
    parse_input("Day 3/input")


if __name__ == "__main__":
    main()
