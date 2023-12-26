#!/usr/bin/env python3

from copy import copy

from common.util import *


def solve(part, file):
  raw_rules, raw_items = load_blocks(file)

  rules = {}
  for rule in raw_rules:
    name, steps = re.fullmatch(r'(\w+)\{(.*)\}', rule).groups()
    rules[name] = steps.split(',')
  
  def accept_ranges(name, item1, item2):
    if name == 'R' or any(item1[c] > item2[c] for c in 'xmas'):
      return
    if name == 'A':
      yield item1, item2
      return
    
    for step in rules[name]:
      if ':' not in step:
        yield from accept_ranges(step, item1, item2)
        return
      expr, dest = step.split(':')
      ch, val = re.split(r'[<>]', expr)
      val = int(val)
      if item1[ch] <= val <= item2[ch]:
        if '<' in expr:
          item2_new = copy(item2)
          item2_new[ch] = val - 1
          yield from accept_ranges(dest, item1, item2_new)
          item1 = copy(item1)
          item1[ch] = val
        else: # if '>' in expr:
          item1_new = copy(item1)
          item1_new[ch] = val + 1
          yield from accept_ranges(dest, item1_new, item2)
          item2 = copy(item2)
          item2[ch] = val

  lo, hi = ({c: x for c in 'xmas'} for x in (1,4000))
  ranges = [*accept_ranges('in', lo, hi)]
  
  t = 0
  if part == 0:
    for item in raw_items:
      item = {c:x for c, x in zip('xmas', parse_nums(item))}
      for item1, item2 in ranges:
        if all(item1[c] <= item[c] <= item2[c] for c in 'xmas'):
          t += sum(item.values())
          break
  else:
    t = 0
    for item1, item2 in ranges:
      t += reduce(mul, (item2[c] - item1[c] + 1 for c in 'xmas'))
  return t
  


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(19114, solve(part=0, file='input-test-1'))
  test(421983, solve(part=0, file='input-real'))

  test(167409079868000, solve(part=1, file='input-test-1'))
  test(129249871135292, solve(part=1, file='input-real'))
