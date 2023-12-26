#!/usr/bin/env python3

from common.util import *


def bfs(start, expand, is_goal):
  seen = {start}
  q = deque([(0, start)])
  while q:
    r, x = q.popleft()
    if is_goal(x):
      yield r, x
    else:
      for y in expand(x):
        if y not in seen:
          seen.add(y)
          q.append((r+1, y))


class MaxDict(dict):
  def __init__(self, items):
    for k, v in items:
      self[k] = max(self.get(k, 0), v)


def solve(part, file):
  data = load(file)

  paths = {}
  rates = {}
  for line in data:
    _, node, _, _, rate, _, _, _, _, *dests = line.split()
    rates[node] = int(rate[5:-1])
    paths[node] = [dest.rstrip(',') for dest in dests]

  positive_nodes = [node for node, rate in rates.items() if rate > 0]

  costs = {(a, b): next(bfs(a, paths.__getitem__, b.__eq__))[0] + 1
           for a, b in permutations(['AA'] + positive_nodes, 2)}

  limit = [30, 26][part]

  def dfs(root, cost, pressure, path):
    yield tuple(sorted(path)), pressure
    for node in positive_nodes - path.keys():
      if (new_cost := cost + costs[root, node]) <= limit:
        new_pressure = pressure + (limit - new_cost) * rates[node]
        yield from dfs(node, new_cost, new_pressure, path | {node: 1})

  bests = MaxDict(dfs('AA', 0, 0, OrderedDict()))

  if part == 0:
    print(len(bests))
    return max(bests.values())
  else:
    print(len(bests))
    print(sum(1 for a, b in permutations(bests, 2) if not set(a) & set(b)))
    return max(bests[a] + bests[b] for a, b in permutations(bests, 2) if not set(a) & set(b))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(1651, solve(part=0, file='input-test-1'))
  test(1638, solve(part=0, file='input-real'))

  test(1707, solve(part=1, file='input-test-1'))
  test(2400, solve(part=1, file='input-real'))
