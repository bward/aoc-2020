import re
from dataclasses import dataclass


with open("input/day08.txt") as puzzle_input:
    raw = [re.search(r"(.+) (.+)", line).groups() for line in puzzle_input.readlines()]
    instructions = [(op, int(arg)) for op, arg in raw]


@dataclass
class Result:
    acc: str
    is_infinite_loop: bool = False


def _run(instructions):
    ptr = 0
    acc = 0
    executed = set()

    while True:
        if ptr == len(instructions):
            return Result(acc)

        if ptr in executed:
            return Result(acc, is_infinite_loop=True)
        else:
            executed.add(ptr)

        op, arg = instructions[ptr]

        if op == "acc":
            acc += arg
        elif op == "jmp":
            ptr += arg
            continue
        elif op == "nop":
            pass
        else:
            raise ValueError("Unknown operation", op)

        ptr += 1


def part_1():
    return _run(instructions)


def part_2():
    for i, (op, arg) in enumerate(instructions):
        if op == "acc":
            continue

        modified_instructions = instructions.copy()
        modified_instructions[i] = ("jmp" if op == "nop" else "nop", arg)

        result = _run(modified_instructions)

        if not result.is_infinite_loop:
            return result


if __name__ == "__main__":
    print(part_1())
    print(part_2())
