#!/usr/bin/env python3

from common.util import *


DIRS = {'R': (1, 0), 'U': (0, -1), 'D': (0, 1), 'L': (-1, 0)}


def follow(h, t):
  dx, dy = t[0] - h[0], t[1] - h[1]
  return t if (abs(dx) <= 1 and abs(dy) <= 1) else (t[0] - sign(dx), t[1] - sign(dy))


def solve(part, file):
  data = load(file)
  snake = [(0, 0) for _ in range([2, 10][part])]
  seen = {(0, 0)}
  for line in data:
    d, c = line.split()
    for _ in range(int(c)):
      dx, dy = DIRS[d]
      snake[0] = (snake[0][0] + dx, snake[0][1] + dy)
      for i in range(len(snake)-1):
        snake[i+1] = follow(snake[i], snake[i+1])
      seen.add(snake[-1])
  return len(seen)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(13, solve(part=0, file='input-test-1'))
  test(6256, solve(part=0, file='input-real'))

  test(1, solve(part=1, file='input-test-1'))
  test(36, solve(part=1, file='input-test-2'))
  test(2665, solve(part=1, file='input-real'))
