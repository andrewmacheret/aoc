#!/usr/bin/env python3

from common.util import *


def parse_nums(line):
  return map(int, re.findall(r'\d+', line))


parts = [
    lambda a, b, c, d: (a <= c <= d <= b) or (c <= a <= b <= d),
    lambda a, b, c, d: b >= c <= d >= a
]


def solve(part, file):
  return sum(parts[part](*parse_nums(line)) for line in load(file))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(2, solve(part=0, file='input-test-1'))
  test(518, solve(part=0, file='input-real'))

  test(4, solve(part=1, file='input-test-1'))
  test(909, solve(part=1, file='input-real'))
