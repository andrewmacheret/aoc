#!/usr/bin/env python3
from day01.main import load, test
from day02.main import load_memory
from day05.main import Program

def part1(filename):
  memory = load_memory(filename, script=__file__)
  return list(Program(memory, [1]).run_computer())

def part2(filename):
  memory = load_memory(filename, script=__file__)
  return list(Program(memory, [2]).run_computer())

if __name__== "__main__":
  test([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99], part1('input-test-1.txt'))
  test(16, len(str(part1('input-test-2.txt')[0])))
  test([1125899906842624], part1('input-test-3.txt'))
  test([2171728567], part1('input.txt'))
  test([49815], part2('input.txt'))
