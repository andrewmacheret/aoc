from collections import defaultdict
from timeit import timeit

class Solution:
  def load(self, filename):
    self.filename = filename
    with open(filename) as f: lines = f.read().splitlines()
    self.points = sorted([int(i) for i in line.strip().split(',')] for line in lines)
    return self

  def prepare_graph(self):
    self.n = n = len(self.points)
    graph = defaultdict(list)
    points = self.points
    _abs = abs
    for i in xrange(n):
      x1,y1,z1,t1 = points[i]
      for j in xrange(i+1, n):
        x2,y2,z2,t2 = points[j]
        x = x2-x1
        if x + _abs(y2-y1) + _abs(z2-z1) + _abs(t2-t1) <= 3:
          graph[i].append(j)
          graph[j].append(i)
        elif x >= 3 and (x > 3 or (y2-y1 >= 0 and (y2-y1 > 0 or (z2-z1 >= 0 and (z2-z1 > 0 or t2-t1 >= 0))))): break
    self.graph = graph

  def count_clusters(self):
    count = 0
    visited = set()
    n = self.n
    graph = self.graph
    for i in xrange(n):
      if i not in visited:
        count += 1
        q = [i]
        while q:
          j = q.pop()
          visited.add(j)
          for k in graph[j]:
            if k not in visited:
              q.append(k)
    self.result = count

  def solve(self):
    time1 = timeit(stmt=self.prepare_graph, number=1)
    time2 = timeit(stmt=self.count_clusters, number=1)

    return [
      {'filename': self.filename},
      {'part1': self.result},
      {'time': time1+time2},
    ]

print(Solution().load('input-test.txt').solve())
print(Solution().load('input-test2.txt').solve())
print(Solution().load('input-test3.txt').solve())
print(Solution().load('input-test4.txt').solve())
print(Solution().load('input.txt').solve())
