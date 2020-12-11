#!/usr/bin/env python3
import re
from collections import *

from day01.main import load, test

def load_regex(filename, regex, script=__file__):
  return [re.match(regex, line).groups() for line in load(filename, script=script)]

def load_passwords(filename, script=__file__):
  regex = r'^(\d+)-(\d+) (\w): (\w+)$'
  return [(int(start), int(end), letter, password) for start, end, letter, password in load_regex(filename, regex=regex, script=__file__)]

def part1(filename):
  P = load_passwords(filename)
  return sum(start <= Counter(password)[letter] <= end for start, end, letter, password in P)

def part2(filename):
  P = load_passwords(filename)
  return sum(sum(int(x-1 < len(password) and password[x-1] == letter) for x in (start, end)) % 2 for start, end, letter, password in P)

if __name__== "__main__":
  test(2, part1('input-test-1.txt'))
  test(638, part1('input.txt'))
  
  test(1, part2('input-test-1.txt'))
  test(699, part2('input.txt'))
