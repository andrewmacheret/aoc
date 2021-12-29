#!/usr/bin/env python3

from collections import deque
from itertools import permutations
from math import inf

from common.util import load, test, change_dir, DIRS_4


def bfs(start, expand, is_goal):
  q = deque(seen := {start})
  while q:
    x = q.popleft()
    if is_goal(*x):
      yield x
    else:
      for y in expand(*x):
        if y not in seen:
          seen.add(y)
          q.append(y)


def load_grid(file):
  return {(x, y): cell for y, row in enumerate(load(file)) for x, cell in enumerate(row)}


def solve(part, file):
  grid = load_grid(file)
  points = {c: (x, y) for (x, y), c in grid.items() if c.isdigit()}

  def expand(r, x, y):
    for dx, dy in DIRS_4:
      x1, y1 = x+dx, y+dy
      if grid.get((x1, y1), '#') != '#':
        yield r+1, x1, y1

  dists = {}
  for a, b in permutations(points.items(), 2):
    dist, _, _ = next(bfs(start=(0, *a[1]), expand=expand,
                          is_goal=lambda _, x, y: (x, y) == b[1]))
    dists[a[1], b[1]] = dist
    dists[b[1], a[1]] = dist

  start = points['0']
  del points['0']

  best = inf
  for perm in permutations(points.values()):
    pair_starts = [start] + list(perm)
    pair_ends = perm if part == 1 else list(perm) + [start]
    path = sum(dists[a, b] for a, b in zip(pair_starts, pair_ends))
    if best > path:
      best = path
  return best

### THE REST IS TESTS ###


if __name__ == "__main__":
  change_dir(__file__)

  test(14, solve(part=1, file='input-test-1'))
  test(500, solve(part=1, file='input-real'))

  test(20, solve(part=2, file='input-test-1'))
  test(748, solve(part=2, file='input-real'))
