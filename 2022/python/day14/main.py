#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  data = load(file)

  world = set()
  for line in data:
    for (x1, y1), (x2, y2) in pairwise(zip(*[iter(parse_nums(line))]*2)):
      if dy := sign(y2-y1):
        for y in range(y1, y2+dy, dy):
          world.add((x1, y))
      elif dx := sign(x2-x1):
        for x in range(x1, x2+dx, dx):
          world.add((x, y1))

  the_floor = max(y for _, y in world) + 2
  if part:
    for i in range(-1000, 1000):
      world.add((i, the_floor))

  def drop_sand():
    x, y = 500, 0
    while 1:
      if y == the_floor:
        return True
      if (down := (x, y+1)) not in world:
        x, y = down
      elif (down_left := (x-1, y+1)) not in world:
        x, y = down_left
      elif (down_right := (x+1, y+1)) not in world:
        x, y = down_right
      else:
        if (x, y) in world:
          return True
        world.add((x, y))
        return False

  for r in count():
    if drop_sand():
      return r


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(24, solve(part=0, file='input-test-1'))
  test(755, solve(part=0, file='input-real'))

  test(93, solve(part=1, file='input-test-1'))
  test(29805, solve(part=1, file='input-real'))
