#!/usr/bin/env python3

from common.util import load, test, change_dir, parse_nums


def solve(part, file, lo=0, hi=0):
  ranges = sorted(parse_nums(line) for line in load(file))
  res = 0
  for x, y in ranges:
    if lo + 1 <= x - 1:
      if part == 1:
        return lo+1
      res += x - lo - 1
    lo = max(lo, y)
  return res + hi - lo


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(3, solve(part=1, hi=9, file='input-test-1'))
  test(19449262, solve(part=1, hi=4294967295, file='input-real'))

  test(2, solve(part=2, hi=9, file='input-test-1'))
  test(119, solve(part=2, hi=4294967295, file='input-real'))
