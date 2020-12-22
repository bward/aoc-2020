from collections import deque


def _parse_decks():
    with open("input/day22.txt") as puzzle_input:
        raw = puzzle_input.read().split("\n\n")
        player_1 = deque(int(c) for c in raw[0].rstrip().split("\n")[1:])
        player_2 = deque(int(c) for c in raw[1].rstrip().split("\n")[1:])
    return player_1, player_2


def _score(deck):
    return sum((len(deck) - i) * c for i, c in enumerate(deck))


def part_1():
    player_1, player_2 = _parse_decks()
    while player_1 and player_2:
        card_1, card_2 = player_1.popleft(), player_2.popleft()

        if card_1 > card_2:
            player_1.extend([card_1, card_2])
        else:
            player_2.extend([card_2, card_1])

    winner = player_1 if player_1 else player_2
    return _score(winner)


def part_2():
    def _play_game(player_1, player_2):
        seen = set()
        while player_1 and player_2:
            if (state := (tuple(player_1), tuple(player_2))) in seen:
                return True
            seen.add(state)

            card_1, card_2 = player_1.popleft(), player_2.popleft()
            if card_1 > len(player_1) or card_2 > len(player_2):
                if card_1 > card_2:
                    player_1.extend([card_1, card_2])
                else:
                    player_2.extend([card_2, card_1])
            else:
                player_1_wins = _play_game(
                    deque([player_1[c] for c in range(card_1)]),
                    deque([player_2[c] for c in range(card_2)]),
                )
                if player_1_wins:
                    player_1.extend([card_1, card_2])
                else:
                    player_2.extend([card_2, card_1])

        return bool(player_1)

    player_1, player_2 = _parse_decks()
    winner = player_1 if _play_game(player_1, player_2) else player_2
    return _score(winner)


if __name__ == "__main__":
    print(part_1())
    print(part_2())
