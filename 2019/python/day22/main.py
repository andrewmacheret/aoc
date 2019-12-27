#!/usr/bin/env python3
import re

from day01.main import load, test

CARD_REGEXES = {
  r'cut (.*)': [int],
  r'deal into new stack': [],
  r'deal with increment (.*)': [int]
}

CARD_COMMANDS = [
  lambda a, b, index: (a, b - index),
  lambda a, b: (-a, -b - 1),
  lambda a, b, increment: (a * increment, b * increment)
]

def match_regexes(line, regexes):
  for i, (regex, fns) in enumerate(regexes.items()):
    m = re.match(regex, line)
    if m: return i, tuple(fn(s) for fn, s in zip(fns, m.groups()))
  raise Exception('Line did not match regexes: ' + line)

def load_commands(filename, regexes=CARD_REGEXES, script=__file__):
  return [match_regexes(line, regexes) for line in load(filename, script=script)]

def solve(filename, shuffles, deck_size, where_is_card=None, at_index=None):
  commands = load_commands(filename)

  # card = a*x + b 
  a, b = 1, 0
  for index, values in commands:
    a, b = CARD_COMMANDS[index](a, b, *values)
  a, b = a % deck_size, b % deck_size

  # MAAAAGIIIIIC
  Ma = pow(a, shuffles, deck_size)
  Mb = (b * (Ma - 1) * pow(a - 1, deck_size - 2, deck_size)) % deck_size
  
  if where_is_card is not None:
    return (Ma * where_is_card + Mb) % deck_size
  else:
    # more magic
    return ((at_index - Mb) * pow(Ma, deck_size - 2, deck_size)) % deck_size

if __name__== "__main__":
  test(1879, solve('input.txt', 1, 10007, where_is_card=2019))
  test(73729306030290, solve('input.txt', 101741582076661, 119315717514047, at_index=2020))
