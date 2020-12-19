import re
import itertools

with open("input/day19.txt") as puzzle_input:
    raw_rules = []
    while (l := puzzle_input.readline()) != "\n":
        raw_rules.append(l.rstrip())

    messages = [l.rstrip() for l in puzzle_input.readlines()]

    rules = [None] * len(raw_rules)
    for r in raw_rules:
        g = re.fullmatch("(\d+): (.+)", r).groups()
        rules[int(g[0])] = [
            tuple([eval(x) for x in rule.split(" ")]) for rule in g[1].split(" | ")
        ]


def _expand_rule(rule_idx):
    rule = rules[rule_idx]

    if isinstance(rule[0][0], str):
        return {rule[0][0]}

    return set(
        itertools.chain.from_iterable(
            ["".join(a) for a in itertools.product(*[_expand_rule(x) for x in opt])]
            for opt in rule
        )
    )
    return matches


def part_1():
    possible_messages = _expand_rule(0)
    return len([m for m in messages if m in possible_messages])


def part_2():
    rule_42 = _expand_rule(42)
    rule_31 = _expand_rule(31)

    def _matches(message):
        chunks = [message[i : i + 8] for i in range(0, len(message), 8)]
        first_31 = next((i for i, c in enumerate(chunks) if c in rule_31), None)

        return (
            first_31
            and len(chunks) / 2 < first_31
            and all(c in rule_42 for c in chunks[:first_31])
            and all(c in rule_31 for c in chunks[first_31:])
        )

    return len([m for m in messages if _matches(m)])


if __name__ == "__main__":
    print(part_1())
    print(part_2())
