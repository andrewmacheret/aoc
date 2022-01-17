#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  table = [parse_nums(line) for line in load(file)]

  def divide(row):
    return next(max(a, b) // min(a, b)
                for a, b in combinations(row, 2)
                if max(a, b) % min(a, b) == 0)
  if part == 0:
    return sum(map(max, table)) - sum(map(min, table))
  else:
    return sum(map(divide, table))


### THE REST IS TESTS ###
if __name__ == "__main__":
  change_dir(__file__)

  test(18, solve(part=0, file='input-test-1'))
  test(32121, solve(part=0, file='input-real'))

  test(9, solve(part=1, file='input-test-2'))
  test(197, solve(part=1, file='input-real'))
