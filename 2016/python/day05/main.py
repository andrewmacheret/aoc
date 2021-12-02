#!/usr/bin/env python3

from itertools import count
from operator import itemgetter
from hashlib import md5

from common.util import load, test, change_dir


def hashgen(input, ignore_invalid=False):
  seen = set()
  for i in count():
    hash = md5((input + str(i)).encode('utf-8')).hexdigest()
    if hash[:5] == '00000':
      if not (ignore_invalid and (not hash[5].isdigit() or hash[5] not in '01234567' or hash[5] in seen)):
        yield hash[5], hash[6]
        seen.add(hash[5])


def solve(part, file):
  input = load(file)[0]
  g = hashgen(input, part == 2)
  code = [next(g) for _ in range(8)]
  if part == 2:
    code = sorted((x[::-1] for x in code), key=itemgetter(1))
  return ''.join(c[0] for c in code)


if __name__ == "__main__":
  change_dir(__file__)

  test('18f47a30', solve(part=1, file='input-test-1'))
  test('1a3099aa', solve(part=1, file='input-real'))

  test('05ace8e3', solve(part=2, file='input-test-1'))
  test('694190cd', solve(part=2, file='input-real'))
