class Solution:
  def load(self, filename):
    self.filename = filename
    with open(filename) as f: lines = f.read().splitlines()
    self.points = [[int(i) for i in line.strip().split(',')] for line in lines]
    return self

  def distance(self, (x1,y1,z1,t1), (x2,y2,z2,t2)):
    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2) + abs(t1-t2)

  def solve(self):
    n = len(self.points)
    graph = [[int(self.distance(self.points[i], self.points[j]) <= 3) for j in xrange(n)] for i in xrange(n)]

    def dfs(graph, x):
      for i in xrange(n):
        if graph[x][i] == 1:
          graph[x][i] = graph[i][x] = 0
          dfs(graph, i)

    count = len(list(dfs(graph, i) for i in xrange(n) if graph[i][i] == 1))
    return [
      {'filename': self.filename},
      {'part1': count},
    ]

print(Solution().load('input-test.txt').solve())
print(Solution().load('input-test2.txt').solve())
print(Solution().load('input-test3.txt').solve())
print(Solution().load('input-test4.txt').solve())
print(Solution().load('input.txt').solve())
