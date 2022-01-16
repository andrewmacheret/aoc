#!/usr/bin/env python3

from itertools import accumulate, repeat, count

from common.util import load, parse_nums, test, change_dir


def diag_count():
  for start_y in count(1):
    for x in range(1, start_y+1):
      yield x, start_y - x + 1


def find_code(row, col):
  codes = accumulate(repeat(20151125), lambda z, _: (z*252533) % 33554393)
  for (x, y), code in zip(diag_count(), codes):
    if x == col and y == row:
      return code


def solve(file):
  row, col = parse_nums(load(file)[0])
  return find_code(row, col)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  expected = [
      [20151125, 18749137, 17289845, 30943339, 10071777, 33511524],
      [31916031, 21629792, 16929656, 7726640, 15514188, 4041754],
      [16080970, 8057251, 1601130, 7981243, 11661866, 16474243],
      [24592653, 32451966, 21345942, 9380097, 10600672, 31527494],
      [77061, 17552253, 28094349, 6899651, 9250759, 31663883],
      [33071741, 6796745, 25397450, 24659492, 1534922, 27995004],
  ]
  actual = [[find_code(col, row) for row in range(1, 7)]
            for col in range(1, 7)]
  test(expected, actual)

  test(8997277, solve(file='input-real'))
