#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  D = defaultdict(list)
  groups = set()
  for line in load(file):
    c1, c2 = line.split('-')
    D[c1].append(c2)
    D[c2].append(c1)
    groups.add(tuple(sorted([c1, c2])))

  while 1:
    new_groups = set()
    for g in groups:
      for y in D[g[0]]:
        if all(y in D[z] for z in g):
          new_groups.add(tuple(sorted([y, *g])))
    if part == 0:
      return sum(any('t'==s[0] for s in g) for g in new_groups)
    if not new_groups:
      return ','.join(next(iter(groups)))
    groups = new_groups
  


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(7, solve(part=0, file='input-test-1'))
  test(1378, solve(part=0, file='input-real'))

  test('co,de,ka,ta', solve(part=1, file='input-test-1'))
  test('bs,ey,fq,fy,he,ii,lh,ol,tc,uu,wl,xq,xv', solve(part=1, file='input-real'))
