#!/usr/bin/env python3

from common.util import *

def solve(part, file):
  grid = load_grid(file)

  def dijk(start, expand, is_goal):
    best_val = inf
    seen = defaultdict(lambda: inf, {start: 0})
    q = [(0, start, [start])]
    best = set()
    while q:
      val, x, path = heappop(q)
      if is_goal(x) and best_val >= val:
        if part == 0:
          return val
        best_val = val
        for y in path:
          best.add((y[0], y[1]))
      for cost, y in expand(x):
        if seen[y] >= (val2 := cost + val) <= best_val:
          seen[y] = val2
          heappush(q, (val2, y, path + [y]))
    
    return len(best)

  start = next((x,y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == 'S')
  end = next((x,y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == 'E')
  start = (start[0], start[1], 1,0)


  def is_goal(z):
    x,y,*_ = z
    return (x,y) == end

  def expand(z):
    x,y,dx,dy = z
    if grid[y+dy][x+dx] in '.E':
      yield 1, (x+dx, y+dy, dx, dy)
    for dx1, dy1 in [(dy,dx), (-dy,-dx)]:
      if grid[y+dy1][x+dx1] in '.E':
        yield 1001, (x+dx1, y+dy1, dx1, dy1)

  return dijk(start, expand, is_goal)



### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(7036, solve(part=0, file='input-test-1'))
  test(90460, solve(part=0, file='input-real'))

  test(45, solve(part=1, file='input-test-1'))
  test(575, solve(part=1, file='input-real'))
