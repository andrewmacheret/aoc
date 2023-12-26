#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  copies = defaultdict(int)
  score = 0
  for r, line in enumerate(load(file), 1):
    copies[r] += 1
    card, winning = map(parse_nums, line.split('|'))
    card = card[1:]
    x = sum(c in winning for c in card)
    for j in range(1, x+1):
      copies[r+j] += copies[r]
    score += (1 << x - 1) if x else 0

  return score if part == 0 else sum(copies.values())


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(13, solve(part=0, file='input-test-1'))
  test(22193, solve(part=0, file='input-real'))

  test(30, solve(part=1, file='input-test-1'))
  test(5625994, solve(part=1, file='input-real'))
