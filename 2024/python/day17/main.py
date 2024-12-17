#!/usr/bin/env python3

from common.util import *


def solve(file, registers=False):
  data = load_blocks(file)
  a,b,c = [x[0] for x in map(parse_nums, data[0])]
  prog = parse_nums(data[1][0])

  def combo(x):
    if 0 <= x <= 3: return x
    if x == 4: return a
    if x == 5: return b
    if x == 6: return c
    raise Exception('Invalid: ' + x)

  i = 0
  res = []
  while i < len(prog):
    op, x = prog[i], prog[i+1]
    if op == 0:
      a = a // (1 << combo(x))
    elif op == 1:
      b = b ^ x
    elif op == 2:
      b = combo(x) % 8
    elif op == 3:
      if a != 0:
        i = x - 2
    elif op == 4:
      b = b ^ c
    elif op == 5:
      res.append(combo(x) % 8)
    elif op == 6:
      b = a // (1 << combo(x))
    elif op == 7:
      c = a // (1 << combo(x))
    else: raise Exception('Invalid: ' + op)
    i += 2
  
  if registers:
    return f"{a},{b},{c}"
  else:
    return ','.join(map(str, res))

def solve2(file):
  data = load_blocks(file)
  prog = parse_nums(data[1][0])

  x = prog[3]
  y = prog[7]

  def step(a):
    b = a & 7
    b ^= x
    c = a // (1 << b)
    b ^= y
    b ^= c
    return b & 7

  def backtrack(a, digit=1):
    if step(a) == prog[-digit]:
      if digit == len(prog):
        yield a
      else:
        for i in range(8):
          yield from backtrack((a << 3) + i, digit + 1)

  return next(b for a in range(8) for b in backtrack(a))

### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test("0,1,9", solve(registers=True, file='input-test-1'))
  test("0,1,2", solve(file='input-test-2'))
  test("0,0,0", solve(registers=True, file='input-test-3'))
  test("4,2,5,6,7,7,7,7,3,1,0", solve(file='input-test-3'))
  test("0,26,0", solve(registers=True, file='input-test-4'))
  test("0,44354,43690", solve(registers=True, file='input-test-5'))
  test("4,6,3,5,6,3,5,2,1,0", solve(file='input-test-6'))

  test("7,4,2,5,1,4,6,0,4", solve(file='input-real'))

  test(164278764924605, solve2(file='input-real'))


