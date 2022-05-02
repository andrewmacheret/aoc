#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  grid = load_grid(file)
  x, y, dx, dy, path = grid[0].index('|'), 0, 0, 1, []
  while grid[y][x] != ' ':
    path.append(grid[(y := y + dy)][(x := x + dx)])
    if grid[y][x] == '+':
      dx, dy = (dy, dx) if grid[y+dx][x+dy] != ' ' else (-dy, -dx)
  return len(path) if part else ''.join(filter(str.isalpha, path))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test('ABCDEF', solve(part=0, file='input-test-1'))
  test('PVBSCMEQHY', solve(part=0, file='input-real'))

  test(38, solve(part=1, file='input-test-1'))
  test(17736, solve(part=1, file='input-real'))
