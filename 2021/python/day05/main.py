#!/usr/bin/env python3

from collections import defaultdict

from common.util import sign, parse_nums, load, test, change_dir


def solve(part, file):
  lines = [*map(parse_nums, load(file))]
  grid = defaultdict(int)
  for x1, y1, x2, y2 in lines:
    dx, dy = sign(x2 - x1), sign(y2 - y1)
    if part == 2 or not dx or not dy:
      for i in range(abs(x2 - x1 or y2 - y1) + 1):
        grid[x1+i*dx, y1+i*dy] += 1

  return sum(c > 1 for c in grid.values())


if __name__ == "__main__":
  change_dir(__file__)

  test(5, solve(part=1, file='input-test-1'))
  test(4873, solve(part=1, file='input-real'))

  test(12, solve(part=2, file='input-test-1'))
  test(19472, solve(part=2, file='input-real'))
