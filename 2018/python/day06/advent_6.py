
"""
..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.


aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf


a........
a........
aaabb..cc
aaabbbccc
AaabbbccC
....B....


aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf


1111113333
11111.3333
1114453333
1144453333
2.44455333
22.4555533
222.5555..
2222555666
2222556666
222.666666
222.666666



1. find minx, find miny
2. for each coordinate, subtract minx, miny
3. find maxx, find maxy
4. create an int grid[maxx+1, maxy+1]
5. fill in all coordinates in grid with coord_index + 1
6. add all coordinates to a queue
7. bfs all nodes:
"""

from collections import defaultdict
from pprint import pprint

def solve(coords):
  minx = min(x for x,y in coords)
  miny = min(y for x,y in coords)

  coords = [(x-minx+1, y-miny+1) for x,y in coords]

  width = max(x for x,y in coords) + 2
  height = max(y for x,y in coords) + 2

  grid = [[0 for _ in xrange(width)] for _ in xrange(height)]
  score = [0]
  q = []
  for coord_index, (x,y) in enumerate(coords):
    q.append((x, y, coord_index+1))
    score.append(1)
    grid[y][x] = coord_index+1

  #for row in grid:
  #  print ''.join([str(i) for i in row])

  dirs = [(1,0), (0,1), (-1,0), (0,-1)]
  while q:
    next_moves = defaultdict(list)
    for x, y, coord_index in q:
      for dx,dy in dirs:
        x2,y2 = x+dx,y+dy
        if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] == 0:
          next_moves[(x2,y2)].append(coord_index)
    q = []
    #print(len(q), len(next_moves))
    for (x, y), coord_indexes in next_moves.iteritems():
      if len(set(coord_indexes)) == 1:
        coord_index = coord_indexes[0]
        q.append((x, y, coord_index))
        score[coord_index] += 1
        grid[y][x] = coord_index
      else:
        grid[y][x] = -1
        #print('woof', x, y)

  for y in xrange(height):
    val = grid[y][0]
    if 0 < val: score[val] = 0
    val = grid[y][width-1]
    if 0 < val: score[val] = 0
  for x in xrange(width):
    val = grid[0][x]
    if 0 < val: score[val] = 0
    val = grid[height-1][x]
    if 0 < val: score[val] = 0

  #for row in grid:
  #  print ''.join([str(i) if i >= 0 else '.' for i in row])
  return max(score)

coords = [
  (292, 73),
  (204, 176),
  (106, 197),
  (155, 265),
  (195, 59),
  (185, 136),
  (54, 82),
  (209, 149),
  (298, 209),
  (274, 157),
  (349, 196),
  (168, 353),
  (193, 129),
  (94, 137),
  (177, 143),
  (196, 357),
  (272, 312),
  (351, 340),
  (253, 115),
  (109, 183),
  (252, 232),
  (193, 258),
  (242, 151),
  (220, 345),
  (336, 348),
  (196, 203),
  (122, 245),
  (265, 189),
  (124, 57),
  (276, 204),
  (309, 125),
  (46, 324),
  (345, 228),
  (251, 134),
  (231, 117),
  (88, 112),
  (256, 229),
  (49, 201),
  (142, 108),
  (150, 337),
  (134, 109),
  (288, 67),
  (297, 231),
  (310, 131),
  (208, 255),
  (246, 132),
  (232, 45),
  (356, 93),
  (356, 207),
  (83, 97)
]
# coords = [
#   (1, 1),
#   (1, 6),
#   (8, 3),
#   (3, 4),
#   (5, 5),
#   (8, 9),
# ]
print(solve(coords))






