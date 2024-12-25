#!/usr/bin/env python3

from common.util import *

def solve(part, file):
  objs = [[], []]
  for block in load_blocks(file):
    grid = list(zip(*parse_grid(block)))
    objs[grid[0][0] == '#'].append(tuple(r.count('#') for r in grid))
  
  total = 0
  for lock in objs[0]:
    for key in objs[1]:
      if all(map((7).__ge__, map(sum, zip(lock, key)))):
        total += 1
  return total


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(3, solve(part=0, file='input-test-1'))
  test(3301, solve(part=0, file='input-real'))
