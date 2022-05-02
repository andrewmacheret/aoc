#!/usr/bin/env python3

from common.util import *


def load_rules(file):
  rules = {}
  for line in load(file):
    key, val = line.split(' => ')
    for _ in range(4):
      # flip x (x)
      key = '/'.join(s[::-1] for s in key.split('/'))
      rules[key] = val

      # flip y (both)
      key = '/'.join([s for s in key.split('/')][::-1])
      rules[key] = val

      # flip x (y)
      key = '/'.join(s[::-1] for s in key.split('/'))
      rules[key] = val

      # flip y (none)
      key = '/'.join([s for s in key.split('/')][::-1])
      rules[key] = val

      # rotate 90
      key = '/'.join(map(''.join, zip(*key.split('/')[::-1])))
      rules[key] = val
  return rules


def solve(file, steps):
  rules = load_rules(file)

  state = ".#./..#/###"
  mat = [list(s) for s in state.split('/')]

  for _ in range(steps):
    size = state.count('/') + 1
    div = 2 if size % 2 == 0 else 3
    size //= div
    next_mat = [[0 for _ in range(size*(div+1))] for _ in range(size*(div+1))]
    for y in range(size):
      for x in range(size):
        before = '/'.join(''.join(mat[y*div+dy][x*div+dx]
                          for dx in range(div)) for dy in range(div))
        after = rules[before]
        for dy, s in enumerate(after.split('/')):
          for dx, c in enumerate(s):
            next_mat[y*(div+1) + dy][x*(div+1) + dx] = c
    mat = next_mat
    state = '/'.join(map(''.join, mat))

  return state.count('#')

  ### THE REST IS TESTS ###


if __name__ == "__main__":
  change_dir(__file__)

  test(12, solve(file='input-test-1', steps=2))
  test(142, solve(file='input-real', steps=5))
  test(1879071, solve(file='input-real', steps=18))
