#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  data = load_grid(file)
  n = len(data)
  m = len(data[0])

  nodes = defaultdict(list)
  for y, row in enumerate(data):
    for x, ch in enumerate(row):
      if ch != '.':
        nodes[ch].append((x, y))
  
  anti = set()
  for v in nodes.values():
    for (x1,y1),(x2,y2) in permutations(v, 2):
      dx = x2-x1
      dy = y2-y1

      if part == 0:
        if 0 <= (x3 := (x1 - dx)) < m and 0 <= (y3 := (y1 - dy)) < n:
          anti.add((x3, y3))
        if 0 <= (x3 := (x2 + dx)) < m and 0 <= (y3 := (y2 + dy)) < n:
          anti.add((x3, y3))

      else:
        g = gcd(dx,dy)
        dx //= g
        dy //= g

        anti.add((x1, y1))

        i = 1
        while 0 <= (x3 := (x1 + i*dx)) < m and 0 <= (y3 := (y1 + i*dy)) < n:
          anti.add((x3, y3))
          i += 1
        i = 1
        while 0 <= (x3 := (x1 - i*dx)) < m and 0 <= (y3 := (y1 - i*dy)) < n:
          anti.add((x3, y3))
          i += 1

  return len(anti)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(14, solve(part=0, file='input-test-1'))
  test(367, solve(part=0, file='input-real'))

  test(9, solve(part=1, file='input-test-2'))
  test(34, solve(part=1, file='input-test-1'))
  test(1285, solve(part=1, file='input-real'))
