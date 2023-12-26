#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  data = load_blocks(file)
  stack_info = data[0][:-1]
  moves = data[1]

  stacks = [[line[i*4+1] for line in stack_info[::-1]
             if line[i*4+1] != ' '] for i in range(len(stack_info[0])//4+1)]

  for line in moves:
    x, a, b = parse_nums(line)
    stacks[b-1].extend([stacks[a-1].pop() for _ in range(x)][::[1, -1][part]])

  return ''.join(s.pop() for s in stacks)


### THE REST IS TESTS ###
if __name__ == "__main__":
  change_dir(__file__)

  test('CMZ', solve(part=0, file='input-test-1'))
  test('GRTSWNJHH', solve(part=0, file='input-real'))

  test('MCD', solve(part=1, file='input-test-1'))
  test('QLFQDBBHM', solve(part=1, file='input-real'))
