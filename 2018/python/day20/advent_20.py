from collections import deque

class Room:
  OPPOSITE_DIRS = {
    'E': 'W',
    'W': 'E',
    'N': 'S',
    'S': 'N',
  }
  DIRS = {
    'E': (+1,  0),
    'W': (-1,  0),
    'N': ( 0, -1),
    'S': ( 0, +1),
  }
  def __init__(self, (x, y)):
    self.doors = {}
    self.x, self.y = x, y

class Solution:
  def __init__(self):
    self.all_rooms = {}
    self.min_x, self.min_y, self.max_x, self.max_y = 0, 0, 0, 0

  def find_or_create_room(self, (x, y)):
    if (x, y) in self.all_rooms:
      room = self.all_rooms[(x, y)]
    else:
      room = Room((x, y))
      self.all_rooms[(x, y)] = room

    if self.min_x > x: self.min_x = x
    if self.max_x < x: self.max_x = x
    if self.min_y > x: self.min_y = y
    if self.max_y < y: self.max_y = y

    return room

  def draw_rooms(self):
    print('')
    for y in xrange(self.min_y, self.max_y+1):
      top, mid, bot = [], [], []
      for x in xrange(self.min_x, self.max_x+1):
        if (x, y) in self.all_rooms:
          room = self.all_rooms[(x, y)]
          top.append('#')
          top.append('-' if 'N' in room.doors else '#')
          mid.append('|' if 'W' in room.doors else '#')
          mid.append('X' if (x,y) == (0,0) else (str(room.distance % 10) if room.distance else ' '))
          bot.append('#')
          bot.append('-' if 'S' in room.doors else '#')
        else:
          top.append('##')
          mid.append('##')
          bot.append('##')
      top.append('#')
      mid.append('#')
      print(''.join(top))
      print(''.join(mid))
    print('#' * ((self.max_x - self.min_x) * 2 + 3))

  def load(self, filename):
    self.filename = filename
    with open(filename) as f:
      self.regex = f.read().rstrip()[1:-1]
    return self

  def bfs(self, start, distance_threshold):
    q = [start]
    visited = set()
    max_distance = start.distance = 0
    rooms_beyond_distance_threshold = 0
    while True:
      next_q = []
      for room in q:
        if max_distance > distance_threshold: rooms_beyond_distance_threshold += 1
        for direction, next_room in room.doors.iteritems():
          if next_room not in visited:
            next_room.distance = max_distance # for drawing
            next_q.append(next_room)
            visited.add(next_room)
      q = next_q
      if not q: return max_distance, rooms_beyond_distance_threshold
      max_distance += 1

  def solve(self, distance_threshold, debug=False):
    x, y = 0, 0
    room = start = self.find_or_create_room((x, y))
    room_stack = deque()
    for ch in self.regex:
      if ch in Room.DIRS:
        dx, dy = Room.DIRS[ch]
        x, y = x+dx, y+dy
        room.doors[ch] = next_room = self.find_or_create_room((x, y))
        next_room.doors[Room.OPPOSITE_DIRS[ch]] = room
        room = next_room
      elif ch == '(':
        room_stack.append(room)
      elif ch == ')':
        room = room_stack.pop()
        x, y = room.x, room.y
      elif ch == '|':
        room = room_stack[-1]
        x, y = room.x, room.y

    max_distance, rooms_beyond_distance_threshold = self.bfs(start, distance_threshold)
    if debug: self.draw_rooms()
    return [
      {'filename': self.filename},
      {'distance_threshold': distance_threshold},
      {'part1': max_distance},
      {'part2': rooms_beyond_distance_threshold},
    ]

# 1. follow all paths of the regex to build a 4d graph
# 2. do a BFS to find shortest path

print(Solution().load('advent_20_input_test.txt').solve(9, True))
print(Solution().load('advent_20_input_test2.txt').solve(19, True))
print(Solution().load('advent_20_input.txt').solve(999, True))
