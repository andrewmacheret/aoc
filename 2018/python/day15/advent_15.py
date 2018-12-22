
from collections import deque

class Unit:
  index = 1
  def __init__(self, type, enemy, location, hp=200, ap=3):
    self.type = type
    self.enemy = enemy
    self.hp = hp
    self.ap = ap
    self.location = location
    self.name = type + str(Unit.index)
    Unit.index += 1
  def type_with_health(self):
    return self.type + '(' + str(self.hp) + ')'

DIRS = [
  (0, -1),
  (-1, 0),
  (1, 0),
  (0, 1)
]



def solve(input, elf_ap=3, elf_can_die=True):
  grid = [[c for c in row] for row in input]
  #print('trying ap ' + str(elf_ap))
  h = len(grid)
  w = len(grid[0])

  units_by_location = {}

  for y in xrange(h):
    for x in xrange(w):
      ch = grid[y][x]
      if ch == 'E' or ch == 'G':
        enemy = 'E' if ch == 'G' else 'G'
        ap = elf_ap if ch == 'E' else 3
        unit = Unit(ch, enemy, (x,y), 200, ap)
        units_by_location[unit.location] = unit

  def print_round(is_end=False):
    print('\nROUND ' + str(rounds) + (' - Done' if is_end else '') + '\n')
    for y in xrange(h):
      units_in_row = []
      for x in xrange(w):
        if grid[y][x] == 'E' or grid[y][x] == 'G':
          units_in_row.append(units_by_location[(x,y)].type_with_health())
      print(''.join(grid[y]) + '   ' + ', '.join(units_in_row))

  rounds = 0

  # if one unit type is totally gone, end combat
  while True:
    #len(set(unit.type for unit in units_by_location.itervalues())) == 2:

    #print_round()

    # if rounds == 1:
    #  break
    died_this_round = set()

    # identify turn order
    turn_order = sorted((unit for unit in units_by_location.itervalues()), key=lambda u: (u.location[1], u.location[0]))
    #print('turn_order', [(unit.location, unit.name) for unit in turn_order])

    # for each unit in turn order, if not already next to an enemy, bfs to find nearest reachable target (READING ORDER FIRST) ... move if found, otherwise dont move
    for unit in turn_order:
      #print('checking unit', unit.name, unit.location)
      if unit not in died_this_round:
        
        direct_targets = []

        # if unit is next to an enemy, dont move
        orig_x, orig_y = unit.location
        for dx, dy in DIRS:
          if 0 <= orig_x+dx < w and 0 <= orig_y+dy < h and grid[orig_y+dy][orig_x+dx] == unit.enemy:
            direct_targets.append(units_by_location[(orig_x+dx, orig_y+dy)])
        #print('direct_targets', [(unit.location, unit.name) for unit in direct_targets])

        if not direct_targets:

          # get locations of all targets (adjacent open squares to enemies)
          move_goals = set()
          enemies = [e for e in units_by_location.itervalues() if unit.enemy == e.type]
          if not enemies:
            #print('NO ENEMIES LEFT', rounds)
            #print_round(True)
            winner_name = 'Elves' if unit.type == 'E' else 'Goblins'
            winner_hp = sum(unit.hp for unit in units_by_location.itervalues())
            solution = rounds * winner_hp
            #print('Combat ends after {0} full rounds'.format(rounds))
            #print('{0} win with {1} total hit points left'.format(winner_name, winner_hp))
            #print('Outcome: {0} * {1} = {2}'.format(rounds, winner_hp, solution))
            return solution
          for enemy in enemies:
            x, y = enemy.location
            for dx, dy in DIRS:
              if 0 <= x+dx < w and 0 <= y+dy < h and grid[y+dy][x+dx] == '.':
                move_goals.add((x+dx, y+dy))
          #print('move_goals', [(x1,y1) for x1,y1 in move_goals])

          if move_goals:
            # bfs to move_goals
            move_square = None
            v = set()
            q = deque()
            q.append((0, orig_y, orig_x, []))
            v.add((orig_x, orig_y))
            while q:
              next_q = []
              move_square_candidates = []
              while q:
                distance, y, x, history = q.popleft()
                #print('name', unit.name, 'distance', distance, 'y', y, 'x', x, 'history', history)
                history.append((x,y))
                if (x, y) in move_goals:
                  #move_square = history[1]
                  #break
                  move_square_candidates.append((y, x, history[1]))
                else:
                  for dx, dy in DIRS:
                    if (x+dx, y+dy) not in v and 0 <= x+dx < w and 0 <= y+dy < h and grid[y+dy][x+dx] == '.':
                      next_q.append((distance + 1, y+dy, x+dx, history[:])) # inefficient
                      v.add((x+dx, y+dy))
              if move_square_candidates:
                #print('candidates', move_square_candidates)
                my, mx, move_square = sorted(move_square_candidates)[0]
                break
              for item in next_q:
                q.append(item)

            #print('move_square', move_square)

            # if we found a move_square, move to it
            if move_square:
              # reborn in new location!
              grid[orig_y][orig_x] = '.'
              del units_by_location[unit.location]
              new_x, new_y = unit.location = move_square
              grid[new_y][new_x] = unit.type
              units_by_location[unit.location] = unit

              # redo direct_targets
              for dx, dy in DIRS:
                if 0 <= new_x+dx < w and 0 <= new_y+dy < h and grid[new_y+dy][new_x+dx] == unit.enemy:
                  direct_targets.append(units_by_location[(new_x+dx, new_y+dy)])
              #print('direct_targets', [(unit.location, unit.name) for unit in direct_targets])

        # if now next to an enemy, attack! ... choose adjascent enemy with lowest HP... hit it. if it dies, replace with open square.
        if direct_targets:
          target = sorted(direct_targets, key=lambda u: (u.hp, u.location[1], u.location[0]))[0]
          target.hp -= unit.ap
          #print(unit.name, 'took a swing at', target.name, target.hp)
          if target.hp <= 0:
            # if elf died, try again... more AP!
            if not elf_can_die and target.type == 'E':
              return solve(input, elf_ap + 1, elf_can_die)

            #print(unit.name, 'killed', target.name)
            died_this_round.add(target)
            del units_by_location[target.location]
            target_x, target_y = target.location
            grid[target_y][target_x] = '.'

    rounds += 1





# input = [
#   '#######',
#   '#E..G.#',
#   '#...#.#',
#   '#.G.#G#',
#   '#######',
# ]
# print(solve(input))
# input = [
#   '#########',
#   '#G..G..G#',
#   '#.......#',
#   '#.......#',
#   '#G..E..G#',
#   '#.......#',
#   '#.......#',
#   '#G..G..G#',
#   '#########',
# ]
# print(solve(parse(input)))
# input = [
#   '#######',
#   '#.G...#',
#   '#...EG#',
#   '#.#.#G#',
#   '#..G#E#',
#   '#.....#',
#   '#######',
# ]
# print(27730, solve(parse(input)))

# input = [
#   '#######',
#   '#G..#E#',
#   '#E#E.E#',
#   '#G.##.#',
#   '#...#E#',
#   '#...E.#',
#   '#######',
# ]
# print(36334, solve(parse(input)))
# print("""Expected:
# Combat ends after 37 full rounds
# Elves win with 982 total hit points left
# Outcome: 37 * 982 = 36334
# """)



# input = [
#   '#######',
#   '#E..EG#',
#   '#.#G.E#',
#   '#E.##E#',
#   '#G..#.#',
#   '#..E#.#',
#   '#######',
# ]
# print(39514, solve(parse(input)))
# print("""Expected:
# Combat ends after 46 full rounds
# Elves win with 859 total hit points left
# Outcome: 46 * 859 = 39514
# """)

# input = [
#   '#######',
#   '#E.G#.#',
#   '#.#G..#',
#   '#G.#.G#',
#   '#G..#.#',
#   '#...E.#',
#   '#######',
# ]
# print(27755, solve(parse(input)))
# print("""Expected:
# Combat ends after 35 full rounds
# Goblins win with 793 total hit points left
# Outcome: 35 * 793 = 27755
# """)

# input = [
#   '#######',
#   '#.E...#',
#   '#.#..G#',
#   '#.###.#',
#   '#E#G#G#',
#   '#...#G#',
#   '#######',
# ]
# print(28944, solve(parse(input)))
# print("""Expected:
# Combat ends after 54 full rounds
# Goblins win with 536 total hit points left
# Outcome: 54 * 536 = 28944
# """)


# input = [
#   '#########',
#   '#G......#',
#   '#.E.#...#',
#   '#..##..G#',
#   '#...##..#',
#   '#...#...#',
#   '#.G...G.#',
#   '#.....G.#',
#   '#########',
# ]
# print(18740, solve(parse(input)))
# print("""Expected:
# Combat ends after 20 full rounds
# Goblins win with 937 total hit points left
# Outcome: 20 * 937 = 18740
# """)


input = [
  '################################',
  '##########..####################',
  '##########..G###################',
  '##########..#.....########.#####',
  '##########........########G#####',
  '############...#..########.#####',
  '################....######.#####',
  '#################..G####...#####',
  '################...#..#....#####',
  '################...G..#.....E###',
  '##############.G..........G....#',
  '###########.G...G..............#',
  '###########G..#####..........###',
  '###########..#######.........###',
  '##########.G#########........#.#',
  '#########...#########....G.....#',
  '#########...#########.........##',
  '##..........#########.........##',
  '######....G.#########.....E....#',
  '##...........#######.......#...#',
  '#...G.........#####E.......#####',
  '##....................#..#######',
  '##.G.................##.########',
  '##..#GG.............###...#..###',
  '#G..#..G.G........G.####.#..E###',
  '#.....#.##...........###.....###',
  '#######...............###EE..###',
  '########.....E........###....###',
  '########..............####..####',
  '##########....E....#...###.#####',
  '###########...EE....#.##########',
  '################################',
]

# part 1
print(178003, solve(input))

# part 2
print(48722, solve(input, 4, False))


