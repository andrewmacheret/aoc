#!/usr/bin/env python3

from common.util import load, test, parse_nums, change_dir


def solve(part, file):
  x1, x2, y1, y2 = parse_nums(load(file)[0])
  if part == 1:
    return y1*(y1-1)//2

  def tryit(vx, vy):
    x = y = 0
    while y > -y1:
      x += vx
      y += vy
      if vx > 0:
        vx -= 1
      vy -= 1
      if x1 <= x <= x2 and -y1 <= y <= -y2:
        return 1
    return 0

  return sum(tryit(vx, vy) for vx in range(1, x2+1) for vy in range(-y1, y1))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(45, solve(part=1, file='input-test-1'))
  test(3160, solve(part=1, file='input-real'))
  test(112, solve(part=2, file='input-test-1'))
  test(1928, solve(part=2, file='input-real'))
