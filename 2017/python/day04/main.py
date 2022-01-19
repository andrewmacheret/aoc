#!/usr/bin/env python3

from common.util import *


def mapper1(token):
  return token


def mapper2(token):
  return tuple(sorted(Counter(token).items()))


def solve(part, file):
  data = load_tokens(file)
  mapper = (mapper1, mapper2)[part]
  return sum(len(set(map(mapper, tokens))) == len(tokens) for tokens in data)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(1, solve(part=0, file='input-test-1'))
  test(0, solve(part=0, file='input-test-2'))
  test(1, solve(part=0, file='input-test-3'))
  test(337, solve(part=0, file='input-real'))

  test(1, solve(part=1, file='input-test-4'))
  test(0, solve(part=1, file='input-test-5'))
  test(1, solve(part=1, file='input-test-6'))
  test(1, solve(part=1, file='input-test-7'))
  test(0, solve(part=1, file='input-test-8'))
  test(231, solve(part=1, file='input-real'))
