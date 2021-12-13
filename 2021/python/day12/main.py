#!/usr/bin/env python3

from collections import defaultdict

from common.util import load, test, change_dir


def solve(part, file):
  data = load(file)
  graph = defaultdict(list)
  for line in data:
    a, b = line.split('-')
    graph[a] += b,
    graph[b] += a,

  def dfs(node, visited, mulligans):
    added = 0
    if node == 'end':
      return 1
    elif node.islower():
      if node in visited and (node == 'start' or not mulligans):
        return 0
      elif node in visited:
        mulligans -= 1
      else:
        added = 1
        visited.add(node)
    try:
      return sum(dfs(g, visited, mulligans) for g in graph[node])
    finally:
      if added:
        visited.remove(node)

  return dfs('start', set(), part - 1)

# THE REST IS TESTS #


if __name__ == "__main__":
  change_dir(__file__)

  test(10, solve(part=1, file='input-test-1'))
  test(19, solve(part=1, file='input-test-2'))
  test(226, solve(part=1, file='input-test-3'))
  test(3738, solve(part=1, file='input-real'))

  test(36, solve(part=2, file='input-test-1'))
  test(103, solve(part=2, file='input-test-2'))
  test(3509, solve(part=2, file='input-test-3'))
  test(120506, solve(part=2, file='input-real'))
