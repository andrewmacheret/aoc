#!/usr/bin/env python3

from common.util import *

def parse_ops(block):
  # format it as: (start, end, add)
  ops = sorted((s, s+c, d-s) for d, s, c in map(parse_nums, block[1:]))
  # add gap intervals
  more_ops = [(a[1], b[0], 0) for a,b in pairwise(ops) if a[1] < b[0]]
  # add initial gap interval
  if ops[0][0] > 0:
    more_ops.append((0, ops[0][0], 0))
  # add final gap interval
  more_ops.append((ops[-1][1], inf, 0))
  return sorted(ops + more_ops)

def part1(seeds, all_ops):
  for seed in seeds:
    for ops in all_ops:
      seed += next(amt for start, end, amt in ops if start <= seed < end)
    yield seed

def part2(seeds, all_ops):
  for seed, seed_count in zip(*[iter(seeds)]*2): # every 2 seed vals
    q = [(seed, seed + seed_count)]
    for ops in all_ops:
      next_q = []
      for seed_start, seed_end in q:
        for op_start, op_end, op_amt in ops:
          # either:
          # 1. op_start is inside the seed range
          # 2. op_end-1 is inside the seed range
          # 3. seed_start and seed_end are inside the op range
          #    (we only need to check one of seed_start or seed_end)
          if seed_start <= op_start < seed_end or \
              seed_start <= op_end-1 < seed_end or \
              op_start <= seed_start < op_end:
            start = max(seed_start, op_start)
            end = min(seed_end, op_end)
            next_q.append((start + op_amt, end + op_amt))
      q = next_q

    for x in q:
      yield x[0]


def solve(part, file):
  seeds, *blocks = load_blocks(file)

  seeds = parse_nums(seeds[0])
  all_ops = list(map(parse_ops, blocks))
  
  return min((part1 if part == 0 else part2)(seeds, all_ops))



### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(35, solve(part=0, file='input-test-1'))
  test(340994526, solve(part=0, file='input-real'))

  test(46, solve(part=1, file='input-test-1'))
  test(52210644, solve(part=1, file='input-real'))
