#!/usr/bin/env python3

import re

from common.util import load_blocks, test, change_dir


def solve(part, file):
  rule_block, goal = load_blocks(file)
  rules = [line.split(' => ') for line in rule_block]
  goal = goal[0]

  def expand(s):
    for a, b in rules:
      for m in re.finditer(a, s):
        s2 = list(s)
        s2[m.start():m.end()] = b
        yield ''.join(s2)

  if part == 1:
    return len(set(expand(goal)))

  return len(re.findall(r'[A-Z]', goal)) \
      - goal.count('Rn') - goal.count('Ar') \
      - 2 * goal.count('Y') - 1


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(4, solve(part=1, file='input-test-1'))
  test(7, solve(part=1, file='input-test-2'))
  test(535, solve(part=1, file='input-real'))

  test(212, solve(part=2, file='input-real'))
