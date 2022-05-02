#!/usr/bin/env python3

from common.util import *


def solve(part, file, steps):
  grid = defaultdict(int, {
      x+y*1j: 2 for (x, y), c in load_grid_dict(file).items() if c == '#'})
  z = complex(n := len(load(file)) // 2, n)

  count = 0
  dz = -1j
  for _ in range(steps):
    dz = ((-1j).__mul__, pos, (+1j).__mul__, neg)[grid[z]](dz)
    grid[z] = (grid[z] + 2 - part) % 4
    count += grid[z] == 2
    z += dz

  return count


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(41, solve(part=0, file='input-test-1', steps=70))
  test(5587, solve(part=0, file='input-test-1', steps=10000))
  test(5256, solve(part=0, file='input-real', steps=10000))

  test(26, solve(part=1, file='input-test-1', steps=100))
  test(2511944, solve(part=1, file='input-test-1', steps=10000000))
  test(2511345, solve(part=1, file='input-real', steps=10000000))
