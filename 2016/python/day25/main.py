#!/usr/bin/env python3

from common.util import load, test, change_dir


def solve(file):
  a, b = (int(line.split()[1]) for line in load(file)[1:3])
  x = 2
  while x <= a * b:
    x = x * 4 + 2
  return x - a * b


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(198, solve(file='input-real'))
