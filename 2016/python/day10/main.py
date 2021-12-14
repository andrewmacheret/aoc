#!/usr/bin/env python3

from collections import defaultdict
from itertools import groupby
from operator import itemgetter

from common.util import load, find_tokens, parse_nums, change_dir, test


def solve(file, compares=None):
  data = load(file)
  instructions = [list(g) for _, g in groupby(sorted(data), key=itemgetter(0))]

  splits = {}
  for line in instructions[0]:
    _, bot, _, _, _, is_out_lo, lo, _, _, _, is_out_hi, hi = find_tokens(line)
    bot, lo, hi = map(int, (bot, lo, hi))
    is_out_lo, is_out_hi = is_out_lo[0] == 'o', is_out_hi[0] == 'o'
    assert bot not in splits
    splits[bot] = ((is_out_lo, lo), (is_out_hi, hi))

  bots = defaultdict(list)
  for line in instructions[1]:
    value, bot = parse_nums(line)
    assert len(bots[bot]) < 2
    bots[bot].append(value)

  def run_bot():
    for b in bots:
      if len(bots[b]) == 2:
        (is_out_lo, lo_id), (is_out_hi, hi_id) = splits[b]
        if (is_out_lo or len(bots[lo_id]) < 2) and (is_out_hi or len(bots[hi_id]) < 2):
          return b

  outs = defaultdict(list)

  while ((b := run_bot()) is not None):
    lo, hi = sorted(bots[b])
    if compares and (lo, hi) == compares:
      return b
    bots[b] = []
    (is_out_lo, lo_id), (is_out_hi, hi_id) = splits[b]
    (outs if is_out_lo else bots)[lo_id] += lo,
    (outs if is_out_hi else bots)[hi_id] += hi,

  return outs[0][0] * outs[1][0] * outs[2][0]


if __name__ == "__main__":
  change_dir(__file__)

  test(2, solve(compares=(2, 5), file='input-test-1'))
  test(56, solve(compares=(17, 61), file='input-real'))

  test(30, solve(file='input-test-1'))
  test(7847, solve(file='input-real'))
