import re

class Group:
  def __init__(self, side, index, count, hp, immune, weak, attack_power, attack_type, initiative, debug):
    self.side = side
    self.index = index
    self.original_count = self.count = count
    self.hp = hp
    self.immune = set(immune)
    self.weak = set(weak)
    self.original_attack_power = self.attack_power = attack_power
    self.attack_type = attack_type
    self.initiative = initiative
    self.debug = debug

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
    if self.debug:
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
    return '{0} units each with {1} hit points{2} with an attack that does {3} {4} damage at initiative {5}'.format(self.count, self.hp, immune_and_weak, self.attack_power, self.attack_type, self.initiative)


  def attack(self):
    if not self._target:
      if self.debug:
        print(self.side + ' ' + self.name() + ' attacks nothing')
      return False

    new_count = max(0, self._target.count - self.damage_against(self._target) / self._target.hp)
    killed = self._target.count - new_count
    self._target.count = new_count

    if self.debug:
      print(self.side + ' ' + self.name() + ' attacks ' + self._target.name() + ', killing ' + str(killed) + ' units')

    return killed > 0



class Solution:
  def __init__(self, debug=False):
    self.debug = debug

  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()

    self.sides = []
    self.groups = {}
    current_side = None
    index = None
    for line in self.lines:
      match = re.match(r'^(.*):$', line)
      if match:
        current_side = match.group(1)
        self.sides.append(current_side)
        self.groups[current_side] = []
        index = 1
      else:
        match = re.match(r'^([0-9]+) units each with ([0-9]+) hit points( \(.*\))? with an attack that does ([0-9]+) (.*) damage at initiative ([0-9]+)$', line)
        if match:
          attr = match.group(3)
          weak = []
          immune = []
          if attr:
            for part in attr[2:-1].split('; '):
              if part[0] == 'w':
                weak = part[len('weak to '):].split(', ')
              elif part[0] == 'i':
                immune = part[len('immune to '):].split(', ')
              else:
                raise Exception('wtf')
          self.groups[current_side].append(
            Group(
              side=current_side,
              index=index,
              count=int(match.group(1)),
              hp=int(match.group(2)),
              immune=immune,
              weak=weak,
              attack_power=int(match.group(4)),
              attack_type=match.group(5),
              initiative=int(match.group(6)),
              debug=self.debug
            )
          )
          index += 1


    return self

  def battle(self, boost_side=None, boost=None):

    for side in self.sides:
      for group in self.groups[side]:
        group.reset(boost=(boost if side==boost_side else 0))

    round = 1
    while True:

      if self.debug: print('\nRound ' + str(round) + '\n')

      winner = None
      for i, side in enumerate(self.sides):
        other_side = self.sides[(i + 1) % 2]

        side_is_alive = False
        if self.debug: print(side + ':')
        for group in self.groups[side]:
          if group.count > 0:
            side_is_alive = True
            if self.debug: print(group.name() + ' contains ' + str(group.count) + ' units')

        if not side_is_alive:
          if self.debug: print('No groups remain.')
          winner = other_side

      if winner:
        return (winner, sum(g.count for g in self.groups[winner]), round)

      if self.debug: print('')
      attackers = []
      for i, side in enumerate(self.sides):
        other_side = self.sides[(i + 1) % 2]
        
        choosing_order = sorted([g for g in self.groups[side] if g.count > 0], key=lambda g: (-g.effective_power(), -g.initiative))

        unchosen = set([g for g in self.groups[other_side] if g.count > 0])

        for chooser in choosing_order:
          if unchosen:
            chosen_groups = sorted(unchosen, key=lambda g: (-chooser.damage_against(g), -g.effective_power(), -g.initiative))
            if chooser.damage_against(chosen_groups[0]) > 0:
              chosen_group = chosen_groups[0]
              chooser.target(chosen_group)
              unchosen.remove(chosen_group)
              attackers.append(chooser)
            else:
              chooser.target()
      
      someone_got_killed = False
      for attacker in sorted(attackers, key=lambda g: -g.initiative):
        if attacker.attack():
          someone_got_killed = True

      if not someone_got_killed:
        return (None, 0, round)

      if self.debug: print('')
      round += 1



  def solve(self, initial_boost):

    winner, winner_count, rounds = self.battle()
    if self.debug: print('')
    print('{0} won with {1} units after {2} rounds'.format(winner, winner_count, rounds))
    if self.debug: print('')

    loser = self.sides[(self.sides.index(winner) + 1)%2]

    boost = initial_boost
    new_winner_count = None
    while True:
      new_winner, new_winner_count, new_rounds = self.battle(loser, boost)
      if self.debug: print('')
      if new_winner:
        print('Boosting {0} by +{1}: {2} won with {3} units after {4} rounds'.format(loser, boost, new_winner, new_winner_count, new_rounds))
      else:
        print('Boosting {0} by +{1}: Stalemate after {2} rounds'.format(loser, boost, new_rounds))
      if self.debug: print('')
  
      if new_winner and new_winner != winner:
        break
      boost += 1

    return [
      {'filename': self.filename},
      {'part1': winner_count},
      {'part2': new_winner_count}
    ]


print(Solution(debug=True).load('input-test.txt').solve(initial_boost=1570))
print(Solution(debug=False).load('input.txt').solve(initial_boost=1))
