#!/usr/bin/env python3


from common.util import *


DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def spiral():
  x = y = 0
  for i, (dx, dy) in enumerate(cycle(DIRS)):
    for _ in range((i//2) + 1):
      yield x, y
      x += dx
      y += dy


def spiral_sums():
  grid = defaultdict(int)
  grid[0, 0] = 1
  for x, y in spiral():
    grid[x, y] += sum(grid[x+dx, y+dy] for dx, dy in DIRS_8)
    yield grid[x, y]


def find_dist(x):
  return sum(map(abs, next(islice(spiral(), x-1, None))))


def find_sum(x):
  return next(dropwhile(x.__ge__, spiral_sums()))


def solve(part, file):
  return (find_dist, find_sum)[part](load_int(file))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(0, find_dist(1))
  test(3, find_dist(12))
  test(2, find_dist(23))
  test(31, find_dist(1024))
  test(475, solve(part=0, file='input-real'))

  test(279138, solve(part=1, file='input-real'))
