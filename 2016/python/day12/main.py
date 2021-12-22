#!/usr/bin/env python3

from collections import defaultdict
import re

from common.util import load, test, change_dir


def parse_instructions(lines):
  return [[int(c) if c[-1].isdigit() else c for c in line.split(' ')] for line in lines]


def optimize(instructions):
  for i in range(len(instructions) - 2):
    s = ','.join(instructions[i:i+3])
    rep = re.sub(r'inc (\w+),dec (\w+),jnz \2 -2',
                 r'noop,add \2 \1,cpy 0 \2', s)
    instructions[i:i+3] = rep.split(',')


def run(instructions, reg):
  reg = defaultdict(int, reg)

  def get(x): return reg[x] if isinstance(x, str) else x

  while 0 <= reg[0] < len(instructions):
    op, *args = instructions[reg[0]]
    reg[0] += 1
    if op == 'inc':
      reg[args[0]] += 1
    elif op == 'dec':
      reg[args[0]] -= 1
    elif op == 'cpy':
      a, b = args
      reg[b] = get(a)
    elif op == 'jnz':
      a, b = args
      if get(a):
        reg[0] += get(b) - 1
    elif op == 'add':
      a, b = args
      reg[b] += get(a)
  return reg['a']


def solve(part, file):
  lines = load(file)
  optimize(lines)
  instructions = parse_instructions(lines)
  return run(instructions, {'c': part - 1})


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(42, solve(part=1, file='input-test-1'))
  test(318083, solve(part=1, file='input-real'))

  test(9227737, solve(part=2, file='input-real'))
