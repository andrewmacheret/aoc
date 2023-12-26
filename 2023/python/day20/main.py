#!/usr/bin/env python3

from common.util import *


def solve(part, file):
  data = load(file)

  modules = {}
  for line in data:
    src, dst = line.split(' -> ')
    modules[src[1:]] = (src[0], dst.split(', '))

  flips = defaultdict(int)
  conjs = defaultdict(dict)
  for src, (_, outs) in modules.items():
    for out in outs:
      if out in modules and modules[out][0] == '&':
        conjs[out][src] = 0
  
  goals = {src:0 for src, (type, _) in modules.items() if type == '&'}

  def press(r):
    sigs = [1, 0]
    q = deque([('roadcaster', 0, 'button')])
    while q:
      mod, sig, src = q.popleft()
      if mod in modules:
        type, outs = modules[mod]
        if type == '%':
          if sig == 1:
            continue
          sig = flips[mod] = 1 - flips[mod]
        elif type == '&':
          conjs[mod][src] = sig
          sig = 1 - all(conjs[mod].values())
        for out in outs:
          sigs[sig] += 1
          q.append((out, sig, mod))
          if sig and mod in goals and goals[mod] == 0:
            goals[mod] = r
    return sigs
  
  if part == 0:
    lo = hi = 0
    for r in range(1000):
      l, h = press(r)
      lo, hi = lo+l, hi+h
    return lo * hi

  for r in count(1):
    press(r)
    if all(goals.values()):
      return lcm(*goals.values())

  # print(data)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(32000000, solve(part=0, file='input-test-1'))
  test(11687500, solve(part=0, file='input-test-2'))
  test(817896682, solve(part=0, file='input-real'))

  test(250924073918341, solve(part=1, file='input-real'))
