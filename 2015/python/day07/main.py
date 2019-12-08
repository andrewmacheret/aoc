#!/usr/bin/env python3
import re
import networkx as nx
from collections import *
from itertools import *
from pprint import pprint
from copy import copy, deepcopy
from heapq import *
import sys
import io
import os

sys.setrecursionlimit(100000)

from day01.main import load, test

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def parse_instruction(expression):
  parts = expression.split(' ')
  vars = [var for var in parts if re.match(r'[a-z]+', var)]
  var = lambda w, s: int(s) if re.match(r'\d+', s) else w[s]
  if len(parts) == 1: return lambda w: var(w, parts[0]), vars
  if len(parts) == 2: return lambda w: ~var(w, parts[1]) & 65535, vars
  a, op, b = parts
  return {
    'AND': lambda w: var(w, a) & var(w, b),
    'OR': lambda w: var(w, a) | var(w, b),
    'LSHIFT': lambda w: (var(w, a) << var(w, b)) & 65535,
    'RSHIFT': lambda w: var(w, a) >> var(w, b)
  }[op], vars

def load_instructions(filename, script=__file__):
  instructions = [line.split(' -> ') for line in load(filename, script=script)]
  return {target: parse_instruction(expression) for expression, target in instructions}

def emulate(ops):
  g = nx.DiGraph()
  for target, (op, vars) in ops.items():
      for var in vars:
          g.add_edge(var, target)

  wires = defaultdict(int)
  for target in nx.topological_sort(g):
    op, vars = ops[target]
    wires[target] = op(wires)
  return wires

def solve(filename, letter, override_letter=None):
  ops = load_instructions(filename)
  if override_letter:
    value = solve(filename, letter)
    ops[override_letter] = lambda w: value, []
  return emulate(ops)[letter]

if __name__== "__main__":
  test(72, solve('input-test-1.txt', 'd'))
  test(507, solve('input-test-1.txt', 'e'))
  test(492, solve('input-test-1.txt', 'f'))
  test(114, solve('input-test-1.txt', 'g'))
  test(65412, solve('input-test-1.txt', 'h'))
  test(65079, solve('input-test-1.txt', 'i'))
  test(123, solve('input-test-1.txt', 'x'))
  test(456, solve('input-test-1.txt', 'y'))
  test(16076, solve('input.txt', 'a'))
  
  test(2797, solve('input.txt', 'a', override_letter='b'))
