#!/usr/bin/env python3

from common.util import *


def redistro(banks):
  n = len(banks)
  x, i = max(zip(banks, count(0, -1)))
  d, m = divmod(x, n)
  return tuple(d + y * (j != -i) + (0 < (j+i) % n <= m) for j, y in enumerate(banks))


def loop(banks):
  seen = set()
  for i in count():
    if banks in seen:
      return i, banks
    seen.add(banks)
    banks = redistro(banks)
  return i, banks


def solve(part, file):
  banks = tuple(parse_nums(load(file)[0]))
  for _ in range(part+1):
    i, banks = loop(banks)
  return i


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(5, solve(part=0, file='input-test-1'))
  test(5042, solve(part=0, file='input-real'))

  test(4, solve(part=1, file='input-test-1'))
  test(1086, solve(part=1, file='input-real'))
