#!/usr/bin/env python3

from day01.main import load, test

def seat_id(seat):
  return int(''.join(str(int(x=='B' or x=='R')) for x in seat), base=2)

def part1(filename):
  lines = load(filename, script=__file__)
  return max(map(seat_id, lines))

def part2(filename):
  lines = load(filename, script=__file__)
  seats = set(map(seat_id, lines))
  for seat in range(min(seats)+1, max(seats)):
    if seat not in seats:
      return seat

if __name__== "__main__":
  test(357, part1('input-test-1.txt'))
  test(567, part1('input-test-2.txt'))
  test(119, part1('input-test-3.txt'))
  test(820, part1('input-test-4.txt'))
  test(904, part1('input.txt'))
  
  test(669, part2('input.txt'))
