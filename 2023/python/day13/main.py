#!/usr/bin/env python3

from common.util import *

def horiz(block, ignore=None):
  n = len(block)
  for i in range(1, n):
    if i != ignore and block[i-1:2*(i-n)-1:-1] == block[i:i+i]:
      return i

def vert(block, ignore=None):
  return horiz([*zip(*block)], ignore)


def flip(block, i, j):
  block[i][j] = '#.'[block[i][j] == '#']


def find_smudged(block, oh, ov):
  for i in range(len(block)):
    for j in range(len(block[0])):
      flip(block, i, j)
      h, v = horiz(block, oh), vert(block, ov)
      if h and h != oh:
        return h, None
      if v and v != ov:
        return None, v
      flip(block, i, j)

def solve(part, file):
  t = 0
  for block in load_blocks(file):
    block = [*map(list, block)]
    h, v = horiz(block), vert(block)
    if part:
      h, v = find_smudged(block, h, v)
    t += v or 100 * h
  return t


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(405, solve(part=0, file='input-test-1'))
  test(28895, solve(part=0, file='input-real'))

  test(400, solve(part=1, file='input-test-1'))
  test(31603, solve(part=1, file='input-real'))
