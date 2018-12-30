from collections import Counter

def quantify(items, condition=bool):
  return sum(map(condition, items))

def count_has_exactly(items, amount):
  return quantify(items, lambda item: amount in Counter(item).values())

def diff(items1, items2):
  return [(i,j) for i,j in zip(items1, items2) if i!=j]

def common(items1, items2):
  return [i for i,j in zip(items1, items2) if i==j]

class Day02:
  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    return self

  def part1(self):
    return count_has_exactly(self.lines, 2) * count_has_exactly(self.lines, 3)

  def part2(self):
    return ''.join(common(*[l1 for l1 in self.lines for l2 in self.lines if len(diff(l1, l2)) == 1]))

  def solve(self):
    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'part2': self.part2()}
    ]

if __name__== "__main__":
  print(Day02().load('input-test.txt').solve())
  print(Day02().load('input.txt').solve())
