import re
import math


with open("input/day16.txt") as puzzle_input:
    rules = {}
    for _ in range(20):
        groups = re.match(
            r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", puzzle_input.readline()
        ).groups()
        rules[groups[0]] = (
            (int(groups[1]), int(groups[2])),
            (int(groups[3]), int(groups[4])),
        )

    puzzle_input.readline()
    puzzle_input.readline()

    ticket = [int(f) for f in puzzle_input.readline().rstrip().split(",")]

    puzzle_input.readline()
    puzzle_input.readline()

    nearby_tickets = [
        [int(f) for f in line.rstrip().split(",")] for line in puzzle_input.readlines()
    ]


def _check_field(field, rule):
    (a, b), (c, d) = rule
    return a <= field <= b or c <= field <= d


def _field_always_invalid(field):
    return not any(_check_field(field, rule) for rule in rules.values())


def part_1():
    all_fields = [f for t in nearby_tickets for f in t]
    return sum(f for f in all_fields if _field_always_invalid(f))


def part_2():
    valid_tickets = [
        t for t in nearby_tickets if not any(_field_always_invalid(f) for f in t)
    ]

    possibilities = [
        [
            name
            for name, rule in rules.items()
            if all(_check_field(t[i], rule) for t in valid_tickets)
        ]
        for i in range(len(ticket))
    ]

    field_types = [None] * len(ticket)

    while True:
        for i, field_possibilities in enumerate(possibilities):
            remaining = [f for f in field_possibilities if f not in field_types]
            if len(remaining) == 1:
                field_types[i] = remaining[0]
        if None not in field_types:
            break

    return math.prod(
        f for i, f in enumerate(ticket) if field_types[i].startswith("departure")
    )


if __name__ == "__main__":
    print(part_1())
    print(part_2())
