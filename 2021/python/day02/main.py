#!/usr/bin/env python3

from common.util import load_tokens, test, change_dir


def solve(part, file):
  data = load_tokens(file)
  h = d = a = 0
  for line in data:
    dir, x = line[0][0], int(line[1])
    if part == 1:
      if dir == 'f':
        h += x
      else:
        d += (1 | -(dir == 'u')) * x
    else:
      if dir == 'f':
        h += x
        a += d * x
      else:
        d += (1 | -(dir == 'u')) * x
  return h * d


if __name__ == "__main__":
  change_dir(__file__)

  test(150, solve(part=1, file='input-test-1'))
  test(1746616, solve(part=1, file='input-real'))

  test(900, solve(part=2, file='input-test-1'))
  test(1741971043, solve(part=2, file='input-real'))
