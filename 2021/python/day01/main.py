#!/usr/bin/env python3
import os

from itertools import *
from operator import *


# common stuff


def load(filename, script=__file__):
  full_path = os.path.dirname(os.path.realpath(script)) + os.sep + filename
  with open(full_path) as f:
    return f.read().splitlines()


def load_ints(filename, script=__file__):
  return list(map(int, load(filename, script)))


def test(expected, actual):
  template = "PASS ... expected={} actual={}" if expected == actual else "FAIL ... expected={} actual={}"
  print((template).format(expected, actual))


# ----


def count_increasing(data):
  return sum(map(lt, data, data[1:]))


def triplet_sums(data):
  return map(sum, zip(data, data[1:], data[2:]))


def part1(filename):
  data = load_ints(filename)
  return count_increasing(data)


def part2(filename):
  data = load_ints(filename)
  triplets = list(triplet_sums(data))
  return count_increasing(triplets)


if __name__ == "__main__":
  test(7, part1('input-test-1.txt'))
  test(1215, part1('input.txt'))

  test(5, part2('input-test-1.txt'))
  test(1150, part2('input.txt'))
