#!/usr/bin/env python3
import os

def load(filename):
  with open(os.path.dirname(os.path.realpath(__file__)) + os.sep + filename) as f:
    return f.read().splitlines()

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
  instructions_list = [line.split(',') for line in load(filename)]
  intersections = set.intersection(*[set(wire_positions(instructions)) for instructions in instructions_list])
  return closest_to_zero_by_manhattan(intersections)

def part2(filename):
  instructions_list = [line.split(',') for line in load(filename)]
  intersections = dict.fromkeys(set.intersection(*[set(wire_positions(instructions)) for instructions in instructions_list]), 0)
  for instructions in instructions_list:
    for dist, coord in enumerate(wire_positions(instructions), 1):
      if coord in intersections:
        intersections[coord] += dist
  return min(intersections.values())

print(6, part1('input-test-1.txt'))
print(159, part1('input-test-2.txt'))
print(135, part1('input-test-3.txt'))
print(2427, part1('input.txt'))

print(30, part2('input-test-1.txt'))
print(610, part2('input-test-2.txt'))
print(410, part2('input-test-3.txt'))
print(27890, part2('input.txt'))
