#!/usr/bin/env python3
import os
import sys
import operator

class Solution:
  def __init__(self):
    pass

  def load(self, filename):
    self.filename = filename
    with open(os.path.dirname(os.path.realpath(__file__)) + os.sep + filename) as f:
      self.memory = next([int(s) for s in line.split(',')] for line in f.read().splitlines())
    return self

  def run_computer(self, skip, add, mul):
    for pos in range(skip, len(self.memory), 4):
      opcode, a, b, c = self.memory[pos], self.memory[pos+1], self.memory[pos+2], self.memory[pos+3]
      if opcode == 1:
        self.memory[c] = add(self.memory[a], self.memory[b])
      elif opcode == 2:
        self.memory[c] = mul(self.memory[a], self.memory[b])
      elif opcode == 99:
        return

  def run_computer_with_numbers(self):
    return self.run_computer(0, operator.add, operator.mul)

  def run_with_grammar(self, noun, verb):
    self.memory[1] = noun
    self.memory[2] = verb
    self.run_computer_with_numbers()
    return self.memory[0]

  def part1(self):
    return self.run_with_grammar(12, 2)

  def part2(self, goal):
    backup = self.memory[:]
    for noun in range(1, 100):
      for verb in range(1, 100):
        self.memory = backup[:]
        if self.run_with_grammar(noun, verb) == goal:
          return noun, verb

  def part2_eval(self, goal):
    self.memory[1] = '{0}'
    self.memory[2] = '{1}'
    fake_add = lambda a, b: '({}+{})'.format(a, b)
    fake_mul = lambda a, b: '({}*{})'.format(a, b)
    self.run_computer(4, fake_add, fake_mul)

    expression = self.memory[0]
    for noun in range(1, 100):
      for verb in range(1, 100):
        if eval(expression.format(noun, verb)) == goal:
          return noun, verb

print('Part 1', Solution().load('input.txt').part1())

print('Part 2', Solution().load('input.txt').part2(19690720))

print('Part 2, with eval', Solution().load('input.txt').part2_eval(19690720))
