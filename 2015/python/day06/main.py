#!/usr/bin/env python3
import re
from itertools import zip_longest

from day01.main import load, test

actions = {
  'binary': {
    'turn on': lambda grid, x, y: 1,
    'turn off': lambda grid, x, y: 0,
    'toggle': lambda grid, x, y: 1 - grid[x, y],
  },
  'dimmable': {
    'turn on': lambda grid, x, y: grid[x, y] + 1,
    'turn off': lambda grid, x, y: max(grid[x, y] - 1, 0),
    'toggle': lambda grid, x, y: grid[x, y] + 2,
  }
}

def grouper(iterable, n, fillvalue=None):
  args = [iter(iterable)] * n
  return zip_longest(fillvalue=fillvalue, *args)

def parse_coords(int_strings):
  return grouper(map(int, int_strings), 2)
  
def load_instructions(filename, script=__file__):
  instructions = [re.match(r'(.*) (\d+),(\d+) through (\d+),(\d+)', line).groups() for line in load(filename, script=script)]
  return [(action, parse_coords(coords)) for action, *coords in instructions]

def follow(instructions, actions):
  grid = {(x, y): 0 for x in range(1000) for y in range(1000)}
  for action, ((x1, y1), (x2, y2)) in instructions:
    for x in range(x1, x2+1):
      for y in range(y1, y2+1):
        grid[x, y] = actions[action](grid, x, y)
  return sum(grid[x, y] for x in range(1000) for y in range(1000))

def solve(filename, action_group):
  instructions = load_instructions(filename)
  return follow(instructions, actions[action_group])

def part1(filename):
  return solve(filename, 'binary')

def part2(filename):
  return solve(filename, 'dimmable')

if __name__== "__main__":
  test(998996, part1('input-test-1.txt'))
  test(377891, part1('input.txt'))
  
  test(2000001, part2('input-test-2.txt'))
  test(14110788, part2('input.txt'))
