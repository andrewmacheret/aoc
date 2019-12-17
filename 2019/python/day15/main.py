#!/usr/bin/env python3
from collections import defaultdict
from math import inf

from day01.main import test
from day02.main import load_memory
from day05.main import Program
from day11.main import grouper, draw
from day12.main import sign

DIRS = {
  (1, 2): (0, -1),
  (2, 1): (0, +1),
  (3, 4): (-1, 0),
  (4, 3): (+1, 0),
}

def solve(filename):
  memory = load_memory(filename, script=__file__)
  prog = Program(memory)
  run = prog.run_computer()

  grid = defaultdict(int, {(0, 0): 1})
  o2_distance = None
  o2_q = []
  def dfs(x, y, distance):
    nonlocal o2_distance, o2_q
    for (dir_code, return_code), (dx, dy) in DIRS.items():
      x1, y1 = x+dx, y+dy
      if (x1, y1) not in grid:
        prog.input.append(dir_code)
        status = next(run)
        grid[x1, y1] = status
        if status != 0:
          dfs(x1, y1, distance+1)
          prog.input.append(return_code)
          next(run)
    if grid[x, y] == 2:
      o2_distance = distance
      o2_q.append((x, y))
  dfs(0, 0, 0)

  o2_minutes = 0
  while o2_q:
    next_q = []
    for x, y in o2_q:
      for dx, dy in DIRS.values():
        x1, y1 = x+dx, y+dy
        if grid[x1, y1] == 1:
          grid[x1, y1] = 2
          next_q.append((x1, y1))
    o2_minutes += 1
    o2_q = next_q

  return (o2_distance, o2_minutes-1)

if __name__== "__main__":
  test(238, solve('input.txt')[0])
  test(392, solve('input.txt')[1])
