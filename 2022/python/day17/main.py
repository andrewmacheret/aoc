#!/usr/bin/env python3

from common.util import *

types = [
    ["####"],
    [".#.", "###", ".#."],
    ["..#", "..#", "###"],
    ["#", "#", "#", "#"],
    ['##', '##'],
]

grid_width = 7


def solve(part, file):
  data = load(file)[0]

  grid = {(x, -1): 'x' for x in range(grid_width)}  # floor
  tower_height = 0
  block = 0
  block_y = 3
  block_x = 2

  def drop(by, bx):
    for y in range(len(types[block])):
      for x in range(len(types[block][0])):
        if types[block][y][x] == '#':
          grid[bx + x, by - y] = '#'

  def valid(by, bx):
    for y in range(len(types[block])):
      for x in range(len(types[block][0])):
        if types[block][y][x] == '#':
          if (bx + x, by - y) in grid:
            return False
    return True

  seen = {}

  def top_of_grid(n):
    return ''.join('.#'[(x, y) in grid] for y in range(tower_height - n, tower_height) for x in range(7))

  goal = [2022, 1_000_000_000_000][part]

  bonus_height = 0
  for r, c in cycle(enumerate(data)):
    if c == '<':
      if block_x > 0 and valid(block_y, block_x - 1):
        block_x -= 1
    else:
      if block_x < grid_width - len(types[block][0]) and valid(block_y, block_x + 1):
        block_x += 1

    if valid(block_y - 1, block_x):
      block_y -= 1
    else:
      drop(block_y, block_x)

      tower_height = max(tower_height, block_y + 1)
      goal -= 1
      block = (block + 1) % len(types)
      block_y = tower_height + len(types[block]) + 2
      block_x = 2

      hash = (r, block, top_of_grid(6))  # barely good enough
      if hash in seen:
        cycle_drop = seen[hash][0] - goal
        cycle_height = tower_height - seen[hash][1]
        cycles = goal // cycle_drop
        bonus_height += cycles * cycle_height
        goal -= cycles * cycle_drop
      else:
        seen[hash] = (goal, tower_height)

      if goal <= 0:
        return tower_height + bonus_height


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(3068, solve(part=0, file='input-test-1'))
  test(3090, solve(part=0, file='input-real'))

  test(1_514_285_714_288, solve(part=1, file='input-test-1'))
  test(1_530_057_803_453, solve(part=1, file='input-real'))
