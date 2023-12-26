#!/usr/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt 
import sys
sys.setrecursionlimit(100000)

from common.util import *

def solve(file, cuts=[], draws=[]):
  g = defaultdict(list)
  edges = set()
  for line in load(file):
    a, *x = line.split(' ')
    a = a.strip(':')
    for b in x:
      edges.add(tuple(sorted([a,b])))
      g[a].append(b)
      g[b].append(a)

  for c in cuts:
    a, b = c.split('/')
    edges.remove(tuple(sorted([a,b])))
    g[a].remove(b)
    g[b].remove(a)

  # copied from https://www.geeksforgeeks.org/visualize-graphs-in-python/
  G = nx.Graph() 
  G.add_edges_from(edges) 
  nx.draw_networkx(G) 
  plt.show()

  def dfs(a, seen):
    if a in seen:
      return
    seen.add(a)
    yield a
    for b in g.get((a), []):
      yield from dfs(b, seen)

  x, y = (len(list(dfs(d, set()))) for d in draws)
  # print(x,y)
  return x * y


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(54, solve(file='input-test-1', cuts=['hfx/pzl', 'bvb/cmg', 'nvd/jqt'], draws=['hfx', 'cmg']))
  test(571753, solve(file='input-real', cuts=['szl/kcn', 'lzd/fbd', 'ptq/fxn'], draws=['drf', 'psp']))
