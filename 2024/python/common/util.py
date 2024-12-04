import os
import re
from math import *

from functools import *
from heapq import *
from collections import *
from itertools import *
from string import *
from operator import *
from pprint import pprint


def change_dir(file):
  os.chdir(os.path.dirname(file))


@cache
def load(file):
  with open(file) as f:
    return f.read().splitlines()


@cache
def load_ints(file):
  return [*map(int, load(file))]


@cache
def load_csv(file):
  return [re.split(r', *', line) for line in load(file)]


@cache
def load_tokens(file):
  return [line.split(' ') for line in load(file)]


@cache
def load_dict(file):
  return parse_dict(load(file))


@cache
def load_grid(file):
  return parse_grid(load(file))


@cache
def load_blocks(file):
  with open(file) as f:
    return [block.splitlines() for block in f.read().split('\n\n')]


def parse_nums(line):
  return [*map(int, re.findall(r'[+-]?\d+', line))]


def parse_tokens(line):
  return re.findall(r'\w+', line)


def parse_words(line):
  return re.findall(r'[a-zA-Z]+', line)


def parse_grid(block):
  return [[*line] for line in block]


def parse_dict(block):
  return {(x,y): ch for y,row in enumerate(block) for x,ch in enumerate(row)}


def sign(x):
  return (x > 0) - (x < 0)


def draw(grid, **vargs):
  for type, fn in ((set, draw_set), (dict, draw_dict), (list, draw_grid)):
    if isinstance(grid, type):
      return fn(grid, **vargs)
  raise Exception('Unrecognized type', grid)


def draw_set(grid, fill='#', empty='.'):
  return draw_dict({(x, y): (empty, fill)[(x, y) in grid] for x, y in grid})


def draw_dict(grid, empty='.'):
  x_min = y_min = inf
  x_max = y_max = -inf
  for x, y in grid:
    x_min, x_max = min(x_min, x), max(x_max, x)
    y_min, y_max = min(y_min, y), max(y_max, y)
  return '\n'.join(''.join(grid.get((x, y), empty) for x in range(x_min, x_max+1)) for y in range(y_min, y_max+1))


def draw_grid(grid):
  n, m = len(grid), len(grid[0]) if grid else 0
  return '\n'.join(''.join(grid[y][x] for x in range(m)) for y in range(n))


def tuples(items):
  return tuple(tuples(item) if isinstance(item, list) else item for item in items)


def lists(items):
  return list(lists(item) if isinstance(item, tuple) else item for item in items)

def run_with_cycles(initial, simulate, num_cycles):
  seen = {initial: 0}
  for i in count(1):
    s = simulate()
    if s in seen:
      start = seen[s]
      cycle = i - start
      for i in range((num_cycles - start) % cycle):
        s = simulate()
      break
    seen[s] = i

def flip_horizontal(x):
    return [y[::-1] for y in x]


def flip_vertical(x):
    return x[::-1]


def rotate_clock(x):
    return list(map(list, zip(*x[::-1])))


def rotate_counter(x):
    return list(map(list, zip(*x)))[::-1]


def ascii_blocks(ascii):
  m = len(ascii[0])
  breaks = [i for i in range(m) if all(line[i] == '.' for line in ascii)]
  for a, b in zip([-1] + breaks, breaks + [m]):
    yield '\n'.join(line[a+1:b] for line in ascii)


def build_letters(ascii, letters):
  ascii = ascii.strip().split('\n')
  return {b: c for b, c in zip(ascii_blocks(ascii), letters)}


def ocr(ascii):
  if isinstance(ascii, str):
    ascii = ascii.split('\n')
  if (n := len(ascii)) not in ascii_mappings:
    raise Exception("Unsupported height: {}".format(n))
  mapping = ascii_mappings[n]
  return ''.join(mapping.get(b, '?') for b in ascii_blocks(ascii))


ascii_6 = """
.##..###...##..###..####.####..##..#..#.###...##.#..#.#....#...#.#...#..##..###..###...###.###.#..#.#...#.#...#.####
#..#.#..#.#..#.#..#.#....#....#..#.#..#..#.....#.#.#..#....##.##.##..#.#..#.#..#.#..#.#.....#..#..#.#...#.#...#....#
#..#.###..#....#..#.###..###..#....####..#.....#.##...#....#.#.#.#.#.#.#..#.#..#.#..#.#.....#..#..#.#...#..#.#....#.
####.#..#.#....#..#.#....#....#.##.#..#..#.....#.#.#..#....#...#.#..##.#..#.###..###...##...#..#..#.#...#...#....#..
#..#.#..#.#..#.#..#.#....#....#..#.#..#..#..#..#.#.#..#....#...#.#...#.#..#.#....#.#.....#..#..#..#..#.#....#...#...
#..#.###...##..###..####.#.....###.#..#.###..##..#..#.####.#...#.#...#..##..#....#..#.###...#...##....#.....#...####
"""
ascii_mappings = {
    # missing Q,W ... not sure about D,T,V,M,N
    6: build_letters(ascii_6, 'ABCDEFGHIJKLMNOPRSTUVYZ')
}


DIRS_4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
DIRS_8 = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if not (x == y == 0)]
DIAG = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
RIGHT = (1,0)
UP = (0,-1)
LEFT = (-1,0)
DOWN = (0,1)


def _color(code):
  return '\033[{}m'.format(code)


TEST_OUTPUT = [_color('91') + "FAIL" + _color('0'),
               _color('92') + "PASS" + _color('0')]


def test(expected, actual):
  result = TEST_OUTPUT[expected == actual]
  if isinstance(expected, str) and '\n' in expected:
    print(("{} ... expected = \n{}\n actual = \n{}\n").format(
        result, expected, actual))
  else:
    print(("{} ... expected = {} actual = {}").format(result, expected, actual))
