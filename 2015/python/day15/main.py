#!/usr/bin/env python3

from collections import namedtuple
from functools import reduce
from operator import mul
import re

from common.util import load, test, change_dir


def parse_nums(line):
  return [*map(int, re.findall(r'[-+]?\d+', line))]


Ingredient = namedtuple(
    'Ingredient', ['capacity', 'durability', 'flavor', 'texture', 'calories'])


def pick_sum(count, size):
  if count == 1:
    for x in range(size):
      yield (x,)
  else:
    for x in range(size):
      for tup in pick_sum(count-1, size-x):
        yield x, *tup


def scores(ingredients, calories):
  ing = list(ingredients.values())
  for tup in pick_sum(len(ing), 101):
    if not calories or calories == sum(i[4]*t for i, t in zip(ing, tup)):
      yield reduce(mul, (max(0, sum(i[x]*t for i, t in zip(ing, tup))) for x in range(4)))


def solve(part, file):
  ingredients = {}
  for line in load(file):
    name, spec = line.split(':')
    ingredients[name] = Ingredient(*parse_nums(spec))

  return max(scores(ingredients, 500*(part-1)))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(62842880, solve(part=1, file='input-test-1'))
  test(18965440, solve(part=1, file='input-real'))

  test(57600000, solve(part=2, file='input-test-1'))
  test(15862900, solve(part=2, file='input-real'))
