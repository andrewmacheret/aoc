#!/usr/bin/env python3

from common.util import *

def solve(steps, file):
  nodes = Counter(parse_nums(load(file)[0]))

  for _ in range(steps):
    next_nodes = Counter()
    for k,v in nodes.items():
      if k == 0:
        next_nodes[1] += v
      elif (x := len(s := str(k))) & 1 == 0:
        next_nodes[int(s[:x>>1])] += v
        next_nodes[int(s[x>>1:])] += v
      else:
        next_nodes[k*2024] += v
    nodes = next_nodes
  return sum(nodes.values())


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(7, solve(steps=1, file='input-test-1'))
  test(22, solve(steps=6, file='input-test-2'))
  test(55312, solve(steps=25, file='input-test-2'))
  test(202019, solve(steps=25, file='input-real'))

  test(239321955280205, solve(steps=75, file='input-real'))
