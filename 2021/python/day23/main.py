#!/usr/bin/env python3

from heapq import heappush, heappop

from common.util import load, sign, lists, tuples, change_dir, test


def is_victory(hall, rooms):
  return set(hall) == {-1} and all(set(room) == {i} for i, room in enumerate(rooms))


def possible_moves(hall, rooms, room_size):
  hall, rooms = list(hall), lists(rooms)

  for r, room in enumerate(rooms):
    if room and set(room) != {r}:
      amph = room.pop()
      h = (r+1)*2
      for path in (range(h-1, -1, -1), range(h+1, 11)):
        for i in path:
          if i % 10 == 0 or i % 2 != 0:
            if hall[i] != -1:
              break
            cost = (10 ** amph) * (abs(h-i) + 1 +
                                   (room_size - 1 - len(rooms[r])))
            hall[i] = amph
            yield cost, tuple(hall), tuples(rooms)
            hall[i] = -1
      room.append(amph)

  for i, amph in enumerate(hall):
    h = (amph+1)*2
    if amph != -1 and (len(rooms[amph]) == 0 or set(rooms[amph]) == {amph}) and \
            all(hall[z] == -1 for z in range(i+sign(h-i), h, sign(h-i))):
      cost = (10 ** amph) * (abs(h-i) + 1 + (room_size - 1 - len(rooms[amph])))
      hall[i] = -1
      rooms[amph].append(amph)
      yield cost, tuple(hall), tuples(rooms)
      rooms[amph].pop()
      hall[i] = amph


def load_amphibians(part, file):
  hall = [-1] * 11
  rooms = [[], [], [], []]
  for line in load(file)[3:1:-1]:
    for i, c in enumerate(line[3:11:2]):
      rooms[i].append(ord(c)-ord('A'))
  if part == 2:
    for room, fold in zip(rooms, [[3, 3], [1, 2], [0, 1], [2, 0]]):
      room[:] = [room[0], *fold, room[1]]
  return tuple(hall), tuples(rooms)


def solve(part, file):
  hall, rooms = load_amphibians(part, file)

  seen = set()
  q = [(0, hall, rooms)]
  while q:
    weight, hall, rooms = heappop(q)
    if (hall, rooms) not in seen:
      seen.add((hall, rooms))
      if is_victory(hall, rooms):
        return weight
      for w, h, r in possible_moves(hall, rooms, part * 2):
        heappush(q, (weight+w, h, r))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(12521, solve(part=1, file='input-test-1'))
  test(10411, solve(part=1, file='input-real'))

  test(44169, solve(part=2, file='input-test-1'))
  test(46721, solve(part=2, file='input-real'))
