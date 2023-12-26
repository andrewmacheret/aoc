#!/usr/bin/env python3

from common.util import *


def run(data):
  return accumulate((s[-1].isdigit() and int(s)
                     for line in data for s in line.split(" ")), initial=1)


def solve(part, file):
  data = load(file)

  array = [*run(data)]

  if part == 0:
    return sum(c*x for c, x in enumerate(array, 1) if c % 40 == 20)

  return draw_set({(c % 40, c // 40)
                   for c, x in enumerate(array)
                   if x-1 <= c % 40 <= x+1})


### THE REST IS TESTS ###
if __name__ == "__main__":
  change_dir(__file__)

  test(13140, solve(part=0, file='input-test-1'))
  test(14540, solve(part=0, file='input-real'))

  test("""\
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....\
""", solve(part=1, file='input-test-1'))

  test("""\
####.#..#.####.####.####.#..#..##..####
#....#..#....#.#.......#.#..#.#..#....#
###..####...#..###....#..####.#......#.
#....#..#..#...#.....#...#..#.#.....#..
#....#..#.#....#....#....#..#.#..#.#...
####.#..#.####.#....####.#..#..##..####\
""", solve(part=1, file='input-real'))
  test('EHZFZHCZ', ocr(solve(part=1, file='input-real')))
