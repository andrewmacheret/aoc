#!/usr/bin/env python3

from common.util import *

EMPTY = -1

class Node:
  def __init__(self, id, size):
    self.prev = self.next = None
    self.id = id
    self.size = size


def solve(part, file):
  return (solve1, solve2)[part](file)

def solve1(file):
  db = []
  for id,a in enumerate(map(int, load(file)[0])):
    for i in range(a):
      db.append(EMPTY if id % 2 else id // 2)
  
  j = len(db) - 1
  i = 0
  while i < j:
    while db[i] != EMPTY:
      i += 1
    while db[j] == EMPTY:
      j -= 1
    if i >= j:
      break
    db[i], db[j] = db[j], db[i]
    i += 1
    j -= 1
  
  total = 0
  for i in range(len(db)):
    if db[i] != EMPTY:
      total += i * db[i]
  return total


def build_linked_list(data):
  head = tail = None
  for id,a in enumerate(map(int, data[0])):
    node = Node(EMPTY, a) if id % 2 else Node(id // 2, a)
    if tail:
      # add at end
      tail.next = node
      node.prev = tail
      tail = node
    else:
      # first node
      head = tail = node
  return head, tail

def solve2(file):
  head, tail = build_linked_list(load(file))
  
  b = tail
  while b.prev:
    while b.id == EMPTY:
      b = b.prev
    if not b.prev:
      break
    a = head
    while a.id != b.id:
      if a.id == EMPTY and a.size >= b.size:
        a.id, b.id = b.id, a.id
        diff = a.size - b.size
        if diff > 0:
          a.size = b.size
          new_node = Node(EMPTY, diff)
          new_node.prev = a
          new_node.next = a.next
          a.next = new_node
          if new_node.next:
            new_node.next.prev = new_node
      a = a.next
    b = b.prev

  total = 0
  a = head
  i = 0
  while a:
    while a.size > 0:
      if a.id != EMPTY:
        total += a.id * i
      a.size -= 1
      i += 1
    a = a.next
  return total

### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(1928, solve(part=0, file='input-test-1'))
  test(6366665108136, solve(part=0, file='input-real'))

  test(2858, solve(part=1, file='input-test-1'))
  test(6398065450842, solve(part=1, file='input-real'))
