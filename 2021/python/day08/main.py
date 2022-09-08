#!/usr/bin/env python3

from common.util import *


decoder = {
    'cf': 1,
    'acf': 7,
    'bcdf': 4,
    'acdeg': 2,
    'acdfg': 3,
    'abdfg': 5,
    'abcefg': 0,
    'abdefg': 6,
    'abcdfg': 9,
    'abcdefg': 8,
}


def get_wiring(digits):
  sets = defaultdict(list)
  for digit in digits:
    sets[len(digit)].append(set(digit))
  pprint(sets)

  found = {}
  def used(): return reduce(set.__or__, found.values())
  found['a'] = sets[3][0] - sets[2][0]
  found['f'] = sets[2][0] & reduce(set.__and__, sets[6])
  found['c'] = sets[2][0] - used()
  found['d'] = sets[4][0] & reduce(set.__and__, sets[5])
  found['b'] = sets[4][0] - used()
  found['g'] = reduce(set.__and__, sets[6]) - used()
  found['e'] = set('abcdefg') - used()
  return {next(iter(b)): a for a, b in found.items()}


def decode(output, wiring):
  return ''.join(str(decoder[''.join(sorted(wiring[c] for c in digit))]) for digit in output)


def solve(part, file):
  data = load(file)

  res = 0
  for line in data:
    digits, output = (s.split(' ') for s in line.split(' | '))

    wiring = get_wiring(digits)
    out = decode(output, wiring)
    res += sum(map(out.count, '1478')) if part == 1 else int(out)
  return res


if __name__ == "__main__":
  change_dir(__file__)

  test(0, solve(part=1, file='input-test-1'))
  # test(26, solve(part=1, file='input-test-2'))
  # test(488, solve(part=1, file='input-real'))

  # test(5353, solve(part=2, file='input-test-1'))
  # test(61229, solve(part=2, file='input-test-2'))
  # test(1040429, solve(part=2, file='input-real'))
