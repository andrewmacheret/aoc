#!/usr/bin/env python3

from common.util import *


def gen_primes(n):
  sieve = [1] * (n+1)
  for p in range(2, n+1):
    if (sieve[p] and sieve[p] % 2 == 1):
      yield p
      for i in range(p, n+1, p):
        sieve[i] = 0


def run(instructions):
  idx = 0
  reg = defaultdict(int)
  count = 0

  def val(arg):
    return reg[arg] if arg.isalpha() else int(arg)

  while 0 <= idx < len(instructions):
    op, *args = instructions[idx]
    if op == 'set':
      reg[args[0]] = val(args[1])
    elif op == 'sub':
      reg[args[0]] -= val(args[1])
    elif op == 'mul':
      reg[args[0]] *= val(args[1])
      count += 1
    elif op == 'jnz':
      if val(args[0]):
        idx += val(args[1]) - 1
    idx += 1
  return count


def run2(instructions):
  a, b, c, d, e = [int(instructions[i][2]) for i in (0, 4, 5, 7, 30)]
  x = a*b - c
  lo, hi = x + e, x - d + 1
  primes = set(gen_primes(hi))
  return sum(b not in primes for b in range(lo, hi, -e))


def solve(part, file):
  instructions = load_tokens(file)
  return (run, run2)[part](instructions)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(9409, solve(part=0, file='input-real'))

  test(913, solve(part=1, file='input-real'))
