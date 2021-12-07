#!/usr/bin/env python3

from math import floor, ceil

from common.util import load, parse_nums, test, change_dir


def solve(part, file):
  data = [*map(parse_nums, load(file))][0]
  data.sort()
  if part == 1:
    def cost(x): return x
    possible = (data[len(data)//2],)
  else:
    def cost(x): return x * (x+1) // 2
    avg = sum(data) / len(data)
    possible = (floor(avg), ceil(avg))
  return min(sum(cost(abs(x - y)) for x in data) for y in possible)


if __name__ == "__main__":
  change_dir(__file__)

  test(37, solve(part=1, file='input-test-1'))
  test(343441, solve(part=1, file='input-real'))

  test(168, solve(part=2, file='input-test-1'))
  test(98925151, solve(part=2, file='input-real'))
