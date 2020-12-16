import re
import itertools
from collections import defaultdict


with open("input/day14.txt") as puzzle_input:
    instructions = []
    for line in puzzle_input.readlines():
        if line.startswith("mask"):
            instructions.append(re.fullmatch("(mask) = (.+)", line.rstrip()).groups())
        else:
            match = re.fullmatch(r"(mem)\[(\d+)\] = (\d+)", line.rstrip()).groups()
            instructions.append((match[0], int(match[1]), int(match[2])))


def _apply_mask(mask, value):
    binary = bin(value)[2:].rjust(36, "0")

    return int("".join(v if m == "X" else m for v, m in zip(binary, mask)), 2)


def part_1():
    memory = defaultdict(int)
    mask = None

    for op, *args in instructions:
        if op == "mask":
            mask = args[0]
        else:
            memory[args[0]] = _apply_mask(mask, args[1])

    return sum(memory.values())


def _apply_memory_mask(mask, value):
    xs = mask.count("X")
    floating_iters = [iter(i) for i in itertools.product(*[[0, 1]] * xs)]
    binary = bin(value)[2:].rjust(36, "0")

    return [
        int(
            "".join(
                v if m == "0" else m if m == "1" else str(next(floating_bits))
                for v, m in zip(binary, mask)
            ),
            2,
        )
        for floating_bits in floating_iters
    ]


def part_2():
    memory = defaultdict(int)
    mask = None

    for op, *args in instructions:
        if op == "mask":
            mask = args[0]
        else:
            addresses = _apply_memory_mask(mask, args[0])
            for address in addresses:
                memory[address] = args[1]

    return sum(memory.values())


if __name__ == "__main__":
    print(part_1())
    print(part_2())
