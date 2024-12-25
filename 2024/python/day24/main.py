#!/usr/bin/env python3

import networkx as nx
from common.util import *

def run(mem, gates):
  mem = mem.copy()
  g = nx.DiGraph()
  for c, (op, a, b) in gates.items():
    g.add_edge(a, c)
    g.add_edge(b, c)

  for gate in nx.topological_sort(g):
    if gate in mem:
      continue
    op, a, b = gates[gate]
    if a not in mem and b not in mem:
      raise Exception('Both inputs are missing')
    if op == 'AND':
      mem[gate] = mem[a] & mem[b]
    elif op == 'OR':
      mem[gate] = mem[a] | mem[b]
    elif op == 'XOR':
      mem[gate] = mem[a] ^ mem[b]
    else:
      raise Exception('Unknown op')

  res = 0
  for gate in sorted(mem, reverse=1):
    if gate[0] == 'z':
      res = (res << 1) | mem[gate]
  return res


def solve(part, file):
  data = load_blocks(file)
  mem = defaultdict()
  for line in data[0]:
    addr, val = line.split(': ')
    mem[addr] = int(val)
  
  gates = {}
  for line in data[1]:
    a, op, b, _, c = line.split(' ')
    gates[c] = (op, a, b)

  if part == 0:
    return run(mem, gates)

  def dfs_gate2(c):
    if c in gates:
      op,a,b = gates[c]
      a,b = sorted([dfs_gate2(a),dfs_gate2(b)])
      return f'({a} {op} {b})'
    return c

  def check(end):
    carry = None
    for i in range(end):
      z = f"z{i:02d}"
      c = f"c{i:02d}"
      try:
        s = dfs_gate2(z)
      except:
        # print(f'Failed at {z}')
        return False
      
      if i > 1:
        expected = f'(({carry} OR (x{i-1:02d} AND y{i-1:02d})) XOR (x{i:02d} XOR y{i:02d}))'
        if s != expected and i not in (17,24):
          # print(f'ACT: {z} = {s}')
          # print(f'EXP: {z} = {expected}')
          return False

      if i == 0:
        carry = '(x00 AND y00)'
      else:
        # replace second to last XOR with AND
        j = s.rfind('XOR', 0, s.rfind('XOR')-1)
        carry = s[:j] + 'AND' + s[j+3:]
    return True

  swaps = []
  for r in range(1,46):
    if not check(r):
      print(f'Failed at {r}')
      for a,b in permutations(gates,2):
        gates[a], gates[b] = gates[b], gates[a]
        if check(r):
          print(f'Swapped {a} and {b} and it worked')
          swaps.append(a)
          swaps.append(b)
          break
        else:
          gates[a], gates[b] = gates[b], gates[a]
  return ','.join(sorted(swaps))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(2024, solve(part=0, file='input-test-1'))
  test(49430469426918, solve(part=0, file='input-real'))

  test('fbq,pbv,qff,qnw,qqp,z16,z23,z36', solve(part=1, file='input-real'))
