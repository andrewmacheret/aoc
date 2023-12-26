
from common.util import *


def load_grid_dict(data):
  return {(x, y): val for y, row in enumerate(data) for x, val in enumerate(row)}


ch = {
    '─': 'lr',
    '│': 'ud',
    '┐': 'ld',
    '└': 'ur',
    '┘': 'ul',
    '┌': 'dr',
    '┴': 'url',
    '┬': 'ldr',
    '├': 'urd',
    '┤': 'ldu',
    '┼': 'ldru',
    '*': 'r',
}

# print(puzzle)


def slide(grid, extra, x, y, dx, dy):
  for _ in range(5):
    grid[x, y], extra = extra, grid[x, y]
    x += dx
    y += dy


slide_moves = [
    (1, 0, 0, 1),
    (3, 0, 0, 1),
    (1, 4, 0, -1),
    (3, 4, 0, -1),
    (0, 1, 1, 0),
    (0, 3, 1, 0),
    (4, 1, -1, 0),
    (4, 3, -1, 0),
]


def works(grid):
  start = (2, 4)
  if grid[start] not in '┐│┌┬├┤┼':
    return False

  seen = set()

  def dfs(x, y):
    if not (0 <= x < 5 and 0 <= y < 5):
      return False
    if (x, y) in seen:
      return False
    seen.add((x, y))
    if (x, y) == (2, 2):
      return True
    for c in ch[grid[x, y]]:
      if c == 'l':
        if x-1 >= 0 and 'r' in ch[grid[x-1, y]] and dfs(x-1, y):
          return True
      elif c == 'r':
        if x+1 < 5 and 'l' in ch[grid[x+1, y]] and dfs(x+1, y):
          return True
      elif c == 'u':
        if y-1 >= 0 and 'd' in ch[grid[x, y-1]] and dfs(x, y-1):
          return True
      elif c == 'd':
        if y+1 < 5 and 'u' in ch[grid[x, y+1]] and dfs(x, y+1):
          return True
    return False
  return dfs(*start)


def solve():
  extra = '│'
  puzzle = """\
─┌┘└┐
┌│┴┐─
┤┼*─┼
└┘├┐┬
└│┬─┐\
""".split("\n")
#   puzzle = """\
# ─┌┘└┐
# ┌│┴┐─
# ┤┼*┐┼
# └┘┌┘┬
# └││─┐\
# """.split("\n")

  grid = load_grid_dict(puzzle)
  print(works(grid))

  for m1, m2, m3 in product(slide_moves, repeat=3):
    slide(grid, extra, *m1)
    slide(grid, extra, *m2)
    slide(grid, extra, *m3)
    if works(grid):
      print(draw(grid))
      return
    slide(grid, extra, *m3)
    slide(grid, extra, *m2)
    slide(grid, extra, *m1)
    return


solve()
