#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  firewall = list(map(parse_nums, load(file)))

  def simulate(waited):
    for depth, range in firewall:
      if (depth + waited) % ((range-1) * 2) == 0:
        yield (depth, range)

  if not part:
    return sum(starmap(mul, simulate(0)))

  for wait in count():
    if next(simulate(wait), None) is None:
      return wait


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(24, solve(part=0, file='input-test-1'))
  test(632, solve(part=0, file='input-real'))

  test(10, solve(part=1, file='input-test-1'))
  test(3849742, solve(part=1, file='input-real'))
