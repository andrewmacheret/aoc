#!/usr/bin/env python3

import sys
sys.setrecursionlimit(100000)

from common.util import *

def solve(part, file):
  data = load(file)
  n, m = len(data), len(data[0])
  grid = parse_dict(data)

  def energized(x,y,dx,dy):
    seen = set()
    def LAZERZ(x, y, dx, dy):
      x, y = x + dx, y + dy
      if (x,y) not in grid or (x,y,dx,dy) in seen: return
      seen.add((x,y,dx,dy))
      ch = grid[x,y]
      if ch in '/':
        dx, dy = -dy, -dx
      elif ch in '\\':
        dx, dy = dy, dx
      elif (ch == '|' and dy == 0) or (ch == '-' and dx == 0):
        LAZERZ(x, y, dy, dx)
        LAZERZ(x, y, -dy, -dx)
        return
      LAZERZ(x, y, dx, dy)
    LAZERZ(x, y, dx, dy)
    return len({(x,y) for x,y,_,_ in seen})
  
  if part == 0:
    return energized(-1,0, *RIGHT)
  else:
    return max(
      *(energized(-1,y,*RIGHT) for y in range(n)),
      *(energized(n,y,*LEFT) for y in range(n)),
      *(energized(x,-1,*DOWN) for x in range(m)),
      *(energized(x,m,*UP) for x in range(m))
    )

### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(46, solve(part=0, file='input-test-1'))
  test(8146, solve(part=0, file='input-real'))
  
  test(51, solve(part=1, file='input-test-1'))
  test(8358, solve(part=1, file='input-real'))
