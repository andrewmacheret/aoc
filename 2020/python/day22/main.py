#!/usr/bin/env python3
from day04.main import load_multiline, test
from collections import deque
from itertools import islice


def load_decks(filename, script=__file__):
    return [deque(map(int, lines[1:])) for lines in load_multiline(filename, script=script)]


def score_deck(deck):
    return sum(i*card for i, card in enumerate(reversed(deck), 1))


def play_game(deck1, deck2, recurse):
    seen = set()

    while deck1 and deck2:
        position = tuple((tuple(deck1), tuple(deck2)))
        if position in seen:
            return 0  # player 1 wins
        seen.add(position)

        a, b = deck1.popleft(), deck2.popleft()
        if recurse and a <= len(deck1) and b <= len(deck2):
            winner = play_game(deque(islice(deck1, 0, a)),
                               deque(islice(deck2, 0, b)), recurse)
        else:
            winner = int(a < b)
        (deck2 if winner else deck1).append(b if winner else a)
        (deck2 if winner else deck1).append(a if winner else b)
    return int(bool(deck2))


def part1(filename):
    decks = load_decks(filename)
    winner = play_game(*decks, recurse=False)
    return score_deck(decks[winner])


def part2(filename):
    decks = load_decks(filename)
    winner = play_game(*decks, recurse=True)
    return score_deck(decks[winner])


if __name__ == "__main__":
    test(306, part1('input-test-1.txt'))
    test(31754, part1('input.txt'))

    test(291, part2('input-test-1.txt'))
    test(35436, part2('input.txt'))
