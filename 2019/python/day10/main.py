#!/usr/bin/env python3
from collections import defaultdict, deque
from itertools import combinations, islice
from math import gcd, copysign, atan2
from bisect import insort

from day01.main import load, test

def next_nth(gen, index):
  return next(islice(gen, index, None))

def load_grid(filename, script=__file__):
  return [[c for c in line] for line in load(filename, script=script)]

def astroid_visibility(grid):
  astroids = {(x, y): defaultdict(list) for y, row in enumerate(grid) for x, cell in enumerate(row) if cell == '#'}
  for (x1, y1), (x2, y2) in combinations(astroids, 2):
    dx, dy = x2 - x1, y2 - y1
    multiplier = gcd(abs(dx), abs(dy))
    dx, dy = dx // multiplier, dy // multiplier
    insort(astroids[x1, y1][dx, dy], multiplier)
    insort(astroids[x2, y2][-dx, -dy], multiplier)
  return astroids

def starting_astroid(astroids):
  return max(astroids, key=lambda k: len(astroids[k]))

def target_astroids(astroids, x, y):
  targets = astroids[x, y]
  for dx, dy in targets: targets[dx, dy].reverse()
  q = deque(sorted(targets, key=lambda coord: -atan2(*coord)))
  while q:
    dx, dy = q.popleft()
    multiple = targets[dx, dy].pop()
    yield x + dx*multiple, y + dy*multiple
    if targets[dx, dy]: q.append((dx, dy))

def part1(filename):
  astroids = astroid_visibility(load_grid(filename))
  x, y = starting_astroid(astroids)
  return (x, y), len(astroids[x, y])

def part2(filename, index):
  astroids = astroid_visibility(load_grid(filename))
  x, y = starting_astroid(astroids)
  return next_nth(target_astroids(astroids, x, y), index)

if __name__== "__main__":
  test(((3, 4), 8), part1('input-test-1.txt'))
  test(((5, 8), 33), part1('input-test-2.txt'))
  test(((1, 2), 35), part1('input-test-3.txt'))
  test(((6, 3), 41), part1('input-test-4.txt'))
  test(((11, 13), 210), part1('input-test-5.txt'))
  test(((8, 3), 30), part1('input-test-6.txt'))
  test(((27, 19), 314), part1('input.txt'))

  test((14, 3), part2('input-test-6.txt', 35))
  test((8, 2), part2('input-test-5.txt', 199))
  test((15, 13), part2('input.txt', 199))
