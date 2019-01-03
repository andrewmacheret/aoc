from networkx import Graph, dijkstra_path_length
from itertools import product, combinations
from collections import defaultdict

import sys
sys.path.append('../')
from day03.main import bounds


DIRS_RIGHT_AND_DOWN = [(0, 1), (1, 0)]

TOOLS_ALLOWED = {'.': 'CT', '=': 'CN', '|': 'TN', 'M': 'CTN', 'T': 'CTN'}
TOOL_SWITCHES = {k: list(combinations(v, 2)) for k, v in TOOLS_ALLOWED.iteritems()}
TOOL_TRAVELINGS = {(k1, k2): list(set(v1).intersection(set(v2))) for k1, v1 in TOOLS_ALLOWED.iteritems() for k2, v2 in TOOLS_ALLOWED.iteritems()}

CAVE_RISK = {'.': 0, '=': 1, '|': 2}
CAVE_ASSESSMENT = {v: k for k, v in CAVE_RISK.iteritems()}


def draw_layout(layout):
  min_x, min_y, max_x, max_y = bounds(layout.keys())
  print('\n'.join(''.join(layout[x, y] for x in xrange(min_x, max_x + 1)) for y in xrange(min_y, max_y + 1)))


def fill_grid(depth, tx, ty, width, height):
  grid = defaultdict(int)
  layout = defaultdict(lambda: '.')
  
  for x, y in product(xrange(width), xrange(height)):
    if x == 0:
      geologic = y * 48271
    elif y == 0:
      geologic = x * 16807
    elif (x, y) == (tx, ty):
      geologic = 0
    else:
      geologic = grid[x - 1, y] * grid[x, y - 1]
    grid[x, y] = (geologic + depth) % 20183
    layout[x, y] = CAVE_ASSESSMENT[grid[x, y] % 3]
  
  layout[0, 0] = 'M'
  layout[tx, ty] = 'T'

  return layout


def shortest_cave_path(layout, tx, ty, width, height):
  graph = Graph()

  for x, y in product(xrange(width), xrange(height)):
    for item_from, item_to in TOOL_SWITCHES[layout[x, y]]:
      graph.add_edge((x, y, item_from), (x, y, item_to), weight=7)
    for dx, dy in DIRS_RIGHT_AND_DOWN:
      x2, y2 = x + dx, y + dy
      if x2 < width and y2 < height:
        for item in TOOL_TRAVELINGS[layout[x, y], layout[x2, y2]]:
          graph.add_edge((x, y, item), (x2, y2, item), weight=1)
  
  return dijkstra_path_length(graph, (0, 0, 'T'), (tx, ty, 'T'))


def parse_cave(lines):
  return int(lines[0].split(': ')[1]), tuple(map(int, lines[1].split(': ')[1].split(',')))


class Day22:
  def __init__(self, verbose=False):
    self.verbose = verbose

  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.depth, (self.tx, self.ty) = parse_cave(self.lines)
    return self

  def part1(self):
    return sum(CAVE_RISK.get(self.layout[x, y], 0) for y in xrange(self.ty + 1) for x in xrange(self.tx + 1))

  def part2(self):
    return shortest_cave_path(self.layout, self.tx, self.ty, self.width, self.height)

  def solve(self, extra):
    self.width, self.height = self.tx + 1 + extra, self.ty + 1 + extra
    self.layout = fill_grid(self.depth, self.tx, self.ty, self.width, self.height)
    if self.verbose: draw_layout(self.layout)

    return [
      {'part1': self.part1()},
      {'part2': self.part2()},
    ]


if __name__== "__main__":
  print(Day22(verbose=True).load('input-test.txt').solve(5))
  print(Day22().load('input.txt').solve(100))
