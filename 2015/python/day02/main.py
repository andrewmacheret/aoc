#!/usr/bin/env python3
from day01.main import load, test

def load_dimensions(filename, script=__file__):
  return [map(int, line.split('x')) for line in load(filename, script=script)]

def wrapping_paper(w, l, h):
  return 2*l*w + 2*w*h + 2*h*l + w*l*h//max(w,l,h)

def ribbon(w, l, h):
  return 2*(w + l + h - max(w,l,h)) + w*l*h

def part1(filename):
  dimensions = load_dimensions(filename)
  return sum(wrapping_paper(w, l, h) for w, l, h in dimensions)

def part2(filename):
  dimensions = load_dimensions(filename)
  return sum(ribbon(w, l, h) for w, l, h in dimensions)

if __name__== "__main__":
  test(58, part1('input-test-1.txt'))
  test(43, part1('input-test-2.txt'))
  test(1586300, part1('input.txt'))
  
  test(34, part2('input-test-1.txt'))
  test(14, part2('input-test-2.txt'))
  test(3737498, part2('input.txt'))
