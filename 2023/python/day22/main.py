#!/usr/bin/env python3

from bisect import *

from common.util import *


def load_bricks(file):
  bricks = []
  for line in load(file):
    x1,y1,z1,x2,y2,z2 = parse_nums(line)
    insort(bricks, ((x1, x2), (y1, y2), (z1, z2)), key=lambda b: b[2])
  return bricks

def overlap(brick1, brick2):
  (ax1, ax2), (ay1, ay2), _ = brick1
  (bx1, bx2), (by1, by2), _ = brick2
  return not (bx2 < ax1 or bx1 > ax2 or by2 < ay1 or by1 > ay2)

def drop(bricks):
  tower = []
  for brick in bricks:
    max_z = max((top[2][1] for top in reversed(tower) if overlap(brick, top)), default=0)
    if (dz := brick[2][0] - max_z - 1):
      brick = (brick[0], brick[1], (brick[2][0] - dz, brick[2][1] - dz))
    insort(tower, brick, key=lambda b: b[2])
  return tower

def count_supported(tower):
  # build a graph of supported bricks
  supported_by = defaultdict(set)
  for (i,brick1), (j,brick2) in permutations(enumerate(tower), 2):
    if brick1[2][0] == brick2[2][1] + 1 and overlap(brick1, brick2):
      supported_by[i].add(j)
  # go through each brick in the tower
  for i in range(len(tower)):
    # try dropping brick i
    dropped = {i}
    for j in range(i+1, len(tower)):
      # if brick j is supported by only bricks that are dropped, drop it too
      if supported_by[j] and not (supported_by[j] - dropped):
        dropped.add(j)
    # return number of dropped bricks (exclude current brick)
    yield len(dropped) - 1


def solve(part, file):
  bricks = load_bricks(file)  
  tower = drop(bricks)
  return sum([not x, x][part] for x in count_supported(tower))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(5, solve(part=0, file='input-test-1'))
  test(459, solve(part=0, file='input-real'))

  test(7, solve(part=1, file='input-test-1'))
  test(75784, solve(part=1, file='input-real'))
