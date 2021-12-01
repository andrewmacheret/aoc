#!/usr/bin/env python3

from collections import defaultdict

from common.util import load_csv, test, change_dir


def solve(part, file):
  data = load_csv(file)[0]
  pos = 0
  dir = 0 + 1j
  grid = defaultdict(int)
  first_revisit = None
  for step in data:
    dir *= 1j if step[0] == 'L' else -1j
    for _ in range(int(step[1:])):
      pos += dir
      grid[pos] += 1
      if grid[pos] > 1 and first_revisit is None:
        first_revisit = pos
  if part == 2:
    pos = first_revisit
  return int(abs(pos.real) + abs(pos.imag))


if __name__ == "__main__":
  change_dir(__file__)

  test(5, solve(part=1, file='input-test-1'))
  test(2, solve(part=1, file='input-test-2'))
  test(12, solve(part=1, file='input-test-3'))
  test(236, solve(part=1, file='input-real'))

  test(4, solve(part=2, file='input-test-4'))
  test(182, solve(part=2, file='input-real'))
