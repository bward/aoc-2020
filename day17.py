import itertools
from collections import defaultdict


def _parse_input(n):
    cubes = defaultdict(lambda: ".")
    with open("input/day17.txt") as puzzle_input:
        for y, row in enumerate(puzzle_input.readlines()):
            for x, val in enumerate(row.rstrip()):
                cubes[tuple([x, y] + [0] * (n - 2))] = val
    return cubes


def _neighbours(coord):
    return [
        tuple(map(sum, zip(coord, delta)))
        for delta in itertools.product([-1, 0, 1], repeat=len(coord))
        if any(delta)
    ]


def _grow_cubes(my_cubes):
    new_cubes = defaultdict(lambda: ".")

    [my_cubes[n] for c in list(my_cubes.keys()) for n in _neighbours(c)]

    for coord, val in list(my_cubes.items()):
        active_neighbours = len([n for n in _neighbours(coord) if my_cubes[n] == "#"])
        if val == "#" and active_neighbours in [2, 3]:
            new_cubes[coord] = "#"
        elif val == "#":
            new_cubes[coord] = "."
        elif val == "." and active_neighbours == 3:
            new_cubes[coord] = "#"
        else:
            new_cubes[coord] = "."

    return defaultdict(lambda: ".", {k: v for k, v in new_cubes.items() if v == "#"})


def _run(n):
    cubes = _parse_input(n)
    for _ in range(6):
        cubes = _grow_cubes(cubes)

    return len([c for c in cubes.values() if c == "#"])


def part_1():
    return _run(3)


def part_2():
    return _run(4)


if __name__ == "__main__":
    print(part_1())
    print(part_2())
