#!/usr/bin/env python3

from common.util import *


def parse_nums(line):
  return [*map(int, re.findall(r'[+-]?\d+', line))]


def dist(x1, y1, x2, y2): return abs(y2-y1) + abs(x2-x1)


def is_possible(beacons, x, y):
  if x % 100_000 == 0:
    print(x)
  for sx, sy, bx, by in beacons:
    if (x, y) == (bx, by):
      return 0
    if dist(sx, sy, x, y) <= dist(sx, sy, bx, by):
      return 1
  return 0


def part1(beacons, y_level):
  return sum(is_possible(beacons, x, y_level) for x in range(-y_level*5, y_level*5))


def part2(sensors, max_xy):
  for y in range(max_xy+1):
    if y % 100_000 == 0 and y:
      print(y)
    ranges = []
    for sx, sy, bx, by in sensors:
      dist_to_beacon = dist(sx, sy, bx, by)
      dy = abs(y - sy)
      if dy <= dist_to_beacon:
        offset_x = dist_to_beacon - dy
        ranges.append((sx - offset_x, sx + offset_x))
    ranges.sort()

    first = ranges[0]
    if first is None:
      return 0

    from_x = first[0]
    if from_x > 0:
      return 0

    to_x = first[1]
    for r in ranges[1:]:
      if r[1] > to_x:
        if r[0] > to_x + 1:
          return (to_x + 1) * 4_000_000 + y
        to_x = r[1]

    if to_x < max_xy:
      return (to_x + 1) * 4_000_000 + y

  return 0


def solve(part, file, level):
  data = load(file)

  sensors = [*map(parse_nums, data)]

  return [part1, part2][part](sensors, level)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(27, solve(part=0, file='input-test-1', level=20))
  test(5870800, solve(part=0, file='input-real', level=2000000))

  test(56000011, solve(part=1, file='input-test-1', level=20))
  test(10908230916597, solve(part=1, file='input-real', level=4_000_000))
