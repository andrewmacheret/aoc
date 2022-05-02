#!/usr/bin/env python3

from common.util import *


def gen(x, inc, multiple=1):
  while 1:
    x *= inc
    x %= 2147483647
    if x % multiple == 0:
      yield x & 0xffff


def solve(part, file):
  a, b = [parse_nums(line)[0] for line in load(file)]
  ga = gen(a, 16807, [1, 4][part])
  gb = gen(b, 48271, [1, 8][part])
  return sum(next(ga) == next(gb) for _ in range([40000000, 5000000][part]))

### THE REST IS TESTS ###


if __name__ == "__main__":
  change_dir(__file__)

  test(588, solve(part=0, file='input-test-1'))
  test(573, solve(part=0, file='input-real'))

  test(309, solve(part=1, file='input-test-1'))
  test(294, solve(part=1, file='input-real'))
