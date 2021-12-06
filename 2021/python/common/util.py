import os
import re
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


def test(expected, actual):
  result = ["FAIL", "PASS"][expected == actual]
  print(("{} ... expected = {} actual = {}").format(result, expected, actual))
