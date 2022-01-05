#!/usr/bin/env python3

from operator import gt, lt, eq
import re

from common.util import load, test, change_dir


my_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

ops_part_2 = {
    'cats': gt,
    'trees': gt,
    'pomeranians': lt,
    'goldfish': lt
}


def solve(part, file):
  data = load(file)
  sues = {}
  for line in data:
    m = re.split(r'[:, ]+', line)
    sues[int(m[1])] = {item: int(count)
                       for item, count in zip(*[iter(m[2:])]*2)}
  ops = (ops_part_2 if part == 2 else {})
  for num, info in sues.items():
    if all(ops.get(item, eq)(count, my_sue[item]) for item, count in info.items()):
      yield num


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test([40], list(solve(part=1, file='input-real')))
  test([241], list(solve(part=2, file='input-real')))
