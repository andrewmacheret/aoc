#!/usr/bin/env python3
from collections import Counter
from itertools import islice
import os

os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
from day01.main import load, test

def is_sorted(iterable):
  return all(a <= b for a, b in zip(iterable, islice(iterable, 1, None)))

def has_at_least_n(iterable, n):
  return any(i >= n for i in Counter(iterable).values())

def has_exactly_n(iterable, n):
  return n in Counter(iterable).values()

def solve(filename, extra_check):
  start, end = map(int, load(filename, script=__file__)[0].split('-', 2))
  return sum(is_sorted(s) and extra_check(s, 2) for s in map(str, range(start, end + 1)))

def part1(filename):
  return solve(filename, has_at_least_n)

def part2(filename):
  return solve(filename, has_exactly_n)

if __name__== "__main__":
  test(1, part1('input-test-1.txt'))
  test(0, part1('input-test-2.txt'))
  test(0, part1('input-test-3.txt'))
  test(1605, part1('input.txt'))

  test(1, part2('input-test-4.txt'))
  test(0, part2('input-test-5.txt'))
  test(1, part2('input-test-6.txt'))
  test(1102, part2('input.txt'))
