#!/usr/bin/env python3

from common.util import load_string, test, change_dir


def step(s):
  return ''.join('.^'[a != c] for a, c in zip('.' + s[:-1], s[1:] + '.'))


def steps(s, n):
  for _ in range(n):
    s = step(s)
  return s


def count_safe(s, n):
  safe = 0
  for _ in range(n):
    safe += s.count('.')
    s = step(s)
  return safe


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test('.^^^^', steps('..^^.', 1))
  test('^^..^', steps('..^^.', 2))

  test('^^^...^..^', steps('.^^.^.^^^^', 1))
  test('^.^^.^.^^.', steps('.^^.^.^^^^', 2))
  test('..^^...^^^', steps('.^^.^.^^^^', 3))
  test('.^^^^.^^.^', steps('.^^.^.^^^^', 4))
  test('^^..^.^^..', steps('.^^.^.^^^^', 5))
  test('^^^^..^^^.', steps('.^^.^.^^^^', 6))
  test('^..^^^^.^^', steps('.^^.^.^^^^', 7))
  test('.^^^..^.^^', steps('.^^.^.^^^^', 8))
  test('^^.^^^..^^', steps('.^^.^.^^^^', 9))

  test(38, count_safe('.^^.^.^^^^', 10))

  input = load_string('input-real')
  test(1926, count_safe(input, 40))
  test(19986699, count_safe(input, 400000))
