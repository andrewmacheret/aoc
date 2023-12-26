#!/usr/bin/env python3

from common.util import *


def part1(data):
  return (set(line[:len(line)//2]) & set(line[len(line)//2:]) for line in data)


def part2(data):
  return (reduce(and_, map(set, lines)) for lines in zip(*[iter(data)]*3))


def priority(s):
  return sum(ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27 for c in s)


def solve(part, file):
  return sum(map(priority, [part1, part2][part](load(file))))


### THE REST IS TESTS ###
if __name__ == "__main__":
  change_dir(__file__)

  test(157, solve(part=0, file='input-test-1'))
  test(8394, solve(part=0, file='input-real'))

  test(70, solve(part=1, file='input-test-1'))
  test(2413, solve(part=1, file='input-real'))
