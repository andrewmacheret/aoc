#!/usr/bin/env python3

from common.util import *

def predict(nums):
  groups = [nums]
  while len(set(groups[-1])) != 1:
    groups.append([b-a for a,b in pairwise(groups[-1])])
  return reduce(lambda x,g: g[0] - x, groups[::-1], 0)

def solve(part, file):
  return sum(predict(parse_nums(line)[::[-1,1][part]]) for line in load(file))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(114, solve(part=0, file='input-test-1'))
  test(1868368343, solve(part=0, file='input-real'))

  test(2, solve(part=1, file='input-test-1'))
  test(1022, solve(part=1, file='input-real'))

  test(None, solve(part=0, file='input-test-2'))
