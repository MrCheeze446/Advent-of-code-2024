def check_difference(nums):
    for previous, current in zip(nums, nums[1:]):
        if not (1 <= abs(int(previous) - int(current)) <= 3):
            return False

    return True


def all_dcreasing(nums):
    for previous, current in zip(nums, nums[1:]):
        if not (int(previous) > int(current)):
            return False
    return True


def all_increasing(nums):
    for previous, current in zip(nums, nums[1:]):
        if not (int(previous) < int(current)):
            return False
    return True


def parse_input(file):
    safe_vals = 0

    with open(file) as f:
        for line in f:
            nums = line.split()
            if (all_increasing(nums) or all_dcreasing(nums)) and check_difference(nums):
                safe_vals += 1
            else:  # let's be stupid for part 2 lol
                num_perms = [nums[:i] + nums[i + 1 :] for i in range(len(nums))]
                for perm in num_perms:
                    if (
                        all_increasing(perm) or all_dcreasing(perm)
                    ) and check_difference(perm):
                        safe_vals += 1
                        break

    return safe_vals


def main():
    print(parse_input("Day 2/input"))


if __name__ == "__main__":
    main()
