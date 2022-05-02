#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor
from queue import SimpleQueue, Empty

from common.util import *


def run(instructions, id, send, receive):
  idx = 0
  reg = defaultdict(int)
  reg['p'] = id
  count = 0

  def val(arg):
    return reg[arg] if arg.isalpha() else int(arg)

  while 0 <= idx < len(instructions):
    op, *args = instructions[idx]
    if op == 'set':
      reg[args[0]] = val(args[1])
    elif op == 'add':
      reg[args[0]] += val(args[1])
    elif op == 'mul':
      reg[args[0]] *= val(args[1])
    elif op == 'mod':
      reg[args[0]] %= val(args[1])
    elif op == 'jgz':
      if val(args[0]) > 0:
        idx += val(args[1]) - 1
    elif op == 'snd':
      count += 1
      send(val(args[0]))
    elif op == 'rcv':
      try:
        reg[args[0]] = receive()
      except Empty:
        return count
    idx += 1


def solve(part, file):
  instructions = load_tokens(file)

  if part == 0:
    last = None

    def send(x):
      nonlocal last
      last = x

    def receive():
      raise Empty

    run(instructions, 0, send, receive)
    return last

  else:
    q1, q2 = SimpleQueue(), SimpleQueue()

    timeout = 0.001  # pretty damn fast
    params = [
        (instructions, 0, q1.put, lambda: q2.get(timeout=timeout)),
        (instructions, 1, q2.put, lambda: q1.get(timeout=timeout)),
    ]

    with ThreadPoolExecutor() as executor:
      return [executor.submit(run, *p) for p in params][1].result()


### THE REST IS TESTS ###
if __name__ == "__main__":
  change_dir(__file__)

  test(4, solve(part=0, file='input-test-1'))
  test(2951, solve(part=0, file='input-real'))

  test(3, solve(part=1, file='input-test-2'))
  test(7366, solve(part=1, file='input-real'))
