from collections import OrderedDict, namedtuple
import operator

import sys
sys.path.append('../')
from day03.main import bounds

def add_tuples(tuple1, tuple2, op=operator.add):
  return tuple(op(a, b) for a, b in zip(tuple1, tuple2))

def last(iter, default=None):
  for default in iter: pass
  return default

Cart = namedtuple('Cart', ['type', 'dir'])

# right, up, left, down (counter-clockwise)
CART_DIRS = OrderedDict([
  ('>', (+1,  0)),
  ('^', ( 0, -1)),
  ('<', (-1,  0)),
  ('v', ( 0, +1)),
])
DIRS = CART_DIRS.keys()

# TURN_BEHAVIOR[dir][dir] -> new_dir
#   0 -> turn left   (DIR -= 1)
#   1 -> go straight (DIR = DIR)
#   2 -> turn right  (DIR += 1)
LEFT, STRAIGHT, RIGHT = 0, 1, 2
TURN_BEHAVIOR = {k: {d: DIRS[(i + {LEFT: 1, STRAIGHT: 0, RIGHT: 3}[k]) % 4] for i, d in enumerate(DIRS)} for k in xrange(3)}

def turn_cart((type, dir), rail):
  if rail == '+':
    type = TURN_BEHAVIOR[dir][type]
    dir = (dir + 1) % 3
  else:
    type = TURN_BEHAVIOR[({'/':  LEFT, '-':  STRAIGHT, '\\': RIGHT} if type in '<>' else \
                          {'\\': LEFT, '|':  STRAIGHT, '/':  RIGHT})[rail]][type]
  return Cart(type, dir)

def parse_rails(lines):
  rails = {(x,y): c for y, line in enumerate(lines) for x, c in enumerate(line) if c != ' '}
  carts = {(x,y): Cart(c, 0) for (x,y), c in rails.iteritems() if c in CART_DIRS}
  for (x, y), cart in carts.iteritems(): rails[(x, y)] = '-' if cart.type in '<>' else '|'
  return rails, carts

def draw_rails(rails, carts):
  cart_locations = {(x, y): cart.type for (x, y), cart in carts.iteritems()}
  min_x, min_y, max_x, max_y = bounds(rails.keys())
  print('\n'.join(''.join(cart_locations.get((x,y), rails.get((x,y), ' ')) for x in xrange(min_x, max_x+1)) for y in xrange(min_y, max_y+1)))

def cart_crashes(rails, carts, verbose=False):
  if verbose: draw_rails(rails, carts)

  while len(carts) > 1:
    for pos, cart in sorted(carts.iteritems(), key=lambda ((x, y), cart): (y, x)):
      if pos not in carts: continue # can occur as a result of a crash

      del carts[pos]

      pos = add_tuples(pos, CART_DIRS[cart.type])

      if pos in carts: # crash!
        del carts[pos]
        yield pos
      else:
        carts[pos] = turn_cart(cart, rails[pos])
    
  if verbose: draw_rails(rails, carts)
  if carts: yield next(carts.iterkeys()) # last remaining cart

class Day13:
  def __init__(self, verbose=False):
    self.verbose = verbose

  def load(self, filename):
    self.filename = filename
    with open(filename) as f: self.lines = f.read().splitlines()
    self.rails, self.carts = parse_rails(self.lines)
    return self

  def part1(self):
    return next(self.cart_crashes)

  def part2(self):
    return last(self.cart_crashes)

  def solve(self):
    self.cart_crashes = cart_crashes(self.rails, self.carts, self.verbose)

    return [
      {'filename': self.filename},
      {'part1': self.part1()},
      {'part2': self.part2()},
    ]

if __name__== "__main__":
  print(Day13(verbose=True).load('input-test.txt').solve())
  print(Day13(verbose=True).load('input-test2.txt').solve())
  print(Day13().load('input.txt').solve())
