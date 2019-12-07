#!/usr/bin/env python3
import re

from day01.main import load, test

def load_strings(filename, script=__file__):
  return load(filename, script=script)

nice_regexes = {
  'v1': [
    r'([aeiou].*){3}',
    r'(.)\1',
    r'^(?!.*(ab|cd|pq|xy))'
  ],
  'v2': [
    r'(..).*\1',
    r'(.).\1'
  ]
}

def search_all(string, regexes):
  return all(bool(re.search(regex, string)) for regex in regexes)

def solve(filename, regexes):
  strings = load_strings(filename)
  return sum(search_all(s, regexes) for s in strings)

def part1(filename):
  return solve(filename, nice_regexes['v1'])

def part2(filename):
  return solve(filename, nice_regexes['v2'])

if __name__== "__main__":
  test(1, part1('input-test-1.txt'))
  test(1, part1('input-test-2.txt'))
  test(0, part1('input-test-3.txt'))
  test(0, part1('input-test-4.txt'))
  test(0, part1('input-test-5.txt'))
  test(255, part1('input.txt'))
  
  test(1, part2('input-test-6.txt'))
  test(1, part2('input-test-7.txt'))
  test(0, part2('input-test-8.txt'))
  test(0, part2('input-test-9.txt'))
  test(55, part2('input.txt'))
