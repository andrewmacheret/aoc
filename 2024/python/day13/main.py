#!/usr/bin/env python3

from common.util import *
from z3 import Solver, Real  # pip3 install z3-solver


def solve_z3(part, file):
  total = 0

  for block in load_blocks(file):
    (ax,ay), (bx, by), (gx, gy) = map(parse_nums, block)
    if part:
      gx += 10000000000000
      gy += 10000000000000

    equations = Solver()
    a, b = map(Real, ('a', 'b'))
    equations.add(a * ax + b * bx == gx)
    equations.add(a * ay + b * by == gy)
    equations.check()
    model = equations.model()
    a,b = (eval(str(model[var])) for var in (a,b))

    # all answers are possible, but only integers answers are the ones we seek
    if type(a) == int and type(b) == int:
      total += 3*a+b

  return total

def solve_normal(file, part):
  total = 0

  for block in load_blocks(file):
    (ax,ay), (bx, by), (gx, gy) = map(parse_nums, block)
    if part:
      gx += 10000000000000
      gy += 10000000000000

    a = round((gx - gy*(bx/by)) / (ax - ay*(bx/by)))
    b = round((gx - a * ax) / bx)
    if a * ax + b * bx == gx and a * ay + b * by == gy:
      total += 3*int(a)+int(b)

  return total



### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  # normal

  test(480, solve_normal(part=0, file='input-test-1'))
  test(31761, solve_normal(part=0, file='input-real'))

  test(875318608908, solve_normal(part=1, file='input-test-1'))
  test(90798500745591, solve_normal(part=1, file='input-real'))

  # with z3

  test(480, solve_z3(part=0, file='input-test-1'))
  test(31761, solve_z3(part=0, file='input-real'))

  test(875318608908, solve_z3(part=1, file='input-test-1'))
  test(90798500745591, solve_z3(part=1, file='input-real'))
