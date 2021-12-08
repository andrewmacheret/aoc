#!/usr/bin/env python3

from collections import Counter

from common.util import load, change_dir, test


def solve(part, file):
  data = load(file)
  return ''.join(Counter(col).most_common()[1-part][0] for col in zip(*data))


if __name__ == "__main__":
  change_dir(__file__)

  test("easter",   solve(part=1, file='input-test-1'))
  test("usccerug", solve(part=1, file='input-real'))

  test("advent",   solve(part=2, file='input-test-1'))
  test("cnvvtafc", solve(part=2, file='input-real'))
