#!/usr/bin/env python3

from collections import Counter
from functools import reduce

from common.util import load_csv, test, change_dir


def solve(days, file):
  data = [*map(int, load_csv(file)[0])]
  return sum(reduce(lambda c, _:
                    Counter({x-1: v for x, v in c.items() if x}) +
                    Counter({6: c[0], 8: c[0]}),
                    range(days), Counter(data)).values())


if __name__ == "__main__":
  change_dir(__file__)

  test(26, solve(days=18, file='input-test-1'))
  test(362740, solve(days=80, file='input-real'))

  test(26984457539, solve(days=256, file='input-test-1'))
  test(1644874076764, solve(days=256, file='input-real'))
