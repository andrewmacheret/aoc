OPS = {
  'addr': lambda reg, a, b: reg[a] + reg[b],
  'addi': lambda reg, a, b: reg[a] + b,
  'mulr': lambda reg, a, b: reg[a] * reg[b],
  'muli': lambda reg, a, b: reg[a] * b,
  'banr': lambda reg, a, b: reg[a] & reg[b],
  'bani': lambda reg, a, b: reg[a] & b,
  'borr': lambda reg, a, b: reg[a] | reg[b],
  'bori': lambda reg, a, b: reg[a] | b,
  'setr': lambda reg, a, b: reg[a],
  'seti': lambda reg, a, b: a,
  'gtir': lambda reg, a, b: int(a > reg[b]),
  'gtri': lambda reg, a, b: int(reg[a] > b),
  'gtrr': lambda reg, a, b: int(reg[a] > reg[b]),
  'eqir': lambda reg, a, b: int(a == reg[b]),
  'eqri': lambda reg, a, b: int(reg[a] == b),
  'eqrr': lambda reg, a, b: int(reg[a] == reg[b]),
}

def parse(filename):
  with open(filename) as f:
    lines = [line.rstrip('\n') for line in f]
  ip = int(lines[0].split(' ')[1])
  ops = []
  for line in lines[1:]:
    op_name, a, b, c = line.split(' ')[0:4]
    ops.append((OPS[op_name], int(a), int(b), int(c)))
  return (ip, ops)

def solve((ip, ops), init_reg_0, factor_me_line, factor_me_reg):
  reg = [0 for _ in xrange(6)]
  reg[0] = init_reg_0

  op_count = [0 for op in ops]

  while reg[ip] < len(ops):
    op, a, b, c = ops[reg[ip]]
    op_count[reg[ip]] += 1
    reg[c] = op(reg, a, b)
    reg[ip] += 1
    if reg[ip] == factor_me_line:
      return solve_simplified(reg[factor_me_reg])
  return reg[0]

def solve_simplified(top):
  possible = [i for i in xrange(top) if top % i == 0]
  return sum(B for B in possible for A in possible if A * B == top)

print(solve(parse('advent_19_input_test.txt'), 0, -1, -1))
print(solve(parse('advent_19_input.txt'), 0, 1, 1))
print(solve(parse('advent_19_input.txt'), 1, 1, 1))
