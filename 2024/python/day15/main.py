#!/usr/bin/env python3

from common.util import *

dirs = {
  '<': LEFT,
  '>': RIGHT,
  '^': UP,
  'v': DOWN,
}

expansions = {
  '@': '@.',
  '#': '##',
  '.': '..',
  'O': '[]',
}

def push_boxes(grid, sx, sy, dx, dy):
  # build a stack of the moves, starting with the player
  stack = [{(sx,sy)}]
  while True:
    # any walls, do nothing
    if any(grid[y+dy][x+dx] == '#' for x,y in stack[-1]):
      return sx, sy
    
    # all empty, perform the move
    if all(grid[y+dy][x+dx] == '.' for x,y in stack[-1]):
      # move all boxes in the stack, one row at a time
      while stack:
        for x,y in stack.pop():
          grid[y+dy][x+dx] = grid[y][x]
          grid[y][x] = '.'
      return sx+dx, sy+dy
    
    # build a new set of boxes in the stack, based on the last row
    new = set()
    for x,y in stack[-1]:
      # always add the next cell if it's a box
      if grid[y+dy][x+dx] in '[]O':
        new.add((x+dx, y+dy))
      # vertical only...
      if dy: 
        # add right cell if it's the left side of a box
        if grid[y+dy][x+dx] == '[':
          new.add((x+dx+1, y+dy))
        # add left cell if it's the right side of a box
        elif grid[y+dy][x+dx] == ']':
          new.add((x+dx-1, y+dy))
    stack.append(new)

def solve(part, file):
  grid, moves = load_blocks(file)
  grid = parse_grid(grid)
  moves = ''.join(moves)

  # expand the grid if part 2
  if part:
    grid = [[c for ch in row for c in expansions[ch]] for row in grid]

  # find the player
  sx, sy = next((x,y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == '@')

  # perform all the moves
  for move in moves:
    sx, sy = push_boxes(grid, sx, sy, *dirs[move])

  # sum based on the left side of all boxes
  return sum(y*100 + x for y, row in enumerate(grid) for x, ch in enumerate(row) if ch in '[O')


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(10092, solve(part=0, file='input-test-1'))
  test(1429911, solve(part=0, file='input-real'))

  test(9021, solve(part=1, file='input-test-1'))
  test(1453087, solve(part=1, file='input-real'))
