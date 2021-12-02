#!/usr/bin/env python3

from string import ascii_lowercase
from collections import Counter
from operator import itemgetter
import re

from common.util import load, test, change_dir


def load_rooms(file):
  return [re.split(r'[\-\]\[]', line)[:-1] for line in load(file)]


def rotate(s, amt):
  return ''.join(chr(((ord(c) - ord('a') + amt) % 26) + ord('a')) if c != '-' else ' ' for c in s)


def checksum(data):
  return ''.join(map(itemgetter(0), Counter(ascii_lowercase + data).most_common(5)))


def solve(part, file, goal=None):
  data = load_rooms(file)
  res = 0
  for line in data:
    words = line[:-2]
    expected = line[-1]
    id = int(line[-2])

    actual = checksum(''.join(words))
    if actual == expected:
      res += id

      if part == 2 and rotate('-'.join(words), id) == goal:
        return id

  return res


if __name__ == "__main__":
  change_dir(__file__)

  test(1514, solve(part=1, file='input-test-1'))
  test(137896, solve(part=1, file='input-real'))

  test(343, solve(part=2, file='input-test-2', goal='very encrypted name'))
  test(501, solve(part=2, file='input-real', goal='northpole object storage'))
