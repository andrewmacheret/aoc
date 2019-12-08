#!/usr/bin/env python3
import re
from itertools import permutations

from day01.main import load, test

def load_distances(filename, script=__file__):
  inputs = [re.match(r'(.*) to (.*) = (.*)', line).groups() for line in load(filename, script=script)]
  distances = {}
  for a, b, dist in inputs:
    distances[a, b] = distances[b, a] = int(dist)
  return distances
    
def shortest_path(distances, op=min):
  places = {a for a, _ in distances.keys()}
  return op(sum(distances[a, b] for a, b in zip(p, p[1:])) for p in permutations(places))

def part1(filename):
  return shortest_path(load_distances(filename))

def part2(filename):
  return shortest_path(load_distances(filename), max)

if __name__== "__main__":
  test(605, part1('input-test-1.txt'))
  test(117, part1('input.txt'))
  
  test(982, part2('input-test-1.txt'))
  test(909, part2('input.txt'))
