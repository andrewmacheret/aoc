#!/usr/bin/env python3

from common.util import *


def load_int_grid(file):
  return [[int(c) for c in x] for x in load(file)]


def solve(steps, file):
  grid = load_int_grid(file)
  n, m = len(grid), len(grid[0])
  flashes = 0

  for round in range(1, steps+1):
    q = [(x, y) for x in range(m) for y in range(n)]
    while q:
      x, y = q.pop()
      grid[y][x] += 1
      if grid[y][x] == 10:
        flashes += 1
        q.extend((x+dx, y+dy) for dx, dy in DIRS_8
                 if 0 <= y+dy < n and 0 <= x+dx < m)
    grid = [[min(grid[y][x], 10) % 10 for x in range(m)] for y in range(n)]
    if max(x for row in grid for x in row) == 0:
      return round
  return flashes


if __name__ == "__main__":
  change_dir(__file__)

  test(0, solve(steps=1, file='input-test-1'))
  test(35, solve(steps=2, file='input-test-1'))
  test(80, solve(steps=3, file='input-test-1'))
  test(204, solve(steps=10, file='input-test-1'))
  test(1656, solve(steps=100, file='input-test-1'))
  test(1700, solve(steps=100, file='input-real'))

  test(195, solve(steps=200, file='input-test-1'))
  test(273, solve(steps=999, file='input-real'))
