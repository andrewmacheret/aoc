#!/usr/bin/env python3
import json

from day01.main import load, test

def load_json(filename, script=__file__):
  return json.loads('\n'.join(load(filename, script=script)))

def find_numbers(data, ignore=None):
  if isinstance(data, list):
    for i in data: yield from find_numbers(i, ignore)
  elif isinstance(data, dict):
    if ignore and ignore in data.values(): return
    for i in data.values(): yield from find_numbers(i, ignore)
  elif isinstance(data, int):
    yield data

def part1(filename):
  return sum(find_numbers(load_json(filename)))

def part2(filename):
  return sum(find_numbers(load_json(filename), ignore="red"))

# def part2(filename):
#   data = load_custom(filename)
#   return None

if __name__== "__main__":
  test(6, part1('input-test-1.txt'))
  test(6, part1('input-test-2.txt'))
  test(3, part1('input-test-3.txt'))
  test(3, part1('input-test-4.txt'))
  test(0, part1('input-test-5.txt'))
  test(0, part1('input-test-6.txt'))
  test(0, part1('input-test-7.txt'))
  test(0, part1('input-test-8.txt'))
  test(191164, part1('input.txt'))

  test(6, part2('input-test-1.txt'))
  test(4, part2('input-test-9.txt'))
  test(0, part2('input-test-10.txt'))
  test(6, part2('input-test-11.txt'))
  test(87842, part2('input.txt'))
