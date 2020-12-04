import math


with open("input/day03.txt") as puzzle_input:
    lines = [l.rstrip() for l in puzzle_input.readlines()]
    trees = {}
    width = len(lines[0])
    for y in range(len(lines)):
        for x in range(width):
            trees[(x, y)] = lines[y][x]


def _get_tree(x, y):
    return trees[(x % width, y)]


def _count_gradient(dx, dy):
    count = 0
    x, y = (0, 0)
    while True:
        try:
            if _get_tree(x, y) == "#":
                count += 1
            x += dx
            y += dy

        except KeyError:
            break

    return count


def part_1():
    return _count_gradient(3, 1)


def part_2():
    return math.prod(
        [
            _count_gradient(1, 1),
            _count_gradient(3, 1),
            _count_gradient(5, 1),
            _count_gradient(7, 1),
            _count_gradient(1, 2),
        ]
    )


if __name__ == "__main__":
    print(part_1())
    print(part_2())
