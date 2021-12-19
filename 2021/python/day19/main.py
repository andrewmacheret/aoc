#!/usr/bin/env python3

from itertools import starmap, product, permutations, chain
from operator import sub

from common.util import load_blocks, test, change_dir


def split_nums(line, delim=','):
  return [*map(int, line.split(delim))]


def manhattan(*points):
  return sum(map(abs, map(sub, *points)))


def get_orientations(beacons):
  # dont need 48 possible orientations...
  # [{(p[a]*d, p[b]*e, p[c]*f) for p in beacons} for a, b, c in permutations((0, 1, 2)) for d, e, f in product((-1, 1), repeat=3)]
  # only 24:
  perms1 = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
  signs1 = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
  perms2 = [(2, 1, 0), (1, 0, 2), (0, 2, 1)]
  signs2 = [(1, -1, 1), (1, 1, -1), (-1, 1, 1), (-1, -1, -1)]
  return [{(p[a]*d, p[b]*e, p[c]*f) for p in beacons} for (a, b, c), (d, e, f) in chain(product(perms1, signs1), product(perms2, signs2))]


def correct(beacons, orientation, threshold=12):
  for (b1, b2, b3), (p1, p2, p3) in product(beacons, orientation):
    s1, s2, s3 = p1-b1, p2-b2, p3-b3
    corrected = {(p1-s1, p2-s2, p3-s3) for p1, p2, p3 in orientation}
    if len(beacons & corrected) >= threshold:
      return corrected, (s1, s2, s3)
  return None, None


def solve(part, file):
  data = load_blocks(file)
  groups = []
  for block in data:
    detected = [split_nums(line) for line in block[1:]]
    groups += get_orientations(detected),

  beacons = groups[0][0]
  del groups[0]

  scanners = []
  while groups:
    for index, orientations in enumerate(groups):
      for orientation in orientations:
        corrected, scanner = correct(beacons, orientation)
        if corrected:
          del groups[index]
          print(len(groups))
          beacons |= corrected
          scanners += scanner,
          break

  if part == 1:
    return len(beacons)
  else:
    return max(starmap(manhattan, permutations(scanners, 2)))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(79, solve(part=1, file='input-test-1'))
  test(3621, solve(part=2, file='input-test-1'))

  test(483, solve(part=1, file='input-real'))
  test(14804, solve(part=2, file='input-real'))
