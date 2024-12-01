#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  data = load(file) # from common.util
  A, B = zip(*(parse_nums(line) for line in data))
  if part == 0:
    return sum(abs(a-b) for a,b in zip(sorted(A), sorted(B)))
  else:
    C = Counter(B)
    return sum(x * C[x] for x in A)



### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(11, solve(part=0, file='input-test-1'))
  test(1530215, solve(part=0, file='input-real'))

  test(31, solve(part=1, file='input-test-1'))
  test(26800609, solve(part=1, file='input-real'))
