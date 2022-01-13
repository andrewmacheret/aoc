#!/usr/bin/env python3

from collections import namedtuple
from itertools import chain, permutations

from common.util import load, parse_nums, test, change_dir

Item = namedtuple('Item', ['cost', 'damage', 'armor'])
Character = namedtuple('Character', ['hp', 'damage', 'armor'])

shop_text = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""


def parse_shop():
  catalog = {}
  for line in filter(None, shop_text.splitlines()):
    if ':' in line:
      items = catalog[line.split(':')[0]] = []
    else:
      items.append(Item(*map(int, line.split()[-3:])))
  return catalog


def parse_character(stats):
  return Character(*(parse_nums(line)[0] for line in stats))


def fight(player, boss):
  damage = [max(1, player.damage - boss.armor),
            max(1, boss.damage - player.armor)]
  hp = [player.hp, boss.hp]
  while 1:
    hp[1] -= damage[0]
    if hp[1] <= 0:
      return 1
    hp[0] -= damage[1]
    if hp[0] <= 0:
      return 0


def combine(*items):
  cost = damage = armor = 0
  for item in items:
    if item:
      cost += item.cost
      damage += item.damage
      armor += item.armor
  return Item(cost, damage, armor)


def solve(part, file):
  boss = parse_character(load(file))
  shop = parse_shop()
  players = []
  for weapon in shop['Weapons']:
    for armor in chain(shop['Armor'], [None]):
      for num_rings in range(3):
        for rings in permutations(shop['Rings'], num_rings):
          stats = combine(weapon, armor, *rings)
          player = Character(100, stats.damage, stats.armor)
          players.append((stats.cost, player))

  players.sort()
  if part == 1:
    return next(cost for cost, player in players if fight(player, boss))
  else:
    return next(cost for cost, player in reversed(players) if not fight(player, boss))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(1, fight(Character(8, 5, 5), Character(12, 7, 2)))
  test(78, solve(part=1, file='input-real'))
  test(148, solve(part=2, file='input-real'))
