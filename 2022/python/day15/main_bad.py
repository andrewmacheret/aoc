#!/usr/bin/env python3

# import networkx as nx
# import numpy as np
# from copy import copy, deepcopy
# import sys
# sys.setrecursionlimit(100000)

from common.util import *


def parse_nums(line):
  return [*map(int, re.findall(r'[+-]?\d+', line))]


def load_custom(file):
  return [line.split(',') for line in load(file)]


def solve(part, file, goal_y):
  # data = load_ints(file)
  # data = load_custom(file)
  # data = load_blocks(file)
  # data = load_csv(file)
  data = load(file)
  beacons = set()
  sensors = {}
  i = 0
  for line in data:
    sx, sy, bx, by = parse_nums(line)
    sensors[sx, sy] = (bx, by)
    beacons.add((bx, by))
    i += 1

  # sensors = {}
  # sensors[8, 7] = (2, 10)
  # sensors[(17, 20)] = (21, 22)
  # print(sensors)

  intervals = []
  for (sx, sy), (bx, by) in sensors.items():
    dx = abs(sx - bx)
    h = abs(sy - by)
    h2 = abs(sy - goal_y)
    lo = (sx - dx - h + h2)
    hi = (sx + dx + h - h2)
    print(lo, hi)
    if lo <= hi:
      if by == goal_y:
        if bx < sx:
          # print('1')
          intervals.append((lo+1, hi+1))
        elif bx > sx:
          # print('2')
          intervals.append((lo, hi))
      elif sy == goal_y:
        # print('3')
        intervals.append((lo, sx))
        intervals.append((sx+1, hi+1))
      else:
        # print('4')
        intervals.append((lo, hi+1))
      # print((sx, sy), (bx, by), 'is', intervals[-1], '...', sx, dx, h, h2)

  intervals.sort()
  # print(intervals)

  for i in range(len(intervals)-1):
    if intervals[i][1] > intervals[i+1][0]:
      intervals[i] = (intervals[i][0], intervals[i+1][0])
  return sum(b-a for a, b in intervals)
  # total = 0
  # last = -inf
  # for x1, x2 in intervals:
  #   x1 = max(last, x1)
  #   if x1 < x2:
  #     total += x2 - x1
  #   last = max(x2-1, last)
  # return total

  #

  # print(data)


### THE REST IS TESTS ###


# 0 35
# 1 70
# 2 103
# 3 133
# 4 162
# 5 189
# 6 214
# 7 237
# 8 260
# 9 285

if __name__ == "__main__":
  change_dir(__file__)

  test(0, solve(part=0, file='input-test-1', goal_y=-11))
  test(1, solve(part=0, file='input-test-1', goal_y=-10))
  test(3, solve(part=0, file='input-test-1', goal_y=-9))
  test(5, solve(part=0, file='input-test-1', goal_y=-8))
  test(7, solve(part=0, file='input-test-1', goal_y=-7))
  test(10, solve(part=0, file='input-test-1', goal_y=-6))
  # test(14, solve(part=0, file='input-test-1', goal_y=-5))
  # test(18, solve(part=0, file='input-test-1', goal_y=-4))
  # test(22, solve(part=0, file='input-test-1', goal_y=-3))
  # test(26, solve(part=0, file='input-test-1', goal_y=-2))
  # test(31, solve(part=0, file='input-test-1', goal_y=-1))
  # test(35, solve(part=0, file='input-test-1', goal_y=0))
  # test(35, solve(part=0, file='input-test-1', goal_y=1))
  # test(33, solve(part=0, file='input-test-1', goal_y=2))
  # test(30, solve(part=0, file='input-test-1', goal_y=3))
  # test(29, solve(part=0, file='input-test-1', goal_y=4))
  # test(27, solve(part=0, file='input-test-1', goal_y=5))
  # test(25, solve(part=0, file='input-test-1', goal_y=6))
  # test(23, solve(part=0, file='input-test-1', goal_y=7))
  # test(23, solve(part=0, file='input-test-1', goal_y=8))
  # test(25, solve(part=0, file='input-test-1', goal_y=9))
  # test(26, solve(part=0, file='input-test-1', goal_y=10))

  # test(5870800, solve(part=0, file='input-real', goal_y=2000000))
  # 4203411 is too low
  # 4710605 is too low

  # test(None, solve(part=1, file='input-test-1'))
  # test(None, solve(part=1, file='input-real'))
