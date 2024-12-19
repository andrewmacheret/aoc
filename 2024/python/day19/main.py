#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  input = open(file).read().splitlines()
  a, b = input[0].split(', '), input[2:]

  f = cache(lambda s: sum(f(s[len(c):]) for c in a if s.startswith(c)) if s else 1)
  return sum(map((bool, int)[part], map(f, b)))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(6, solve(part=0, file='input-test-1'))
  test(216, solve(part=0, file='input-real'))

  test(16, solve(part=1, file='input-test-1'))
  test(603191454138773, solve(part=1, file='input-real'))
