#!/usr/bin/env python3

from common.util import *


def load_elves(file):
  return [sum(int(line) for line in lines) for lines in load_blocks(file)]


def solve(part, file):
  elves = load_elves(file)
  return max(elves) if part == 0 else sum(nlargest(3, elves))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(24000, solve(part=0, file='input-test-1'))
  test(68923, solve(part=0, file='input-real'))

  test(200044, solve(part=1, file='input-real'))
