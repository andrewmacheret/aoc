#!/usr/bin/env python3

from common.util import *


DIRS_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def load_grid(file):
  return [[int(val) for val in row] for row in load(file)]


def solve(part, file):
  data = load_grid(file)

  n = len(data)

  if part == 0:
    visible = set()
    for y in range(n):
      for r in (range(n), range(n-1, -1, -1)):
        v = -1
        for x in r:
          if v < data[y][x]:
            v = data[y][x]
            visible.add((x, y))
        v = -1
        for x in r:
          if v < data[x][y]:
            v = data[x][y]
            visible.add((y, x))
    return len(visible)

  best = 0
  for y in range(1, n-1):
    for x in range(1, n-1):
      score = 1
      for dx, dy in DIRS_4:
        dist = 0
        x1, y1 = x + dx, y + dy
        while 0 <= x1 < n and 0 <= y1 < n:
          dist += 1
          if data[y1][x1] >= data[y][x]:
            break
          x1, y1 = x1 + dx, y1 + dy
        score *= dist
      best = max(best, score)
  return best


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(21, solve(part=0, file='input-test-1'))
  test(1538, solve(part=0, file='input-real'))

  test(8, solve(part=1, file='input-test-1'))
  test(496125, solve(part=1, file='input-real'))
