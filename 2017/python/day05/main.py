#!/usr/bin/env python3


from common.util import *


def solve(part, file):
  jumps = load_ints(file)[:]
  ptr = 0
  for steps in count():
    if not (0 <= ptr < len(jumps)):
      return steps
    amt = (1, -1)[part and jumps[ptr] >= 3]
    jumps[ptr] += amt
    ptr += jumps[ptr] - amt
  return steps


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(5, solve(part=0, file='input-test-1'))
  test(351282, solve(part=0, file='input-real'))

  test(10, solve(part=1, file='input-test-1'))
  test(24568703, solve(part=1, file='input-real'))
