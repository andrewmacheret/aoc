#!/usr/bin/env python3

from common.util import *


def to_snafu(val):
  return ''.join(('=-012'[(x + 2) % 5] for x in takewhile((0).__lt__, accumulate(repeat(val), lambda x, _: (x + 2) // 5))))[::-1]


def from_snafu(snafu):
  return sum(('=-012'.index(c)-2) * 5**i for i, c in enumerate(snafu[::-1]))


def solve(file):
  return to_snafu(sum(map(from_snafu, load(file))))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test("2=-1=0", solve(file='input-test-1'))
  test("2---0-1-2=0=22=2-011", solve(file='input-real'))
