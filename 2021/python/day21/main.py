#!/usr/bin/env python3

from collections import defaultdict
from itertools import cycle, product

from common.util import load, test, change_dir, parse_nums


def mod_up(x, m=10):
  return x % m or m


def part1(players, goal=1000, die_sides=100):
  dice = cycle(range(1, die_sides+1))
  scores = [0, 0]
  for round, turn in enumerate(cycle((0, 1)), 1):
    roll = next(dice) + next(dice) + next(dice)
    players[turn] = mod_up(players[turn] + roll)
    scores[turn] += players[turn]
    if scores[turn] >= goal:
      return (round * 3) * scores[1 - turn]


def part2(players, goal=21, die_sides=3):
  roll_counts = defaultdict(int)
  for i, j, k in product(range(1, die_sides+1), repeat=3):
    roll_counts[i+j+k] += 1

  dp = defaultdict(int, {(*players, 0, 0): 1})
  totals = [0, 0]
  for turn in cycle((0, 1)):
    dp_next = defaultdict(int)
    for (player1, player2, score1, score2), universes in dp.items():
      if score2 < goal:
        for roll, roll_count in roll_counts.items():
          player1_next = mod_up(player1 + roll)
          score1_next = score1 + player1_next
          dp_next[player2, player1_next, score2, score1_next] \
              += universes * roll_count
      else:
        totals[turn] += universes
    if not (dp := dp_next):
      return max(totals)


def solve(part, file):
  players = [parse_nums(line)[-1] for line in load(file)]
  return (part1, part2)[part - 1](players)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(739785, solve(part=1, file='input-test-1'))
  test(903630, solve(part=1, file='input-real'))

  test(303121579983974, solve(part=2, file='input-real'))
