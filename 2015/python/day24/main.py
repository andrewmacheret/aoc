#!/usr/bin/env python3

from itertools import combinations
from functools import reduce
from operator import mul

from common.util import load_ints, test, change_dir


def partition(nums, num_groups):
  if num_groups == 1:
    yield (nums,)
  else:
    num_set = set(nums)
    goal = sum(nums) // num_groups

    for y in range(1, len(nums)):
      for combo in sorted(combinations(nums, y), key=lambda x: reduce(mul, x)):
        if sum(combo) == goal:
          remaining = sorted(num_set - set(combo))
          for other_combos in partition(remaining, num_groups - 1):
            yield combo, *other_combos


def solve(part, file):
  data = load_ints(file)
  combos = next(partition(data, 2 + part))
  return reduce(mul, combos[0])


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(99, solve(part=1, file='input-test-1'))
  test(11846773891, solve(part=1, file='input-real'))

  test(44, solve(part=2, file='input-test-1'))
  test(80393059, solve(part=2, file='input-real'))
