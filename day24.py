import re
from collections import defaultdict

neighbours = {
    "ne": (0, 1),
    "nw": (-1, 1),
    "w": (-1, 0),
    "sw": (0, -1),
    "se": (1, -1),
    "e": (1, 0),
}

with open("input/day24.txt") as puzzle_input:
    all_directions = [re.findall("|".join(neighbours), line) for line in puzzle_input]


def part_1():
    flipped = defaultdict(bool)
    for directions in all_directions:
        x, y = 0, 0
        for direction in directions:
            dx, dy = neighbours[direction]
            x += dx
            y += dy
        flipped[(x, y)] = not flipped[(x, y)]

    return flipped


def _get_neighbours(x, y):
    return [(x + dx, y + dy) for dx, dy in neighbours.values()]


def part_2(state):
    for _ in range(100):
        new_state = defaultdict(bool)
        [state[n] for (x, y) in list(state.keys()) for n in _get_neighbours(x, y)]

        for (x, y), is_black in list(state.items()):
            black_neighbours = len([n for n in _get_neighbours(x, y) if state[n]])

            if is_black and (black_neighbours == 0 or black_neighbours > 2):
                new_state[(x, y)] = False
            elif not is_black and black_neighbours == 2:
                new_state[(x, y)] = True
            else:
                new_state[(x, y)] = is_black

        state = new_state

    return len([v for v in state.values() if v])


if __name__ == "__main__":
    p1 = part_1()
    print(len([v for v in p1.values() if v]))
    print(part_2(p1))
