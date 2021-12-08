#!/usr/bin/env python3

from itertools import product
import re

from common.util import load, test, change_dir


def has_abba(s):
  return re.search(r'(.)(?!\1)(.)\2\1', s) is not None


def find_babs(seq):
  for s in seq:
    for m in re.finditer(r'(.)(?!\1)(?=(.)\1)', s):
      yield m[2] + m[1] + m[2]


def solve(part, file):
  data = load(file)
  total = 0
  for line in data:
    seqs = re.split(r'\[|\]', line)
    outs, ins = seqs[::2], seqs[1::2]
    if part == 1:
      total += not any(map(has_abba, ins)) and any(map(has_abba, outs))
    else:
      total += any(bab in s for bab, s in product(find_babs(outs), ins))

  return total


if __name__ == "__main__":
  change_dir(__file__)

  test(1, solve(part=1, file='input-test-1'))
  test(0, solve(part=1, file='input-test-2'))
  test(0, solve(part=1, file='input-test-3'))
  test(1, solve(part=1, file='input-test-4'))
  test(110, solve(part=1, file='input-real'))

  test(1, solve(part=2, file='input-test-5'))
  test(0, solve(part=2, file='input-test-6'))
  test(1, solve(part=2, file='input-test-7'))
  test(1, solve(part=2, file='input-test-8'))
  test(242, solve(part=2, file='input-real'))
