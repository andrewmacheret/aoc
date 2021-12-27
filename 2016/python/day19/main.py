#!/usr/bin/env python3

from common.util import load_int, test, change_dir


def josephus(n, k):
  x = 1
  for i in range(2, n+1):
    x = (x + k - 1) % i + 1
  return x


def josephus2(n):
  x = 1
  while x * 3 < n:
    x *= 3
  return n - x if n > 1 else 1


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(3, josephus(5, 2))
  test(13, josephus(14, 2))

  input = load_int('input-real')
  test(1808357, josephus(input, 2))

  test(1, josephus2(1))
  test(1, josephus2(2))
  test(2, josephus2(3))
  test(1, josephus2(4))
  test(2, josephus2(5))
  test(3, josephus2(6))
  test(4, josephus2(7))
  test(5, josephus2(8))
  test(1407007, josephus2(input))
