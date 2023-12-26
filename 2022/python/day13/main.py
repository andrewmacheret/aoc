#!/usr/bin/env python3

from common.util import *
from json import loads


def cmp(a, b):
  if isinstance(a, list) and isinstance(b, list):
    for x, y in zip(a, b):
      if (val := cmp(x, y)) != 0:
        return val
    return cmp(len(a), len(b))
  elif isinstance(a, list):
    return cmp(a, [b])
  elif isinstance(b, list):
    return cmp([a], b)
  else:
    return (a > b) - (a < b)


def solve(part, file):
  data = load(file)
  packets = [loads(line) for line in data if line]

  if part == 0:
    return sum(i for i, (a, b) in enumerate(zip(*[iter(packets)]*2), 1) if cmp(a, b) < 1)

  packets += [0, [[2]], [[6]]]
  packets.sort(key=cmp_to_key(cmp))
  return packets.index([[2]]) * packets.index([[6]])


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(13, solve(part=0, file='input-test-1'))
  test(5330, solve(part=0, file='input-real'))

  test(140, solve(part=1, file='input-test-1'))
  test(27648, solve(part=1, file='input-real'))
