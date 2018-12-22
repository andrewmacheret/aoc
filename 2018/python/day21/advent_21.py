
class Solution:
  def simulate(self, fastest):
    visited = set()

    small = 65536
    big = 10828530
    last_big = 0

    while True:
      big += small & 255
      big &= 16777215
      big *= 65899
      big &= 16777215
      
      if 256 <= small:
        small /= 0x100
        continue
      
      if fastest:
        return big
      else: # slowest
        if big in visited:
          return last_big
        visited.add(big)
        last_big = big

      small = big | 65536
      big = 10828530

  def solve(self):
    return [
      {'part1': self.simulate(True)},
      {'part2': self.simulate(False)},
    ]


print(Solution().solve())
