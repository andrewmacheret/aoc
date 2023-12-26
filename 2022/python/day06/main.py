#!/usr/bin/env python3

from common.util import *


def solve2(data, k):
  num_processed = 0
  num_distinct = 0
  distinct = {}
  for character in data:
    num_processed += 1
    if character not in distinct:
      num_distinct += 1
      distinct[character] = True
      if num_distinct == k:
        return num_processed - k
    else:
      num_distinct -= 1
  return -1


def solve(part, file):
  data = load(file)[0]
  x = 4 + part * 10
  return solve2(data, x)
  # return next(i for i in range(x, len(data)) if len(set(data[i-x:i])) == x)


### THE REST IS TESTS ###
if __name__ == "__main__":
  change_dir(__file__)

  test(7, solve(part=0, file='input-test-1'))
  test(5, solve(part=0, file='input-test-2'))
  test(6, solve(part=0, file='input-test-3'))
  test(10, solve(part=0, file='input-test-4'))
  test(11, solve(part=0, file='input-test-5'))
  test(1034, solve(part=0, file='input-real'))

  test(19, solve(part=1, file='input-test-1'))
  test(23, solve(part=1, file='input-test-2'))
  test(23, solve(part=1, file='input-test-3'))
  test(29, solve(part=1, file='input-test-4'))
  test(26, solve(part=1, file='input-test-5'))
  test(2472, solve(part=1, file='input-real'))
