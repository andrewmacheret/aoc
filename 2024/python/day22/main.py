#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  def step(x):
    x = ((x<<6) ^ x) % 16777216
    x = ((x>>5) ^ x) % 16777216
    x = ((x<<11) ^ x) % 16777216
    return x

  firsts = defaultdict(int)
  total = 0
  for line in load(file):
    seen = set()
    x = int(line)
    a = b = c = d = None
    for _ in range(2000):
      last = x % 10
      x = step(x)
      val = x % 10
      diff = val - last
      a, b, c, d = b, c, d, diff
      if a is not None and (a,b,c,d) not in seen:
        seen.add((a,b,c,d))
        firsts[a,b,c,d] += val
    total += x
  return (total, max(firsts.values()))[part]


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(37327623, solve(part=0, file='input-test-1'))
  test(14082561342, solve(part=0, file='input-real'))

  test(23, solve(part=1, file='input-test-2'))
  test(1568, solve(part=1, file='input-real'))
