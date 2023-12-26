#!/usr/bin/env python3

# import networkx as nx
# import numpy as np
# from copy import copy, deepcopy
# import sys
# sys.setrecursionlimit(100000)

from common.util import *

import z3


def solve(part, file):
  nodes = {line[:4]: line.split()[1:] for line in load(file)}

  if part:
    nodes['humn'] = [x := z3.Int('x')]
    nodes['root'][1] = '=='

  def calc(name):
    node = nodes[name]
    if len(node) == 1:
      return int(v) if isinstance(v := node[0], str) else v
    a, op, b = node
    a, b = map(calc, (a, b))
    return {'+': add, '-': sub, '*': mul, '/': truediv, '==': eq}[op](a, b)

  res = calc('root')

  if part == 0:
    return int(res)

  s = z3.Solver()
  s.add(res)
  s.check()
  return s.model()[x].as_long()


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(152, solve(part=0, file='input-test-1'))
  test(268597611536314, solve(part=0, file='input-real'))

  test(301, solve(part=1, file='input-test-1'))
  test(3451534022348, solve(part=1, file='input-real'))
