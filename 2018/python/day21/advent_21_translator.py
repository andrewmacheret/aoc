class Solution:
  OP_TRANS = {
    'addr': 'r[{a}] + r[{b}]',
    'addi': 'r[{a}] + {b}',
    'mulr': 'r[{a}] * r[{b}]',
    'muli': 'r[{a}] * {b}',
    'banr': 'r[{a}] & r[{b}]',
    'bani': 'r[{a}] & {b}',
    'borr': 'r[{a}] | r[{b}]',
    'bori': 'r[{a}] | {b}',
    'setr': 'r[{a}]',
    'seti': '{a}',
    'gtir': 'int({a} > r[{b}])',
    'gtri': 'int(r[{a}] > {b})',
    'gtrr': 'int(r[{a}] > r[{b}])',
    'eqir': 'int({a} == r[{b}])',
    'eqri': 'int(r[{a}] == {b})',
    'eqrr': 'int(r[{a}] == r[{b}])',
  }

  def load(self, filename):
    with open(filename) as f:
      lines = [line.rstrip('\n') for line in f]
    self.ip = int(lines[0].split(' ')[1])
    self.ops = []
    for line in lines[1:]:
      op_name, a, b, c = line.split(' ')[0:4]
      self.ops.append((op_name, int(a), int(b), int(c)))
    return self

  def pprint(self):
    for i, (op_name, a, b, c) in enumerate(self.ops):
      starter = str(i) + ':\t'
      operation = self.OP_TRANS[op_name].format(a=a, b=b)
      if c != self.ip:
        line = starter + 'r[{c}] = '.format(c=c) + operation
      else:
        line = starter + 'goto ' + operation + ' + 1'
      print(line)
  
Solution().load('advent_21_input.txt').pprint()
