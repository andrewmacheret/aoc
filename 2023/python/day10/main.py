#!/usr/bin/env python3

import sys
sys.setrecursionlimit(100000)

from common.util import *

UP    = (0,-1)
DOWN  = (0, 1)
LEFT  = (-1,0)
RIGHT = ( 1,0)
DIRS_4 = (UP, DOWN, LEFT, RIGHT)
mapping = {
  '-' : (LEFT, RIGHT),
  '|' : (UP,DOWN),
  'J' : (LEFT, UP),
  'L' : (RIGHT, UP),
  '7' : (LEFT, DOWN),
  'F' : (RIGHT, DOWN),
  '.' : (),
  '#' : (),
}

def solve(part, file):
  data = load(file)
  grid = parse_dict(data)

  # calculate start
  start = next((x,y) for (x,y),char in grid.items() if char == 'S')
  
  # dfs function to find the longest path
  def dfs(x,y):
    if (x,y) not in grid or grid[x,y] == '.':
      return 0
    c = grid[x,y]
    grid[x,y] = '#'
    m = 0
    if c == 'S':
      m = max(dfs(x+dx, y+dy) for dx,dy in DIRS_4 if (-dx,-dy) in mapping[grid[x+dx, y+dy]])
    elif mapping[c]:
      for dx,dy in mapping[c]:
        m = max(m, dfs(x+dx, y+dy))
    return 1 + m

  # part 1 - return half of the length of the path
  if part == 0:
    return dfs(start[0], start[1]) // 2
  
  # redraw the grid with extra spacing (horizontal pipes and vertical pipes)
  data2 = []
  for line in data:
    data2.append('-'.join(line))
    data2.append('|' * (len(line) * 2 - 1))
  grid = parse_dict(data2)
  
  # recalculate start
  start = next((x,y) for (x,y),char in grid.items() if char == 'S')

  # dfs again to fill path with '#' 
  dfs(*start)

  # dfs function to fill with letters
  # and keep track of bad letters that go out of bounds
  bad = set()
  def dfs_fill(x,y,fill):
    if (x,y) not in grid:
      return bad.add(fill)
    c = grid[x,y]
    if c != fill and c != '#':
      grid[x,y] = fill
      dfs_fill(x+1,y, fill),
      dfs_fill(x-1,y, fill),
      dfs_fill(x,y+1, fill),
      dfs_fill(x,y-1, fill)

  # fill corners with letters
  for fill,(dx,dy) in zip('ABCD', product((-1, 1), repeat=2)):
    dfs_fill(start[0]+dx, start[1]+dy, fill)

  # there should be only two letters, inside (good) and outside (bad)
  # count the good letters and return
  res = 0
  for (x,y), ch in grid.items():
    if x % 2 == 0 and y % 2 == 0 and ch in 'ABCD' and ch not in bad:
      res += 1
  return res


### THE REST IS TESTS ###

if __name__ == "__main__":

  change_dir(__file__)
  

  test(4, solve(part=0, file='input-test-1'))
  test(6812, solve(part=0, file='input-real'))

  test(527, solve(part=1, file='input-real'))
