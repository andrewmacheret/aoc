#!/usr/bin/env python3

from common.util import test, load_ints, change_dir


def solve(part, file):
  data = load_ints(file)
  return sum(map(int.__lt__, data, data[part * 2 - 1:]))


if __name__ == "__main__":
  change_dir(__file__)

  test(7,    solve(part=1, file='input-test-1'))
  test(1215, solve(part=1, file='input-real'))

  test(5,    solve(part=2, file='input-test-1'))
  test(1150, solve(part=2, file='input-real'))
