from itertools import chain

alphabet = ''.join(chr(i) for i in xrange(ord('a'), ord('z') + 1))
ALPHABET = alphabet.upper()
alphabet_opposites = {a: A for a, A in chain(zip(alphabet, ALPHABET), zip(ALPHABET, alphabet))}

def react(str):
  stack = ['']
  for s in str:
    stack.pop() if stack[-1] == alphabet_opposites[s] else stack.append(s)
  return len(''.join(stack))

class Day05:
  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.polymer = self.lines[0]
    return self

  def part1(self):
    return react(self.polymer)

  def part2(self):
    return min(react(self.polymer.replace(a,'').replace(A,'')) for a, A in zip(alphabet, ALPHABET))

  def solve(self):
    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'part2': self.part2()}
    ]

if __name__== "__main__":
  print(Day05().load('input-test.txt').solve())
  print(Day05().load('input.txt').solve())
