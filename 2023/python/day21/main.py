#!/usr/bin/env python3

# import networkx as nx
# import numpy as np
# from copy import copy, deepcopy
# import sys
# sys.setrecursionlimit(100000)

from common.util import *



goal = 26501365
def f(n):
    a0 = 3955
    a1 = 34778
    a2 = 97389

    b0 = a0
    b1 = a1-a0
    b2 = a2-a1
    return b0 + b1*n + (n*(n-1)//2)*(b2-b1)
print(f(goal//131))
  

def solve(part, file, steps):
  # data = load_ints(file)
  # data = load_custom(file)
  # data = load_blocks(file)
  # data = load_csv(file)
  data = load(file)
  n = len(data)

  g = parse_dict(data)
  sx = sy = n // 2

  # def fill(sx1,sy1):
  #   sizes = {-1: 0, 0: 1}
  #   i = 1
  #   seen = {(sx1, sy1)}
  #   q = {(sx1, sy1)}
  #   while True:
  #     next_q = set()
  #     for x,y in q:
  #       for dx,dy in DIRS_4:
  #         nx, ny = x+dx, y+dy
  #         if (nx,ny) in g and g[nx,ny] == '.' and (nx,ny) not in seen:
  #           next_q.add((nx,ny))
  #           seen.add((nx,ny))
  #     q = next_q
  #     sizes[i] = sum((x + y) % 2 == i%2 for x,y in seen)
  #     if sizes[i] == sizes[i-2]:
  #       break
  #     i = i + 1
  #   # print(sizes)
  #   return sizes

  # if part == 0:
  #   return fill(sx,sy)[steps]

  # print(26501365 / n)
  # print((sx,sy) == (n//2,m//2))
  # sizes = [
  #   [ fill(n-1,n-1),fill(n-1,n//2),fill(n-1,0) ],
  #   [ fill(n//2,n-1),fill(n//2,n//2),fill(n//2,0) ],
  #   [ fill(0,n-1),fill(0,n//2),fill(0,0) ],
  # ]
  # print([[len(x) for x in s] for s in sizes])
  # # print(n//2 + m//2, len(sizes[0][0]))
  

  # goal = 26501365
  # def f(n):
  #     a0 = 3955
  #     a1 = 35214
  #     a2 = 97607

  #     b0 = a0
  #     b1 = a1-a0
  #     b2 = a2-a1
  #     return b0 + b1*n + (n*(n-1)//2)*(b2-b1)
  # print()
  # return f(goal//131) 
  dx = [0,-1,0,1]
  dy = [-1,0,1,0]

  # q = {(sx, sy)}
  # for itt in range(1,100000):
  #     nq = set()
  #     for i,j in q:
  #         for dx, dy in DIRS_4:
  #             ni = i+dx
  #             nj = j+dy
  #             if g[ni%n,nj%n] != "#":
  #                 nq.add((ni,nj))
  #     q = nq
  #     if itt%n == goal%n:
  #         print(itt, len(q))

  

  def move():
    q = {(sx, sy)}
    for i in count(1):
      next_q = set()
      for x,y in q:
        for dx,dy in DIRS_4:
          nx, ny = x+dx, y+dy
          if g[nx%n,ny%n] != '#':
            next_q.add((nx,ny))
      q = next_q
      if i % n == steps % n:
        yield len(q)

  it = move()
  a0, a1, a2 = next(it), next(it), next(it)
  x = steps//n
  b0 = a0
  b1 = a1-a0
  b2 = a2-a1
  return b0 + b1*x + (x*(x-1)//2)*(b2-b1)




  # return sum((x+y) % 2 == 0 for x,y in q)

  # run_with_cycles(q, step, steps)
  # last_i = 0
  # for _ in range(steps):
  #   q = step()

    # print(draw(set(q)))
  # t = 0
  # for y in range(-steps,steps+1):
  #   for x in range(-steps,steps+1):
  #     if g[x%m,y%n] == '.' and (x + y) % 2 == 0:
  #       t += 1
  # return t  
  # for _ in range(30):
  #   q = step()
  # print(draw(set(q)))
  # q = step()
  # for _ in range(100)
  # print(draw(set(q)))
  # return len(q)
  
  
  # for 
  
  # t = 0
  # seen = set()
  # q = {(sy, sx)}
  # for _ in range(64):
  #   next_q = set()
  #   for x,y in q:
  #     for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
  #       nx, ny = x+dx, y+dy
  #       if g[nx,ny] == '.':
  #         next_q.add((nx,ny))
  #   q = next_q
  #   print(len(q))

  # print(draw(q))
  # return len(q)


  # print(draw(g))
  # return t


  # print(data)


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  # test(16, solve(part=0, file='input-test-1', steps=6))
  # test(3830, solve(part=0, file='input-real', steps=64))

  # test(16, solve(part=1, file='input-test-1', steps=6))
  # test(50, solve(part=1, file='input-test-1', steps=10))
  # test(1594, solve(part=1, file='input-test-1', steps=50))
  # test(6536, solve(part=1, file='input-test-1', steps=100))
  # test(167004, solve(part=1, file='input-test-1', steps=500))
  # test(668697, solve(part=1, file='input-test-1', steps=1000))
  # test(16733044, solve(part=1, file='input-test-1', steps=5000))

  # test(3955, solve(part=1, file='input-real', steps=65))
  # test(35214, solve(part=1, file='input-real', steps=65+131))
  # test(97607, solve(part=1, file='input-real', steps=65+131+131))
  test(637087163925555, solve(part=1, file='input-real', steps=26501365))
  # 3222027238633805 is too high
  # 3985680103403355 is too high
  # 637087163925555
    
