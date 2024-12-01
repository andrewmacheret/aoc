#!/usr/bin/env python3
from collections import deque, defaultdict
import os

from day01.main import test
from day02.main import load_memory

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
  # print("OUT {} {} rel={}".format(list(reversed(list(str(modes)))), a, prog.relative_base))
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

def part1(filename):
  memory = load_memory(filename, script=__file__)
  return list(Program(memory, [1]).run_computer())[-1]

def part2(filename):
  memory = load_memory(filename, script=__file__)
  return list(Program(memory, [5]).run_computer())[-1]

if __name__== "__main__":
  test(13787043, part1("input.txt"))
  test(3892695, part2("input.txt"))
