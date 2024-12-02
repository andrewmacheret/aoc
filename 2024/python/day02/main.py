#!/usr/bin/env python3

from common.util import *


def safe(nums):
  A = [*starmap(sub, pairwise(nums))]
  return all(0 < x < 4 for x in A) or all(0 < -x < 4 for x in A)
 
def solve(part, file):
  total = 0
  for nums in map(parse_nums, load(file)):
    total += safe(nums) or part and any(safe(nums[:i] + nums[i+1:]) for i in range(len(nums)))
  return total


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(2, solve(part=0, file='input-test-1'))
  test(236, solve(part=0, file='input-real'))

  test(4, solve(part=1, file='input-test-1'))
  test(308, solve(part=1, file='input-real'))
