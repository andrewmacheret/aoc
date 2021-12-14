#!/usr/bin/env python3

from collections import Counter, defaultdict

from common.util import load_blocks, test, change_dir


def solve(steps, file):
  data = load_blocks(file)

  rules = defaultdict(str)
  for line in data[1]:
    a, b, _, _, _, _, c = line
    rules[a, b] = c

  s = data[0][0]
  C = Counter(zip(s, s[1:]))

  for _ in range(steps):
    D = Counter()
    for (a, b), v in C.items():
      c = rules[a, b]
      D[a, c] += v
      D[c, b] += v
    C = D

  D = Counter((s[0], s[-1]))
  for (a, b), v in C.items():
    D[a] += v
    D[b] += v
  mc = D.most_common()
  return (mc[0][1] - mc[-1][1]) // 2


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(1588, solve(steps=10, file='input-test-1'))
  test(2851, solve(steps=10, file='input-real'))

  test(2188189693529, solve(steps=40, file='input-test-1'))
  test(10002813279337, solve(steps=40, file='input-real'))
