#!/usr/bin/env python3

from common.util import *

# this works but is kinda slow
# def tilt_n(grid):
#   n = len(grid)
#   for _ in range(n):
#     for x in range(n):
#       for y in range(n-1):
#         if grid[y][x] == '.' and grid[y+1][x] == 'O':
#           grid[y][x] = 'O'
#           grid[y+1][x] = '.'

def tilt_n(grid):
  n = len(grid)
  for x in range(n):
    last_open = None
    for y in range(n):
      if grid[y][x] == '.' and last_open is None:
        last_open = y
      elif grid[y][x] == '#':
        last_open = None
      elif grid[y][x] == 'O' and last_open is not None:
        grid[last_open][x] = 'O'
        grid[y][x] = '.'
        last_open += 1

def solve(part, file):
  data = load(file)
  grid = [[*line] for line in data]

  if part == 0:
    tilt_n(grid)
  else:
    initial = tuples(grid)
    def simulate():
      nonlocal grid
      for _ in range(4):
        tilt_n(grid)
        grid[:] = rotate_clock(grid)
      return tuples(grid)
    run_with_cycles(initial, simulate, 1000000000)

  return sum(len(data) - y \
             for y, line in enumerate(grid) \
             for ch in line if ch == 'O')

### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(136, solve(part=0, file='input-test-1'))
  test(106378, solve(part=0, file='input-real'))

  test(64, solve(part=1, file='input-test-1'))
  test(90795, solve(part=1, file='input-real'))
