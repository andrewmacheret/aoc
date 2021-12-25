#!/usr/bin/env python3

from itertools import count

from common.util import load, test, change_dir


def solve(file):
  data = load(file)
  n, m = len(data), len(data[0])
  grid = {(x, y): data[y][x] for y in range(n) for x in range(m)
          if data[y][x] != '.'}

  for r in count(1):
    moved = 0
    for dx, dy, c in ((1, 0, '>'), (0, 1, 'v')):
      moves = [(x, y) for x, y in grid
               if grid[x, y] == c
               and ((x+dx) % m, (y+dy) % n) not in grid]
      moved = moved or len(moves)
      for x, y in moves:
        del grid[x, y]
        grid[(x + dx) % m, (y+dy) % n] = c
    if not moved:
      return r


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(58, solve(file='input-test-1'))
  test(471, solve(file='input-real'))
