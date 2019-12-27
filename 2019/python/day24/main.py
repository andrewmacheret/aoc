#!/usr/bin/env python3
from itertools import product
from copy import copy

from day01.main import test
from day11.main import DIRS, draw
from day18.main import load_grid

w, h, mid_x, mid_y = 5, 5, 2, 2

def next_grid(grid):
  grid2 = {}
  for y in range(h):
    for x in range(w):
      count = sum(grid.get((x+dx, y+dy)) == '#' for dx, dy in DIRS)
      grid2[x, y] = '.#'[count == 1] if grid[x, y] == '#' else '.#'[count == 1 or count == 2]
  return grid2

def next_grid_recursive(grids, depth):
  grid2 = {}
  for y in range(h):
    for x in range(w):
      if (x, y) != (mid_x, mid_y):
        count = 0
        if depth-1 in grids:
          if y == 0: count += grids[depth-1][mid_x, mid_y-1] == '#'
          elif y == h-1: count += grids[depth-1][mid_x, mid_y+1] == '#'
          if x == 0: count += grids[depth-1][mid_x-1, mid_y] == '#'
          elif x == w-1: count += grids[depth-1][mid_x+1, mid_y] == '#'
        for dx, dy in DIRS:
          if (x+dx, y+dy) == (mid_x, mid_y):
            if depth+1 in grids:
              if dx == 1: count += sum(grids[depth+1][0, y1] == '#' for y1 in range(h))
              elif dx == -1: count += sum(grids[depth+1][w-1, y1] == '#' for y1 in range(h))
              elif dy == 1: count += sum(grids[depth+1][x1, 0] == '#' for x1 in range(w))
              elif dy == -1: count += sum(grids[depth+1][x1, h-1] == '#' for x1 in range(w))
          elif 0 <= x+dx < w and 0 <= y+dy < h:
            count += grids[depth][x+dx, y+dy] == '#'
        grid2[x, y] = '.#'[count == 1] if grids[depth][x, y] == '#' else '.#'[count == 1 or count == 2]
  grid2[mid_x, mid_y] = '?'
  return grid2

def grid_value(grid):
  return sum(2 ** i for i, (y, x) in enumerate(product(range(h), range(w))) if grid[x, y] == '#')

def is_blank_grid(grid):
  return all(val != '#' for val in grid.values())

def draw_bugs(grid):
  draw(grid, out={'.':'.','#':'#','?':'?'})
  print()

def part1(filename):
  grid = load_grid(filename, script=__file__)
  visited = set()
  while True:
    grid = next_grid(grid)
    value = grid_value(grid)
    if value in visited:
      draw_bugs(grid)
      return value
    visited.add(value)

def part2(filename, time):
  grids = {0: load_grid(filename, script=__file__)}
  blank_grid = {(x, y): '.' for y in range(h) for x in range(w)}
  grids[0][mid_x, mid_y] = blank_grid[mid_x, mid_y] = '?'

  lowest, highest = 0, 0

  for _ in range(1, time+1):
    if not is_blank_grid(grids[lowest]):
      lowest -= 1
      grids[lowest] = copy(blank_grid)
    if not is_blank_grid(grids[highest]):
      highest += 1
      grids[highest] = copy(blank_grid)
    grids = {i: next_grid_recursive(grids, i) for i, grid in grids.items()}
  
  for i, grid in sorted(grids.items()):
    print('Depth {}:'.format(i))
    draw_bugs(grid)
  
  return sum(grid[x, y] == '#' for grid in grids.values() for y in range(h) for x in range(w))

if __name__== "__main__":
  test(2129920, part1('input-test-1.txt'))
  test(32506911, part1('input.txt'))
  
  test(99, part2('input-test-1.txt', 10))
  test(2025, part2('input.txt', 200))
