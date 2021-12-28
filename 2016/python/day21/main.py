#!/usr/bin/env python3

from common.util import load, test, change_dir, parse_nums


def swap_pos(s, x, y):
  s[x], s[y] = s[y], s[x]
  return s


def swap_letter(s, x, y):
  return [y if c == x else x if c == y else c for c in s]


def reverse(s, x, y):
  s[x:y+1] = s[x:y+1][::-1]
  return s


def rotate_left(s, x):
  x %= len(s)
  return s[x:] + s[:x]


def rotate_right(s, x):
  x %= len(s)
  return s[-x:] + s[:-x]


def move(s, x, y):
  c = s.pop(x)
  s.insert(y, c)
  return s


def rotate_by_letter(s, c):
  r = 1 + s.index(c)
  if r > 4:
    r += 1
  return rotate_right(s, r)


def rotate_by_letter_inverse(s, c):
  r = s.index(c)
  if r and r % 2 == 0:
    r += len(s)
  r = (r // 2 + 1) % len(s)
  return rotate_left(s, r)


def solve(part, input, file):
  s = list(input)
  lines = load(file)
  if part == 2:
    lines = lines[::-1]

  for line in lines:
    tokens = line.split()
    nums = parse_nums(line)
    if tokens[0] == 'swap' and tokens[1] == 'position':
      s = swap_pos(s, *nums)
    elif tokens[0] == 'swap' and tokens[1] == 'letter':
      s = swap_letter(s, tokens[2], tokens[5])
    elif tokens[0] == 'move':
      if part == 1:
        s = move(s, *nums)
      else:
        s = move(s, *nums[::-1])
    elif tokens[0] == 'reverse':
      s = reverse(s, *nums)
    elif tokens[0] == 'rotate' and tokens[1] == 'left':
      if part == 1:
        s = rotate_left(s, *nums)
      else:
        s = rotate_right(s, *nums)
    elif tokens[0] == 'rotate' and tokens[1] == 'right':
      if part == 1:
        s = rotate_right(s, *nums)
      else:
        s = rotate_left(s, *nums)
    elif tokens[0] == 'rotate' and tokens[1] == 'based':
      if part == 1:
        s = rotate_by_letter(s, tokens[-1])
      else:
        s = rotate_by_letter_inverse(s, tokens[-1])
    else:
      raise Exception('no match', line)
  return ''.join(s)

### THE REST IS TESTS ###


if __name__ == "__main__":
  change_dir(__file__)

  test('ebcda', ''.join(swap_pos(list('abcde'), 4, 0)))
  test('edcba', ''.join(swap_letter(list('ebcda'), 'd', 'b')))
  test('abcde', ''.join(reverse(list('edcba'), 0, 4)))
  test('bcdea', ''.join(rotate_left(list('abcde'), 1)))
  test('eabcd', ''.join(rotate_right(list('abcde'), 1)))
  test('bdeac', ''.join(move(list('bcdea'), 1, 4)))
  test('abdec', ''.join(move(list('bdeac'), 3, 0)))
  test('ecabd', ''.join(rotate_by_letter(list('abdec'), 'b')))
  test('decab', ''.join(rotate_by_letter(list('ecabd'), 'd')))

  test('decab', solve(part=1, input='abcde', file='input-test-1'))
  test('baecdfgh', solve(part=1, input='abcdefgh', file='input-real'))

  for x in range(8):
    for y in range(8):
      test('abcdefgh', ''.join(swap_pos(
          swap_pos(list('abcdefgh'), x, y), x, y)))

  for x in 'abcdefgh':
    for y in 'abcdefgh':
      test('abcdefgh', ''.join(swap_letter(
          swap_letter(list('abcdefgh'), x, y), x, y)))

  for x in range(8):
    for y in range(8):
      test('abcdefgh', ''.join(reverse(
          reverse(list('abcdefgh'), x, y), x, y)))

  for x in range(8):
    test('abcdefgh', ''.join(rotate_right(
        rotate_left(list('abcdefgh'), x), x)))

  for x in range(8):
    test('abcdefgh', ''.join(rotate_left(
        rotate_right(list('abcdefgh'), x), x)))

  for c in 'abcdefgh':
    test('abcdefgh', ''.join(rotate_by_letter_inverse(
        rotate_by_letter(list('abcdefgh'), c), c)))

  for x in range(8):
    for y in range(8):
      test('abcdefgh', ''.join(move(
          move(list('abcdefgh'), x, y), y, x)))

  test('abcde', solve(part=2, input='decab', file='input-test-1'))
  test('cegdahbf', solve(part=2, input='fbgdceah', file='input-real'))
