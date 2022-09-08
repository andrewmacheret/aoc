#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappush, heappop
from math import inf
from common.util import load, test, change_dir, DIRS_4


def solve(mult, file):
  grid = [[int(x) for x in line] for line in load(file)]
  seen = defaultdict(lambda: inf, {(0, 0): 0})
  n, m = len(grid), len(grid[0])
  goal = m*mult-1, n*mult-1
  q = [(0, 0, 0)]
  while q:
    score, x, y = heappop(q)
    if (x, y) == goal:
      return score
    for dx, dy in DIRS_4:
      if 0 <= (x1 := x+dx) <= goal[0] and 0 <= (y1 := y+dy) <= goal[1]:
        yd, ym = divmod(y1, n)
        xd, xm = divmod(x1, m)
        val = score + (grid[ym][xm] + xd + yd - 1) % 9 + 1
        if seen[x1, y1] > val:
          seen[x1, y1] = val
          heappush(q, (val, x1, y1))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(40, solve(mult=1, file='input-test-1'))
  test(748, solve(mult=1, file='input-real'))

  test(315, solve(mult=5, file='input-test-1'))
  test(3045, solve(mult=5, file='input-real'))
