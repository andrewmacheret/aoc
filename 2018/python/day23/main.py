import re
from z3 import Optimize, Int, If  # pip install z3-solver

import sys
sys.path.append('../')
from day20.main import tuple_add


def parse_bots(lines):
  return [map(int, re.match(r'^pos=<([^,]*),([^,]*),([^,]*)>, r=([^,]*)$', line).groups()) for line in lines]


def distance(tuple1, tuple2, abs_func=abs):
  return sum(tuple_add(tuple1, tuple2, op=lambda a, b: abs_func(a - b)))


def max_bots_in_range_of_bot(bots):
  max_radius = max(r for x, y, z, r in bots)
  bx, by, bz = next((x, y, z) for x, y, z, r in bots if r == max_radius)
  return sum(distance((x, y, z), (bx, by, bz)) <= max_radius for x, y, z, r in bots)


def maximize_distance(bots):
  o = Optimize()

  z3_abs = lambda k: If(k >= 0, k, -k)
  z3_in_ranges = [Int('in_range_of_bot_' + str(i)) for i in xrange(len(bots))]
  z3_x, z3_y, z3_z = (Int('x'), Int('y'), Int('z'))
  z3_sum = Int('sum')
  z3_dist = Int('dist')

  for i, (x, y, z, r) in enumerate(bots):
    o.add(z3_in_ranges[i] == If(distance((z3_x, z3_y, z3_z), (x, y, z), z3_abs) <= r, 1, 0))

  o.add(z3_sum == sum(z3_in_ranges))

  o.add(z3_dist == distance((z3_x, z3_y, z3_z), (0, 0, 0), z3_abs))

  h1, h2 = o.maximize(z3_sum), o.minimize(z3_dist)
  o.check()
  # o.lower(h1), o.upper(h1)

  lower, upper = o.lower(h2), o.upper(h2)
  # o.model()[z3_x], o.model()[z3_y], o.model()[z3_z]

  if str(lower) != str(upper): raise Exception('lower ({}) != upper ({})'.format(lower, upper))
  return (lower, upper)


class Day23:
  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.bots = parse_bots(self.lines)
    return self

  def part1(self):
    return max_bots_in_range_of_bot(self.bots)

  def part2(self):
    return maximize_distance(self.bots)

  def solve(self):
    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'part2': self.part2()},
    ]

print(Day23().load('input-test.txt').solve())
print(Day23().load('input-test2.txt').solve())
print(Day23().load('input.txt').solve())
