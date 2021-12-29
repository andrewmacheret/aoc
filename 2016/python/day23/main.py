#!/usr/bin/env python3

from math import factorial

from common.util import load, test, change_dir


def parse_instructions(lines):
  return [[int(c) if c[-1].isdigit() else c for c in line.split()] for line in lines]


def solve(part, file):
  lines = load(file)
  instructions = parse_instructions(lines)
  return instructions[19][1] * instructions[20][1] + factorial((7, 12)[part-1])


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(10953, solve(part=1, file='input-real'))

  test(479007513, solve(part=2, file='input-real'))
