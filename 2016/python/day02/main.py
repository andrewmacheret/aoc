#!/usr/bin/env python3

from common.util import load, test, change_dir

keypads = {
    1: """\
     
 123 
 456 
 789 
     
""",
    2: """\
       
   1   
  234  
 56789 
  ABC  
   D   
       
""",
}

starts = {
    1: (2, 2),
    2: (1, 3),
}


def solve(part, file):
  data = load(file)
  res = []
  keypad = keypads[part].splitlines()
  x, y = starts[part]
  for line in data:
    for c in line:
      if c == 'U':
        if keypad[y-1][x] != ' ':
          y -= 1
      elif c == 'D':
        if keypad[y+1][x] != ' ':
          y += 1
      elif c == 'L':
        if keypad[y][x-1] != ' ':
          x -= 1
      elif c == 'R':
        if keypad[y][x+1] != ' ':
          x += 1
    res += keypad[y][x],
  return ''.join(res)


if __name__ == "__main__":
  change_dir(__file__)

  test('1985', solve(part=1, file='input-test-1'))
  test('35749', solve(part=1, file='input-real'))

  test('5DB3', solve(part=2, file='input-test-1'))
  test('9365C', solve(part=2, file='input-real'))
