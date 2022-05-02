#!/usr/bin/env python3

from common.util import *


def load_states(file):
  blocks = load_blocks(file)
  meta, *state_infos = blocks
  initial = meta[0][-2]
  steps = int(meta[1].split()[5])
  states = {}
  for info in state_infos:
    name = info[0][-2]
    write0 = int(info[2][-2])
    dir0 = {'l': -1, 'r': 1}[info[3][27]]
    next0 = info[4][26]
    write1 = int(info[6][-2])
    dir1 = {'l': -1, 'r': 1}[info[7][27]]
    next1 = info[8][26]
    states[name] = {
        0: (write0, dir0, next0),
        1: (write1, dir1, next1),
    }
  return states, initial, steps


def solve(file):
  states, current, steps = load_states(file)

  tape = defaultdict(int)
  pos = 0
  for _ in range(steps):
    w, d, n = states[current][tape[pos]]
    tape[pos] = w
    pos += d
    current = n

  return sum(tape.values())


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(3, solve(file='input-test-1'))
  test(4230, solve(file='input-real'))
