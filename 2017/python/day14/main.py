#!/usr/bin/env python3

# import networkx as nx
# import numpy as np
# from copy import copy, deepcopy
# import sys
# sys.setrecursionlimit(100000)

from common.util import *


def knothash(s, size=256):
  lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
  nums = list(range(size))
  pos = skip = 0
  for _ in range(64):
    for x in lengths:
      nums = nums[pos:] + nums[:pos]
      nums[:x] = nums[:x][::-1]
      nums = nums[size-pos:] + nums[:size-pos]
      pos = (pos + x + skip) % size
      skip += 1
  return ''.join(f"{reduce(xor, tup):02x}" for tup in zip(*[iter(nums)]*16))


def solve(part, file):
  key = load_string(file)
  d = {}
  for i in range(128):
    for j, c in enumerate(f'{int(knothash(f"{key}-{i}"), 16):0128b}'):
      if c == '1':
        d[i + j*1j] = 1
  if not part:
    return sum(d.values())

  def dfs(x):
    return d.pop(x, 0) and sum(dfs(y) for y in (x+1, x-1, x+1j, x-1j))

  total = 0
  while d:
    dfs(next(iter(d)))
    total += 1
  return total


### THE REST IS TESTS ###
if __name__ == "__main__":
  change_dir(__file__)

  test(8108, solve(part=0, file='input-test-1'))
  test(8106, solve(part=0, file='input-real'))

  test(1242, solve(part=1, file='input-test-1'))
  test(1164, solve(part=1, file='input-real'))
