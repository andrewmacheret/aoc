#!/usr/bin/env python3

from common.util import *


def spinlock(steps, times):
  pos = 0
  for t in range(1, times+1):
    pos = (pos + steps) % t + 1
    yield t, pos


def spinlock1(steps, times):
  q = [0]
  for t, pos in spinlock(steps, times):
    q.insert(pos, t)
  return q[(pos + 1) % t]


def spinlock2(steps, times):
  return last(t for t, pos in spinlock(steps, times) if pos == 1)


def solve(part, file):
  steps = load_int(file)
  if part == 0:
    return spinlock1(steps, 2017)
  else:
    return spinlock2(steps, 50000000)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(638, solve(part=0, file='input-test-1'))
  test(1311, solve(part=0, file='input-real'))

  test(1222153, solve(part=1, file='input-test-1'))
  test(39170601, solve(part=1, file='input-real'))
