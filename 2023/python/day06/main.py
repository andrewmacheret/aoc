#!/usr/bin/env python3

from common.util import *
from math import *

def count_ways(t, d):
  lo, hi = (op((t + i*sqrt(t*t - 4*d)) / 2) for op, i in ((ceil, -1+1e-9), (floor, 1-1e-9)))
  return hi - lo + 1


def solve(part, file):
  times, dists = map(parse_nums, load(file))
  if part == 1:
    times, dists = ([int(''.join(map(str, x)))] for x in (times, dists))
  return reduce(mul, starmap(count_ways, zip(times, dists)))




### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(288, solve(part=0, file='input-test-1'))
  test(2612736, solve(part=0, file='input-real'))

  test(71503, solve(part=1, file='input-test-1'))
  test(29891250, solve(part=1, file='input-real'))
