#!/usr/bin/env python3

from common.util import *


DIRS = {
    'n': -2j,
    's': +2j,
    'ne': +1 + -1j,
    'nw': -1 + -1j,
    'se': +1 + +1j,
    'sw': -1 + +1j,
}


def simulate(dirs):
  for x in accumulate(map(DIRS.__getitem__, dirs)):
    yield int((abs(x.real) + abs(x.imag)) // 2)


def solve(part, file):
  dists = simulate(load_csv(file)[0])
  return max(dists) if part else deque(dists, maxlen=1).pop()


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(3, solve(part=0, file='input-test-1'))
  test(0, solve(part=0, file='input-test-2'))
  test(2, solve(part=0, file='input-test-3'))
  test(3, solve(part=0, file='input-test-4'))
  test(682, solve(part=0, file='input-real'))

  test(1406, solve(part=1, file='input-real'))
