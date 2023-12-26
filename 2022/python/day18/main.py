#!/usr/bin/env python3

from common.util import *

import sys
sys.setrecursionlimit(100000)


def dirs3d(x, y, z):
  return [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]


def solve(part, file):
  cubes = {tuple(map(int, line.split(','))): 1 for line in load(file)}

  if part == 0:
    return len(cubes)*6 - sum(xyz1 in cubes for xyz in cubes for xyz1 in dirs3d(*xyz))

  lo_x, lo_y, lo_z = map((-1).__add__, map(min, zip(*cubes)))
  hi_x, hi_y, hi_z = map((+1).__add__, map(max, zip(*cubes)))

  def exposed(*xyz):
    if not (lo_x <= xyz[0] <= hi_x and lo_y <= xyz[1] <= hi_y and lo_z <= xyz[2] <= hi_z):
      return 0
    if xyz in cubes:
      return cubes[xyz]
    cubes[xyz] = 0
    return sum(exposed(*xyz1) for xyz1 in dirs3d(*xyz))

  return exposed(lo_x, lo_y, lo_z)  # lo_x,lo_y,lo_z must not be in cubes


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(64, solve(part=0, file='input-test-1'))
  test(10, solve(part=0, file='input-test-2'))
  test(3454, solve(part=0, file='input-real'))

  test(58, solve(part=1, file='input-test-1'))
  test(10, solve(part=1, file='input-test-2'))
  test(2014, solve(part=1, file='input-real'))
