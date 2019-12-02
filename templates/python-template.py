#!/usr/bin/env python3
import re
import networkx as nx
import numpy as np
from collections import OrderedDict, defaultdict, deque, Counter
from pprint import pprint
from copy import copy, deepcopy
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge, nlargest, nsmallest
import sys
import io
import os

sys.setrecursionlimit(100000)

class Solution:
  def __init__(self):
    pass

  def load(self, filename):
    self.filename = filename
    with open(os.path.dirname(os.path.realpath(__file__)) + os.sep + filename) as f:
      self.lines = f.read().splitlines()
    return self

  def part1(self):
    pass

  def part2(self):
    pass

print('Part 1 [test]', Solution().load('input-test.txt').part1())
#print('Part 1 [real]', Solution().load('input.txt').part1())

print('Part 2 [test]', Solution().load('input-test.txt').part2())
#print('Part 2 [real]', Solution().load('input.txt').part2())
