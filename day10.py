from functools import lru_cache

with open("input/day10.txt") as puzzle_input:
    joltages = sorted([int(line) for line in puzzle_input.readlines()])
    end = max(joltages) + 3


def part_1():
    ones = 0
    threes = 0
    cur = 0

    for j in joltages:
        if j - cur == 1:
            ones += 1
        elif j - cur == 3:
            threes += 1
        cur = j

    return ones * (threes + 1)


@lru_cache
def part_2(pos=0):
    if pos + 3 == end:
        return 1
    else:
        return sum(part_2(j) for j in joltages if pos < j <= pos + 3)


if __name__ == "__main__":
    print(part_1())
    print(part_2())
