#!/usr/bin/env python3

from common.util import *


class Monkey:
  def __init__(self, block):
    self.items = parse_nums(block[1])
    parts = block[2].split('= old ')[1].split(" ")
    op = {'+': add, '*': mul}[parts[0]]
    self.op = (lambda x: op(x, x)) if parts[1] == 'old' else \
        partial(op, int(parts[1]))
    self.div = parse_nums(block[3])[0]
    self.throw = [parse_nums(block[5])[0],  parse_nums(block[4])[0]]
    self.inspections = 0


def solve(part, file):
  data = load_blocks(file)

  monkeys = [Monkey(block) for block in data]

  big = reduce(mul, (m.div for m in monkeys))
  limit = [lambda x: x // 3, lambda x: x % big][part]
  for _ in range([20, 10000][part]):
    for m in monkeys:
      for i in m.items:
        i = limit(m.op(i))
        x = m.throw[i % m.div == 0]
        monkeys[x].items.append(i)
        m.inspections += 1
      m.items = []

  return mul(*nlargest(2, (m.inspections for m in monkeys)))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(10605, solve(part=0, file='input-test-1'))
  test(56595, solve(part=0, file='input-real'))

  test(2713310158, solve(part=1, file='input-test-1'))
  test(15693274740, solve(part=1, file='input-real'))
