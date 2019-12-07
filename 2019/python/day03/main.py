#!/usr/bin/env python3
import os

from day01.main import load, test

DIRS = { 'R': (1, 0), 'U': (0, -1), 'L': (-1, 0), 'D': (0, 1) }

def wire_positions(instructions):
  x, y = 0, 0
  for instruction in instructions:
    dx, dy = DIRS[instruction[0]]
    for _ in range(int(instruction[1:])):
      x, y = x + dx, y + dy
      yield x, y

def closest_to_zero_by_manhattan(coords):
  return min(abs(x) + abs(y) for x, y in coords)

def part1(filename):
  instructions_list = [line.split(',') for line in load(filename, script=__file__)]
  intersections = set.intersection(*[set(wire_positions(instructions)) for instructions in instructions_list])
  return closest_to_zero_by_manhattan(intersections)

def part2(filename):
  instructions_list = [line.split(',') for line in load(filename, script=__file__)]
  intersections = dict.fromkeys(set.intersection(*[set(wire_positions(instructions)) for instructions in instructions_list]), 0)
  for instructions in instructions_list:
    for dist, coord in enumerate(wire_positions(instructions), 1):
      if coord in intersections:
        intersections[coord] += dist
  return min(intersections.values())

if __name__== "__main__":
  test(6, part1('input-test-1.txt'))
  test(159, part1('input-test-2.txt'))
  test(135, part1('input-test-3.txt'))
  test(2427, part1('input.txt'))

  test(30, part2('input-test-1.txt'))
  test(610, part2('input-test-2.txt'))
  test(410, part2('input-test-3.txt'))
  test(27890, part2('input.txt'))
