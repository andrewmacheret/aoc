#!/usr/bin/env python3

from itertools import permutations
import re

from common.util import load, test, change_dir


def solve(part, file):
  data = load(file)
  grid = {}
  for line in data[2:]:
    pattern = r'/dev/grid/node-x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T +(\d+)%'
    x, y, size, used, avail, percent = map(
        int, re.fullmatch(pattern, line).groups())
    grid[x, y] = (size, used, avail, percent)

  space_x, space_y = next((x, y) for x, y in grid if grid[x, y][1] == 0)
  too_big = set(grid) - {(space_x, space_y)} \
      - {(x, y) for x, y in grid
         if 0 < grid[x, y][1] <= grid[space_x, space_y][2]}
  barrier_x = {x for x, _ in too_big}
  opening_x = next(x for x in range(space_x, -1, -1) if x not in barrier_x)
  goal_x = max(x for x, _ in grid)

  if part == 1:
    return sum(0 < a[1] <= b[2] for a, b in permutations(grid.values(), 2))
  else:
    return 2*(space_x-opening_x) + space_y + (goal_x - space_x) + 5*(goal_x-1)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(7, solve(part=1, file='input-test-1'))
  test(910, solve(part=1, file='input-real'))

  test(7, solve(part=2, file='input-test-1'))
  test(222, solve(part=2, file='input-real'))
