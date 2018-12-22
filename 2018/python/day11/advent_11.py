

def power_level(serial, x, y):
  return ((((x + 10) * y + serial) * (x + 10)) / 100) % 10 - 5


def rack(serial, width=300, height=300):
  return [[power_level(serial, x, y) for x in xrange(1, width+1)] for y in xrange(1, height+1)]

def draw_part(rack, x, y, width=5, height=5):
  print('\n'.join(''.join('{0:4d}'.format(power_level) for power_level in r[(x-1):(x-1+width)]) for r in rack[(y-1):(y-1+height)]))

def find_best(rack, w=3, h=3):
  height = len(rack)
  width = len(rack[0]) if rack else 0
  best_total = -1000
  best_x, best_y = 0, 0

  for y in xrange(height-h):
    for x in xrange(width-w):
      total = 0
      for dy in xrange(h):
        for dx in xrange(w):
          total += rack[y+dy][x+dx]
      if best_total < total:
        best_total, best_x, best_y = total, x, y
  #draw_part(rack, best_x, best_y, 5, 5)
  return (best_x+1, best_y+1)


print(4, power_level(8, 3, 5))
print(-5, power_level(57, 122, 79))
print(0, power_level(39, 217, 196))
print(4, power_level(71, 101, 153))

print('')
draw_part(rack(18), 32, 44)
print('')
draw_part(rack(42), 20, 60)

print('')
print((33, 45), find_best(rack(18)))

print('')
print((21, 61), find_best(rack(42)))

print(find_best(rack(6878)))
