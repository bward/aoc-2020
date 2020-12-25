import itertools

modulus = 20201227

with open("input/day25.txt") as puzzle_input:
    card_key = int(puzzle_input.readline())
    door_key = int(puzzle_input.readline())


for l in itertools.count(1):
    if pow(7, l, modulus) == card_key:
        print(pow(door_key, l, modulus))
        break
