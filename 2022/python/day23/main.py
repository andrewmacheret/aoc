#!/usr/bin/env python3

from common.util import *

DIRS_8 = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if not (x == y == 0)]

DIRS_N = ([(x, y) for x in (-1, 0, 1) for y in (-1,)], (0, -1))
DIRS_S = ([(x, y) for x in (-1, 0, 1) for y in (+1,)], (0, +1))
DIRS_W = ([(x, y) for x in (-1,) for y in (-1, 0, 1)], (-1, 0))
DIRS_E = ([(x, y) for x in (+1,) for y in (-1, 0, 1)], (+1, 0))


def load_grid_set(data):
  return {(x, y) for y, row in enumerate(data) for x, val in enumerate(row) if val == '#'}


def solve(part, file):
  grid = load_grid_set(load(file))

  DIRS_4D = deque([DIRS_N, DIRS_S, DIRS_W, DIRS_E])
  for r in [range(10), count(1)][part]:
    last = set(grid)
    proposed = defaultdict(list)
    for x, y in grid:
      if any((x+dx, y+dy) in grid for dx, dy in DIRS_8):
        for DIR, dxy in DIRS_4D:
          if all((x+dx, y+dy) not in grid for dx, dy in DIR):
            dx, dy = dxy
            proposed[(x+dx, y+dy)].append((x, y))
            break

    for x1, y1 in proposed:
      if len(proposed[(x1, y1)]) == 1:
        x, y = proposed[(x1, y1)][0]
        grid.remove((x, y))
        grid.add((x1, y1))

    DIRS_4D.append(DIRS_4D.popleft())

    if last == grid:
      return r

  Mx = max(x for x, y in grid)
  My = max(y for x, y in grid)
  mx = min(x for x, y in grid)
  my = min(y for x, y in grid)
  return ((((Mx-mx)+1)) * ((My-my)+1) - len(grid))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(110, solve(part=0, file='input-test-1'))
  test(4109, solve(part=0, file='input-real'))

  test(20, solve(part=1, file='input-test-1'))
  test(1055, solve(part=1, file='input-real'))
