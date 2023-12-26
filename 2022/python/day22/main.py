#!/usr/bin/env python3

from common.util import *


def draw(grid, **vargs):
  for type, fn in ((set, draw_set), (dict, draw_dict), (list, draw_grid)):
    if isinstance(grid, type):
      return fn(grid, **vargs)
  raise Exception('Unrecognized type', grid)


def draw_dict(grid, empty=' '):
  x_min = y_min = inf
  x_max = y_max = -inf
  for x, y in grid:
    x_min, x_max = min(x_min, x), max(x_max, x)
    y_min, y_max = min(y_min, y), max(y_max, y)
  return '\n'.join(''.join(grid.get((x, y), empty) for x in range(x_min, x_max+1)) for y in range(y_min, y_max+1))


def load_grid_dict(data):
  return {(x, y): val for y, row in enumerate(data) for x, val in enumerate(row)}


DIRS_4 = [(1, 0), (0, -1), (-1, 0), (0, 1)]
DIR_CHARS = '>^<v'


def solve(part, file, n):
  data = load_blocks(file)
  grid = load_grid_dict(data[0])

  @cache
  def min_x(y):
    return min(x for x, y2 in grid if y2 == y and grid.get((x, y2), ' ') in '.#')

  @cache
  def max_x(y):
    return max(x for x, y2 in grid if y2 == y and grid.get((x, y2), ' ') in '.#')

  @cache
  def min_y(x):
    return min(y for x2, y in grid if x2 == x and grid.get((x2, y), ' ') in '.#')

  @cache
  def max_y(x):
    return max(y for x2, y in grid if x2 == x and grid.get((x2, y), ' ') in '.#')

  turns = {
      (0, 1): ((5, 0), lambda x, y: (0, x)),
      (5, 2): ((0, 3), lambda x, y: (y, 0)),
      (1, 1): ((5, 1), lambda x, y: (x, n-1)),
      (5, 3): ((1, 3), lambda x, y: (x, 0)),
      (4, 3): ((5, 2), lambda x, y: (n-1, x)),
      (5, 0): ((4, 1), lambda x, y: (y, n-1)),
      (0, 2): ((3, 0), lambda x, y: (0, n-1-y)),
      (3, 2): ((0, 0), lambda x, y: (0, n-1-y)),
      (2, 2): ((3, 3), lambda x, y: (y, 0)),
      (3, 1): ((2, 0), lambda x, y: (0, x)),
      (1, 0): ((4, 2), lambda x, y: (n-1, n-1-y)),
      (4, 0): ((1, 2), lambda x, y: (n-1, n-1-y)),
      (1, 3): ((2, 2), lambda x, y: (n-1, x)),
      (2, 0): ((1, 1), lambda x, y: (y, n-1)),
  }

  sc = count()
  to_section = {}
  for y, x in product(range(6), repeat=2):
    if grid.get((x*n, y*n), ' ') != ' ':
      to_section[x, y] = next(sc)
  print(to_section)

  from_section = {v: k for k, v in to_section.items()}
  print(from_section)

  def travel2d(x, y, d):
    dx, dy = DIRS_4[d]
    x1 = max_x(y) if dx < 0 else min_x(y) if dx > 0 else x+dx
    y1 = max_y(x) if dy < 0 else min_y(x) if dy > 0 else y+dy
    return x1, y1, d

  def travel3d(x, y, d):
    d1 = d
    s = to_section[x//n, y//n]
    (s1, d1), fn = turns[s, d]
    x1, y1 = fn(x % n, y % n)
    xm, ym = from_section[s1]
    return x1 + xm * n, y1 + ym * n, d1

  x, y = min_x(0), 0
  d = 0

  moves = re.findall(r'[0-9]+[LR]', data[1][0] + 'L0R')
  for move in moves:
    amt = int(move[:-1])

    for _ in range(amt):
      dx, dy = DIRS_4[d]
      x1, y1, d1 = x+dx, y+dy, d
      if grid.get((x1, y1), ' ') == ' ':
        x1, y1, d1 = (travel2d, travel3d)[part](x, y, d)
      if grid.get((x1, y1), ' ') == '#':
        break
      x, y, d = x1, y1, d1

    dd = move[-1]
    d = (d + '0L@R'.index(dd)) % 4

    # t = grid[x, y]
    # grid[x, y] = '*'
    # print(draw(grid))
    # print()
    # grid[x, y] = t

  return sum((1000*(y+1), (x+1)*4, d))

  # print(data)

  ### THE REST IS TESTS ###


if __name__ == "__main__":
  change_dir(__file__)

  test(6032, solve(part=0, file='input-test-1', n=4))
  test(1484, solve(part=0, file='input-real', n=50))

  # test(None, solve(part=1, file='input-test-1', n=4))
  test(142228, solve(part=1, file='input-real', n=50))
