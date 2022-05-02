#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  points = {(px, py, pz): [(i, *p)]
            for i, (px, py, pz, *p) in enumerate(map(parse_nums, load(file)))}

  for _ in range(500):  # should be good enough
    next_points = defaultdict(list)
    for (px, py, pz), ps in points.items():
      for (i, vx, vy, vz, ax, ay, az) in ps:
        vx, vy, vz = vx+ax, vy+ay, vz+az
        next_points[px+vx, py+vy, pz+vz].append((i, vx, vy, vz, ax, ay, az))
    if part:
      next_points = {k: ps for k, ps in next_points.items() if len(ps) == 1}
    points = next_points

  return len(points) if part else points[min(points, key=lambda p: sum(map(abs, p)))][0][0]


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(0, solve(part=0, file='input-test-1'))
  test(161, solve(part=0, file='input-real'))

  test(1, solve(part=1, file='input-test-2'))
  test(438, solve(part=1, file='input-real'))
