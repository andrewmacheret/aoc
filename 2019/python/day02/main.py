#!/usr/bin/env python3
import os
import operator
from sympy import Symbol, Eq, S, solve

from day01.main import load, test


def load_memory(filename, script=__file__):
  return next([int(s) for s in line.split(',')] for line in load(filename, script=script))

def run_computer(memory, skip, add, mul):
  for pos in range(skip, len(memory), 4):
    opcode = memory[pos]
    if opcode == 1:
      a, b, c = memory[pos+1], memory[pos+2], memory[pos+3]
      memory[c] = add(memory[a], memory[b])
    elif opcode == 2:
      a, b, c = memory[pos+1], memory[pos+2], memory[pos+3]
      memory[c] = mul(memory[a], memory[b])
    elif opcode == 99:
      return

def run_with_grammar(memory, noun, verb, skip=0, add=operator.add, mul=operator.mul):
  memory[1] = noun
  memory[2] = verb
  run_computer(memory, skip, add, mul)
  return memory[0]

def part0(filename):
  memory = load_memory(filename)
  run_computer(memory, skip=0, add=operator.add, mul=operator.mul)
  return memory
  
def part1(filename):
  memory = load_memory(filename)
  return run_with_grammar(memory, 12, 2)

def part2(filename, goal):
  backup = load_memory(filename)
  for noun in range(0, 100):
    for verb in range(0, 100):
      memory = backup[:]
      if run_with_grammar(memory, noun, verb) == goal:
        return noun, verb

def part2_eval(filename, goal):
  memory = load_memory(filename)
  fake_add = lambda a, b: '({}+{})'.format(a, b)
  fake_mul = lambda a, b: '({}*{})'.format(a, b)
  run_with_grammar(memory, 'noun', 'verb', skip=4, add=fake_add, mul=fake_mul)

  expression = memory[0]
  for noun in range(1, 100):
    for verb in range(1, 100):
      if eval(expression) == goal:
        return noun, verb

def part2_solve_imperfect(filename, goal, override_noun=None, override_verb=None):
  memory = load_memory(filename)
  fake_add = lambda a, b: '({}+{})'.format(a, b)
  fake_mul = lambda a, b: '({}*{})'.format(a, b)
  run_with_grammar(memory, 'noun', 'verb', skip=4, add=fake_add, mul=fake_mul)
  expression = memory[0]
  noun = override_noun or Symbol('noun')
  verb = override_verb or Symbol('verb')
  return solve(Eq(eval(expression), goal), noun, verb)

if __name__== "__main__":
  test([3500,9,10,70,2,3,11,0,99,30,40,50], part0('input-test-1.txt'))
  test([2,0,0,0,99], part0('input-test-2.txt'))
  test([2,3,0,6,99], part0('input-test-3.txt'))
  test([2,4,4,5,99,9801], part0('input-test-4.txt'))
  test([30,1,1,4,2,5,6,0,99], part0('input-test-5.txt'))
  test(3085697, part1('input.txt'))

  test((94, 25), part2('input.txt', 19690720))
  test((94, 25), part2_eval('input.txt', 19690720))
  test("[(761401/8100 - verb/202500, verb)]", str(part2_solve_imperfect('input.txt', 19690720)))
  test("[{verb: 25}]", str(part2_solve_imperfect('input.txt', 19690720, override_noun=94)))
