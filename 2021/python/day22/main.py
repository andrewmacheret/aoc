#!/usr/bin/env python3

from itertools import product
import re

from common.util import load, test, change_dir


def parse_nums(line):
  return [*map(int, re.findall(r'[-+]?\d+', line))]


def is_overlapping(cube1, cube2):
  x1, x2, y1, y2, z1, z2 = cube1
  a1, a2, b1, b2, c1, c2 = cube2
  return a1 <= x2 and x1 <= a2 \
      and b1 <= y2 and y1 <= b2 \
      and c1 <= z2 and z1 <= c2


def cut_cube(cube_to_cut, cube_to_keep):
  x1, x2, y1, y2, z1, z2 = cube_to_cut
  a1, a2, b1, b2, c1, c2 = cube_to_keep

  for dx, dy, dz in product((-1, 0, 1), repeat=3):
    if dx == dy == dz == 0:
      continue
    if dx == -1 and x1 < a1:
      x = (x1, a1-1)
    elif dx == 0 and max(x1, a1) <= min(x2, a2):
      x = (max(x1, a1), min(x2, a2))
    elif dx == 1 and a2 < x2:
      x = (a2+1, x2)
    else:
      continue
    if dy == -1 and y1 < b1:
      y = (y1, b1-1)
    elif dy == 0 and max(y1, b1) <= min(y2, b2):
      y = (max(y1, b1), min(y2, b2))
    elif dy == 1 and b2 < y2:
      y = (b2+1, y2)
    else:
      continue
    if dz == -1 and z1 < c1:
      z = (z1, c1-1)
    elif dz == 0 and max(z1, c1) <= min(z2, c2):
      z = (max(z1, c1), min(z2, c2))
    elif dz == 1 and c2 < z2:
      z = (c2+1, z2)
    else:
      continue
    yield (*x, *y, *z)


def is_within(cube, limit):
  x1, x2, y1, y2, z1, z2 = cube
  return -limit <= x1 <= limit and -limit <= x2 <= limit \
      and -limit <= y1 <= limit and -limit <= y2 <= limit \
      and -limit <= z1 <= limit and -limit <= z2 <= limit


def area(cube):
  x1, x2, y1, y2, z1, z2 = cube
  return (x2-x1+1) * (y2-y1+1) * (z2-z1+1)


def solve(part, file):
  cube_input = [(line[:2] == 'on', parse_nums(line)) for line in load(file)]

  cubes = {}
  for on, cube in cube_input:
    if part == 2 or is_within(cube, 50):
      cube = tuple(cube)
      for other_cube in list(cubes):
        if is_overlapping(cube, other_cube):
          del cubes[other_cube]
          for piece in cut_cube(other_cube, cube):
            cubes[piece] = area(piece)
      if on:
        cubes[cube] = area(cube)
  return sum(cubes.values())


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(39, solve(part=1, file='input-test-1'))
  test(590784, solve(part=1, file='input-test-2'))
  test(474140, solve(part=1, file='input-test-3'))
  test(606484, solve(part=1, file='input-real'))

  test(2758514936282235, solve(part=2, file='input-test-3'))
  test(1162571910364852, solve(part=2, file='input-real'))
