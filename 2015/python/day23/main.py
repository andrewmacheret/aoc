#!/usr/bin/env python3

from common.util import load, test, change_dir


def load_instructions(file):
  return [line.replace(',', '').split() for line in load(file)]


def sim(instructions, vars):
  idx = 0
  while 0 <= idx < len(instructions):
    instruction, *args = instructions[idx]
    idx += 1
    if instruction == 'inc':
      vars[args[0]] += 1
    elif instruction == 'tpl':
      vars[args[0]] *= 3
    elif instruction == 'hlf':
      vars[args[0]] //= 2
    elif instruction == 'jmp':
      idx += int(args[0]) - 1
    elif instruction == 'jio':
      if vars[args[0]] == 1:
        idx += int(args[1]) - 1
    elif instruction == 'jie':
      if vars[args[0]] % 2 == 0:
        idx += int(args[1]) - 1
  return vars


def solve(var, part, file):
  instructions = load_instructions(file)
  return sim(instructions, {'a': part - 1, 'b': 0})[var]


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(2, solve('a', part=1, file='input-test-1'))
  test(184, solve('b', part=1, file='input-real'))

  test(231, solve('b', part=2, file='input-real'))
