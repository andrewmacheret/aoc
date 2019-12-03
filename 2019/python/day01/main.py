#!/usr/bin/env python3
import os

def load(filename, script=__file__):
  with open(os.path.dirname(os.path.realpath(script)) + os.sep + filename) as f:
    return f.read().splitlines()

def test(expected, actual):
  template = "PASS ... expected={} actual={}" if expected == actual else "FAIL ... expected={} actual={}"
  print((template).format(expected, actual))

def reduce(fuel):
  return fuel // 3 - 2

def reduce_until_zero(fuel):
  while True:
    fuel = reduce(fuel)
    if fuel <= 0: return
    yield fuel

def load_ints(filename, script=__file__):
  return map(int, load(filename, script=script))

def part1(filename):
  fuels = load_ints(filename)
  # take its mass, divide by three, round down, and subtract 2.
  return sum(reduce(fuel) for fuel in fuels)

def part2(filename):
  fuels = load_ints(filename)
  # repeat over and over
  return sum(sum(reduce_until_zero(fuel)) for fuel in fuels)

if __name__== "__main__":
  test(2, part1('input-test-1.txt'))
  test(2, part1('input-test-2.txt'))
  test(654, part1('input-test-3.txt'))
  test(33583, part1('input-test-4.txt'))
  test(3538016, part1('input.txt'))

  test(2, part2('input-test-1.txt'))
  test(2, part2('input-test-2.txt'))
  test(966, part2('input-test-3.txt'))
  test(50346, part2('input-test-4.txt'))
  test(5304147, part2('input.txt'))
