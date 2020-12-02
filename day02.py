import common
import re


with open("input/day02.txt") as puzzle_input:
    passwords = [
        re.search(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", line).groups()
        for line in puzzle_input.readlines()
    ]


def part_1():
    return sum(
        1
        if int(password[0]) <= password[3].count(password[2]) <= int(password[1])
        else 0
        for password in passwords
    )


def part_2():
    return sum(
        1
        if (password[3][int(password[0]) - 1] == password[2])
        != (password[3][int(password[1]) - 1] == password[2])
        else 0
        for password in passwords
    )


if __name__ == "__main__":
    print(part_1())
    print(part_2())
