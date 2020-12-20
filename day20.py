import itertools
import math
import re

with open("input/day20.txt") as puzzle_input:
    raw_tiles = puzzle_input.read().split("\n\n")
    tiles = {}

    for t in raw_tiles:
        r = re.compile(r"Tile (\d+):\n([#.\n]+)$", re.MULTILINE)
        groups = re.match(r, t).groups()
        tiles[int(groups[0])] = groups[1].rstrip().split("\n")


def _get_edges(tile):
    return [
        tile[0],
        "".join(t[-1] for t in tile),
        tile[-1],
        "".join(t[0] for t in tile),
    ]


def _get_all_other_edges(tile):
    return set(
        itertools.chain.from_iterable(_get_edges(tiles[t]) for t in tiles if t != tile)
    )


def _identify_corners():
    corner_tiles = []

    for tile in tiles:
        edges = _get_edges(tiles[tile])
        all_other_edges = _get_all_other_edges(tile)
        non_matched = len(
            [
                e
                for e in edges
                if e not in all_other_edges and e[::-1] not in all_other_edges
            ]
        )

        if non_matched == 2:
            corner_tiles.append(tile)

    return corner_tiles


def part_1():
    return math.prod(_identify_corners())


monster = [
    (0, 0),
    (1, 1),
    (4, 1),
    (5, 0),
    (6, 0),
    (7, 1),
    (10, 1),
    (11, 0),
    (12, 0),
    (13, 1),
    (16, 1),
    (17, 0),
    (18, -1),
    (18, 0),
    (19, 0),
]


def _monster_at_location(puzzle, x, y):
    try:
        return all(puzzle[y + dy][x + dx] == "#" for dx, dy in monster)
    except IndexError:
        return False


def _count_monsters(puzzle):
    return len(
        [
            (x, y)
            for y in range(len(puzzle))
            for x in range(len(puzzle[0]))
            if _monster_at_location(puzzle, x, y)
        ]
    )


def _rotate(tile):
    return ["".join(r) for r in zip(*tile)][::-1]


def _reflect(tile):
    return tile[::-1]


def _all_states(tile):
    states = [tile, _reflect(tile)]

    for _ in range(3):
        states.extend([_rotate(s) for s in states[-2:]])

    return states


def _find_tile(grid, used, x, y):
    edge_above = _get_edges(grid[y - 1][x])[2] if y > 0 else None
    edge_before = _get_edges(grid[y][x - 1])[1] if x > 0 else None

    for tile in tiles:
        if tile in used:
            continue
        states = _all_states(tiles[tile])
        above_matches = [
            s for s in states if not edge_above or _get_edges(s)[0] == edge_above
        ]
        both_matches = [
            s
            for s in above_matches
            if not edge_before or _get_edges(s)[3] == edge_before
        ]

        if len(both_matches) == 1:
            used.add(tile)
            return both_matches[0]


def part_2():
    solved = [[None for _ in range(12)] for _ in range(12)]
    corner_tiles = _identify_corners()
    used = set()

    # Place the first corner with non-matched edges facing outwards
    first_corner = tiles[corner_tiles[0]]
    used.add(corner_tiles[0])
    lone_edges = [
        e
        for e in _get_edges(first_corner)
        if e not in _get_all_other_edges(corner_tiles[0])
        and e[::-1] not in _get_all_other_edges(corner_tiles[0])
    ]
    first_corner_states = _all_states(first_corner)

    solved[0][0] = next(
        s
        for s in first_corner_states
        if (_get_edges(s)[0] in lone_edges or _get_edges(s)[0][::-1] in lone_edges)
        and (_get_edges(s)[3] in lone_edges or _get_edges(s)[3][::-1] in lone_edges)
    )

    # Complete the puzzle piece by piece, adding the first tile we find that fits in each spot
    # Luckily this works!
    for y in range(12):
        for x in range(12):
            if (x, y) == (0, 0):
                continue
            solved[y][x] = _find_tile(solved, used, x, y)

    image = ["".join(x[i + 1][1:-1] for x in row) for row in solved for i in range(8)]

    total = sum(row.count("#") for row in image)
    monsters = max(_count_monsters(state) for state in _all_states(image))

    return total - monsters * len(monster)


if __name__ == "__main__":
    print(part_1())
    print(part_2())
