from collections import deque, defaultdict
from operator import add
from itertools import izip

import sys
sys.path.append('../')
from day03.main import bounds
from day15.main import bfs


def tuple_add(tuple1, tuple2, op=add):
  return tuple(op(a, b) for a, b in izip(tuple1, tuple2))


DIRS = {'E': (+1,  0), 'W': (-1,  0), 'N': ( 0, -1), 'S': ( 0, +1)}
OPPOSITE_DIRS = {'E': 'W', 'W': 'E', 'N': 'S', 'S': 'N'}


def draw_rooms(doors, distances):
  min_x, min_y, max_x, max_y = bounds(doors.keys())

  door = lambda x, y, d: '|' if d in doors[x, y] else '#'
  room = lambda x, y: 'X' if (x, y) == (0, 0) else (str(distances[x, y] % 10) if distances[x, y] else ' ')
  
  top = lambda x, y: '#' + door(x, y, 'N')
  mid = lambda x, y: door(x, y, 'W') + room(x, y)
  
  ilines = lambda fn: (''.join(fn(x, y) for x in xrange(min_x, max_x + 1)) + '#' for y in xrange(min_y, max_y + 1))

  print('\n'.join(row for lst in izip(ilines(top), ilines(mid)) for row in lst))
  print('#' * ((max_x - min_x) * 2 + 3))


def build_rooms(regex):
  doors = defaultdict(dict)
  p = 0, 0
  stack = deque()
  for ch in regex:
    if ch in DIRS:
      last_p = p
      p = tuple_add(last_p, DIRS[ch])
      doors[last_p][ch] = p
      doors[p][OPPOSITE_DIRS[ch]] = last_p
    elif ch == '(':
      stack.append(p)
    elif ch == ')':
      p = stack.pop()
    elif ch == '|':
      p = stack[-1]
  return doors


def room_distances(doors):
  distances = {}
  def next_rooms(p, distance):
    distances[p] = distance
    return doors[p].itervalues()
  for _ in bfs(queue=[(0, 0)], next_items=next_rooms): pass
  return distances


class Day20:
  def __init__(self, verbose=False):
    self.verbose = verbose

  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.regex = self.lines[0]
    return self

  def part1(self, distances):
    return max(distances.itervalues())

  def part2(self, distances, distance_threshold):
    return sum(d >= distance_threshold for d in distances.itervalues())

  def solve(self, distance_threshold):
    doors = build_rooms(self.regex)
    distances = room_distances(doors)
    if self.verbose: draw_rooms(doors, distances)

    return [
      {'filename': self.filename},
      {'distance_threshold': distance_threshold},
      {'part1': self.part1(distances)},
      {'part2': self.part2(distances, distance_threshold)},
    ]


if __name__== "__main__":
  print(Day20(verbose=True).load('input-test.txt').solve(10))
  print(Day20().load('input-test2.txt').solve(20))
  print(Day20().load('input.txt').solve(1000))
