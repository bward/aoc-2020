from collections import defaultdict

puzzle_input = [9, 6, 0, 10, 18, 2, 1]


def part_1():
    output = []
    for i in range(2020):
        if i < len(puzzle_input):
            output.append(puzzle_input[i])
        else:
            last = output[-1]
            if output.count(last) == 1:
                output.append(0)
            else:
                last_but_one_index = output[-2::-1].index(last)
                output.append(last_but_one_index + 1)
    return output[-1]


def _update(seen, i, value):
    x1, x2 = seen[value]
    if x1 is None:
        seen[value] = (i, None)
    elif x2 is None:
        seen[value] = (x1, i)
    else:
        seen[value] = (x2, i)


def part_2():
    seen = defaultdict(lambda: (None, None))
    last = puzzle_input[-1]

    for i, value in enumerate(puzzle_input):
        seen[value] = (i, None)

    for i in range(len(seen), 30000000):
        t1, t2 = seen[last]

        if t2 is None:
            _update(seen, i, 0)
            last = 0

        else:
            new = t2 - t1
            _update(seen, i, new)
            last = new

    return last


if __name__ == "__main__":
    print(part_1())
    print(part_2())
