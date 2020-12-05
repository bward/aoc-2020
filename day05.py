import itertools


with open("input/day05.txt") as puzzle_input:
    raw = [line.rstrip() for line in puzzle_input.readlines()]
    passes = [(p[:7], p[7:]) for p in raw]


def _seat_id(boarding_pass):
    row, col = boarding_pass
    row_bin = int(row.replace("F", "0").replace("B", "1"), 2)
    col_bin = int(col.replace("L", "0").replace("R", "1"), 2)
    return 8 * row_bin + col_bin


def part_1():
    return max(_seat_id(p) for p in passes)


def part_2():
    all_ids = set(
        itertools.chain.from_iterable(
            [[8 * row + col for col in range(8)] for row in range(128)]
        )
    )

    booked_ids = set(_seat_id(p) for p in passes)

    for seat_id in all_ids:
        if (
            seat_id not in booked_ids
            and seat_id + 1 in booked_ids
            and seat_id - 1 in booked_ids
        ):
            return seat_id


if __name__ == "__main__":
    print(part_1())
    print(part_2())
