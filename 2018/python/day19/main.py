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
    return self

  def solve(self):
    pass

print(Solution().load('input-test.txt').solve())
#print(Solution().load('input.txt').solve())
