#!/usr/bin/env python3
from day01.main import test
from day02.main import load_memory
from day05.main import Program
from day17.main import parse_input

SECURITY = 'Security Checkpoint'
FORBIDDEN_ITEMS = {'molten lava', 'photons', 'infinite loop', 'escape pod', 'giant electromagnet'}
DIRS = {'east': (1, 0), 'north': (0, -1), 'west': (-1, 0), 'south': (0, 1)}
DIRS_BY_COORD = {(dx, dy): d for d, (dx, dy) in DIRS.items()}
OPPOSITE_DIRS = {d: DIRS_BY_COORD[-dx, -dy] for d, (dx, dy) in DIRS.items()}

def until_str(it, suffix):
  s=''
  for i in it:
    s += i
    if s.endswith(suffix): break
  return s

class Game:
  def __init__(self, memory):
    self.prog = Program(memory, [])
    self.run = self.prog.run_computer()
  
  def get_output(self):
    return ''.join(until_str(map(chr, self.run), 'Command?'))

  def give_input(self, s):
    self.prog.input.extend(map(ord, s + '\n'))
    return self.get_output()

  def manipulate(self, action, item):
    return self.give_input(action + ' ' + item)

  def go(self, direction):
    return self.give_input(direction)

  def parse_output(self, output):
    title, doors, items, messages, mode = '', set(), [], [], ''
    for line in filter(None, output.split('\n')):
      if line.startswith('== ') and line.endswith(' =='):
        title, doors, items, mode = line[3:-3], set(), [], ''
      elif line == 'Doors here lead:': mode = 'doors'
      elif line == 'Items here:': mode = 'items'
      elif line.startswith('- '):
        if mode == 'doors': doors.add(line[2:])
        elif mode == 'items': items.append(line[2:])
      elif line != 'Command?':
        if mode != '':
          messages.append(line)
    return title, doors, items, messages

  def solve(self):
    rooms, usable_items = {}, []

    def dfs(path, output):
      title, doors, items, _ = self.parse_output(output)
      for item in items:
        if item not in FORBIDDEN_ITEMS:
          self.manipulate('take', item)
          usable_items.append(item)
      if title not in rooms:
        rooms[title] = {'ch': '.', 'doors': {}, 'path': path}
        for d in doors:
          title_dest = dfs(path + [d], self.go(d))
          rooms[title]['doors'][d] = title_dest
          if title_dest != title: self.go(OPPOSITE_DIRS[d])
      return title
    dfs([], self.get_output())
    
    for d in rooms[SECURITY]['path']: self.go(d)
    end_direction = next(d for d, name in rooms[SECURITY]['doors'].items() if name == SECURITY)

    carrying = set(usable_items)
    for b in range(2 ** len(usable_items)):
      for i, item in enumerate(usable_items):
        if (1 << i) & b:
          if item not in carrying:
            self.manipulate('take', item)
            carrying.add(item)
        else:
          if item in carrying:
            self.manipulate('drop', item)
            carrying.remove(item)
      title, _, _, messages = self.parse_output(self.go(end_direction))
      if title != SECURITY: return int(messages[2].split(' ')[11])

def solve(filename):
  memory = load_memory(filename, script=__file__)
  game = Game(memory)
  return game.solve()

if __name__== "__main__":
  test(537002052, solve('input.txt'))
