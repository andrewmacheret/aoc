#!/usr/bin/env python3

from collections import deque

from common.util import load_string, test, change_dir, md5

DIRS = [('U', 0, -1), ('D', 0, 1), ('L', -1, 0), ('R', 1, 0)]


def bfs(start, expand, is_goal):
  q = deque(seen := {start})
  while q:
    x = q.popleft()
    if is_goal(*x):
      yield x
    else:
      for y in expand(*x):
        if y not in seen:
          seen.add(y)
          q.append(y)


def solve(part, input=None, file=None):
  seed = input or load_string(file)

  def expand(x, y, path):
    opens = md5(seed + path)[:4]
    for (c, dx, dy), door in zip(DIRS, opens):
      x1, y1 = x+dx, y+dy
      if 0 <= x1 < 4 and 0 <= y1 < 4 and door in 'bcdef':
        yield x1, y1, path + c

  def is_goal(x, y, _):
    return x == y == 3

  gen = bfs((0, 0, ''), expand, is_goal)

  if part == 1:
    return next(gen)[2]
  else:
    return len(list(gen)[-1][2])


### THE REST IS TESTS ###


if __name__ == "__main__":
  change_dir(__file__)

  test('DDRRRD', solve(part=1, input='ihgpwlah'))
  test('DDUDRLRRUDRD', solve(part=1, input='kglvqrro'))
  test('DRURDRUDDLLDLUURRDULRLDUUDDDRR', solve(part=1, input='ulqzkmiv'))

  test('RLDUDRDDRR', solve(part=1, file='input-real'))

  test(370, solve(part=2, input='ihgpwlah'))
  test(492, solve(part=2, input='kglvqrro'))
  test(830, solve(part=2, input='ulqzkmiv'))

  test(590, solve(part=2, file='input-real'))
