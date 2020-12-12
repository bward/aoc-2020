import re


with open("input/day12.txt") as puzzle_input:
    instructions = [
        (a, int(v))
        for a, v in [
            re.match("([A-Z])(\d+)", line).groups() for line in puzzle_input.readlines()
        ]
    ]

directions = {
    "N": lambda p, v, f: (p + v * (1 + 0), f),
    "E": lambda p, v, f: (p + v * (0 + 1j), f),
    "S": lambda p, v, f: (p + v * (-1 - 0j), f),
    "W": lambda p, v, f: (p + v * (0 - 1j), f),
    "L": lambda p, v, f: (p, f * ((0 - 1j) ** (v // 90))),
    "R": lambda p, v, f: (p, f * ((0 + 1j) ** (v // 90))),
    "F": lambda p, v, f: (p + v * f, f),
}


def part_1():
    position = 0
    facing = 0 + 1j

    for action, value in instructions:
        position, facing = directions[action](position, value, facing)

    return int(abs(position.real) + abs(position.imag))


def part_2():
    ship = 0
    facing = 0 + 1j
    waypoint = 1 + 10j

    for action, value in instructions:
        if action in ["N", "E", "S", "W"]:
            waypoint, _ = directions[action](waypoint, value, facing)
        elif action in ["L", "R"]:
            _, waypoint = directions[action](ship, value, waypoint)
        elif action == "F":
            ship += waypoint * value

    return int(abs(ship.real) + abs(ship.imag))


if __name__ == "__main__":
    print(part_1())
    print(part_2())
