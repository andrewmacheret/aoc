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

pattern = re.compile(r'\((\d+)x(\d+)\)')


def decompress(s, recursive):
  i = 0
  while i < len(s):
    c = s[i]
    if c == '(':
      m = pattern.match(s, i)
      size, times = map(int, m.groups())
      j = m.end()
      i = j + size
      if recursive:
        yield sum(decompress(s[j:i], 1)) * times
      else:
        yield (i-j) * times
    else:
      yield 1
      i += 1


def solve(part, file):
  data = load(file)[0]
  return sum(decompress(data, part == 2))


if __name__ == "__main__":
  change_dir(__file__)

  test(len("ADVENT"), solve(part=1, file='input-test-1'))
  test(len("ABBBBBC"), solve(part=1, file='input-test-2'))
  test(len("XYZXYZXYZ"), solve(part=1, file='input-test-3'))
  test(len("ABCBCDEFEFG"), solve(part=1, file='input-test-4'))
  test(len("(1x3)A"), solve(part=1, file='input-test-5'))
  test(len("X(3x3)ABC(3x3)ABCY"), solve(part=1, file='input-test-6'))
  test(112830, solve(part=1, file='input-real'))

  test(len('XYZXYZXYZ'), solve(part=2, file='input-test-3'))
  test(len('XABCABCABCABCABCABCY'), solve(part=2, file='input-test-6'))
  test(241920, solve(part=2, file='input-test-7'))
  test(445, solve(part=2, file='input-test-8'))
  test(10931789799, solve(part=2, file='input-real'))
