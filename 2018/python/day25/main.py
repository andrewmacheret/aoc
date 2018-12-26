from collections import defaultdict
from timeit import timeit
from python_algorithms.basic.union_find import UF as UnionFind

class Solution:
  def load(self, filename):
    self.filename = filename
    with open(filename) as f: lines = f.read().splitlines()
    self.points = sorted(tuple(int(i) for i in line.strip().split(',')) for line in lines)
    return self

  def count_clusters(self):
    n = len(self.points)
    points = self.points
    _abs = abs
    uf = UnionFind(n)
    for i in xrange(n):
      x1,y1,z1,t1 = points[i]
      for j in xrange(i+1, n):
        x2,y2,z2,t2 = points[j]
        x = x2-x1
        if x + _abs(y2-y1) + _abs(z2-z1) + _abs(t2-t1) <= 3:
          uf.union(i, j)
        elif x >= 3 and (x > 3 or (y2-y1 >= 0 and (y2-y1 > 0 or (z2-z1 >= 0 and (z2-z1 > 0 or t2-t1 >= 0))))): break
    self.result = uf.count()

  def solve(self):
    time = timeit(stmt=self.count_clusters, number=1)

    return [
      {'filename': self.filename},
      {'part1': self.result},
      {'time': time},
    ]

print(Solution().load('input-test.txt').solve())
print(Solution().load('input-test2.txt').solve())
print(Solution().load('input-test3.txt').solve())
print(Solution().load('input-test4.txt').solve())
print(Solution().load('input.txt').solve())
