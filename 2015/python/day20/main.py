#!/usr/bin/env python3

from common.util import load_int, test, change_dir


def solve(part, file):
  goal = load_int(file)

  n = 1000000
  totals = [0] * n
  for i in range(1, n):
    limit = n if part == 1 else min(n, i*51)
    for j in range(i, limit, i):
      totals[j] += i * (10 + part - 1)
  return next(i for i, x in enumerate(totals) if x >= goal)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(786240, solve(part=1, file='input-real'))

  test(831600, solve(part=2, file='input-real'))
