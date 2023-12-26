#!/usr/bin/env python3

# import networkx as nx
# import numpy as np
# from copy import copy, deepcopy
# import sys
# sys.setrecursionlimit(100000)

from common.util import *


def find_path(g, path, node, goals):
  for r in count():
    for i, d in enumerate(path):
      node = g[node][d == 'R']
      if node in goals:
        return r*len(path) + i + 1

def solve(part, file):
  paths, nodes = load_blocks(file)

  g = {}
  for line in nodes:
    a,b,c = re.findall('\w+', line)
    g[a] = [b,c]

  starts, goals = ([{x*3}, {c for c in g if c[2] == x}][part] for x in 'AZ')
  return reduce(lcm, (find_path(g, paths[0], c, goals) for c in starts))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(2, solve(part=0, file='input-test-1'))
  test(6, solve(part=0, file='input-test-2'))
  test(14893, solve(part=0, file='input-real'))

  test(6, solve(part=1, file='input-test-3'))
  test(10241191004509, solve(part=1, file='input-real'))
