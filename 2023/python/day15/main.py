#!/usr/bin/env python3

from common.util import *

def solve(part, file):
  data = load(file)[0].split(',')

  hash = lambda s: reduce(lambda x,c: ((x + ord(c)) * 17) % 256, s, 0)

  if part == 0:
    return sum(map(hash, data))

  boxes = [{} for _ in range(256)]
  for x in data:
    label, *op = re.split("\\b", x)[1:-1]
    box = boxes[hash(label)]
    if op:
      box[label] = int(op[1])
    elif label in box:
      del box[label]
  return sum(i*j*v for i,b in enumerate(boxes, 1) \
                   for j,v in enumerate(b.values(), 1))


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(1320, solve(part=0, file='input-test-1'))
  test(506869, solve(part=0, file='input-real'))

  test(145, solve(part=1, file='input-test-1'))
  test(271384, solve(part=1, file='input-real'))
