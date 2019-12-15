#!/usr/bin/env python3
from day01.main import test
from day02.main import load_memory
from day05.main import Program
from day11.main import grouper, draw
from day12.main import sign

def part1(filename):
  memory = load_memory(filename, script=__file__)
  grid = {(x, y): id for x, y, id in grouper(Program(memory, []).run_computer(), 3)}
  draw(grid, out=' █#-o')
  return sum(id == 2 for (x, y), id in grid.items())

def part2(filename):
  memory = load_memory(filename, script=__file__)
  memory[0] = 2
  prog = Program(memory)
  grid = {}
  ball_x = paddle_x = score = None
  block_count = 0

  class PaddleInput: popleft = lambda self: sign(ball_x - paddle_x)
  prog.input = PaddleInput()

  for x, y, id in grouper(prog.run_computer(), 3):
    if (x, y) == (-1, 0):
      score = id
      if block_count == 0: return score
    else:
      if id == 2: block_count += 1
      elif id == 3: paddle_x = x
      elif id == 4: ball_x = x
      elif id == 0 and grid.get((x, y)) == 2: block_count -= 1
      grid[x, y] = id
  draw(grid, out=' |#-o')

if __name__== "__main__":
  test(398, part1('input.txt'))
  test(19447, part2('input.txt'))
