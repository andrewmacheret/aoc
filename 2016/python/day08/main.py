#!/usr/bin/env python3

import re

from common.util import *


def solve(part, screen, file):
  # data = load_ints(file)
  # data = load_custom(file)
  # data = load_blocks(file)
  # data = load_csv(file)
  data = load(file)
  grid = [[0] * screen[0] for _ in range(screen[1])]
  for line in data:
    a, b = [*map(int, re.findall(r'\d+', line))]
    if line[1] == 'e':  # rect
      for y in range(b):
        for x in range(a):
          grid[y][x] = 1
    elif line[7] == 'c':  # rot column
      grid = [*map(list, zip(*grid))]
      grid[a][:] = grid[a][-b:] + grid[a][:-b]
      grid = [*map(list, zip(*grid))]
    else:  # rot row
      grid[a][:] = grid[a][-b:] + grid[a][:-b]
  if part == 1:
    return sum(x for row in grid for x in row)
  else:
    return '\n'.join(''.join('#' if x else ' ' for x in row) for row in grid)


if __name__ == "__main__":
  change_dir(__file__)

  test(6, solve(part=1, screen=(7, 3), file='input-test-1'))
  test(110, solve(part=1, screen=(50, 6), file='input-real'))

  expected = """
####   ## #  # ###  #  #  ##  ###  #    #   #  ## 
   #    # #  # #  # # #  #  # #  # #    #   #   # 
  #     # #### #  # ##   #    #  # #     # #    # 
 #      # #  # ###  # #  #    ###  #      #     # 
#    #  # #  # # #  # #  #  # #    #      #  #  # 
####  ##  #  # #  # #  #  ##  #    ####   #   ##  
"""

  test(expected, '\n' + solve(part=2, screen=(50, 6), file='input-real') + '\n')
