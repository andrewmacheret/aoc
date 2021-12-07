#!/usr/bin/env python3

from math import floor, ceil

from common.util import load, parse_nums, test, change_dir


def compute(data, cost_fn, *possible):
  return min(sum(cost_fn(abs(x - y)) for x in data) for y in possible)


def solve(part, file):
  data = [*map(parse_nums, load(file))][0]
  if part == 1:
    return compute(data, lambda x: x, sorted(data)[len(data)//2])
  else:
    avg = sum(data) / len(data)
    return compute(data, lambda x: x*(x+1)//2, *{floor(avg), ceil(avg)})


if __name__ == "__main__":
  change_dir(__file__)

  test(37, solve(part=1, file='input-test-1'))
  test(343441, solve(part=1, file='input-real'))

  test(168, solve(part=2, file='input-test-1'))
  test(98925151, solve(part=2, file='input-real'))
