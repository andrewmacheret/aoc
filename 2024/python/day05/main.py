#!/usr/bin/env python3

import networkx as nx

from common.util import *


def solve(part, file):
  block1, block2 = load_blocks(file)
  rules = [[*map(int, row.split('|'))] for row in block1]
  total = 0

  for line in block2:
    pages = list(map(int, line.split(',')))
    pages_set = set(pages)
    g = nx.DiGraph()
    for pre, post in rules:
      if pre in pages_set and post in pages_set:
        g.add_edge(pre, post)
    
    pages2 = [*nx.topological_sort(g)]
    if part == 0 and pages == pages2:
      total += pages[len(pages) // 2]
    elif part == 1 and pages != pages2:
      total += pages2[len(pages2) // 2]

  return total


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(143, solve(part=0, file='input-test-1'))
  test(6505, solve(part=0, file='input-real'))

  test(123, solve(part=1, file='input-test-1'))
  test(6897, solve(part=1, file='input-real'))
