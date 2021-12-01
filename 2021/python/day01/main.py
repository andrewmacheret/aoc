#!/usr/bin/env python3
from operator import lt

from common.util import test, load_ints, change_dir


def solve(part, filename):
  data = list(load_ints(filename))
  if part == 2:
    data = list(map(sum, zip(data, data[1:], data[2:])))
  return sum(map(lt, data, data[1:]))


if __name__ == "__main__":
  change_dir(__file__)
  test(7, solve(1, 'input-test-1'))
  test(1215, solve(1, 'input'))

  test(5, solve(2, 'input-test-1'))
  test(1150, solve(2, 'input'))
