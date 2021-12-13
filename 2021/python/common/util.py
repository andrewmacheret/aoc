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


def draw_set(grid):
  y_min = inf
  y_max = -inf
  x_min = inf
  x_max = -inf
  for x, y in grid:
    x_max = max(x_max, x)
    x_min = min(x_min, x)
    y_max = max(y_max, y)
    y_min = min(y_min, y)
  return '\n'.join(''.join('#' if (x, y) in grid else '.' for x in range(x_min, x_max+1)) for y in range(y_min, y_max+1))


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


DIRS_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
DIRS_8 = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if not (x == y == 0)]


def test(expected, actual):
  result = ["FAIL", "PASS"][expected == actual]
  print(("{} ... expected = {} actual = {}").format(result, expected, actual))
