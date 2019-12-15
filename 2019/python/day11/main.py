#!/usr/bin/env python3
from itertools import zip_longest

from day01.main import load, test
from day02.main import load_memory
from day05.main import Program

DIRS = [(0,-1), (1,0), (0,1), (-1,0)]
def next_dir(dx, dy, delta):
  return DIRS[(DIRS.index((dx, dy)) + delta) % len(DIRS)]

def grouper(iterable, n, fillvalue=None):
  args = [iter(iterable)] * n
  return zip_longest(fillvalue=fillvalue, *args)

def paint(prog, initial_color):
  dx, dy = DIRS[0]
  x, y = 0, 0
  grid = {(x, y): initial_color}
  for color, right in grouper(prog.run_computer(), 2):
    grid[x, y] = color
    dx, dy = next_dir(dx, dy, 1 if right else -1)
    x, y = x+dx, y+dy
    prog.input.append(grid.get((x, y), 0))
  return grid

def draw(grid):
  min_x = min(x for x, y in grid)
  max_x = max(x for x, y in grid)
  min_y = min(y for x, y in grid)
  max_y = max(y for x, y in grid)
  for y in range(min_y, max_y + 1):
    print(''.join(' *'[grid.get((x, y), 0)] for x in range(min_x, max_x + 1)))

def solve(filename, initial_color):
  memory = load_memory(filename, script=__file__)
  prog = Program(memory, [initial_color])
  return paint(prog, initial_color)

if __name__== "__main__":
  test(2088, len(solve('input.txt', 0)))
  test(249, len(solve('input.txt', 1)))
  draw(solve('input.txt', 1))
