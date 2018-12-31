def next_nth(gen, n):
  for _ in xrange(n-1): next(gen)
  return next(gen) if n > 0 else None

def guess_linear(gen, key, steps, stable_from, stable_to):
  at_stable_from = key(next_nth(gen, stable_from))
  at_stable_to = key(next_nth(gen, stable_to - stable_from))
  return ((steps - stable_to) / (stable_to - stable_from)) * (at_stable_to - at_stable_from) + at_stable_to

def life_of_plants(mappings, (offset, state), verbose=False):
  while True:
    state = '....' + state + '....'
    state = ''.join(mappings.get(state[i-2:i+3], '.') for i in xrange(2, len(state)-2))
    offset, state = offset + state.index('#') - 2, state.strip('.')
    if verbose: print('offset={:3}  {}'.format(offset, state))
    yield offset, state

def plants_value((offset, state)):
  return sum(i + offset for i,s in enumerate(state) if s == '#')

class Day12:
  def __init__(self, verbose=False):
    self.verbose = verbose

  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.initial_state = (0, self.lines[0].split(': ')[1])
    self.mappings = dict(line.split(' => ') for line in self.lines[2:])
    return self

  def part1(self):
    gen = life_of_plants(self.mappings, self.initial_state, self.verbose)
    return plants_value(next_nth(gen, 20))

  def part2(self):
    gen = life_of_plants(self.mappings, self.initial_state)
    return guess_linear(gen, key=plants_value, steps=50000000000, stable_from=9000, stable_to=10000)

  def solve(self):
    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'part2': self.part2()},
    ]

print(Day12(verbose=True).load('input-test.txt').solve())
print(Day12().load('input.txt').solve())
