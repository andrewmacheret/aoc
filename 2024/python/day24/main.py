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


@cache
def expected_add(i):
  if i == 0:
    return f'(x00 XOR y00)'
  elif i == 1:
    return f'((x00 AND y00) XOR (x01 XOR y01))'
  else:
    # using the last expected value
    # replace second to last XOR with AND
    last = expected_add(i-1)
    j = last.rfind('XOR', 0, last.rfind('XOR')-1)
    carry = last[:j] + 'AND' + last[j+3:]
    return f'(({carry} OR (x{i-1:02d} AND y{i-1:02d})) XOR (x{i:02d} XOR y{i:02d}))'

def expected_and(i):
  return f'(x{i:02d} AND y{i:02d})'

def solve(file, expected_op=None):
  data = load_blocks(file)
  mem = defaultdict()
  for line in data[0]:
    addr, val = line.split(': ')
    mem[addr] = int(val)
  
  gates = {}
  for line in data[1]:
    a, op, b, _, c = line.split(' ')
    gates[c] = (op, a, b)

  if not expected_op:
    return run(mem, gates)

  def build_actual(c):
    if c in gates:
      op,a,b = gates[c]
      a,b = sorted([build_actual(a), build_actual(b)])
      return f'({a} {op} {b})'
    return c

  def build_actual_safe(c):
    try:
      return build_actual(c)
    except:
      return "broken"

  def check(end):
    return all(build_actual_safe(f"z{i:02d}") == expected_op(i) for i in range(end))

  max_z = max(int(k[1:]) for k in gates if k[0] == 'z')
  print(f'Max z: {max_z}')
  swaps = []
  for r in range(1,max_z+1):
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

  test(2024, solve(file='input-test-1'))
  test(49430469426918, solve(file='input-real'))

  test('z00,z01,z02,z05', solve(expected_op=expected_and, file='input-test-2'))
  test('fbq,pbv,qff,qnw,qqp,z16,z23,z36', solve(expected_op=expected_add, file='input-real'))
