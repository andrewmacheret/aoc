#!/usr/bin/env python3

from collections import defaultdict, deque
from itertools import permutations
import re

from common.util import load, test, change_dir, tuples, lists


def bfs(start, expand, is_goal):
  seen = {start}
  q = deque([(0, start)])
  while q:
    r, x = q.popleft()
    if is_goal(*x):
      yield r, x
    else:
      for y in expand(*x):
        if y not in seen:
          seen.add(y)
          q.append((r+1, y))


def load_floors(file):
  locations = defaultdict(lambda: [0, 0])
  for floor_num, line in enumerate(load(file), 1):
    for material, type in re.findall(r'a (\w+)( generator|-compatible microchip)', line):
      locations[material][type[0] == '-'] = floor_num
  return tuple(map(tuple, sorted(locations.values())))


def find_items(e, floors):
  for i1, item in enumerate(floors):
    for j1, x1 in enumerate(item):
      if x1 == e:
        yield i1, j1


def possible_floors(e, e1, floors):
  for i1, j1 in find_items(e, floors):
    floors2 = lists(floors)
    floors2[i1][j1] = e1
    yield tuples(sorted(floors2))
  for (i1, j1), (i2, j2) in permutations(find_items(e, floors), 2):
    floors2 = lists(floors)
    floors2[i1][j1] = e1
    floors2[i2][j2] = e1
    yield tuples(sorted(floors2))


def safe(floors):
  gens = {g for g, _ in floors}
  return all(mc == g or mc not in gens for g, mc in floors)


def solve(part, file):
  floors = load_floors(file)

  if part == 2:
    floors = tuple(list(floors) + [(1, 1), (1, 1)])

  start = (1, floors)

  def expand(e, floors):
    for e1 in (e-1, e+1):
      if 1 <= e1 <= 4:
        for floors1 in possible_floors(e, e1, floors):
          if safe(floors1):
            yield (e1, floors1)

  def is_goal(_, floors):
    return all(x == 4 for item in floors for x in item)

  return next(bfs(start, expand, is_goal))[0]


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(11, solve(part=1, file='input-test-1'))
  test(31, solve(part=1, file='input-real'))
  test(55, solve(part=2, file='input-real'))
