#!/usr/bin/env python3

from collections import *
from itertools import *
from pprint import pprint
from heapq import *
from operator import *
from functools import *
from bisect import *
from math import *
import re
# import networkx as nx
# import numpy as np
# from copy import copy, deepcopy
# import sys
# import io
# import os
# sys.setrecursionlimit(100000)

from common.util import *


def load_custom(file):
  return [line.split(',') for line in load(file)]


def pixels(number):
  return lambda x, y: x < 0 or y < 0 or bin(x*x + 3*x + 2*x*y + y + y*y + number).count('1') % 2


def solve(part, file, goal=None):
  number = load_ints(file)[0]
  pixel = pixels(number)

  q = [(1, 1)]
  seen = set(q)
  for r in count(1) if part == 1 else range(50):
    q2 = []
    for x, y in q:
      for dx, dy in DIRS_4:
        x1, y1 = x+dx, y+dy
        if (x1, y1) == goal:
          return r
        elif (x1, y1) not in seen and not pixel(x1, y1):
          seen.add((x1, y1))
          q2 += (x1, y1),
    q = q2
  return len(seen)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(11, solve(part=1, goal=(7, 4), file='input-test-1'))
  test(90, solve(part=1, goal=(31, 39), file='input-real'))

  test(135, solve(part=2, file='input-real'))
