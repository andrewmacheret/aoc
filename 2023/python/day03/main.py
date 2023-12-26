#!/usr/bin/env python3


from common.util import *


def solve(part, file):
  data = load(file)
  
  grid = {(x,y): val for y, row in enumerate(data) for x, val in enumerate(row)}
  grid = defaultdict(lambda: '.', grid)

  width = len(data[0])

  res = defaultdict(list)

  for x,y in grid:
    if grid[x,y].isdigit():
      for dx, dy in DIRS_8:
        if (x+dx, y+dy) in grid:
          c = grid[x + dx, y + dy]
          # if it's a symbol
          if c != '.' and not c.isdigit():
            # find the beginning and end of the number
            x1 = x2 = x
            while x1 > 0 and grid[x1-1, y].isdigit():
              x1 -= 1
            while x2 + 1 < width and grid[x2+1, y].isdigit():
              x2 += 1
            # get the number
            val = int(''.join(grid[x3, y] for x3 in range(x1, x2+1)))
            # save the symbol -> result mapping
            res[(x+dx, y+dy)].append(val)
            # remove the number from the grid
            for x3 in range(x1, x2+1):
              grid[x3, y] = '.'

  if part == 0:
    return sum(x for v in res.values() for x in v)
  else:
    return sum(mul(*v) for v in res.values() if len(v) == 2)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(4361, solve(part=0, file='input-test-1'))
  test(529618, solve(part=0, file='input-real'))

  test(467835, solve(part=1, file='input-test-1'))
  test(77509019, solve(part=1, file='input-real'))
