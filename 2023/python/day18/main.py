#!/usr/bin/env python3

from common.util import *

def shoelace(path):
  perim = area = 0
  for (x1,y1),(x2,y2) in pairwise(path):
    perim += abs(x2-x1) + abs(y2-y1)
    area += x2 * (y2-y1)
  return area + perim//2 + 1

def solve(part, file):
  x,y = 0,0
  path = [(0,0)]
  for line in load(file):
    d,length,color = line.split(' ')
    if part == 0:
      length = int(length)
      dx, dy = {'R': RIGHT, 'U': UP, 'L': LEFT, 'D': DOWN}[d]
    else:
      length = int(color[2:-2], 16)
      dx, dy = [RIGHT, DOWN, LEFT, UP][int(color[-2])]
    x += dx * length
    y += dy * length
    path.append((x,y))

  return shoelace(path)

### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(62, solve(part=0, file='input-test-1'))
  test(68115, solve(part=0, file='input-real'))

  test(952408144115, solve(part=1, file='input-test-1'))
  test(71262565063800, solve(part=1, file='input-real'))
