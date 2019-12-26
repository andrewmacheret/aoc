#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop

from day01.main import test
from day11.main import DIRS
from day18.main import load_grid

def portals_by_coord(grid):
  w = max(x for x, y in grid)
  h = max(y for x, y in grid)
  portals = {}
  for x, y in grid:
    if grid[x, y].isupper():
      for dx, dy in DIRS:
        if grid.get((x+dx, y+dy)) == '.':
          id = grid[min(x, x-dx), min(y, y-dy)] + grid[max(x, x-dx), max(y, y-dy)]
          dd = 1 if 0 < x-dx < w and 0 < y-dy < h else -1
          portals[x+dx, y+dy] = (id, dd)
  return portals

def portal_distances(grid, portals_by_coord):
  distances = defaultdict(dict)
  for coord, (id, dd) in portals_by_coord.items():
    q = deque([(0, *coord)])
    visited = set()
    while q:
      dist, x, y = q.popleft()
      if (x, y) not in visited:
        visited.add((x, y))
        if (x, y) in portals_by_coord and (x,y) != coord:
          distances[(id, dd)][portals_by_coord[(x, y)]] = dist
        for dx, dy in DIRS:
          if grid[x+dx, y+dy] == '.':
            q.append((dist+1, x+dx, y+dy))
  return distances

def fastest_to_exit(distances, use_level):
  q = [(0, 1, 'AA', -1)]
  while q:
    distance, level, id, dd = heappop(q)
    if id == 'ZZ': return distance - 1
    for (id1, dd1), distance1 in distances[id, dd].items():
      if id1 != 'AA' \
            and (level == 1 if id1 == 'ZZ' else not use_level or level+dd1 > 0) \
            and 0 <= level <= len(distances):
        heappush(q, (distance+distance1+1, level+dd1 if use_level else level, id1, -dd1))

def solve(grid, use_level):
  portals = portals_by_coord(grid)
  distances = portal_distances(grid, portals)
  return fastest_to_exit(distances, use_level)

def part1(filename):
  return solve(load_grid(filename, script=__file__), use_level=False)

def part2(filename):
  return solve(load_grid(filename, script=__file__), use_level=True)

if __name__== "__main__":
  test(23, part1('input-test-1.txt'))
  test(58, part1('input-test-2.txt'))
  test(544, part1('input.txt'))
  
  test(26, part2('input-test-1.txt'))
  test(396, part2('input-test-3.txt'))
  test(18, part2('input-test-4.txt'))
  test(6238, part2('input.txt'))
