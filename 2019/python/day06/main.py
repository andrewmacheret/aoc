#!/usr/bin/env python3
import os

os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
from day01.main import load, test

def load_orbits(filename, script=__file__):
  return [line.split(')') for line in load(filename, script=script)]

class Node:
  def __init__(self, name):
    self.name = name
    self.parent = None
    self.children = []

def build_tree(pairs):
  nodes = {}
  for parent, child in pairs:
    if parent not in nodes: nodes[parent] = Node(parent)
    if child not in nodes: nodes[child] = Node(child)
    nodes[child].parent = nodes[parent]
    nodes[parent].children.append(nodes[child])
  return nodes

def find_root(nodes):
  root = next(iter(nodes.values()))
  while root.parent: root = root.parent
  return root

def depths(node, depth=0):
  if not node: return
  yield depth
  for child in node.children:
    yield from depths(child, depth+1)

def depth(node):
  depth = 0
  while node.parent:
    node = node.parent
    depth += 1
  return depth

def distance(node1, node2):
  d1, d2, delta = depth(node1), depth(node2), 0
  while d1 > d2:
    node1 = node1.parent
    d1 -= 1
    delta += 1
  while d1 < d2:
    node2 = node2.parent
    d2 -= 1
    delta += 1
  while node1 != node2:
    node1 = node1.parent
    node2 = node2.parent
    delta += 2
  return delta

def part1(filename):
  orbits = load_orbits(filename)
  nodes = build_tree(orbits)
  root = find_root(nodes)
  return sum(depths(root))

def part2(filename, name1, name2):
  orbits = load_orbits(filename)
  nodes = build_tree(orbits)
  return distance(nodes[name1].parent, nodes[name2].parent)

if __name__== "__main__":
  test(42, part1('input-test-1.txt'))
  test(271151, part1('input.txt'))

  test(4, part2('input-test-2.txt','YOU', 'SAN'))
  test(388, part2('input.txt','YOU', 'SAN'))
