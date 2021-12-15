#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
from math import inf
from common.util import load, test, change_dir, DIRS_4


def solve(part, file):
  data = load(file)
  grid = []
  for line in data:
    nums = [int(x) for x in line]
    grid.append(nums)

  seen = defaultdict(lambda: inf)
  seen[0, 0] = 0
  n, m = len(grid), len(grid[0])
  goal = (m*5-1, n*5-1) if part == 2 else (m-1, n-1)
  q = [(0, 0, 0)]
  while q:
    score, x, y = heappop(q)
    if (x, y) == goal:
      return score
    for dx, dy in DIRS_4:
      x1, y1 = x+dx, y+dy
      if 0 <= x1 <= goal[0] and 0 <= y1 <= goal[1]:
        val = (grid[y1 % n][x1 % m] + (x1//m) + (y1//n) -
               1) % 9 + 1 if part == 2 else grid[y1][x1]
        if (s := score + val) < seen[x1, y1]:
          heappush(q, (s, x1, y1))
          seen[x1, y1] = s


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(40, solve(part=1, file='input-test-1'))
  test(748, solve(part=1, file='input-real'))

  test(315, solve(part=2, file='input-test-1'))
  test(3045, solve(part=2, file='input-real'))
