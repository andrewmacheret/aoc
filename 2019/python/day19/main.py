#!/usr/bin/env python3
from itertools import chain, count

from day01.main import test
from day02.main import load_memory
from day05.main import Program
from day11.main import draw

class Scanner():
  def __init__(self, memory):
    self.memory = memory
  def scan(self, x, y):
    return next(Program(self.memory, [x, y]).run_computer())
  
def part1(filename):
  scanner = Scanner(load_memory(filename, script=__file__))
  return sum(scanner.scan(x, y) for y in range(50) for x in range(50))

def find_box(scanner, w, h):
  lx, y = next((x, y) for y in range(1, 10) for x in range(1, 10) if scanner.scan(x, y))
  rx = next(x for x in range(9, 0, -1) if scanner.scan(x, y))
  ranges = {}
  for y in count(y+1):
    while not scanner.scan(lx, y): lx += 1
    while scanner.scan(rx+1, y): rx += 1
    y0 = y - h + 1
    if y0 in ranges and ranges[y0][0] <= lx+w-1 <= ranges[y0][1]: return lx, y0
    ranges[y] = (lx, rx)

def part2(filename):
  scanner = Scanner(load_memory(filename, script=__file__))
  return find_box(scanner, 100, 100)

if __name__== "__main__":
  test(213, part1('input.txt'))
  test((783, 987), part2('input.txt'))
