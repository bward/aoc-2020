import itertools

modulus = 20201227

with open("input/day25.txt") as puzzle_input:
    card_key = int(puzzle_input.readline())
    door_key = int(puzzle_input.readline())


def _transform(subject, loop_size):
    out = 1
    subject = subject % modulus
    while loop_size > 0:
        if loop_size % 2 == 1:
            out = (out * subject) % modulus
        loop_size = loop_size >> 1
        subject = (subject * subject) % modulus
    return out


for l in itertools.count(1):
    if _transform(7, l) == card_key:
        print(_transform(door_key, l))
        break
