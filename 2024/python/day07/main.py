#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  def recurse(nums):
    if len(nums) == 1:
      yield nums[0]
    else:
      for x in recurse(nums[:-1]):
        yield x + nums[-1]
        yield x * nums[-1]
        if part: yield int(str(x) + str(nums[-1]))

  total = 0
  for line in load(file):
    goal, *nums = parse_nums(line)
    if any(result for result in recurse(nums) if result == goal):
      total += goal

  return total


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(3749, solve(part=0, file='input-test-1'))
  test(7579994664753, solve(part=0, file='input-real'))

  test(11387, solve(part=1, file='input-test-1'))
  test(438027111276610, solve(part=1, file='input-real'))
