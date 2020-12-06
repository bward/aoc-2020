from collections import Counter


with open("input/day06.txt") as puzzle_input:
    raw_groups = puzzle_input.read().rstrip().split("\n\n")
    groups = [g.split("\n") for g in raw_groups]


def _build_counters():
    counters = []
    for g in groups:
        c = Counter()
        for answer in g:
            c.update(answer)
        counters.append(c)
    return counters


counters = _build_counters()


def part_1():
    return sum(len(c) for c in counters)


def part_2():
    return sum(len([k for k in c if c[k] == len(g)]) for c, g in zip(counters, groups))


if __name__ == "__main__":
    print(part_1())
    print(part_2())
