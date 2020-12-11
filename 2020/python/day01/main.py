#!/usr/bin/env python3
import os
import sys
from itertools import *
from collections import *

sys.setrecursionlimit(100000)

def load(filename, script=__file__):
  full_path = os.path.dirname(os.path.realpath(script)) + os.sep + filename
  with open(full_path) as f:
    return f.read().splitlines()

def test(expected, actual):
  template = "PASS ... expected={} actual={}" if expected == actual else "FAIL ... expected={} actual={}"
  print((template).format(expected, actual))

# ----

def load_ints(filename, script=__file__):
  return map(int, load(filename))

def part1(filename):
  A = set(load_ints(filename))
  return next(x*(2020-x) for x in A if 2020-x in A)

def part2(filename):
  A = set(load_ints(filename))
  return next(x*y*(2020-(x+y)) for x,y in product(A,A) if 2020-(x+y) in A)

if __name__== "__main__":
  test(514579, part1('input-test-1.txt'))
  test(1016964, part1('input.txt'))
  
  test(241861950, part2('input-test-1.txt'))
  test(182588480, part2('input.txt'))
