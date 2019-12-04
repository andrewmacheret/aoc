#!/usr/bin/env python3
from collections import Counter
import os

os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
from day01.main import load, test

def is_not_decreasing(indexable):
  return all(a <= b for a, b in zip(indexable, indexable[1:]))

def has_double(indexable):
  return any(a == b for a, b in zip(indexable, indexable[1:]))

def has_exactly_double(indexable):
  return 2 in Counter(indexable).values()

def part1(filename):
  start, end = map(int, load(filename, script=__file__)[0].split('-', 2))
  return sum(1 for s in map(str, range(start, end + 1)) if is_not_decreasing(s) and has_double(s))

def part2(filename):
  start, end = map(int, load(filename, script=__file__)[0].split('-', 2))
  return sum(1 for s in map(str, range(start, end + 1)) if is_not_decreasing(s) and has_exactly_double(s))

if __name__== "__main__":
  test(1, part1('input-test-1.txt'))
  test(0, part1('input-test-2.txt'))
  test(0, part1('input-test-3.txt'))
  test(1605, part1('input.txt'))

  test(1, part2('input-test-4.txt'))
  test(0, part2('input-test-5.txt'))
  test(1, part2('input-test-6.txt'))
  test(1102, part2('input.txt'))
