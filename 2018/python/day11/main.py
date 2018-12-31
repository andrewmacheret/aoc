from itertools import product

def power_level(serial, x, y):
  return ((((x + 10) * y + serial) * (x + 10)) / 100) % 10 - 5

def power_grid(serial, width=300, height=300):
  return [[power_level(serial, x, y) for x in xrange(1, width+1)] for y in xrange(1, height+1)]

def draw_square(grid, x, y, width, height):
  print('\n'.join(''.join('{0:4d}'.format(power_level) for power_level in r[x:(x+width)]) for r in grid[y:(y+height)]))

def power_levels_of_size(grid, width, height):
  n = len(grid)

  for x,y in product(xrange(n-width), xrange(n-height)):
    yield x, y, sum(grid[y+dy][x+dx] for dx,dy in product(xrange(width), xrange(height)))

def square_power_levels(grid):
  n = len(grid)

  sum_grid = [[0 for x in xrange(n+1)] for y in xrange(n+1)]
  for x,y in product(xrange(1, n+1), xrange(1, n+1)):
    sum_grid[y][x] = grid[y-1][x-1] + sum_grid[y-1][x] + sum_grid[y][x-1] - sum_grid[y-1][x-1]

  for w in xrange(1, n+1):
    for x,y in product(xrange(n-w+1), xrange(n-w+1)):
      yield x, y, w, sum_grid[y+w][x+w] - sum_grid[y+w][x] - sum_grid[y][x+w] + sum_grid[y][x]

class Day11:
  def __init__(self, verbose=False):
    self.verbose = verbose

  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.serial = int(self.lines[0])
    return self

  def part1(self):
    x, y, total = max(power_levels_of_size(self.grid, 3, 3), key=lambda (x,y,total): total)
    if self.verbose: draw_square(self.grid, x, y, 3, 3)
    return (x+1,y+1)

  def part2(self):
    x, y, w, total = max(square_power_levels(self.grid), key=lambda (x,y,w,total): total)
    if self.verbose: draw_square(self.grid, x, y, w, w)
    return (x+1, y+1, w)

  def solve(self):
    self.grid = power_grid(self.serial)
    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'part2': self.part2()},
    ]

print(Day11(verbose=True).load('input-test.txt').solve())
print(Day11(verbose=True).load('input-test2.txt').solve())
print(Day11().load('input.txt').solve())
