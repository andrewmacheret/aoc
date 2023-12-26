#!/usr/bin/env python3

from common.util import *
from bisect import bisect


def solve(part, file):
  data = load(file)

  dirs = defaultdict(int)
  pwd = ''
  for line in data[1:]:
    parts = line.split()
    if parts[0] == '$':
      if parts[1] == 'cd':
        if parts[2] == '..':
          pwd = pwd[:pwd.rfind('/')]
        else:
          pwd = pwd + '/' + parts[2]
    elif parts[0] != 'dir':
      size = int(parts[0])
      path = pwd
      while path:
        dirs[path] += size
        path = path[:path.rfind('/')]
      dirs[0] += size

  sizes = dirs.values()
  if part == 0:
    return sum(x for x in sizes if x <= 100000)
  else:
    need = 30000000 - (70000000 - dirs[0])
    sizes = sorted(sizes)
    return sizes[bisect(sizes, need)]


### THE REST IS TESTS ###
if __name__ == "__main__":
  change_dir(__file__)

  test(95437, solve(part=0, file='input-test-1'))
  test(1583951, solve(part=0, file='input-real'))

  test(24933642, solve(part=1, file='input-test-1'))
  test(214171, solve(part=1, file='input-real'))
