#!/usr/bin/env python3

from common.util import *


digits = list(enumerate((map(str, range(1, 10))), 1))
words = list(enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], 1))

def search(line, terms):
  a = min((line.index(term), i) for i, term in terms if term in line)[1]
  b = max((line.rindex(term), i) for i, term in terms if term in line)[1]
  return a * 10 + b

def solve(part, file):
  return sum(search(line, digits if part == 0 else digits + words) for line in load(file))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(142, solve(part=0, file='input-test-1'))
  test(55123, solve(part=0, file='input-real'))

  test(281, solve(part=1, file='input-test-2'))
  test(55260, solve(part=1, file='input-real'))
