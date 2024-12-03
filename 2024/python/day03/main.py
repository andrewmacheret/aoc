#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  data = '\n'.join(load(file))
  total = 0
  enable = True
  for x in re.findall(r'mul\(\d+,\d+\)|do(?:n\'t)?\(\)', data):
    if x[0] == 'd':
      enable = len(x) == 4
    elif not part or enable:
      total += mul(*parse_nums(x))
  return total


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(161, solve(part=0, file='input-test-1'))
  test(184122457, solve(part=0, file='input-real'))

  test(48, solve(part=1, file='input-test-2'))
  test(107862689, solve(part=1, file='input-real'))
