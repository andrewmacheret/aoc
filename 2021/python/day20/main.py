#!/usr/bin/env python3

from common.util import load_blocks, test, change_dir


def enhance(grid, algo, outside, n):
  def enhance_x_y(x, y):
    return algo[int(''.join(
        '01'[grid.get((x+dx, y+dy), outside)]
        for dy in (-1, 0, 1)
        for dx in (-1, 0, 1)), 2)]
  return {(x+1, y+1): enhance_x_y(x, y)
          for y in range(-1, n+1)
          for x in range(-1, n+1)}


def solve(part, file):
  data = load_blocks(file)
  algo = [c == '#' for c in data[0][0]]
  grid = {(x, y): c == '#'
          for y, line in enumerate(data[1])
          for x, c in enumerate(line)}

  outside = 0
  n = len(data[1])
  for _ in range((2, 50)[part-1]):
    grid = enhance(grid, algo, outside, n)
    outside = algo[outside * 255]
    n += 2
  return sum(grid.values())


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(35, solve(part=1, file='input-test-1'))
  test(5249, solve(part=1, file='input-real'))

  test(3351, solve(part=2, file='input-test-1'))
  test(15714, solve(part=2, file='input-real'))
