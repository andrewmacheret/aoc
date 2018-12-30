from itertools import cycle

def partial_sum(nums, verbose=False):
  total = 0
  for i in nums:
    if verbose: print('Current frequency {:2}, change of {:+2d}; resulting frequency {:2}.'.format(total, i, total+i))
    total += i
    yield total

def duplicates(items):
  seen = set()
  for i in items:
    if i in seen: 
      yield i
    seen.add(i)

class Day01:
  def __init__(self, verbose=False):
    self.verbose = verbose

  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.changes = map(int, self.lines)
    return self

  def part1(self):
    return sum(self.changes)

  def part2(self):
    return next(duplicates(partial_sum(cycle(self.changes), verbose=self.verbose)))

  def solve(self):
    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'part2': self.part2()}
    ]

if __name__== "__main__":
  print(Day01(verbose=True).load('input-test.txt').solve())
  print(Day01().load('input.txt').solve())
