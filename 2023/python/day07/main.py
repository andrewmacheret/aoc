#!/usr/bin/env python3

from common.util import *



def solve(part, file):  
  order = ['23456789TJQKA', 'J23456789TQKA'][part].index

  def sort_key(line):
    c = Counter(cards := line.split()[0])

    if part == 1:
      j, c['J'] = c['J'], 0
      c[max((v,k) for k,v in c.items())[1]] += j

    return (sorted(c.values(), reverse=1), *map(order, cards))

  return sum(i * int(line.split()[1]) \
             for i, line in enumerate(sorted(load(file), key=sort_key), 1))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(6440, solve(part=0, file='input-test-1'))
  test(248105065, solve(part=0, file='input-real'))

  test(5905, solve(part=1, file='input-test-1'))
  test(249515436, solve(part=1, file='input-real'))
