import common


with open("input/day13.txt") as puzzle_input:
    timestamp = int(puzzle_input.readline())
    buses = puzzle_input.readline().rstrip().split(",")


def part_1():
    in_service = [int(bus) for bus in buses if bus != "x"]
    wait_times = dict([(bus, bus - (timestamp % bus)) for bus in in_service])
    best_bus = min(wait_times, key=wait_times.get)

    return best_bus * wait_times[best_bus]


def part_2():
    departures = dict([(bus, t) for t, bus in enumerate(buses) if bus != "x"])
    remainders = [str(-v) for v in departures.values()]
    moduli = [m for m in departures.keys()]

    return f"ChineseRemainder[{{{','.join(remainders)}}}, {{{','.join(moduli)}}}]"


if __name__ == "__main__":
    print(part_1())
    print(part_2())
