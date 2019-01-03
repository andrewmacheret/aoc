from timeit import timeit
from python_algorithms.basic.union_find import UF as UnionFind


def count_clusters(points, dist):
  n = len(points)
  uf = UnionFind(n)

  # compute all (dx,dy,dz,dt) such that abs(dx) + abs(dy) + abs(dz) + abs(dt) <= 3
  # and don't include (0,0,0,0)
  DIRS = [(dx,dy,dz,dt) for dx in xrange(-dist, dist+1) \
                        for dy in xrange(-dist+abs(dx), dist+1-abs(dx)) \
                        for dz in xrange(-dist+abs(dx)+abs(dy), dist+1-abs(dx)-abs(dy)) \
                        for dt in xrange(-dist+abs(dx)+abs(dy)+abs(dz), dist+1-abs(dx)-abs(dy)-abs(dz)) \
                        if (dx,dy,dz,dt) != (0,0,0,0)]

  # generate a dict of each point to its index
  point_to_index = {p: i for i, p in enumerate(points)}

  # for each connected points, perform a union find between the indices of the two points
  for i in xrange(n):
    x,y,z,t = points[i]
    for dx,dy,dz,dt in DIRS:
      p2 = (x+dx, y+dy, z+dz, t+dt)
      if p2 in point_to_index:
        uf.union(i, point_to_index[p2])

  # return the number of disjoint sets we found
  return uf.count()


class Day25:
  def load(self, filename):
    self.filename = filename
    with open(filename) as f: lines = f.read().splitlines()
    self.points = [tuple(int(i) for i in line.strip().split(',')) for line in lines]
    return self

  def part1(self):
    self.part1_result = count_clusters(self.points, 3)

  def solve(self):
    time = timeit(stmt=self.part1, number=1)

    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'time': time},
    ]


if __name__== "__main__":
  print(Day25().load('input-test.txt').solve())
  print(Day25().load('input-test2.txt').solve())
  print(Day25().load('input-test3.txt').solve())
  print(Day25().load('input-test4.txt').solve())
  print(Day25().load('input.txt').solve())
