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
  return [line.split(', ') for line in load(file)]


def parse_nums(line):
  return [*map(int, re.findall(r'\d+', line))]


def test(expected, actual):
  result = ["FAIL", "PASS"][expected == actual]
  print(("{} ... expected = {} actual = {}").format(result, expected, actual))
