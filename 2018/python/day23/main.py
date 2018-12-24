import re
import networkx as nx
import numpy as np
from collections import OrderedDict, defaultdict, deque, Counter
from pprint import pprint
from copy import copy, deepcopy
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge, nlargest, nsmallest
import sys
import io

sys.setrecursionlimit(100000)

class Solution:
  def __init__(self):
    pass

  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()

    self.bots = []
    for line in self.lines:
      match = re.match(r'^pos=<([^,]*),([^,]*),([^,]*)>, r=([^,]*)$', line)
      self.bots.append({
        'pos': (int(match.group(1)), int(match.group(2)), int(match.group(3))),
        'radius': int(match.group(4))
      })

    return self

  def distance(self, (x1, y1, z1), (x2, y2, z2)):
    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

  def solve(self):
    max_radius = max(bot['radius'] for bot in self.bots)
    best_bot = next(bot for bot in self.bots if bot['radius'] == max_radius)
    in_range = sum(1 for bot in self.bots if self.distance(bot['pos'], best_bot['pos']) <= max_radius)

    return {
      'part1': in_range,
    }


print(Solution().load('input-test.txt').solve())
print(Solution().load('input-test2.txt').solve())
print(Solution().load('input.txt').solve())
