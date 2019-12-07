#!/usr/bin/env python3
import os

def load(filename, script=__file__):
  with open(os.path.dirname(os.path.realpath(script)) + os.sep + filename) as f:
    return f.read().splitlines()

def test(expected, actual):
  template = "PASS ... expected={} actual={}" if expected == actual else "FAIL ... expected={} actual={}"
  print((template).format(expected, actual))

def depths(parens):
  depth = 0
  for paren in parens:
    depth += [-1, 1][paren == '(']
    yield depth

def part1(filename):
  parens = load(filename)[0]
  return list(depths(parens))[-1]

def part2(filename):
  parens = load(filename)[0]
  return next(i for i, depth in enumerate(depths(parens), 1) if depth == -1)

if __name__== "__main__":
  test(0, part1('input-test-1.txt'))
  test(0, part1('input-test-2.txt'))
  test(3, part1('input-test-3.txt'))
  test(3, part1('input-test-4.txt'))
  test(3, part1('input-test-5.txt'))
  test(-1, part1('input-test-6.txt'))
  test(-1, part1('input-test-7.txt'))
  test(-3, part1('input-test-8.txt'))
  test(-3, part1('input-test-9.txt'))
  test(232, part1('input.txt'))

  test(1, part2('input-test-10.txt'))
  test(5, part2('input-test-11.txt'))
  test(1783, part2('input.txt'))
