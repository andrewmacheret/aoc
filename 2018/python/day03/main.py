import re
from collections import defaultdict
from itertools import chain

import sys
sys.path.append('../')
from day01.main import duplicates
from day02.main import quantify

def bounds(coords): # x,y -> returns min_x, min_y, max_x, max_y
  dim = len(coords[0]) if coords else 0
  return tuple(op(coords[j][i] for j in xrange(len(coords))) for op in (min, max) for i in xrange(dim))

def bounds_rects(rects): # x,y,w,h -> returns min_x, min_y, max_x, max_y
  return bounds(list(chain([(x,y) for x,y,w,h in rects], [(x+w-1,y+h-1) for x,y,w,h in rects])))

def multimap(items, type=list):
  result = defaultdict(type)
  for key, val in items:
    result[key].append(val)
  return result

def rect_overlaps(rects):
  return set(duplicates((x+dx,y+dy) for x,y,w,h in rects for dy in xrange(h) for dx in xrange(w)))

def parse_claims(lines):
  return [map(int, re.match(r'^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$', line).groups()) for line in lines]

def draw(claims, overlaps):
  grid = multimap(((x+dx,y+dy), str(n)) for n,x,y,w,h in claims for dy in xrange(h) for dx in xrange(w))

  min_x, min_y, max_x, max_y = bounds_rects([(x,y,w,h) for n,x,y,w,h in claims])

  grid_get = lambda x,y: 'X' if (x,y) in overlaps else grid.get((x,y), ['.'])[0]
  print('\n'.join(''.join([grid_get(x,y) for x in xrange(min_x-1, max_x+2)]) for y in xrange(min_y-1, max_y+2)))

class Day03:
  def __init__(self, verbose=False):
    self.verbose = verbose

  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.claims = parse_claims(self.lines)
    return self

  def part1(self):
    return len(self.overlaps)

  def part2(self):
    return next(n for n,x,y,w,h in self.claims if not any((x+dx,y+dy) in self.overlaps for dy in xrange(h) for dx in xrange(w)))

  def solve(self):
    self.overlaps = rect_overlaps([(x,y,w,h) for n,x,y,w,h in self.claims])
    if self.verbose: draw(self.claims, self.overlaps)

    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'part2': self.part2()}
    ]

if __name__== "__main__":
  print(Day03(verbose=True).load('input-test.txt').solve())
  print(Day03().load('input.txt').solve())
