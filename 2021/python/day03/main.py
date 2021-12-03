#!/usr/bin/env python3

from collections import Counter
from common.util import *


def get_rate(data, i):
  return int(''.join(Counter(row).most_common()[i][0] for row in [*zip(*data)]), 2)


def get_rating(data, i):
  for j in range(len(data[0])):
    mc = Counter([*zip(*data)][j]).most_common()
    b = '10'[i] if len(mc) == 2 and mc[0][1] == mc[1][1] else mc[-i][0]
    data = [row for row in data if row[j] == b]
  return int(data[0], 2)


def solve(part, file):
  data = load(file)
  fn = get_rate if part == 1 else get_rating
  return fn(data, 0) * fn(data, 1)


if __name__ == "__main__":
  change_dir(__file__)

  test(198, solve(part=1, file='input-test-1'))
  test(3985686, solve(part=1, file='input-real'))

  test(230, solve(part=2, file='input-test-1'))
  test(2555739, solve(part=2, file='input-real'))
