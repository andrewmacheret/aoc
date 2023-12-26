#!/usr/bin/env python3

from common.util import *


def process_game(part, line):
  d = defaultdict(int)
  for x, c in re.findall(r'(\d+) (.)', line):
    d[c] = max(d[c], int(x))
  if part == 0:
    id = int(re.search(r'\d+', line)[0])
    return id * (d['r'] <= 12 and d['g'] <= 13 and d['b'] <= 14)
  else:
    return reduce(mul, d.values())


def solve(part, file):
  return sum(process_game(part, line) for line in load(file))

### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(8, solve(part=0, file='input-test-1'))
  test(2348, solve(part=0, file='input-real'))

  test(2286, solve(part=1, file='input-test-1'))
  test(76008, solve(part=1, file='input-real'))
