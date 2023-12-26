#!/usr/bin/env python3

from heapq import * 

from common.util import *


def dijk(start, expand, is_goal):
  seen = defaultdict(lambda: inf, {start: 0})
  q = [(0, start)]
  while q:
    val, item = heappop(q)
    if is_goal(*item):
      return val
    for cost, y in expand(*item):
      val2 = cost + val
      if seen[y] > val2:
        seen[y] = val2
        heappush(q, (val2, y))


def solve(part, file):
  grid = [[int(c) for c in line] for line in load(file)]
  n, m = len(grid), len(grid[0])

  start = (0,0,1,0,0) # x, y, dx, dy, last count
  
  def is_goal(x,y,ldx,ldy,lc):
    return (x,y) == (m-1,n-1) and (part == 0 or lc >= 4)
  
  def expand(x,y,ldx,ldy,lc):
    for dx,dy,lc1 in [(ldy,ldx,1),(-ldy,-ldx,1),(ldx,ldy,lc+1)]: # left, right, straight
      if (0 <= (x1 := x+dx) < m and 0 <= (y1 := y+dy) < n) and \
         (not lc or (not (part == 0 and (dx, dy) == (ldx, ldy) and lc == 3) \
                  and not (part == 1 and (dx, dy) == (ldx, ldy) and lc == 10) \
                  and not (part == 1 and (dx, dy) != (ldx, ldy) and lc < 4))):
        yield grid[y1][x1], (x1,y1,dx,dy,lc1)
  
  return dijk(start, expand, is_goal)



### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(102, solve(part=0, file='input-test-1'))
  test(742, solve(part=0, file='input-real'))

  test(94, solve(part=1, file='input-test-1'))
  test(71, solve(part=1, file='input-test-2'))
  test(918, solve(part=1, file='input-real'))
