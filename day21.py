import re

with open("input/day21.txt") as puzzle_input:
    foods = []
    for line in puzzle_input.readlines():
        groups = re.match(r"(.+) \(contains (.+)\)", line).groups()
        foods.append((set(groups[0].split(" ")), set(groups[1].split(", "))))

    all_ingredients = frozenset().union(*(i for i, a in foods))
    all_allergens = frozenset().union(*(a for i, a in foods))


def part_1():
    possible_allergens = set()
    for allergen in all_allergens:
        possible_ingredients = all_ingredients.intersection(
            *(i for i, a in foods if allergen in a)
        )
        possible_allergens.update(possible_ingredients)

    return sum(
        len(ingredients.difference(possible_allergens)) for ingredients, _ in foods
    )


def part_2():
    possible_allergens = {}
    for allergen in all_allergens:
        possible_ingredients = all_ingredients.intersection(
            *(i for i, a in foods if allergen in a)
        )
        possible_allergens[allergen] = possible_ingredients

    determined = {}
    while True:
        for allergen, possible_ingredients in possible_allergens.items():
            if allergen in determined:
                continue
            remaining_possibilities = [
                i for i in possible_ingredients if i not in determined.values()
            ]
            if len(remaining_possibilities) == 1:
                determined[allergen] = remaining_possibilities[0]
                break
        else:
            break

    return ",".join(determined[d] for d in sorted(determined))


if __name__ == "__main__":
    print(part_1())
    print(part_2())
