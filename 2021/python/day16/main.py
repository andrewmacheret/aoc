#!/usr/bin/env python3

from operator import add, mul, gt, lt, eq
from functools import reduce

from common.util import load, test, change_dir

OPS = (add, mul, min, max, lambda a, b: a*16 + b, gt, lt, eq)


def solve(part, file):
  data = load(file)[0]
  bits = iter(bin(int(data, 16))[2:].zfill(len(data)*4))

  versions = pos = 0

  def read(x):
    nonlocal pos
    pos += x
    return int(''.join(next(bits) for _ in range(x)), 2)

  def parts(type):
    if type == 4:
      while read(1):
        yield read(4)
      yield read(4)
    elif read(1):
      for _ in range(read(11)):
        yield parse()
    else:
      end = read(15) + pos
      while pos != end:
        yield parse()

  def parse():
    nonlocal versions
    versions += read(3)
    type = read(3)
    return reduce(OPS[type], parts(type))

  root = int(parse())
  return (versions, root)[part == 2]


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(6, solve(part=1, file='input-test-1'))
  test(9, solve(part=1, file='input-test-2'))
  test(14, solve(part=1, file='input-test-3'))
  test(16, solve(part=1, file='input-test-4'))
  test(12, solve(part=1, file='input-test-5'))
  test(23, solve(part=1, file='input-test-6'))
  test(31, solve(part=1, file='input-test-7'))
  test(1007, solve(part=1, file='input-real'))

  test(2021, solve(part=2, file='input-test-1'))
  test(1, solve(part=2, file='input-test-2'))
  test(3, solve(part=2, file='input-test-3'))
  test(15, solve(part=2, file='input-test-4'))
  test(46, solve(part=2, file='input-test-5'))
  test(46, solve(part=2, file='input-test-6'))
  test(54, solve(part=2, file='input-test-7'))
  test(3, solve(part=2, file='input-test-8'))
  test(54, solve(part=2, file='input-test-9'))
  test(7, solve(part=2, file='input-test-10'))
  test(9, solve(part=2, file='input-test-11'))
  test(1, solve(part=2, file='input-test-12'))
  test(0, solve(part=2, file='input-test-13'))
  test(0, solve(part=2, file='input-test-14'))
  test(1, solve(part=2, file='input-test-15'))
  test(834151779165, solve(part=2, file='input-real'))
