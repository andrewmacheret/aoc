#!/usr/bin/env python3

from copy import copy

from common.util import *


def load_grid_dict(file):
  return {(x, y): val for y, row in enumerate(load(file)) for x, val in enumerate(row)}


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


mapper = [
    {c: set(ascii_lowercase[:i+2]) for i, c in enumerate(ascii_lowercase)},
    {c: set(ascii_lowercase[i-1:]) for i, c in enumerate(ascii_lowercase)}
]
mapper[0]['y'].add('E')
mapper[0]['z'].add('E')
mapper[0]['S'] = {'a', 'b'}
mapper[1]['E'] = {'y', 'z'}


def search(grid, part):
  grid = copy(orig := grid)

  start = next(xy for xy, v in grid.items() if v == 'SE'[part])

  def expand(x, y):
    for xy1 in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
      if grid.get(xy1, 0) in mapper[part][orig[x, y]]:
        grid[xy1] = '#'
        yield xy1

  def is_goal(*xy): return orig[xy] == 'Ea'[part]

  return next(bfs(start, expand, is_goal), [inf])[0]


def solve(part, file):
  grid = load_grid_dict(file)
  return search(grid, part)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(31, solve(part=0, file='input-test-1'))
  test(383, solve(part=0, file='input-real'))

  test(29, solve(part=1, file='input-test-1'))
  test(377, solve(part=1, file='input-real'))
