#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  data = load(file)
  games = [(ord(a)-ord('A'), ord(c)-ord('X')) for a, _, c in data]
  if part == 0:
    return sum(b * 1 + (b-a+1) % 3 * 3 + 1 for a, b in games)
  else:
    return sum(b * 3 + (b+a-1) % 3 * 1 + 1 for a, b in games)


### THE REST IS TESTS ###
if __name__ == "__main__":
  change_dir(__file__)

  test(15, solve(part=0, file='input-test-1'))
  test(14163, solve(part=0, file='input-real'))

  test(12, solve(part=1, file='input-test-1'))
  test(12091, solve(part=1, file='input-real'))  # not 10579
