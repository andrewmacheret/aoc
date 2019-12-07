#!/usr/bin/env python3
import re
import networkx as nx
import numpy as np
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

arrows = {
  '>': (1, 0),
  '^': (0, -1),
  '<': (-1, 0),
  'v': (0, 1)
}

def load_steps(filename, script=__file__):
  return load(filename, script=__file__)[0]

def follow(steps):
  x, y = 0, 0
  yield x, y
  for step in steps:
    dx, dy = arrows[step]
    x, y = x+dx, y+dy
    yield x, y

def part1(filename):
  steps = load_steps(filename)
  return len(set(follow(steps)))

def part2(filename):
  steps = load_steps(filename)
  return len(set(chain(follow(islice(steps, 0, None, 2)), follow(islice(steps, 1, None, 2)))))

if __name__== "__main__":
  test(2, part1('input-test-1.txt'))
  test(4, part1('input-test-2.txt'))
  test(2, part1('input-test-3.txt'))
  test(2565, part1('input.txt'))
  
  test(3, part2('input-test-4.txt'))
  test(3, part2('input-test-2.txt'))
  test(11, part2('input-test-3.txt'))
  test(2639, part2('input.txt'))
