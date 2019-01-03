import re
from itertools import count

import sys
sys.path.append('../')
from day03.main import bounds

def parse_particles(lines):
  # x, y, dx, dy
  return [map(int, re.match(r'^position=< *(-?[0-9]+), *(-?[0-9]+)> velocity=< *(-?[0-9]+), *(-?[0-9]+)>$', line).groups()) for line in lines]

def extent(particles):
  min_x, min_y, max_x, max_y = bounds(particles, 2)
  return (max_x - min_x) * (max_y - min_y)

def local_min(sequence, key):
  last_score = float('inf')
  for item in sequence:
    score = key(item)
    if last_score < score:
      return last
    last, last_score = item, score

def draw_particles(particles):
  min_x, min_y, max_x, max_y = bounds(particles, 2)
  grid = [['.' for _ in xrange(min_x, max_x+1)] for _ in xrange(min_y, max_y+1)]
  for x,y,dx,dy in particles: grid[y-min_y][x-min_x] = '*'
  print('\n'.join(''.join(row) for row in grid))

def move_particles(particles):
  for time in count():
    yield particles
    particles = [(x+dx, y+dy, dx, dy) for x,y,dx,dy in particles]

def move_particles_until_readable(particles):
  time, particles = local_min(enumerate(move_particles(particles)), lambda (t,p): extent(p))
  draw_particles(particles)
  return time

class Day10:
  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.particles = parse_particles(self.lines)
    return self

  def part2(self):
    return move_particles_until_readable(self.particles)

  def solve(self):
    return [
      {'filename': self.filename},
      {'part2': self.part2()},
    ]

if __name__== "__main__":
  print(Day10().load('input-test.txt').solve())
  print(Day10().load('input.txt').solve())
