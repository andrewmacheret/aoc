#!/usr/bin/env python3
from itertools import count
from hashlib import md5 

from day01.main import load, test

def load_secret(filename, script=__file__):
  return load(filename, script=script)[0]

def str_to_md5(s):
  return md5(s.encode()).hexdigest()

def advent_md5s(secret):
  for i in count(1):
    yield i, str_to_md5(secret + str(i))

def solve(filename, n):
  secret = load_secret(filename)
  return next(i for i, hex in advent_md5s(secret) if hex[:n] == "0" * n)

def part1(filename):
  return solve(filename, 5)

def part2(filename):
  return solve(filename, 6)

if __name__== "__main__":
  test(609043, part1('input-test-1.txt'))
  test(1048970, part1('input-test-2.txt'))
  test(254575, part1('input.txt'))
  
  test(1038736, part2('input.txt'))
