
import re
from collections import deque

class Life:
  def __init__(self, initial_state, mappings):
    self.base_index = 0
    self.state = initial_state
    self.mappings = {}
    for mapping in mappings:
      self.mappings[mapping[0:5]] = mapping[9]
    #print(self.state)

  def advance(self):
    new_state = deque()
    self.state = '....' + self.state + '....'
    self.base_index -= 2
    for i in xrange(2, len(self.state)-2):
      part = self.state[i-2:i+3]
      new_state.append(self.mappings[part] if part in self.mappings else '.')
    while new_state and new_state[0] == '.':
      new_state.popleft()
      self.base_index += 1
    while new_state and new_state[-1] == '.':
      new_state.pop()
    self.state = re.sub(r'^[.]+|[.]+$', '', ''.join(new_state))
  
  def play(self, steps):
    for _ in xrange(steps):
      self.advance()
      #print(self.state)
    sum = 0
    for i in xrange(len(self.state)):
      if self.state[i] == '#': sum += i + self.base_index
    return sum

  def guess(self, total_steps):
    #((50000000000-10000)/1000)*75000 + 751113
    at_9000 = self.play(9000)
    at_10000 = self.play(1000)

    return ((total_steps - 10000)/1000) * (at_10000 - at_9000) + at_10000


initial_state = '#..#.#..##......###...###'
mappings = [
  '...## => #',
  '..#.. => #',
  '.#... => #',
  '.#.#. => #',
  '.#.## => #',
  '.##.. => #',
  '.#### => #',
  '#.#.# => #',
  '#.### => #',
  '##.#. => #',
  '##.## => #',
  '###.. => #',
  '###.# => #',
  '####. => #',
]
print(Life(initial_state, mappings).play(20))

initial_state = '#......##...#.#.###.#.##..##.#.....##....#.#.##.##.#..#.##........####.###.###.##..#....#...###.##'
mappings = [
  '.#.## => .',
  '.#### => .',
  '#..#. => .',
  '##.## => #',
  '..##. => #',
  '##... => #',
  '..#.. => #',
  '#.##. => .',
  '##.#. => .',
  '.###. => #',
  '.#.#. => #',
  '#..## => #',
  '.##.# => #',
  '#.### => #',
  '.##.. => #',
  '###.# => .',
  '#.#.# => #',
  '#.... => .',
  '#...# => .',
  '.#... => #',
  '##..# => .',
  '....# => .',
  '..... => .',
  '.#..# => #',
  '##### => .',
  '#.#.. => .',
  '..#.# => #',
  '...## => .',
  '...#. => #',
  '..### => .',
  '####. => #',
  '###.. => #',
]
print(Life(initial_state, mappings).play(20))

print(Life(initial_state, mappings).guess(50000000000))

