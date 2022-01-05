#!/usr/bin/env python3

from itertools import groupby

from common.util import load_ints, test, change_dir


def load_custom(file):
  return [line.split(',') for line in load(file)]


def solve(part, goal, file):
  dp = [[] for _ in range(151)]
  dp[0].append([])
  jugs = sorted(load_ints(file))

  def backtrack(i, remaining, count=0):
    if i < 0:
      if remaining == 0:
        yield count
    else:
      yield from backtrack(i-1, remaining, count)
      if remaining >= jugs[i]:
        yield from backtrack(i-1, remaining - jugs[i], count + 1)

  res = list(backtrack(len(jugs)-1, goal))
  if part == 2:
    res = list(next(groupby(sorted(res)))[1])
  return len(res)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(4, solve(part=1, goal=25, file='input-test-1'))
  test(4372, solve(part=1, goal=150, file='input-real'))

  test(3, solve(part=2, goal=25, file='input-test-1'))
  test(4, solve(part=2, goal=150, file='input-real'))
