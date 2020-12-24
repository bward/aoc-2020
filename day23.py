cups = [1, 5, 8, 9, 3, 7, 4, 6, 2]


def _move_cups(linked, cur):
    picked_up = [
        linked[cur][1],
        linked[linked[cur][1]][1],
        linked[linked[linked[cur][1]][1]][1],
    ]

    dest = ((cur - 2) % len(linked)) + 1
    while dest in picked_up:
        dest = ((dest - 2) % len(linked)) + 1

    start_removed = linked[picked_up[0]][0]
    end_removed = linked[picked_up[2]][1]
    start_insert = dest
    end_insert = linked[dest][1]

    linked[start_removed] = (linked[start_removed][0], end_removed)
    linked[end_removed] = (start_removed, linked[end_removed][1])

    linked[start_insert] = (linked[start_insert][0], picked_up[0])
    linked[picked_up[0]] = (start_insert, picked_up[1])

    linked[picked_up[2]] = (picked_up[1], end_insert)
    linked[end_insert] = (picked_up[2], linked[end_insert][1])

    return linked[cur][1]


def _build_linked_list(cups):
    return dict(
        (cups[i], (cups[i - 1], cups[(i + 1) % len(cups)])) for i in range(len(cups))
    )


def part_1():
    linked_cups = _build_linked_list(cups)
    cup = cups[0]
    for _ in range(100):
        cup = _move_cups(linked_cups, cup)

    ptr = 1
    out = ""
    for _ in range(8):
        ptr = linked_cups[ptr][1]
        out += str(ptr)

    return out


def part_2():
    linked_cups = _build_linked_list(cups + list(range(10, 1000001)))
    cup = cups[0]
    for _ in range(10000000):
        cup = _move_cups(linked_cups, cup)

    return linked_cups[1][1] * linked_cups[linked_cups[1][1]][1]


if __name__ == "__main__":
    print(part_1())
    print(part_2())
