#!/usr/bin/env python3

# import networkx as nx
# import numpy as np
# from copy import copy, deepcopy
# import sys
# sys.setrecursionlimit(100000)

from common.util import *


def solve(part, file):
  # data = load_ints(file)
  # data = load_custom(file)
  # data = load_blocks(file)
  # data = load_csv(file)
  data = load_grid(file)

  def dfs(ch, x,y, seen):
    if (x,y) in seen:
      return 0, 0
    
    if data[y][x] != ch:
      return 0, 1 # area, perim
    
    seen.add((x,y))
    data[y][x] = '.'

    area = 1
    perim = 0
    for dx,dy in DIRS_4:
      x1, y1 = x+dx, y+dy
      if 0 <= x1 < len(data[0]) and 0 <= y1 < len(data):
        a,p = dfs(ch, x1, y1, seen)
        area += a
        perim += p
      else:
        perim += 1
    return area, perim

  def dfs2(ch, x,y, seen, idx,idy):
    if (x,y) in seen:
      return 0, []
    
    if data[y][x] != ch:
      return 0, [(x,y,idx,idy)] # area, perim
    
    seen.add((x,y))
    data[y][x] = '.'

    area = 1
    perim = []
    for dx,dy in DIRS_4:
      x1, y1 = x+dx, y+dy
      if 0 <= x1 < len(data[0]) and 0 <= y1 < len(data):
        a,p = dfs2(ch, x1, y1, seen,dx,dy)
        area += a
        for p in p:
          perim.append(p)
      else:
        perim.append((x1,y1,dx,dy))
    return area, perim

  total = 0
  done = {}
  for y, row in enumerate(data):
    for x, ch in enumerate(row):
      if data[y][x] != '.':
        area, perim = dfs2(ch, x, y, set(), 0, 0)

        # print(perim)
        sides = 0
        while perim:
          sides += 1
          x1,y1,dx,dy = next(iter(perim))
          perim.remove((x1,y1,dx,dy))
          # print('start removed', x1,y1,dx,dy)
          x2,y2 = x1, y1
          dx1,dy1 = dy,dx
          # print('trying in dir', dx1,dy1, 'vals', x2+dx1, y2+dy1)
          while (x2+dx1,y2+dy1,dx,dy) in perim:
            x2,y2 = x2+dx1, y2+dy1
            perim.remove((x2,y2,dx,dy))
            # print('removed', x2,y2,dx,dy)
          x2,y2 = x1, y1
          # print('trying in dir', dx1,dy1, 'vals', x2-dx1, y2-dy1)
          while (x2-dx1,y2-dy1,dx,dy) in perim:
            x2,y2 = x2-dx1, y2-dy1
            perim.remove((x2,y2,dx,dy))
            # print('removed', x2,y2,dx,dy)
          



        done[ch] = [area, sides]

        print(ch, area, sides)
        total += area * sides



  #print(data)
  return total


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  # test(140, solve(part=0, file='input-test-1'))
  # test(772, solve(part=0, file='input-test-2'))
  # test(1483212, solve(part=0, file='input-real'))

  test(None, solve(part=1, file='input-test-1'))
  test(None, solve(part=1, file='input-test-2'))
  test(None, solve(part=1, file='input-real'))
