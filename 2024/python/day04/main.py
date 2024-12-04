#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  D = defaultdict(lambda: '.', load_dict(file))
  n = max(y for x,y in D) + 1
  m = max(x for x,y in D) + 1

  def part1(x,y):
    for dx,dy in DIRS_8:
      yield all(D[x+dx*i,y+dy*i] == c for i,c in enumerate('XMAS'))
  def part2(x,y):
    if D[x,y] == 'A':
      for i in range(4):
        yield all(D[x+dx,y+dy] == c for c,(dx,dy) in zip('MMSS', DIAG[i:] + DIAG[:i]))

  return sum(v for y in range(n) for x in range(m) for v in (part1,part2)[part](x,y))

### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(18, solve(part=0, file='input-test-1'))
  test(2551, solve(part=0, file='input-real'))

  test(9, solve(part=1, file='input-test-1'))
  test(1985, solve(part=1, file='input-real'))
