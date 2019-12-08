#!/usr/bin/env python3
import re
from itertools import chain, permutations

from day01.main import load, test

def load_regex(filename, regex, script=__file__):
  return [re.match(regex, line).groups() for line in load(filename, script=script)]

def load_happies(filename, script=__file__):
  happy_regex = r'(.*) would (.*) (.*) happiness units by sitting next to (.*).'
  return {(a, b): int(amount) * [-1,1][act=='gain'] for a, act, amount, b in load_regex(filename, regex=happy_regex, script=__file__)}

def maximize_happiness(filename, add_yourself=False):
  happies = load_happies(filename)
  names = {a for a, _ in happies.keys()}
  if add_yourself: names.add(None)
  return max(sum(happies.get((a, b), 0) + happies.get((b, a), 0) for a, b in zip(p, chain(p[1:], [p[0]]))) for p in permutations(names))

if __name__== "__main__":
  test(330, maximize_happiness('input-test-1.txt'))
  test(664, maximize_happiness('input.txt'))
  test(640, maximize_happiness('input.txt', add_yourself=True))
