#!/usr/bin/env python3

from common.util import *


def load_ports(file):
  return sorted(sorted(map(int, line.split('/'))) for line in load(file))


def solve(part, file):
  ports = load_ports(file)

  valid_ports = defaultdict(set)
  for a, b in ports:
    valid_ports[a].add(b)
    valid_ports[b].add(a)

  def dfs(a, path=[]):
    for b in list(valid_ports[a]):
      valid_ports[a].discard(b)
      valid_ports[b].discard(a)
      for p in dfs(b, path):
        yield path + [a+b] + p
      valid_ports[a].add(b)
      valid_ports[b].add(a)
    yield path

  def strength(path): return sum(path)
  if not part:
    return max(map(strength, dfs(0)))
  return strength(max(dfs(0), key=lambda p: (len(p), strength(p))))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(31, solve(part=0, file='input-test-1'))
  test(1906, solve(part=0, file='input-real'))

  test(19, solve(part=1, file='input-test-1'))
  test(1824, solve(part=1, file='input-real'))
