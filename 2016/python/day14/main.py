#!/usr/bin/env python3

from collections import defaultdict, deque
from itertools import groupby, count, islice
from hashlib import md5
from functools import cache
from math import inf

from common.util import load, test, change_dir


def repeated(s, x):
  res = ((k, len(list(g))) for k, g in groupby(s))
  return (k for k, v in res if v >= x)


def repeating_md5(s, repeat):
  for _ in range(repeat):
    s = md5(s.encode()).hexdigest()
  return s


def keys(salt, md5_count):
  hash5_indexes = defaultdict(lambda: inf)
  hashes = deque()
  for i in count():
    hash5 = repeating_md5(salt + str(i), md5_count)
    for ch in set(repeated(hash5, 5)):
      hash5_indexes[ch] = i
    hashes.append(hash5)

    if i >= 1000:
      hash = hashes.popleft()
      ch = next(repeated(hash, 3), None)
      if ch and -999 <= hash5_indexes[ch] - i <= 0:
        yield i - 1000


def solve(part, file):
  salt = load(file)[0]
  gen = keys(salt, (1, 2017)[part-1])
  return next(islice(gen, 63, None))


### THE REST IS TESTS ###
if __name__ == "__main__":
  change_dir(__file__)

  test(22728, solve(part=1, file='input-test-1'))
  test(25427, solve(part=1, file='input-real'))

  test(22551, solve(part=2, file='input-test-1'))
  test(22045, solve(part=2, file='input-real'))
