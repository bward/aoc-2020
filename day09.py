with open("input/day09.txt") as puzzle_input:
    nums = [int(line) for line in puzzle_input.readlines()]


def part_1():
    for i, num in enumerate(nums[25:]):
        previous = set(nums[i : i + 25])
        if all(num - p not in previous for p in previous):
            return num


def part_2(target=part_1()):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            subarray = nums[i:j]
            if sum(subarray) == target:
                return min(subarray) + max(subarray)


if __name__ == "__main__":
    print(part_1())
    print(part_2())
