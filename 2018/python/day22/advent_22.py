import networkx

class Solution:

  DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

  def draw(self):
    for row in self.layout:
      print(''.join(row))

  def determine_risk(self):
    sum = 0
    for y in xrange(self.ty+1):
      for x in xrange(self.tx+1):
        sum += {'T': 0, 'M': 0, '.': 0, '=': 1, '|': 2}[self.layout[y][x]]
    return sum

  def get_allowed(self, (x, y)):
    ch = self.layout[y][x]
    if ch == '.':
      return 'CT'
    elif ch == '=':
      return 'CN'
    elif ch == '|':
      return 'TN'
    else:
      return 'CTN'


  def shortest_path(self):
    graph = networkx.Graph()

    for y in xrange(self.height):
      for x in xrange(self.width):
        allowed = self.get_allowed((x, y))
        for i in allowed:
          for j in allowed:
            if i != j:
              graph.add_edge((x, y, i), (x, y, j), weight=7)
        for dx,dy in Solution.DIRS:
          x2, y2 = x+dx, y+dy
          if 0 <= x2 < self.width and 0 <= y2 < self.height:
            allowed2 = self.get_allowed((x2, y2))
            for item in set(allowed).intersection(set(allowed2)):
              graph.add_edge((x, y, item), (x2, y2, item), weight=1)
    return networkx.dijkstra_path_length(graph, (0, 0, 'T'), (self.tx, self.ty, 'T'))

  def fill_grid(self):
    self.grid = [[0 for x in xrange(self.width)] for y in xrange(self.height)]
    self.layout = [['.' for x in xrange(self.width)] for y in xrange(self.height)]
    for y in xrange(self.height):
      for x in xrange(self.width):
        if x == 0:
          geologic = y * 48271
        elif y == 0:
          geologic = x * 16807
        elif x == self.tx and y == self.ty:
          geologic = 0
        else:
          geologic = self.grid[y][x-1] * self.grid[y-1][x]
        self.grid[y][x] = (geologic + self.depth) % 20183

        self.layout[y][x] = {0: '.', 1: '=', 2: '|'}[self.grid[y][x] % 3]
    self.layout[0][0] = 'M'
    self.layout[self.ty][self.tx] = 'T'

  def solve(self, depth, (tx, ty), extra=10, debug=False):
    self.tx, self.ty = tx, ty
    self.width, self.height = tx + 1 + extra, ty + 1 + extra
    self.depth = depth

    self.fill_grid()

    if debug: self.draw()

    risk = self.determine_risk()

    time = self.shortest_path()

    return [
      {'risk': risk},
      {'time': time},
    ]

print(Solution().solve(510, (10,10), 5, debug=True))
print(Solution().solve(8787, (10,725), 100))
