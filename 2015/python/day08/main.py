#!/usr/bin/env python3
import json

from day01.main import load, test

def load_strings(filename, script=__file__):
  return load(filename, script=script)

def part1(filename):
  strings = load_strings(filename)
  return sum(len(string) - len(eval(string)) for string in strings)

def part2(filename):
  strings = load_strings(filename)
  return sum(len(json.dumps(string)) - len(string) for string in strings)

if __name__== "__main__":
  test(2, part1('input-test-1.txt'))
  test(2, part1('input-test-2.txt'))
  test(3, part1('input-test-3.txt'))
  test(5, part1('input-test-4.txt'))
  test(1350, part1('input.txt'))
  
  test(4, part2('input-test-1.txt'))
  test(4, part2('input-test-2.txt'))
  test(6, part2('input-test-3.txt'))
  test(5, part2('input-test-4.txt'))
  test(2085, part2('input.txt'))
