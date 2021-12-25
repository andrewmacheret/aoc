#!/usr/bin/env python3

from common.util import load, test, change_dir


def solve(part, file):
  lines = load(file)
  blocks = [block.split('\n')
            for block in '\n'.join(lines).split('inp w\n')[1:]]
  model = [0] * 14
  stack = []
  for i, block in enumerate(blocks):
    if block[3] == 'div z 1':
      x = int(block[14].split(' ')[-1])
      stack.append((i, x))
    elif block[3] == 'div z 26':
      y = int(block[4].split(' ')[-1])
      j, x = stack.pop()
      diff = x + y
      if diff < 0:
        i, j, diff = j, i, -diff
      if part == 1:
        model[i] = 9
        model[j] = 9 - diff
      else:
        model[i] = 1 + diff
        model[j] = 1
  return int(''.join(map(str, model)))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(93997999296912, solve(part=1, file='input-real'))
  test(81111379141811, solve(part=2, file='input-real'))
