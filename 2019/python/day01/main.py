#!/usr/bin/env python3
import os

class Solution:
  def __init__(self):
    pass

  def load(self, filename):
    self.filename = filename
    with open(os.path.dirname(os.path.realpath(__file__)) + os.sep + filename) as f:
      self.fuels = map(int, f.read().splitlines())
    return self

  def reduce(self, fuel):
    return fuel // 3 - 2

  def reduce_until_zero(self, fuel):
    while True:
      fuel = self.reduce(fuel)
      if fuel <= 0: return
      yield fuel

  def part1(self):
    # take its mass, divide by three, round down, and subtract 2.
    return sum(self.reduce(fuel) for fuel in self.fuels)

  def part2(self):
    # repeat over and over
    return sum(sum(self.reduce_until_zero(fuel)) for fuel in self.fuels)

print('Part 1 ...', Solution().load('input.txt').part1())

print('Part 2 ...', Solution().load('input.txt').part2())
