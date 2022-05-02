#!/usr/bin/env python3

from common.util import *


def simulate(instructions):
  mem = defaultdict(int)
  for reg, op, amt, *test in instructions:
    exec(f"{' '.join(test)}: {reg} {'-+'[op == 'inc']}= {amt}", {}, mem)
    yield max(mem.values())


def solve(part, file):
  maxes = simulate(load_tokens(file))
  return max(maxes) if part else deque(maxes, maxlen=1).pop()


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(1, solve(part=0, file='input-test-1'))
  test(5752, solve(part=0, file='input-real'))

  test(10, solve(part=1, file='input-test-1'))
  test(6366, solve(part=1, file='input-real'))
