#!/usr/bin/env python3
from collections import OrderedDict, defaultdict, deque, Counter
import os
import operator

os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
from day01.main import test
from day02.main import load_memory

def run_computer(memory, input):
  parse_modes = lambda modes, n: list(map(int, str(modes).zfill(n)))[:n]
  
  output = []
  pos = 0

  def grab_vals(modes, n, positionals=[]):
    nonlocal pos
    output = []
    for i in range(1, n+1):
      val = memory[pos]
      mode = modes % 10
      output.append(val if mode or i in positionals else memory[val])
      modes //= 10
      pos += 1
    # print('params', output)
    return output if len(output) != 1 else output[0]

  while pos < len(memory):
    modes, opcode = divmod(memory[pos], 100)
    pos += 1
    # print('opcode={} modes={}'.format(opcode, modes))
    if opcode == 1:
      a, b, c = grab_vals(modes, 3, [3])
      memory[c] = a + b
    elif opcode == 2:
      a, b, c = grab_vals(modes, 3, [3])
      memory[c] = a * b
    elif opcode == 3:
      a = grab_vals(modes, 1, [1])
      memory[a] = input.popleft()
    elif opcode == 4:
      a = grab_vals(modes, 1, [])
      output.append(a)
    elif opcode == 5:
      a, b = grab_vals(modes, 2, [])
      if a != 0: pos = b
    elif opcode == 6:
      a, b = grab_vals(modes, 2, [])
      if a == 0: pos = b
    elif opcode == 7:
      a, b, c = grab_vals(modes, 3, [3])
      memory[c] = int(a < b)
    elif opcode == 8:
      a, b, c = grab_vals(modes, 3, [3])
      memory[c] = int(a == b)
    elif opcode == 99:
      return output
    else:
      raise Exception("Invalid opcode " + str(opcode))

def part1(filename):
  memory = load_memory(filename, script=__file__)
  return run_computer(memory, deque([1]))[-1]

def part2(filename):
  memory = load_memory(filename, script=__file__)
  return run_computer(memory, deque([5]))[-1]

if __name__== "__main__":
  test(13787043, part1("input.txt"))
  test(3892695, part2("input.txt"))
