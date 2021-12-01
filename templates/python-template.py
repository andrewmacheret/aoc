#!/usr/bin/env python3

from collections import *
from itertools import *
from pprint import pprint
from heapq import *
from operator import *
from functools import *
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


def solve(part, file):
  # data = load_ints(file)
  data = load_custom(file)
  print(data)
  if part == 2:
    pass
  return None


if __name__ == "__main__":
  change_dir(__file__)

  test(None, solve(part=1, file='input-test-1'))
  # test(None, solve(part=1, file='input'))

  # test(None, solve(part=2, file='input-test-1'))
  # test(None, solve(part=2, file='input'))
