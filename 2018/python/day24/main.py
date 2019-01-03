import re
from collections import defaultdict
from itertools import count

import sys
sys.path.append('../')
from day13.main import last


class Group:
  def __init__(self, side, index, count, hp, immune, weak, attack_power, attack_type, initiative, verbose):
    self.side = side
    self.index = index
    self.original_count = self.count = count
    self.hp = hp
    self.immune = set(immune)
    self.weak = set(weak)
    self.original_attack_power = self.attack_power = attack_power
    self.attack_type = attack_type
    self.initiative = initiative
    self.verbose = verbose

  def reset(self, boost):
    self.count = self.original_count
    self.attack_power = self.original_attack_power + boost

  def name(self):
    return 'Group ' + str(self.index) + ' (' + str(self.count) + ', ' + str(self.hp) + ')'

  def effective_power(self):
    return self.attack_power * self.count

  def damage_against(self, enemy):
    return 0 if self.attack_type in enemy.immune else self.count * self.attack_power * (2 if self.attack_type in enemy.weak else 1)

  def target(self, enemy=None):
    self._target = enemy
    if self.verbose:
      if enemy:
        print(self.side + ' ' + self.name() + ' targets ' + enemy.name() + ' for ' + str(self.damage_against(enemy)) + ' damage')
      else:
        print(self.side + ' ' + self.name() + ' targets noone')

  def describe(self):
    if self.immune and self.weak:
      immune_and_weak = ' (immune to ' + ', '.join(self.immune) + '; weak to ' + ', '.join(self.weak) + ')'
    elif self.immune:
      immune_and_weak = ' (immune to ' + ', '.join(self.immune) + ')'
    elif self.weak:
      immune_and_weak = ' (weak to ' + ', '.join(self.weak) + ')'
    else:
      immune_and_weak = ''
    return '{} units each with {} hit points{} with an attack that does {} {} damage at initiative {}'.format(
      self.count, self.hp, immune_and_weak, self.attack_power, self.attack_type, self.initiative)

  def attack(self):
    if not self._target:
      if self.verbose:
        print(self.side + ' ' + self.name() + ' attacks nothing')
      return False

    new_count = max(0, self._target.count - self.damage_against(self._target) / self._target.hp)
    killed = self._target.count - new_count
    self._target.count = new_count

    if self.verbose:
      print(self.side + ' ' + self.name() + ' attacks ' + self._target.name() + ', killing ' + str(killed) + ' units')

    return killed > 0


def parse_groups(lines, verbose=False):
  groups, current_side, index = defaultdict(list), None, None
  for line in lines:
    match = re.match(r'^(.*):$', line)
    if match:
      current_side = match.group(1)
      index = 1
    else:
      match = re.match(r'^([0-9]+) units each with ([0-9]+) hit points( \(.*\))? with an attack that does ([0-9]+) (.*) damage at initiative ([0-9]+)$', line)
      if match:
        weak_immune = defaultdict(list)
        if match.group(3):
          for part in match.group(3)[2:-1].split('; '):
            if part[0] == 'w':
              weak_immune['weak'] += part[len('weak to '):].split(', ')
            elif part[0] == 'i':
              weak_immune['immune'] = part[len('immune to '):].split(', ')
            else: raise Exception('wtf')
        groups[current_side].append(
          Group(
            side=current_side,
            index=index,
            count=int(match.group(1)),
            hp=int(match.group(2)),
            immune=weak_immune['immune'],
            weak=weak_immune['weak'],
            attack_power=int(match.group(4)),
            attack_type=match.group(5),
            initiative=int(match.group(6)),
            verbose=verbose
          )
        )
        index += 1
  return groups


def battle(groups, verbose=False, boost_side=None, boost=None):
  sides = groups.keys()

  for side in sides:
    for group in groups[side]:
      group.reset(boost=(boost if side == boost_side else 0))

  for rounds in count(1):

    if verbose: print('\nRound {}\n'.format(rounds))

    for i, side in enumerate(sides):
      if verbose: print(side + ':')

      if any(group.count > 0 for group in groups[side]): # is this side alive?
        if verbose: print('{} contains {} units'.format(group.name(), group.count))
      else:
        if verbose: print('No groups remain.')
        winner = sides[(i + 1) % 2]
        return (winner, sum(g.count for g in groups[winner]), rounds)

    if verbose: print('')
    
    attackers = []
    for i, side in enumerate(sides):
      unchosen = set([g for g in groups[sides[(i + 1) % 2]] if g.count > 0])

      for attacker in sorted([g for g in groups[side] if g.count > 0], key=lambda g: (-g.effective_power(), -g.initiative)):
        if not unchosen: break
        target = min(unchosen, key=lambda g: (-attacker.damage_against(g), -g.effective_power(), -g.initiative))
        if attacker.damage_against(target) > 0:
          attacker.target(target)
          unchosen.remove(target)
          attackers.append(attacker)
        else:
          attacker.target()
    
    if sum(attacker.attack() for attacker in sorted(attackers, key=lambda g: -g.initiative)) == 0:
      return (None, 0, rounds)

    if verbose: print('')


def battle_until_win(groups, initial_boost, verbose=False):
  winner, winner_count, rounds = battle(groups, verbose)
  yield winner_count

  if verbose: print('')
  print('{} won with {} units after {} rounds'.format(winner, winner_count, rounds))
  if verbose: print('')

  sides = groups.keys()
  loser = sides[(sides.index(winner) + 1) % 2]

  for boost in count(initial_boost):
    winner, winner_count, rounds = battle(groups, verbose, loser, boost)
    yield winner_count

    if verbose: print('')
    if winner:
      print('Boosting {} by +{}: {} won with {} units after {} rounds'.format(loser, boost, winner, winner_count, rounds))
    else:
      print('Boosting {} by +{}: Stalemate after {} rounds'.format(loser, boost, rounds))
    if verbose: print('')

    if winner and winner == loser: break


class Day24:
  def __init__(self, verbose=False):
    self.verbose = verbose

  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.groups = parse_groups(self.lines)
    return self

  def part1(self):
    return next(self.results_iter)

  def part2(self):
    return last(self.results_iter)

  def solve(self, initial_boost):
    self.results_iter = battle_until_win(self.groups, initial_boost, self.verbose)

    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'part2': self.part2()}
    ]


if __name__== "__main__":
  print(Day24(verbose=True).load('input-test.txt').solve(initial_boost=1570))
  print(Day24().load('input.txt').solve(initial_boost=1))
