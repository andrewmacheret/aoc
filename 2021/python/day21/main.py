#!/usr/bin/env python3

from collections import Counter
from itertools import cycle, product

from common.util import load, test, change_dir, parse_nums


def deterministic_dice(sides):
  gen = cycle(range(1, sides+1))
  return lambda: {next(gen) + next(gen) + next(gen): 1}


def quantum_dice(sides):
  counter = Counter(i+j+k for i, j, k in product(range(1, sides+1), repeat=3))
  return lambda: counter


def dirac_dice(players, roll_counts, goal):
  dp = Counter([(*players, 0, 0)])
  totals = [0, 0]
  first_to_win = None
  for round, turn in enumerate(cycle((0, 1)), 1):
    dp_next = Counter()
    for (player1, player2, score1, score2), universes in dp.items():
      for roll, roll_count in roll_counts().items():
        next_player1 = (player1 + roll) % 10 or 10
        next_score1 = score1 + next_player1
        if next_score1 < goal:
          next_state = (player2, next_player1, score2, next_score1)
          dp_next[next_state] += universes * roll_count
        else:
          if not first_to_win:
            first_to_win = (round * 3) * score2
          totals[turn] += universes * roll_count
    if not (dp := dp_next):
      return first_to_win, max(totals)


def solve(part, file):
  players = [parse_nums(line)[-1] for line in load(file)]
  args = (deterministic_dice(100), 1000) if part == 1 else (quantum_dice(3), 21)
  return dirac_dice(players, *args)[part - 1]


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(739785, solve(part=1, file='input-test-1'))
  test(903630, solve(part=1, file='input-real'))

  test(444356092776315, solve(part=2, file='input-test-1'))
  test(303121579983974, solve(part=2, file='input-real'))
