from collections import deque

def build_license(numbers):
  k, n = numbers.popleft(), numbers.popleft()
  return (
    [build_license(numbers) for _ in xrange(k)],
    [numbers.popleft() for _ in xrange(n)]
  )

def license_metadata((children, metadata)):
  for m in metadata:
    yield m
  for child in children:
    for m in license_metadata(child):
      yield m

def license_values((children, metadata)):
  if children:
    for m in metadata:
      if 1 <= m <= len(children):
        for m2 in license_values(children[m-1]):
          yield m2
  else:
    for m in metadata:
      yield m

class Day08:
  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.numbers = map(int, self.lines[0].split(' '))
    return self

  def part1(self):
    return sum(license_metadata(self.license))

  def part2(self):
    return sum(license_values(self.license))

  def solve(self):
    self.license = build_license(deque(self.numbers))
    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'part2': self.part2()}
    ]

if __name__== "__main__":
  print(Day08().load('input-test.txt').solve())
  print(Day08().load('input.txt').solve())
