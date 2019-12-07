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

def load_custom(filename, script=__file__):
  return [line.split(',') for line in load(filename, script=script)]

def part1(filename):
  data = load_custom(filename)
  return None

# def part2(filename):
#   data = load_custom(filename)
#   return None

if __name__== "__main__":
  test(None, part1('input-test-1.txt'))
  # test(None, part1('input.txt'))
  # 
  # test(None, part2('input-test-1.txt'))
  # test(None, part2('input.txt'))
