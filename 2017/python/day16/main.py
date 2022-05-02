#!/usr/bin/env python3

from common.util import *


def solve(part, file, n):
  steps = list(load(file)[0].split(','))

  @cache
  def dance(start):
    spin = 0
    order = list(start)
    pos = {c: i for i, c in enumerate(order)}

    for step in steps:
      if step[0] == 's':
        s = int(step[1:])
        spin = (spin + s) % n
      elif step[0] == 'x':
        x, y = ((int(x) - spin) % n for x in step[1:].split('/'))
        a, b = order[x], order[y] = order[y], order[x]
        pos[a], pos[b] = pos[b], pos[a]
      elif step[0] == 'p':
        a, b = step[1:].split('/')
        x, y = pos[a], pos[b] = pos[b], pos[a]
        order[x], order[y] = order[y], order[x]
    return ''.join(order[-spin:] + order[:-spin])

  current = start = ''.join(ascii_lowercase[:n])

  if not part:
    return dance(start)

  for cycle in count(1):
    current = dance(current)
    if current == start:
      break
  for _ in range(1000000000 % cycle):
    current = dance(current)
  return current


### THE REST IS TESTS ###


if __name__ == "__main__":
  change_dir(__file__)

  test('baedc', solve(part=0, file='input-test-1', n=5))
  test('cgpfhdnambekjiol', solve(part=0, file='input-real', n=16))

  test('abcde', solve(part=1, file='input-test-1', n=5))
  test('gjmiofcnaehpdlbk', solve(part=1, file='input-real', n=16))
