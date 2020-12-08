import common
import re


with open("input/day02.txt") as puzzle_input:
    passwords = [
        re.search(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", line).groups()
        for line in puzzle_input.readlines()
    ]


def part_1():
    return len([p for p in passwords if int(p[0]) <= p[3].count(p[2]) <= int(p[1])])


def part_2():
    return len(
        [
            p
            for p in passwords
            if (p[3][int(p[0]) - 1] == p[2]) != (p[3][int(p[1]) - 1] == p[2])
        ]
    )


if __name__ == "__main__":
    print(part_1())
    print(part_2())
