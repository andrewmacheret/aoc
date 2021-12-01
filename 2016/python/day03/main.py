#!/usr/bin/env python3

import re

from common.util import load, test, change_dir


def load_triangles(file):
  return [[int(x.strip()) for x in re.split(r' +', line) if x.strip()] for line in load(file)]


def count_valid_trianges(data):
  return sum(a + b > c for a, b, c in map(sorted, data))


def solve1(file):
  data = load_triangles(file)
  return count_valid_trianges(data)


def solve2(file):
  data = list(zip(*load_triangles(file)))
  return sum(count_valid_trianges(zip(*[iter(row)] * 3)) for row in data)


if __name__ == "__main__":
  change_dir(__file__)

  test(2, solve1(file='input-test-1'))
  test(862, solve1(file='input-real'))

  test(6, solve2(file='input-test-2'))
  test(1577, solve2(file='input-real'))
