import os
import re
from math import inf
from functools import cache


def change_dir(file):
  os.chdir(os.path.dirname(file))


@cache
def load(file):
  with open(file) as f:
    return f.read().splitlines()


@cache
def load_ints(file):
  return list(map(int, load(file)))


@cache
def load_csv(file):
  return [re.split(r', *', line) for line in load(file)]


@cache
def load_tokens(file):
  return [line.split(' ') for line in load(file)]


def parse_nums(line):
  return [*map(int, re.findall(r'\d+', line))]


@cache
def load_blocks(file):
  def gen():
    lines = []
    for line in load(file):
      if not line:
        yield lines
        lines = []
      else:
        lines.append(line)
    if lines:
      yield lines
  return list(gen())


def sign(x):
  return (x > 0) - (x < 0)


def parse_nums(line):
  return [*map(int, re.findall(r'\d+', line))]


def find_tokens(line):
  return re.findall(r'\w+', line)


def find_words(line):
  return re.findall(r'[a-zA-Z]+', line)


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


DIRS_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
DIRS_8 = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if not (x == y == 0)]


def test(expected, actual):
  result = ["FAIL", "PASS"][expected == actual]
  print(("{} ... expected = {} actual = {}").format(result, expected, actual))
