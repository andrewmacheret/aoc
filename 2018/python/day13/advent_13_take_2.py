from copy import copy, deepcopy

CART_DIRS = {
  '>': (1, 0),
  '^': (0, -1),
  '<': (-1, 0),
  'v': (0, 1),
}
CART_TYPES = {v: k for k, v in CART_DIRS.iteritems()}
DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

CART_BEHAVIOR = {
  ('>', '-'):  '>',
  ('>', '/'):  '^',
  ('>', '\\'): 'v',
  ('^', '|'):  '^',
  ('^', '/'):  '>',
  ('^', '\\'): '<',
  ('<', '-'):  '<',
  ('<', '/'):  'v',
  ('<', '\\'): '^',
  ('v', '|'):  'v',
  ('v', '/'):  '<',
  ('v', '\\'): '>',
} # does not include running into another cart or a '+'

def load_grid(filename):
  with open(filename) as fp:
    lines = fp.readlines()
  return [[c for c in line[0:-1]] for line in lines]

def draw(grid, carts):
  grid = deepcopy(grid)
  for cart in carts:
    x, y = cart['location']
    grid[y][x] = cart['cart_type']
  for row in grid:
    print(''.join(row))
  print('')

def solve(grid):
  cart_locations = set()
  carts = []

  for y, row in enumerate(grid):
    for x, cart_type in enumerate(row):
      if cart_type in CART_DIRS:
        carts.append({
          'location': (x, y),
          'cart_type': cart_type,
          'turn_index': 1,
        })
        cart_locations.add((x, y))
        grid[y][x] = '-' if cart_type in '<>' else '|'

  #draw(grid, carts)
  output = []
  while True:
    crash_locations = set()
    for cart in carts:
      x, y = cart['location']
      if (x,y) in crash_locations: continue
      cart_type = cart['cart_type']
      dx, dy = CART_DIRS[cart_type]

      cart_locations.remove((x, y))
      next_location = (x+dx, y+dy)
      next_rail = grid[y+dy][x+dx]
      if next_location in cart_locations:
        #draw(grid, carts)
        crash_locations.add(next_location)
        cart_locations.remove(next_location)
        output.append(str({'crash': next_location}))
      elif next_rail == '+':
        cart['cart_type'] = CART_TYPES[DIRS[(DIRS.index((dx, dy)) + cart['turn_index'] + 4) % 4]]
        cart['turn_index'] = (cart['turn_index'] + 3) % 3 - 1
      else:
        cart['cart_type'] = CART_BEHAVIOR[(cart_type, next_rail)]
      cart['location'] = next_location
      cart_locations.add(next_location)
    carts = sorted([c for c in carts if c['location'] not in crash_locations], key=lambda c: reversed(c['location']))
    for location in crash_locations: cart_locations.remove(location)
    #draw(grid, carts)
    if len(carts) <= 1:
      #draw(grid, carts)
      output.append(str({'last_cart': carts[0]['location']}))
      return '\n'.join(output)



print(solve(load_grid('advent_13_input.txt')))

