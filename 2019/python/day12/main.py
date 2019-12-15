#!/usr/bin/env python3
import re
from itertools import combinations, count
from math import copysign, gcd

from day01.main import load, test

def lcm(a, b):
  return abs(a*b) // gcd(a, b)

def sign(x):
  return int(copysign(1, x)) if x != 0 else 0

class Body:
  def __init__(self, x, y, z):
    self.x, self.y, self.z = x, y, z
    self.dx = self.dy = self.dz = 0


def load_bodies(filename, script=__file__):
  return [Body(*map(int, re.match(r'<x=(.+), y=(.+), z=(.+)>', line).groups())) for line in load(filename, script=script)]

def part1(filename, time):
  bodies = load_bodies(filename)
  for _ in range(time):
    for a, b in combinations(bodies, 2):
      a.dx += sign(b.x - a.x)
      a.dy += sign(b.y - a.y)
      a.dz += sign(b.z - a.z)
      b.dx += sign(a.x - b.x)
      b.dy += sign(a.y - b.y)
      b.dz += sign(a.z - b.z)
    for b in bodies:
      b.x += b.dx
      b.y += b.dy
      b.z += b.dz
  return sum((abs(b.x) + abs(b.y) + abs(b.z)) * (abs(b.dx) + abs(b.dy) + abs(b.dz)) for b in bodies)

def period(positions):
  n = len(positions)
  velocities = [0] * n
  seen = set()
  for time in count():
    z = (tuple(positions), tuple(velocities))
    if z in seen: return time
    seen.add(z)
    for i, j in combinations(range(n), 2):
      change = sign(positions[j] - positions[i])
      velocities[i] += change
      velocities[j] -= change
    for i in range(n):
      positions[i] += velocities[i]

def part2(filename):
  bodies = load_bodies(filename)
  px = period([b.x for b in bodies])
  py = period([b.y for b in bodies])
  pz = period([b.z for b in bodies])
  return lcm(lcm(px, py), pz)

if __name__== "__main__":
  test(179, part1('input-test-1.txt', 10))
  test(1940, part1('input-test-2.txt', 100))
  test(12070, part1('input.txt', 1000))
  
  test(2772, part2('input-test-1.txt'))
  test(4686774924, part2('input-test-2.txt'))
  test(500903629351944, part2('input.txt'))
