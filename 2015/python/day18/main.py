#!/usr/bin/env python3


from common.util import load_grid_dict, DIRS_8, test, change_dir


def step(grid, max_x=None, max_y=None):
  res = {}
  for x, y in grid:
    count = sum(grid.get((x+dx, y+dy), '.') == '#' for dx, dy in DIRS_8)
    if max_x is not None and max_y is not None and x in {0, max_x} and y in {0, max_y}:
      res[x, y] = '#'
    elif grid[x, y] == '#':
      res[x, y] = '.#'[count in {2, 3}]
    else:
      res[x, y] = '.#'[count == 3]
  return res


def solve(part, steps, file):
  grid = load_grid_dict(file)
  max_x = max_y = None
  if part == 2:
    max_x = max(x for x, _ in grid)
    max_y = max(y for _, y in grid)
    grid[0, 0] = grid[0, max_y] = grid[max_x, 0] = grid[max_x, max_y] = '#'
  for _ in range(steps):
    grid = step(grid, max_x, max_y)
  return sum(x == '#' for x in grid.values())


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(4, solve(part=1, steps=4, file='input-test-1'))
  test(814, solve(part=1, steps=100, file='input-real'))

  test(14, solve(part=2, steps=4, file='input-test-1'))
  test(924, solve(part=2, steps=100, file='input-real'))  # not 861
