#!/usr/bin/env python3

from collections import Counter
from common.util import *


def get_common_bit(rows, column, i):
  bits = [*zip(*rows)][column]
  mc = Counter(bits).most_common()
  return '10'[i] if len(mc) == 2 and mc[0][1] == mc[1][1] else mc[-i][0]


def get_rate(data, i):
  return int(''.join(get_common_bit(data, c, i) for c in range(len(data[0]))), 2)


def get_rating(data, i):
  for c in range(len(data[0])):
    b = get_common_bit(data, c, i)
    data = [row for row in data if row[c] == b]
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
