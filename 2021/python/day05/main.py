#!/usr/bin/env python3

from collections import defaultdict
import re

from common.util import load, test, change_dir


def solve(part, file):
  data = load(file)
  lines = [[*map(int, re.findall(r'\d+', line))] for line in data]
  grid = defaultdict(int)
  for x1, y1, x2, y2 in lines:
    if x1 == x2:
      for y in range(min(y1, y2), max(y1, y2)+1):
        grid[x1, y] += 1
    elif y1 == y2:
      for x in range(min(x1, x2), max(x1, x2)+1):
        grid[x, y1] += 1
    elif part == 2:
      dx, dy = 1 | -(x1 > x2), 1 | -(y1 > y2)
      for i in range(abs(x2 - x1)+1):
        grid[x1+i*dx, y1+i*dy] += 1
  return sum(c > 1 for c in grid.values())


if __name__ == "__main__":
  change_dir(__file__)

  test(5, solve(part=1, file='input-test-1'))
  test(4873, solve(part=1, file='input-real'))

  test(12, solve(part=2, file='input-test-1'))
  test(19472, solve(part=2, file='input-real'))
