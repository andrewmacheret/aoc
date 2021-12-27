#!/usr/bin/env python3

from operator import mul, sub, itemgetter
from functools import reduce

from common.util import load, test, change_dir, parse_nums


def chinese_remainder(a_n):
  sum = 0
  prod = reduce(mul, map(itemgetter(1), a_n))
  for a_i, n_i in a_n:
    p = prod // n_i
    sum += a_i * mul_inv(p, n_i) * p
  return sum % prod, prod


def mul_inv(a, b):
  b0 = b
  x0, x1 = 0, 1
  if b == 1:
    return 1
  while a > 1:
    q = a // b
    a, b = b, a % b
    x0, x1 = x1 - q * x0, x0
  if x1 < 0:
    x1 += b0
  return x1


def load_discs(file):
  return [parse_nums(line)[3::-2] for line in load(file)]


def solve(part, file):
  discs = load_discs(file)
  if part == 2:
    discs.append([0, 11])
  for i in range(len(discs)):
    x, size = discs[i]
    discs[i][0] = (x+i+1) % size
  return -sub(*chinese_remainder(discs))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(5, solve(part=1, file='input-test-1'))
  test(148737, solve(part=1, file='input-real'))

  test(85, solve(part=2, file='input-test-1'))
  test(2353212, solve(part=2, file='input-real'))
