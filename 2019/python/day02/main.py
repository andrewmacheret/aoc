#!/usr/bin/env python3
import os
import operator
from sympy import Symbol, Eq, S, solve

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

  def run_with_grammar(self, noun, verb, skip=0, add=operator.add, mul=operator.mul):
    self.memory[1] = noun
    self.memory[2] = verb
    self.run_computer(skip, add, mul)
    return self.memory[0]

  def part1(self):
    return self.run_with_grammar(12, 2)

  def part2(self, goal):
    backup = self.memory
    for noun in range(0, 100):
      for verb in range(0, 100):
        self.memory = backup[:]
        if self.run_with_grammar(noun, verb) == goal:
          return noun, verb

  def part2_eval(self, goal):
    fake_add = lambda a, b: '({}+{})'.format(a, b)
    fake_mul = lambda a, b: '({}*{})'.format(a, b)
    self.run_with_grammar('noun', 'verb', skip=4, add=fake_add, mul=fake_mul)

    expression = self.memory[0]
    for noun in range(1, 100):
      for verb in range(1, 100):
        if eval(expression) == goal:
          return noun, verb

  def part2_solve_imperfect(self, goal, override_noun=None, override_verb=None):
    fake_add = lambda a, b: '({}+{})'.format(a, b)
    fake_mul = lambda a, b: '({}*{})'.format(a, b)
    self.run_with_grammar('noun', 'verb', skip=4, add=fake_add, mul=fake_mul)
    expression = self.memory[0]
    noun = override_noun or Symbol('noun')
    verb = override_verb or Symbol('verb')
    return solve(Eq(eval(expression), goal), noun, verb)

print('Part 1 ...', Solution().load('input.txt').part1())

print('Part 2 ...', Solution().load('input.txt').part2(19690720))

print('Part 2, with eval ...', Solution().load('input.txt').part2_eval(19690720))

print('Part 2, with sympy ...', Solution().load('input.txt').part2_solve_imperfect(19690720))
# above outputs `noun = 761401/8100 - verb/202500` which is effectively `noun = 94`
print('Part 2, with sympy ...', Solution().load('input.txt').part2_solve_imperfect(19690720, override_noun=94))
