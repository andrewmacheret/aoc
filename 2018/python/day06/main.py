from itertools import chain

import sys
sys.path.append('../')
from day03.main import bounds, multimap
from day05.main import alphabet, ALPHABET

def parse_coords(lines):
  return [tuple(map(int, line.split(', '))) for line in lines]

DIRS_ADJACENT = [(1,0), (0,1), (-1,0), (0,-1)]

def largest_inner_coord_size(coords, verbose):
  min_x, min_y, max_x, max_y = bounds(coords)
  grid = {(x,y): i for i, (x,y) in enumerate(coords)}
  score = [1] * len(coords)
  q = [(x,y) for i,(x,y) in enumerate(coords)]

  while q:
    next_moves = multimap( \
      ((x+dx,y+dy), grid[(x,y)]) \
        for x,y in q \
          for dx,dy in DIRS_ADJACENT \
            if min_x-1 <= x+dx <= max_x+1 and min_y-1 <= y+dy <= max_y+1 and (x+dx,y+dy) not in grid \
    )
    q = []

    for (x, y), coord_indexes in next_moves.iteritems():
      if len(set(coord_indexes)) == 1:
        score[coord_indexes[0]] += 1
        grid[(x, y)] = coord_indexes[0]
      else:
        grid[(x, y)] = -1
      q.append((x, y))

  for x,y in chain([(x,y) for x in (min_x-1, max_x+1) for y in xrange(min_y-1, max_y+2)], \
                   [(x,y) for x in xrange(min_x-1, max_x+2) for y in (min_y-1, max_y+1)]):
    if grid[(x, y)] > 0:
      score[grid[(x, y)]] = 0

  if verbose:
    coords_set = set(coords)
    print('\n'.join(''.join((ALPHABET if (x, y) in coords_set else alphabet)[grid[(x,y)] % len(alphabet)] if grid.get((x,y), -1) != -1 else '.' for x in xrange(min_x-1, max_x+2)) for y in xrange(min_y-1, max_y+2)))

  return max(score)

def area_in_range_of_coords(coords, max_distance, verbose):
  min_x, min_y, max_x, max_y = bounds(coords)
  return sum(sum(abs(x-x2) + abs(y-y2) for x2,y2 in coords) < max_distance for x in xrange(min_x, max_x+1) for y in xrange(min_y, max_y+1))



class Day06:
  def __init__(self, verbose=False):
    self.verbose = verbose

  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.coords = parse_coords(self.lines)
    return self

  def part1(self):
    return largest_inner_coord_size(self.coords, self.verbose)

  def part2(self, limit):
    return area_in_range_of_coords(self.coords, limit, self.verbose)

  def solve(self, limit):
    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'part2': self.part2(limit)}
    ]

if __name__== "__main__":
  print(Day06(verbose=True).load('input-test.txt').solve(32))
  print(Day06().load('input.txt').solve(10000))
