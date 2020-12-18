import itertools


with open("input/day11.txt") as puzzle_input:
    seats = [line.rstrip() for line in puzzle_input.readlines()]


def _count_occupied(state):
    return len([seat for row in state for seat in row if seat == "#"])


def _count_neighbours(pos, state, max_range):
    deltas = [-1, 0, 1]
    neighbours = [
        _first_in_dir(state, pos, delta, max_range)
        for delta in itertools.product(deltas, repeat=2)
        if any(delta)
    ]

    return len([n for n in neighbours if n == "#"])


def _new_seat_state(pos, state, max_range, threshold):
    n = _count_neighbours(pos, state, max_range)
    x, y = pos

    if state[y][x] == "L" and n == 0:
        return "#"
    elif state[y][x] == "#" and n >= threshold:
        return "L"
    else:
        return state[y][x]


def _new_state(state, max_range, threshold):
    return [
        [
            _new_seat_state((x, y), state, max_range, threshold)
            for x in range(len(seats[0]))
        ]
        for y in range(len(seats))
    ]


def _first_in_dir(state, pos, delta, max_range):
    x, y = pos
    dx, dy = delta

    for m in range(1, max_range + 1):
        try:
            seat = state[y + m * dy][x + m * dx]
            if seat != "." and y + m * dy >= 0 and x + m * dx >= 0:
                return seat
        except Exception:
            break

    return "."


def _run(state, max_range, threshold):
    new_state = _new_state(state, max_range, threshold)
    if (n := _count_occupied(new_state)) == _count_occupied(state):
        return n
    return _run(new_state, max_range, threshold)


def part_1(state=seats):
    return _run(state, 1, 4)


def part_2(state=seats):
    return _run(state, 50, 5)


if __name__ == "__main__":
    print(part_1())
    print(part_2())
