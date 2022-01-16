#!/usr/bin/env python3

from collections import defaultdict
from math import inf
from heapq import heappush, heappop
from dataclasses import dataclass, replace

from common.util import load, parse_nums, test, change_dir

spell_costs = {
    'missle': 53,
    'drain': 73,
    'shield': 113,
    'poison': 173,
    'recharge': 229
}


class EndOfFight(Exception):
  def __init__(self, message, win=False):
    super().__init__(message)
    self.win = win


@dataclass(unsafe_hash=True, order=True)
class Fight:
  player_hp: int
  boss_hp: int
  mana: int
  poison: int = 0
  shield: int = 0
  recharge: int = 0
  armor: int = 0

  def copy(self):
    return replace(self)

  def cast_spell(self, spell):
    if self.mana < (cost := spell_costs[spell]):
      raise EndOfFight('not enough mana for ' + spell)
    self.mana -= cost
    return getattr(self, 'cast_' + spell)()

  def cast_poison(self):
    if self.poison:
      raise EndOfFight('too soon for poison')
    self.poison = 6

  def cast_shield(self):
    if self.shield:
      raise EndOfFight('too soon for shield')
    self.shield = 6

  def cast_recharge(self):
    if self.recharge:
      raise EndOfFight('too soon for recharge')
    self.recharge = 5

  def cast_missle(self):
    self.boss_hp -= 4
    if self.boss_hp <= 0:
      raise EndOfFight('boss dead by missle', win=True)

  def cast_drain(self):
    self.boss_hp -= 2
    if self.boss_hp <= 0:
      raise EndOfFight('boss dead by drain', win=True)
    self.player_hp += 2

  def effects(self):
    self.effect_poison()
    self.effect_recharge()
    self.effect_shield()

  def effect_poison(self):
    if self.poison:
      self.boss_hp -= 3
      if self.boss_hp <= 0:
        raise EndOfFight('boss dead by poision', win=True)
      self.poison -= 1

  def effect_shield(self):
    if self.shield:
      self.shield -= 1
      self.armor = 7
    else:
      self.armor = 0

  def effect_recharge(self):
    if self.recharge:
      self.recharge -= 1
      self.mana += 101

  def attack(self, boss_damage):
    self.player_hp -= max(1, boss_damage - self.armor)
    if self.player_hp <= 0:
      raise EndOfFight('player dead')

  def player_turn(self, spell, sap_player):
    if sap_player:
      self.attack(1)
    self.effects()
    self.cast_spell(spell)

  def boss_turn(self, boss_damage):
    self.effects()
    self.attack(boss_damage)

  def round(self, boss_damage, spell, sap_player):
    try:
      self.player_turn(spell, sap_player)
      self.boss_turn(boss_damage)
    except EndOfFight as e:
      return e.win


def djyk(start, expand, is_goal):
  seen = defaultdict(lambda: inf, {start: 0})
  q = [(0, start)]
  while q:
    val, x = heappop(q)
    if is_goal(x):
      return val
    for cost, y in expand(x):
      val2 = cost + val
      if seen[y] > val2:
        seen[y] = val2
        heappush(q, (val2, y))


def solve(part, file):
  boss_hp, boss_damage = (parse_nums(line)[0] for line in load(file))

  start = Fight(mana=500, player_hp=50, boss_hp=boss_hp)

  def is_goal(fight):
    return fight.boss_hp <= 0

  def expand(fight):
    for spell, cost in spell_costs.items():
      result = fight.copy()
      if result.round(boss_damage, spell, part == 2) != False:
        yield cost, result

  return djyk(start, expand, is_goal)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(953, solve(part=1, file='input-real'))

  test(1289, solve(part=2, file='input-real'))
