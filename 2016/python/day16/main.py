#!/usr/bin/env python3

from common.util import load, test, change_dir


def step(s):
  return s + '0' + ''.join('01'[c == '0'] for c in s[::-1])


def checksum(s):
  while len(s) % 2 == 0:
    s = ''.join('01'[a == b] for a, b in zip(*[iter(s)]*2))
  return s


def fill(s, size):
  while len(s) < size:
    s = step(s)
  return checksum(s[:size])


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test('100', step('1'))
  test('001', step('0'))
  test('11111000000', step('11111'))
  test('1111000010100101011110000', step('111100001010'))

  test('100', checksum('110010110100'))

  test('01100', fill('10000', 20))

  input = load('input-real')[0]
  test('01110011101111011', fill(input, 272))
  test('11001111011000111', fill(input, 35651584))
