#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  d = {k: vals for k, *vals in map(parse_nums, load(file))}
  for g in takewhile(lambda _: d, count(1)) if part else [0]:
    q = deque([min(d)])
    while q:
      q.extend(d.pop(q.popleft(), []))
  return g if part else len(load(file)) - len(d)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(6, solve(part=0, file='input-test-1'))
  test(306, solve(part=0, file='input-real'))

  test(2, solve(part=1, file='input-test-1'))
  test(200, solve(part=1, file='input-real'))
