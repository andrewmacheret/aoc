#!/usr/bin/env python3

from statistics import median
from common.util import load, test, change_dir


points = [1, 2, 3, 4, 3, 57, 1197, 25137]
parens = '([{<)]}>'


def get_score(s):
  stack = []
  for c in s.strip():
    if c in parens[:4]:
      stack += c,
    elif c != parens[parens.index(stack.pop()) + 4]:
      return (points[parens.index(c)], 0)
  score = 0
  while stack:
    score = score * 5 + points[parens.index(stack.pop())]
  return (0, score)


def solve(part, file):
  data = load(file)
  res = filter(None, (get_score(line)[part-1] for line in data))
  return (sum, median)[part-1](res)


if __name__ == "__main__":
  change_dir(__file__)

  test(26397, solve(part=1, file='input-test-1'))
  test(345441, solve(part=1, file='input-real'))

  test(288957, solve(part=2, file='input-test-1'))
  test(3235371166, solve(part=2, file='input-real'))
