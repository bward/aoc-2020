import common
import itertools


with open("input/day01.txt") as puzzle_input:
    nums = [int(line.rstrip()) for line in puzzle_input.readlines()]


def part_1():
    for x, y in itertools.combinations(nums, 2):
        if x + y == 2020:
            return x * y


def part_2():
    for x, y, z in itertools.combinations(nums, 3):
        if x + y + z == 2020:
            return x * y * z


if __name__ == "__main__":
    print(part_1())
    print(part_2())
