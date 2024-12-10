#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  grid = load_grid(file)
  n, m = len(grid), len(grid[0])

  def dfs(x, y):
    if grid[y][x] == '9':
      yield (x,y)
    goal = str(int(grid[y][x]) + 1)
    for dx, dy in DIRS_4:
      if 0 <= x+dx < m and 0 <= y+dy < n and grid[y+dy][x+dx] == goal:
        yield from dfs(x+dx, y+dy)

  total = 0
  for y, row in enumerate(grid):
    for x, ch in enumerate(row):
      if ch == '0':
        total += len((set,list)[part](dfs(x,y)))
  return total


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(36, solve(part=0, file='input-test-1'))
  test(820, solve(part=0, file='input-real'))

  test(81, solve(part=1, file='input-test-1'))
  test(1786, solve(part=1, file='input-real'))
