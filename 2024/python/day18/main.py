#!/usr/bin/env python3

from common.util import *
from bisect import bisect

def solve(part, file, size, count):
  drops = [*map(tuple, map(parse_nums, load(file)))]

  def bfs(grid):
    seen = set()
    q = deque([(0, 0, 0)])
    while q:
      c, x, y = q.popleft()
      if (x,y) in seen:
        continue
      seen.add((x,y))
      if (x,y) == (size-1, size-1):
        return c
      for dx, dy in DIRS_4:
        if 0<=x+dx<size and 0<=y+dy<size and (x+dx, y+dy) not in grid:
          q.append((c+1, x+dx, y+dy))
    return -1
  
  if part == 0:
    return bfs(set(drops[:count]))
  else:
    class Search: __getitem__ = lambda _, i: bfs(set(drops[:i])) == -1
    return drops[bisect(Search(), 0, 0, len(drops)) - 1]

### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(22, solve(part=0, size=7, count=12, file='input-test-1'))
  test(380, solve(part=0, size=71, count=1024, file='input-real'))

  test((6,1), solve(part=1, file='input-test-1', size=7, count=inf))
  test((26,50), solve(part=1, file='input-real', size=71, count=inf))
