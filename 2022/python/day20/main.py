#!/usr/bin/env python3

from common.util import *


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None


def solve(part, file):
  nodes = [Node(int(line)) for line in load(file)]
  n = len(nodes)

  for i, node in enumerate(nodes):
    node.prev = nodes[(i-1) % n]
    node.next = nodes[(i+1) % n]
    if part:
      node.val *= 811589153

  for _ in range((1, 10)[part]):
    for node in list(nodes):
      if node.val:
        old_prev = node.prev
        old_next = node.next

        target = node
        for _ in range(node.val % (n - 1)):
          target = target.next

        new_prev = target
        new_next = target.next

        node.prev = new_prev
        node.next = new_next
        new_next.prev = node
        new_prev.next = node
        old_prev.next = old_next
        old_next.prev = old_prev

  node = nodes[0]
  vals = [(node := node.next).val for i in range(n)]
  zero = vals.index(0)
  return sum(vals[(zero + i*1000) % n] for i in (1, 2, 3))


### THE REST IS TESTS ###
if __name__ == "__main__":
  change_dir(__file__)

  test(3, solve(part=0, file='input-test-1'))
  test(2203, solve(part=0, file='input-real'))

  test(1623178306, solve(part=1, file='input-test-1'))
  test(6641234038999, solve(part=1, file='input-real'))
