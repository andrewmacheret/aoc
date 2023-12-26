#!/usr/bin/env python3

from common.util import *

def dirs4(x,y):
  for dx,dy in DIRS_4:
    yield x+dx,y+dy

def dfs(init, expand, is_goal):
  stack = [(0,init,set())]
  while stack:
    l,item,seen = stack.pop()
    if is_goal(l,*item):
      yield l,item
      continue
    seen = seen | {item}
    for l1,i1 in expand(l,*item):
      if i1 not in seen:
        stack.append((l1,i1,seen))

def part1(grid, n, m):
  is_goal = lambda l,x,y: x == m-2 and y == n-1
  def expand(l,x,y):
    for dx,dy in DIRS_4:
      ch = grid[x+dx,y+dy]
      if ch == '.' or \
            (ch == '>' and (dx,dy) == RIGHT) or \
            (ch == '<' and (dx,dy) == LEFT) or \
            (ch == '^' and (dx,dy) == UP) or \
            (ch == 'v' and (dx,dy) == DOWN):
        yield l+1,(x+dx,y+dy)
  return max(dfs((1,0), expand, is_goal))[0]

def part2(grid, n, m):
  # find all the significant locations surrounded by 3 or more paths
  joins = [(1,0),(m-2,n-1)]
  start, goal = 0, 1 # index of the ultimate start and goal
  for x,y in list(grid):
    if grid[x,y] == '.':
      if 3 <= sum(grid[nx,ny] in '.<>^v' for nx,ny in dirs4(x,y)):
        joins.append((x,y))
  for x,y in joins:
    grid[x,y] = '+'
    for nx,ny in dirs4(x,y):
      if grid[nx,ny] == '<>^v':
          grid[nx,ny] = '+'

  # find the longest path between each pair of significant locations
  is_goal = lambda l,x,y: grid[x,y] == '+'
  def expand(l,x,y):
    for nx,ny in dirs4(x,y):
      if grid[nx,ny] != '#':
        yield l+1,(nx,ny)

  # build a graph and the distance between each pair of significant locations
  best = defaultdict(int)
  g = defaultdict(set)
  for i,(x,y) in enumerate(joins):
    grid[x,y] = '#'
    for nx,ny in dirs4(x,y):
      if grid[nx,ny] != '#':
        for l,(x1,y1) in dfs((x,y),expand,is_goal):
          j = joins.index((x1,y1))
          best[i,j] = max(best[i,j], l)
          best[j,i] = max(best[j,i], l)
          g[i].add(j)
          g[j].add(i)
    grid[x,y] = '+'

  # find the longest path between the start and the goal
  is_goal = lambda l,i: i == goal
  def expand(l,i):
    for j in g[i]:
      yield l+best[i,j], (j,)
  return max(dfs((start,),expand,is_goal))[0]

def solve(part, file):
  data = load(file)
  n, m = len(data), len(data[0])
  grid = defaultdict(lambda: '#', parse_dict(data))
  return (part1, part2)[part](grid, n, m)



### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(94, solve(part=0, file='input-test-1'))
  test(2294, solve(part=0, file='input-real'))

  test(154, solve(part=1, file='input-test-1'))
  test(6418, solve(part=1, file='input-real'))
