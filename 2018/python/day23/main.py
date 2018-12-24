import re
from z3 import Optimize, Int, If  # pip install z3-solver

class Solution:
  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()

    self.bots = []
    for line in self.lines:
      match = re.match(r'^pos=<([^,]*),([^,]*),([^,]*)>, r=([^,]*)$', line)
      self.bots.append({
        'pos': (int(match.group(1)), int(match.group(2)), int(match.group(3))),
        'radius': int(match.group(4))
      })

    return self

  def distance(self, (x1, y1, z1), (x2, y2, z2), abs_func=abs):
    return abs_func(x1-x2) + abs_func(y1-y2) + abs_func(z1-z2)

  def maximize_distance(self):
    o = Optimize()

    z3_abs = lambda i: If(i >= 0, i, -i)
    z3_in_ranges = [ Int('in_range_of_bot_' + str(i)) for i in xrange(len(self.bots)) ]
    z3_xyz = (Int('x'), Int('y'), Int('z'))
    z3_sum = Int('sum')
    z3_dist = Int('dist')

    for i, bot in enumerate(self.bots):
      o.add(z3_in_ranges[i] == If(self.distance(z3_xyz, bot['pos'], z3_abs) <= bot['radius'], 1, 0))

    o.add(z3_sum == sum(z3_in_ranges))

    o.add(z3_dist == self.distance(z3_xyz, (0,0,0), z3_abs))

    h1 = o.maximize(z3_sum)
    h2 = o.minimize(z3_dist)
    o.check()
    # o.lower(h1), o.upper(h1)

    return o.lower(h2), o.upper(h2)
    # o.model()[Int('x')], o.model()[Int('y')], o.model()[Int('z')]

  def solve(self):
    max_radius = max(bot['radius'] for bot in self.bots)
    best_bot = next(bot for bot in self.bots if bot['radius'] == max_radius)
    in_range = sum(1 for bot in self.bots if self.distance(bot['pos'], best_bot['pos']) <= max_radius)
    max_dist = self.maximize_distance()

    return {
      'part1': in_range,
      'part2': max_dist
    }

print(Solution().load('input-test.txt').solve())
print(Solution().load('input-test2.txt').solve())
print(Solution().load('input.txt').solve())
