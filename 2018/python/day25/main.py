from collections import defaultdict
from timeit import timeit

class Solution:
  def load(self, filename):
    self.filename = filename
    with open(filename) as f: lines = f.read().splitlines()
    self.points = sorted([int(i) for i in line.strip().split(',')] for line in lines)
    return self

  def prepare_graph(self):
    self.n = len(self.points)
    self.graph = defaultdict(list)
    for i in xrange(self.n):
      x1,y1,z1,t1 = self.points[i]
      for j in xrange(i+1,self.n):
        x2,y2,z2,t2 = self.points[j]
        x = x2-x1
        if x > 3: break
        if x + abs(y2-y1) + abs(z2-z1) + abs(t2-t1) <= 3:
          self.graph[i].append(j)
          self.graph[j].append(i)

  def count_clusters(self):
    count = 0
    visited = set()
    for i in xrange(self.n):
      if i not in visited:
        count += 1
        q = [i]
        while q:
          j = q.pop()
          visited.add(j)
          for k in self.graph[j]:
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
