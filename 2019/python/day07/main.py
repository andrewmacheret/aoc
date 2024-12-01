#!/usr/bin/env python3
from itertools import permutations
import os
from math import inf
from collections import *

from day01.main import load, test
# from day02.main import load_memory
# from day05.main import Program

def load(filename, script=__file__):
  full_path = os.path.dirname(os.path.realpath(script)) + os.sep + filename
  # print('loading ' + full_path)
  with open(full_path) as f:
    return f.read().splitlines()

def load_memory(filename, script=__file__):
  return next([int(s) for s in line.split(',')] for line in load(filename, script=script))

def add(prog, modes):
  a, b, c = prog.grab_vals(modes, [0, 0, 1])
  prog.memory[c] = a + b
  # print("ADD {} prog.memory[{}] := {} + {} ... {}".format(list(reversed(list(str(modes)))), c, a, b, prog.memory[c]))

def mul(prog, modes):
  a, b, c = prog.grab_vals(modes, [0, 0, 1])
  prog.memory[c] = a * b
  # print("MUL {} prog.memory[{}] := {} * {} ... {}".format(list(reversed(list(str(modes)))), c, a, b, prog.memory[c]))

def input(prog, modes):
  (a, ) = prog.grab_vals(modes, [1])
  prog.memory[a] = prog.input.popleft() if (prog.input or prog.default is None) else prog.default
  # print("INP {} prog.memory[{}] := {}".format(list(reversed(list(str(modes)))), a, prog.memory[a]))

def output(prog, modes):
  (a, ) = prog.grab_vals(modes, [0])
  # print("OUT {} {}".format(list(reversed(list(str(modes)))), a))
  return a

def jump_non_zero(prog, modes):
  a, b = prog.grab_vals(modes, [0, 0])
  if a != 0: prog.pos = b
  # print("JNZ {} prog.pos := {} if {} != 0".format(list(reversed(list(str(modes)))), b, a))

def jump_zero(prog, modes):
  a, b = prog.grab_vals(modes, [0, 0])
  if a == 0: prog.pos = b
  # print("JEZ {} prog.pos := {} if {} == 0".format(list(reversed(list(str(modes)))), b, a))

def lt(prog, modes):
  a, b, c = prog.grab_vals(modes, [0, 0, 1])
  prog.memory[c] = int(a < b)
  # print("LT  {} prog.memory[{}] := {} < {} ... {}".format(list(reversed(list(str(modes)))), c, a, b, prog.memory[c]))

def eq(prog, modes):
  a, b, c = prog.grab_vals(modes, [0, 0, 1])
  prog.memory[c] = int(a == b)
  # print("EQ  {} prog.memory[{}] := {} == {} ... {}".format(list(reversed(list(str(modes)))), c, a, b, prog.memory[c]))

def rel(prog, modes):
  (a, ) = prog.grab_vals(modes, [0])
  prog.relative_base += a
  # print("REL  {} prog.relative_base += {} ... {}".format(list(reversed(list(str(modes)))), a, prog.relative_base))

default_ops = {
  1: add,
  2: mul,
  3: input,
  4: output,
  5: jump_non_zero,
  6: jump_zero,
  7: lt,
  8: eq,
  9: rel
}

class Program:
  def __init__(self, memory, input=[], default=None):
    self.memory = defaultdict(int)
    for i, m in enumerate(memory):
      self.memory[i] = m
    self.input = deque(input)
    self.pos = 0
    self.relative_base = 0
    self.default = default
    self.interrupt = False

  def grab_vals(self, modes, overrides=[]):
    vals = []
    for override in overrides:
      val = self.memory[self.pos]
      mode = modes % 10
      adjust = self.relative_base if mode == 2 else 0
      if mode == 1 or override:
        vals.append(val + adjust)
      else:
        vals.append(self.memory[adjust + val])
      modes //= 10
      self.pos += 1
    return vals

  def run_computer(self, ops=default_ops):
    while self.pos < len(self.memory) and not self.interrupt:
      modes, opcode = divmod(self.memory[self.pos], 100)
      if opcode == 99: return
      self.pos += 1
      output = ops[opcode](self, modes)
      if output is not None: yield output


single_loop = [0]
inf_loop = iter(int, 1)

def chain_progs(progs, input=0):
  for prog, run in progs:
    prog.input.append(input)
    try: input = next(run, None)
    except: return
    if input is None: return
    yield input

def init_progs(combo, memory):
  return [(prog, prog.run_computer()) for prog in (Program(memory, [val]) for val in combo)]

def last(it, val):
  for val in it: pass
  return val

def chain_once(progs):
  return last(chain_progs(progs), None)

def chain_repeatedly(progs):
  input = 0
  while True:
    if not (output := last(chain_progs(progs, input), None)):
      print("returned")
      return input
    print("output", output)
    input = output

def part1(filename):
  memory = load_memory(filename, script=__file__)
  return max(chain_once(init_progs(perm, memory)) for perm in permutations(range(5)))

def part2(filename):
  memory = load_memory(filename, script=__file__)
  return max(chain_repeatedly(init_progs(perm, memory)) for perm in [[*permutations(range(5, 10))][0]])

if __name__== "__main__":
  # test(43210, part1('input-test-1.txt'))
  # test(54321, part1('input-test-2.txt'))
  # test(65210, part1('input-test-3.txt'))
  # test(24625, part1('input.txt'))
  
  test(139629729, part2('input-test-4.txt'))
  # test(18216, part2('input-test-5.txt'))
  # test(36497698, part2('input.txt'))
