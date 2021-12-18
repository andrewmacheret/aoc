#!/usr/bin/env python3

from itertools import permutations, starmap
from functools import reduce

from common.util import load, test, change_dir


def num(obj):
  return isinstance(obj, int)


def combine(*root):
  root = list(root)
  while 1:
    did = 1
    while did:
      root, did = explode(root)[0]
    root, did = split(root)
    if not did:
      return root


def explode(obj, depth=0):
  if not num(obj):
    x, y = obj
    if depth >= 4:
      return (0, 1), (x, y)
    (x, did), (left_val, right_val) = explode(x, depth+1)
    if did:
      return ([x, left(y, right_val) if right_val else y], did), (left_val, 0)
    (y, did), (left_val, right_val) = explode(y, depth+1)
    if did:
      return ([right(x, left_val) if left_val else x, y], did), (0, right_val)
  return (obj, 0), (0, 0)


def split(obj):
  if num(obj):
    return ([obj//2, sum(divmod(obj, 2))], 1) if obj > 9 else (obj, 0)
  x, y = obj
  x, did = split(x)
  if not did:
    y, did = split(y)
  return [x, y], did


def left(obj, val):
  return obj + val if num(obj) else [left(obj[0], val), obj[1]]


def right(obj, val):
  return obj + val if num(obj) else [obj[0], right(obj[1], val)]


def mag(obj):
  return obj if num(obj) else 3*mag(obj[0]) + 2*mag(obj[1])


def solve(part, file):
  snails = list(map(eval, load(file)))
  if part == 1:
    return mag(reduce(combine, snails))
  else:
    return max(map(mag, starmap(combine, permutations(snails, 2))))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(4140, solve(part=1, file='input-test-1'))
  test(4116, solve(part=1, file='input-real'))

  test(3993, solve(part=2, file='input-test-1'))
  test(4638, solve(part=2, file='input-real'))
