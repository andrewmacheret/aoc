#!/usr/bin/env python3
from collections import deque
from itertools import filterfalse
from math import inf
from functools import lru_cache

from day01.main import load, test
from day11.main import DIRS

def load_grid(filename, script=__file__):
  rows = [line for line in load(filename, script=script)]
  return {(x, y): cell for y, row in enumerate(rows) for x, cell in enumerate(row)}

class CollectKeys:
  def __init__(self, grid):
    self.distances = {ch: dict(self.find_keys(grid, x, y)) for (x, y), ch in grid.items() if ch not in '.#' and not ch.isupper()}

  def find_keys(self, grid, start_x, start_y):
    q = deque([(start_x, start_y, 0, frozenset())])
    visited = set()
    while q:
      x, y, dist, doors = q.popleft()
      item = grid.get((x, y))
      if item and item != '#' and (x, y) not in visited:
        visited.add((x, y))
        if item.islower():
          yield item, (dist, doors)
        elif item.isupper():
          doors = doors.union(item.lower())
        for dx, dy in DIRS:
          q.append((x+dx, y+dy, dist+1, doors))

  def distance_to_collect_keys(self):
    keys = frozenset(filter(str.islower, self.distances))
    starts = frozenset(filterfalse(str.islower, self.distances))
    return self.distance_to_collect_keys_cached(starts, keys)

  @lru_cache(maxsize=None)
  def distance_to_collect_keys_cached(self, current_keys, remaining_keys):
    def search():
      for current_key in current_keys:
        for key in remaining_keys & self.distances[current_key].keys():
          dist, req_doors = self.distances[current_key][key]
          if not req_doors & remaining_keys:
            yield dist + self.distance_to_collect_keys_cached(current_keys.difference(current_key).union(key), remaining_keys.difference(key))
    return min(search(), default=0)

def part1(filename):
  grid = load_grid(filename)
  return CollectKeys(grid).distance_to_collect_keys()

def part2(filename):
  grid = load_grid(filename)
  x, y = next((x, y) for x, y in grid if grid[x, y] == '@')
  for dy, row in enumerate(['1#2', '###', '3#4'], -1):
    for dx, ch in enumerate(row, -1):
      grid[x+dx, y+dy] = ch
  return CollectKeys(grid).distance_to_collect_keys()

if __name__== "__main__":
  test(8, part1('input-test-1.txt'))
  test(86, part1('input-test-2.txt'))
  test(132, part1('input-test-3.txt'))
  test(136, part1('input-test-4.txt'))
  test(81, part1('input-test-5.txt'))
  test(4544, part1('input.txt'))

  test(8, part2('input-test-6.txt'))
  test(24, part2('input-test-7.txt'))
  test(32, part2('input-test-8.txt'))
  test(72, part2('input-test-9.txt'))
  test(1692, part2('input.txt'))
