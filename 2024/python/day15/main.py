#!/usr/bin/env python3

# import networkx as nx
# import numpy as np
# from copy import copy, deepcopy
# import sys
# sys.setrecursionlimit(100000)

from common.util import *

dirs = {
  '<': (-1, 0),
  '>': (1, 0),
  '^': (0, -1),
  'v': (0, 1),
}

def solve(part, file):
  # data = load_ints(file)
  # data = load_custom(file)
  # data = load_blocks(file)
  # data = load_csv(file)
  g, m = load_blocks(file)
  grid = parse_grid(g)
  m = list(''.join(m))

  grid2 = []
  for y in range(len(grid)):
    grid2.append([])
    for x in range(len(grid[y])):
      if grid[y][x] == '@':
        grid2[y].append('@')
        grid2[y].append('.')
      elif grid[y][x] == '#':
        grid2[y].append('#')
        grid2[y].append('#')
      elif grid[y][x] == '.':
        grid2[y].append('.')
        grid2[y].append('.')
      elif grid[y][x] == 'O':
        grid2[y].append('[')
        grid2[y].append(']')
  grid = grid2

  sx, sy = 0, 0
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x] == '@':
        sx, sy = x, y
        break

  # for mov in m:
  #   dx, dy = dirs[mov]
  #   x1 = sx + dx
  #   y1 = sy + dy
  #   if grid[y1][x1] == '#':
  #     continue
  #   if grid[y1][x1] == '.':
  #     grid[sy][sx] = '.'
  #     grid[y1][x1] = '@'
  #     sx, sy = x1, y1
  #     continue
  #   for i in count(1):
  #     x2 = sx + dx * i
  #     y2 = sy + dy * i
  #     if grid[y2][x2] == '#':
  #       break
  #     if grid[y2][x2] == '.':
  #       grid[y2][x2] = 'O'
  #       grid[y1][x1] = '@'
  #       grid[sy][sx] = '.'
  #       sx, sy = x1, y1
  #       break

  for mov in m:
    # print(mov)
    # print(draw_grid(grid))
    dx, dy = dirs[mov]
    x1 = sx + dx
    y1 = sy + dy
    if grid[y1][x1] == '#':
      continue
    if grid[y1][x1] == '.':
      grid[sy][sx] = '.'
      grid[y1][x1] = '@'
      sx, sy = x1, y1
      continue
    
    q = [{(sx,sy)}]
    doit = False
    for i in count():
      print(q)
      if any(grid[y+dy][x+dx] == '#' for x,y in q[-1]):
        break
      if all(grid[y+dy][x+dx] == '.' for x,y in q[-1]):
        doit = True
        break
      new = set()
      if dy == 0:
        for x,y in q[-1]:
          if grid[y+dy][x+dx] in '[]':
            new.add((x+dx, y+dy))
      else:
        for x,y in q[-1]:
          if grid[y+dy][x+dx] == '[':
            new.add((x+dx, y+dy))
            new.add((x+dx+1, y+dy))
          elif grid[y+dy][x+dx] == ']':
            new.add((x+dx, y+dy))
            new.add((x+dx-1, y+dy))
      q.append(new)
    if doit:
      while q:
        for x,y in q.pop():
          grid[y+dy][x+dx] = grid[y][x]
          grid[y][x] = '.'
      # grid[sy][sx] = '.'
      sx, sy = sx+dx, sy+dy

  total = 0
  for y, row in enumerate(grid):
    for x, ch in enumerate(row):
      if ch == '[':
        total += y*100 + x
  # print(draw_grid(grid))
      
  


  #print(data)
  return total


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  # test(None, solve(part=0, file='input-test-1'))
  # test(None, solve(part=0, file='input-real'))

  test(None, solve(part=1, file='input-test-1'))
  test(None, solve(part=1, file='input-real'))
