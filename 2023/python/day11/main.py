#!/usr/bin/env python3

from common.util import *

from bisect import bisect

def solve(dist, file):
  data = load(file)

  ys = [y for y, line in enumerate(data) if '#' not in line]
  xs = [x for x, col in enumerate(zip(*data)) if '#' not in col]

  galaxies = []
  for y, row in enumerate(data):
    for x, ch in enumerate(row):
      if ch == '#':
        x1 = x + (dist-1) * bisect(xs, x)
        y1 = y + (dist-1) * bisect(ys, y)
        galaxies.append((x1, y1))
  
  return sum(abs(x1-x2) + abs(y1-y2) for (x1,y1),(x2,y2) in combinations(galaxies, 2))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(374, solve(dist=2, file='input-test-1'))
  test(9799681, solve(dist=2, file='input-real'))

  test(1030, solve(dist=10, file='input-test-1'))
  test(8410, solve(dist=100, file='input-test-1'))
  test(513171773355, solve(dist=1000000, file='input-real'))
