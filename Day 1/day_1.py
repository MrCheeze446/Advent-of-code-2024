left_side = []
right_side = []


def parse_input(file):
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            split_line = line.split()
            left_side.append(int(split_line[0]))
            right_side.append(int(split_line[1]))
            left_side.sort()
            right_side.sort()


def get_distances():
    total_distance = 0
    for pair in zip(left_side, right_side):
        distance = abs(pair[0] - pair[1])
        total_distance += distance

    print(f"distance: {total_distance}")


def get_simularities():
    total_sim = 0
    for num in left_side:
        total_sim += num * right_side.count(num)

    print(f"simularity: {total_sim}")


def main():
    parse_input("Day 1/input")
    get_distances()
    get_simularities()


if __name__ == "__main__":
    main()
