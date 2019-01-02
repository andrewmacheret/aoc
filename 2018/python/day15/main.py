from collections import OrderedDict
from itertools import count


def bfs(queue, goal, next_items):
  seen = set(queue)

  while queue:
    next_queue = []

    for item in queue:
      if goal(item):
        yield item
        next_queue = None
      elif next_queue is not None:
        for next_item in next_items(item):
          if next_item not in seen:
            next_queue.append(next_item)
            seen.add(next_item)
    queue = next_queue


DIRS_IN_READ_ORDER = [(0, -1), (-1, 0), (1, 0), (0, 1)]

def neighbors(start_x, start_y, dirs=DIRS_IN_READ_ORDER):
  for dx, dy in DIRS_IN_READ_ORDER: yield start_x + dx, start_y + dy


class Unit:
  def __init__(self, type, hp=200, ap=3):
    self.type = type
    self.enemy = {'G': 'E', 'E': 'G'}[type]
    self.hp = hp
    self.ap = ap
  def type_with_health(self):
    return '{}({})'.format(self.type, self.hp)


def draw_combat(grid, rounds, units, winner_type=None, winner_hp=None):
  print('\nROUND {}{}\n'.format(rounds, ' - Done' if winner_type else ''))
  
  w, h = max(x for (x, y) in grid) + 1, max(y for (x, y) in grid) + 1
  for y in xrange(h):
    units_in_row = ['{}({})'.format(units[x, y].type, units[x, y].hp) for x in xrange(w) if grid.get((x, y)) in 'EG']
    print(''.join(grid[x, y] for x in xrange(w)) + '   ' + ', '.join(units_in_row))
  
  if winner_type:
    print('Combat ends after {0} full rounds'.format(rounds))
    print('{0} win with {1} total hit points left'.format({'E': 'Elves', 'G': 'Goblins'}[winner_type], winner_hp))
    print('Outcome: {0} * {1} = {2}'.format(rounds, winner_hp, rounds * winner_hp))


def bfs_next_move(grid, move_goals, start):
  closest = list(bfs(
    queue = [(y, x, y, x) for x, y in neighbors(*start) if grid.get((x, y)) == '.'],
    goal = lambda (y, x, hy, hx): (x, y) in move_goals,
    next_items = lambda (y, x, hy, hx): ((y2, x2, hy, hx) for x2, y2 in neighbors(x, y) if grid.get((x2, y2)) == '.')
  ))
  return tuple(reversed(min(closest)[2:])) if closest else None


def combat(input, elf_ap=3, elf_can_die=True, verbose=False):
  grid = OrderedDict(((x, y), c) for y, row in enumerate(input) for x, c in enumerate(row))
  bounds = min_x, min_y, max_x, max_y = 0, 0, len(input) - 1, len(input[0]) - 1 # x, y, w, h

  units = {p: Unit(ch, 200, {'E': elf_ap, 'G': 3}[ch]) for p, ch in grid.iteritems() if ch in 'EG'}

  for rounds in count():
    if verbose: draw_combat(grid, rounds, units)

    # for each unit in turn order
    for pos, unit in sorted(units.iteritems(), key=lambda (p, u): (p[1], p[0])):
      if pos not in units: continue
      
      direct_targets = [p for p in neighbors(*pos) if grid.get(p) == unit.enemy]
      if not direct_targets:

        # find enemies
        enemies = [p for p, e in units.iteritems() if e.type == unit.enemy]
        if not enemies:
          winner_hp = sum(unit.hp for unit in units.itervalues())
          if verbose: draw_combat(grid, rounds, units, unit.type, winner_hp)
          return rounds * winner_hp
        
        # find open squares adjacent to enemies
        move_goals = {p2 for p in enemies for p2 in neighbors(*p) if grid.get(p2) == '.'}

        # if there's at least one open squares adjacent to enemies
        if move_goals:

          # bfs to move_goals
          next_move = bfs_next_move(grid, move_goals, pos)

          # if we found a next_move, move to it
          if next_move:
            # reborn in new location!
            grid[pos] = '.'
            del units[pos]
            
            pos = next_move
            units[pos], grid[pos] = unit, unit.type

            # redo direct_targets
            direct_targets = [p for p in neighbors(*pos) if grid.get(p) == unit.enemy]

      # if now next to an enemy, attack! ... choose adjacent enemy with lowest HP... hit it. if it dies, replace with open square.
      if direct_targets:
        target_pos = min(direct_targets, key=lambda p: (units[p].hp, p[1], p[0]))
        target = units[target_pos]
        target.hp -= unit.ap

        # killed!
        if target.hp <= 0:
          # if elf died, try again... more AP!
          if not elf_can_die and target.type == 'E':
            return combat(input, elf_ap + 1, elf_can_die, verbose)

          del units[target_pos]
          grid[target_pos] = '.'


class Day15:
  def __init__(self, verbose=False):
    self.verbose = verbose

  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    return self

  def part1(self):
    return combat(self.lines, elf_ap=3, elf_can_die=True, verbose=self.verbose)

  def part2(self):
    return combat(self.lines, elf_ap=4, elf_can_die=False)

  def solve(self):
    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'part2': self.part2()},
    ]

print(Day15(verbose=True).load('input-test.txt').solve())
print(Day15().load('input.txt').solve())
