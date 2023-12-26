#!/usr/bin/env python3

from common.util import *

DIRS_5 = [(1, 0), (0, -1), (-1, 0), (0, 1), (0, 0)]
DIR_CHARS = '>^<v'


def load_grid_dict(data):
  return {(x, y): val for y, row in enumerate(data) for x, val in enumerate(row)}


def dijkstra(start, expand, is_goal):
  seen = {start}
  q = [(0, start)]
  while q:
    _, item = heappop(q)
    for dist1, item1 in expand(*item):
      if is_goal(*item1):
        yield item1[0]
      if (hash := (item1)) not in seen:
        seen.add(hash)
        heappush(q, (dist1, item1))


def solve(part, file):
  data = load(file)
  n, m = len(data), len(data[0])
  start, end = (1, 0), (m-2, n - 1)
  grid = load_grid_dict(data)

  @cache
  def get_blizzards(r):
    if r == 0:
      blizzards = [set() for _ in DIR_CHARS]
      for (x, y), val in grid.items():
        if val in DIR_CHARS:
          blizzards[DIR_CHARS.index(val)].add((x, y))
      return blizzards
    return [{((x+dx - 1) % (m-2) + 1,
              (y+dy - 1) % (n-2) + 1) for x, y in b}
            for (dx, dy), b in zip(DIRS_5, get_blizzards(r-1))]

  def expand(r, ms, x, y):
    r += 1
    blizzards = get_blizzards(r)
    for dx, dy in DIRS_5:
      x1, y1 = x+dx, y+dy
      if grid.get((x1, y1), '#') != '#' and all((x1, y1) not in b for b in blizzards):
        if (x1, y1) == (subgoal := (end, start)[(ms1 := ms) % 2]):
          subgoal = (end, start)[(ms1 := ms1 - 1) % 2]
        dist = (ms1, r + (subgoal[1] - y1 + subgoal[0] - x1))
        yield dist, (r, ms1, x1, y1)

  def is_goal(r, ms, x, y): return ms == (-1, -3)[part]

  return next(dijkstra((0, 0, *start), expand=expand, is_goal=is_goal))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(18, solve(part=0, file='input-test-1'))
  test(308, solve(part=0, file='input-real'))

  test(54, solve(part=1, file='input-test-1'))
  test(908, solve(part=1, file='input-real'))
