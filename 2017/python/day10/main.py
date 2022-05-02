#!/usr/bin/env python3

# import networkx as nx
# import numpy as np
# from copy import copy, deepcopy
# import sys
# sys.setrecursionlimit(100000)

from common.util import *


def knothash(s, size=256, part=1):
  if part == 0:
    lengths = parse_nums(s)
  else:
    lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
  nums = list(range(size))
  pos = skip = 0
  for _ in range((1, 64)[part]):
    for x in lengths:
      nums = nums[pos:] + nums[:pos]
      nums[:x] = nums[:x][::-1]
      nums = nums[size-pos:] + nums[:size-pos]
      pos = (pos + x + skip) % size
      skip += 1
  if part:
    return ''.join(f"{reduce(xor, tup):02x}" for tup in zip(*[iter(nums)]*16))
  return nums[0] * nums[1]


def solve(part, file, size=256):
  data = load_string(file)
  return knothash(data, size, part)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(12, solve(part=0, file='input-test-1', size=5))
  test(4114, solve(part=0, file='input-real'))

  test('a2582a3a0e66e6e86e3812dcb672a272', solve(part=1, file='input-test-2'))
  test('33efeb34ea91902bb2f59c9920caa6cd', solve(part=1, file='input-test-3'))
  test('3efbe78a8d82f29979031a4aa0b16a9d', solve(part=1, file='input-test-4'))
  test('63960835bcdc130f0b66d7ff4f6a5a8e', solve(part=1, file='input-test-5'))
  test('2f8c3d2100fdd57cec130d928b0fd2dd', solve(part=1, file='input-real'))
