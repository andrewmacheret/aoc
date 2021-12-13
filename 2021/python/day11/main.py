#!/usr/bin/env python3

from common.util import load, test, change_dir, DIRS_8


def solve(steps, file):
  data = load(file)
  grid = [[int(c) for c in x] for x in data]
  n, m = len(grid), len(grid[0])
  flashes = 0

  def flash(q, x, y):
    grid[y][x] = (grid[y][x] + 1) % 10
    if not grid[y][x]:
      for dx, dy in DIRS_8:
        if 0 <= y+dy < n and 0 <= x+dx < m:
          q += (x+dx, y+dy),
    return not grid[y][x]

  for round in range(1, (steps or 999)+1):
    q = []
    for x in range(m):
      for y in range(n):
        flashes += flash(q, x, y)
    while q:
      x, y = q.pop()
      if grid[y][x]:
        flashes += flash(q, x, y)
    if set(x for row in grid for x in row) == {0}:
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
