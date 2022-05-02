#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  data = load_string(file)
  stack = [(cur := [])]
  depth_score = garbage_score = ignore = garbage = 0
  for c in data:
    if garbage:
      if ignore:
        ignore = 0
      elif c == '!':
        ignore = 1
      elif c == '>':
        garbage = 0
      else:
        garbage_score += 1
    else:
      if c == '{':
        depth_score += len(stack)
        cur.append(cur := [])
        stack.append(cur)
      elif c == '}':
        stack.pop()
        cur = stack[-1]
      elif c == '<':
        garbage = 1

  return (depth_score, garbage_score)[part]


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(1, solve(part=0, file='input-test-1'))
  test(6, solve(part=0, file='input-test-2'))
  test(5, solve(part=0, file='input-test-3'))
  test(16, solve(part=0, file='input-test-4'))
  test(1, solve(part=0, file='input-test-5'))
  test(9, solve(part=0, file='input-test-6'))
  test(9, solve(part=0, file='input-test-7'))
  test(3, solve(part=0, file='input-test-8'))
  test(14204, solve(part=0, file='input-real'))

  test(0, solve(part=1, file='input-test-9'))
  test(17, solve(part=1, file='input-test-10'))
  test(3, solve(part=1, file='input-test-11'))
  test(2, solve(part=1, file='input-test-12'))
  test(0, solve(part=1, file='input-test-13'))
  test(0, solve(part=1, file='input-test-14'))
  test(10, solve(part=1, file='input-test-15'))
  test(6622, solve(part=1, file='input-real'))
