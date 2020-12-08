def _parse_bag(bag):
    words = bag.split(" ")
    colour = " ".join(words[:2])

    contents = []
    remainder = words[4:]

    for i in range(len(remainder) // 4):
        contents.append(
            (int(remainder[4 * i]), " ".join(remainder[4 * i + 1 : 4 * i + 3]))
        )

    return colour, contents


with open("input/day07.txt") as puzzle_input:
    bag_list = [_parse_bag(line.rstrip()) for line in puzzle_input.readlines()]
    bags = dict(bag_list)


def _can_contain(bag, colour):
    return any(b[1] == colour for b in bag)


def part_1():
    colours = set(["shiny gold"])

    while True:
        old = len(colours)
        for bag in bags:
            for colour in colours:
                if _can_contain(bags[bag], colour):
                    colours.add(bag)
                    break
        if len(colours) == old:
            break
    return len(colours)


def _size(bag):
    if len(bags[bag]) == 0:
        return 1

    return 1 + sum(n * _size(c) for n, c in bags[bag])


def part_2():
    return _size("shiny gold") - 1


if __name__ == "__main__":
    print(part_1())
    print(part_2())
