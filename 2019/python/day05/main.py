#!/usr/bin/env python3
from collections import deque
import os

from day01.main import test
from day02.main import load_memory

def add(prog, modes):
  a, b, c = prog.grab_vals(modes, [0, 0, 1])
  prog.memory[c] = a + b

def mul(prog, modes):
  a, b, c = prog.grab_vals(modes, [0, 0, 1])
  prog.memory[c] = a * b

def input(prog, modes):
  a = prog.grab_vals(modes, [1])[0]
  prog.memory[a] = prog.input.popleft()

def output(prog, modes):
  a = prog.grab_vals(modes, [0])[0]
  return a

def jump_non_zero(prog, modes):
  a, b = prog.grab_vals(modes, [0, 0])
  if a != 0: prog.pos = b

def jump_zero(prog, modes):
  a, b = prog.grab_vals(modes, [0, 0])
  if a == 0: prog.pos = b

def lt(prog, modes):
  a, b, c = prog.grab_vals(modes, [0, 0, 1])
  prog.memory[c] = int(a < b)

def eq(prog, modes):
  a, b, c = prog.grab_vals(modes, [0, 0, 1])
  prog.memory[c] = int(a == b)

default_ops = {
  1: add,
  2: mul,
  3: input,
  4: output,
  5: jump_non_zero,
  6: jump_zero,
  7: lt,
  8: eq
}

class Program:
  def __init__(self, memory, input):
    self.memory = memory[:]
    self.input = deque(input)
    self.pos = 0

  def grab_vals(self, modes, overrides=[]):
    vals = []
    for override in overrides:
      val = self.memory[self.pos]
      mode = modes % 10
      vals.append(val if mode or override else self.memory[val])
      modes //= 10
      self.pos += 1
    return vals

  def run_computer(self, ops=default_ops):
    while self.pos < len(self.memory):
      modes, opcode = divmod(self.memory[self.pos], 100)
      if opcode == 99: return
      self.pos += 1
      output = ops[opcode](self, modes)
      if output: yield output

def part1(filename):
  memory = load_memory(filename, script=__file__)
  return list(Program(memory, [1]).run_computer())[-1]

def part2(filename):
  memory = load_memory(filename, script=__file__)
  return list(Program(memory, [5]).run_computer())[-1]

if __name__== "__main__":
  test(13787043, part1("input.txt"))
  test(3892695, part2("input.txt"))
