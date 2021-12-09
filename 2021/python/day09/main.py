#!/usr/bin/env python3

from collections import defaultdict
from functools import reduce
from heapq import nlargest

from common.util import load, test, change_dir


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solve(part, file):
  data = load(file)

  grid = defaultdict(lambda: 9)
  for y, line in enumerate(data):
    for x, c in enumerate(line):
      grid[x, y] = int(c)

  res = []
  if part == 1:
    for x, y in list(grid.keys()):
      if all(grid[x, y] < grid[x+dx, y+dy] for dx, dy in DIRS):
        res.append(1 + grid[x, y])
    return sum(res)
  else:
    def dfs(x, y):
      return grid.pop((x, y), 9) < 9 and 1 + sum(dfs(x+dx, y+dy) for dx, dy in DIRS)
    for x, y in list(grid.keys()):
      if (size := dfs(x, y)):
        res.append(size)
    return reduce(int.__mul__, nlargest(3, res))


if __name__ == "__main__":
  change_dir(__file__)

  test(15, solve(part=1, file='input-test-1'))
  test(554, solve(part=1, file='input-real'))

  test(1134, solve(part=2, file='input-test-1'))
  test(1017792, solve(part=2, file='input-real'))
