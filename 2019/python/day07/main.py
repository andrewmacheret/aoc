#!/usr/bin/env python3
from itertools import permutations
import os
from math import inf

from day01.main import load, test
from day02.main import load_memory
from day05.main import Program

single_loop = [0]
inf_loop = iter(int, 1)

def chain_progs(progs, input=0):
  for prog, run in progs:
    prog.input.append(input)
    try: input = next(run, None)
    except: return
    if input is None: return
    yield input

def init_programs(combo, memory):
  return [(prog, prog.run_computer()) for prog in (Program(memory, [val]) for val in combo)]

def try_combos_once(combo, memory):
  progs = init_programs(combo, memory)
  return (list(chain_progs(progs)) or [-inf])[-1]

def try_combos(combo, memory, input=0):
  progs = init_programs(combo, memory)
  while True:
    output = list(chain_progs(progs, input))
    if len(output) > 0: input = output[-1]
    if len(output) < len(combo): return input

def part1(filename):
  memory = load_memory(filename, script=__file__)
  return max(try_combos_once(perm, memory) for perm in permutations(list(range(5))))

def part2(filename):
  memory = load_memory(filename, script=__file__)
  return max(try_combos(perm, memory) for perm in permutations(list(range(5, 10))))

if __name__== "__main__":
  test(43210, part1('input-test-1.txt'))
  test(54321, part1('input-test-2.txt'))
  test(65210, part1('input-test-3.txt'))
  test(24625, part1('input.txt'))
  
  test(139629729, part2('input-test-4.txt'))
  test(18216, part2('input-test-5.txt'))
  test(36497698, part2('input.txt'))
