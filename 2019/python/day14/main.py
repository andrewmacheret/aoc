#!/usr/bin/env python3
import re
import networkx as nx
from collections import defaultdict
from math import ceil

from day01.main import load, test
from day12.main import lcm

def split_quantity(s, regex=r' '):
  amount, item = re.split(regex, s)
  return int(amount), item

def load_formulas(filename, script=__file__):
  return {i[-1][1]: (i[-1][0], i[:-1]) for i in (list(map(split_quantity, re.split(', | => ', line))) for line in load(filename, script=script))}

def min_ore(formulas, order, fuel):
  have = defaultdict(int, {'FUEL': fuel})
  for item in order:
    if item != 'ORE':
      amount = have[item]
      formula_amount, prereqs = formulas[item]
      multiplier = ceil(amount / formula_amount)
      for prereq_amount, prereq_item in prereqs:
        have[prereq_item] += prereq_amount * multiplier
  return have['ORE']

def formula_order(formulas):
  items_for_graph = [(goal, item) for goal, (_, items) in formulas.items() for _, item in items]
  return list(nx.topological_sort(nx.DiGraph(items_for_graph)))

def part1(filename):
  formulas = load_formulas(filename)
  order = formula_order(formulas)
  return min_ore(formulas, order, 1)

def part2(filename, goal=1000000000000):
  formulas = load_formulas(filename)
  order = formula_order(formulas)

  lo = goal // min_ore(formulas, order, 1)
  hi = lo * 4
  while lo < hi:
    mid = (lo + hi) // 2
    ore = min_ore(formulas, order, mid)
    if ore < goal:
      lo = mid + 1
    else:
      hi = mid
  return lo - 1

if __name__== "__main__":
  test(31, part1('input-test-1.txt'))
  test(165, part1('input-test-2.txt'))
  test(13312, part1('input-test-3.txt'))
  test(180697, part1('input-test-4.txt'))
  test(2210736, part1('input-test-5.txt'))
  test(2486514, part1('input.txt'))
  # 
  test(82892753, part2('input-test-3.txt'))
  test(5586022, part2('input-test-4.txt'))
  test(460664, part2('input-test-5.txt'))
  test(998536, part2('input.txt'))
