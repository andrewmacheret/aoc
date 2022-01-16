#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  data = load(file)[0]
  k = (1, len(data) // 2)[part == 2]
  return sum(int(a) for a, b in zip(data, data[k:] + data[:k]) if a == b)


### THE REST IS TESTS ###
if __name__ == "__main__":
  change_dir(__file__)

  test(3, solve(part=1, file='input-test-1'))
  test(4, solve(part=1, file='input-test-2'))
  test(0, solve(part=1, file='input-test-3'))
  test(9, solve(part=1, file='input-test-4'))
  test(1044, solve(part=1, file='input-real'))

  test(6, solve(part=2, file='input-test-5'))
  test(0, solve(part=2, file='input-test-6'))
  test(4, solve(part=2, file='input-test-7'))
  test(12, solve(part=2, file='input-test-8'))
  test(4, solve(part=2, file='input-test-9'))
  test(1054, solve(part=2, file='input-real'))
