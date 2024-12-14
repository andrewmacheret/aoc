#!/usr/bin/env python3

from common.util import *


def solve(part, file, w, h):
  bots = [list(parse_nums(line)) for line in load(file)]
  
  for i in count(1):
    for j in range(len(bots)):
      px,py,vx,vy = bots[j]
      bots[j][0] = (px + vx) % w
      bots[j][1] = (py + vy) % h
    
    if part:
      grid = [['.' for _ in range(w)] for _ in range(h)]
      for px,py,vx,vy in bots:
        grid[py][px] = '#'
      for line in grid:
        if '#' * 20 in ''.join(line):
          print(draw_grid(grid))
          return i
    elif i == 100:
      q= [0,0,0,0]
      for px,py,vx,vy in bots:
        if px < w // 2 and py < h // 2:
          q[0] += 1
        elif px > w // 2 and py < h // 2:
          q[1] += 1
        elif px < w // 2 and py > h // 2:
          q[2] += 1
        elif px > w // 2 and py > h // 2:
          q[3] += 1
      return q[0]*q[1]*q[2]*q[3]


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(12, solve(part=0, w=11, h=7, file='input-test-1'))
  test(218619120, solve(part=0, w=101, h=103, file='input-real'))

  test(7055, solve(part=1, w=101, h=103, file='input-real'))
