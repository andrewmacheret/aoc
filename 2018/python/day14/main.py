from collections import deque

def iter_recent(iter, memory):
  q = deque()
  for item in iter:
    q.append(item)
    if len(q) > memory: q.popleft()
    yield q

def next_nth(iter, n):
  for _ in xrange(n-1): next(iter)
  return next(iter)

def next_when(iter, cond):
  for item in iter:
    if cond(item): return item

def draw_scores(scores, elf_1, elf_2):
  number_format = {(True,True): '{{{}}}', (True,False): '({})', (False,True): '[{}]', (False,False): ' {} '}
  print(''.join(number_format[(i == elf_1, i == elf_2)].format(score) for i, score in enumerate(scores)))

def generate_scores(verbose=False):
  elves, scores = [0, 1], [3, 7]
  for score in scores: yield score

  while True:
    if verbose: draw_scores(scores, *elves)

    new_recipe = sum(scores[e] for e in elves)
    if new_recipe >= 10:
      new_recipe -= 10
      scores.append(1)
      yield 1

    scores.append(new_recipe)
    yield new_recipe

    elves = [(1 + e + scores[e]) % len(scores) for e in elves]

def recipes_after(steps, verbose=False, n=10):
  return ''.join(map(str, next_nth(iter_recent(generate_scores(verbose), n), steps + n)))

def recipes_until(until):
  until_q, n = deque(map(int, until)), len(until)
  return next_when(enumerate(iter_recent(generate_scores(), n), 1), cond=lambda (i, last_n): until_q == last_n)[0] - n

class Day14:
  def __init__(self, verbose=False):
    self.verbose = verbose

  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.input = self.lines[0]
    return self

  def part1(self):
    self.part1_result = recipes_after(int(self.input), self.verbose)
    return self.part1_result

  def part2(self, inverse):
    return recipes_until(self.part1_result[:5] if inverse else self.input)

  def solve(self, inverse=False):
    return [
      {'filename': self.filename},
      {'input': self.input},
      {'part1': self.part1()},
      {'part2': self.part2(inverse)},
    ]

if __name__== "__main__":
  print(Day14(verbose=True).load('input-test.txt').solve(inverse=True))
  print(Day14().load('input-test2.txt').solve(inverse=True))
  print(Day14().load('input-test3.txt').solve(inverse=True))
  print(Day14().load('input-test4.txt').solve(inverse=True))
  print(Day14().load('input.txt').solve())
