#!/usr/bin/env python3

# import networkx as nx
# import numpy as np
# from copy import copy, deepcopy
# import sys
# sys.setrecursionlimit(100000)

from common.util import *


def load_custom(file):
  return [line.split(',') for line in load(file)]


def solve(part, file):
  # data = load_ints(file)
  # data = load_custom(file)
  # data = load_blocks(file)
  # data = load_csv(file)
  data = load(file)

  #

  print(data)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(None, solve(part=0, file='input-test-1'))
  # test(None, solve(part=0, file='input-real'))

  # test(None, solve(part=1, file='input-test-1'))
  # test(None, solve(part=1, file='input-real'))
