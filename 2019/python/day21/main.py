#!/usr/bin/env python3
from day01.main import load, test
from day02.main import load_memory
from day05.main import Program
from day17.main import parse_input

def execute_springdroid(memory, input):
  prog = Program(memory, input)
  run = prog.run_computer()
  output = list(run)
  if output[-1] >= 256: return output[-1]
  print(''.join(map(chr, output)))

def solve(filename, script):
  memory = load_memory(filename, script=__file__)
  input = parse_input(load(script, script=__file__))
  return execute_springdroid(memory, input)

if __name__== "__main__":
  test(19360288, solve('input.txt', script='input-springdroid-walk.txt'))
  test(1143814750, solve('input.txt', script='input-springdroid-run.txt'))
