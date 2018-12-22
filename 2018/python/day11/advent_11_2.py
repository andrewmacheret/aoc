"""
--- Part Two ---
You discover a dial on the side of the device; it seems to let you select a square of any size, not just 3x3. Sizes from 1x1 to 300x300 are supported.

Realizing this, you now must find the square of any size with the largest total power. Identify this square by including its size as a third parameter after the top-left coordinate: a 9x9 square with a top-left corner of 3,5 is identified as 3,5,9.

For example:

For grid serial number 18, the largest total square (with a total power of 113) is 16x16 and has a top-left corner of 90,269, so its identifier is 90,269,16.
For grid serial number 42, the largest total square (with a total power of 119) is 12x12 and has a top-left corner of 232,251, so its identifier is 232,251,12.



   A   B   C
   D   E   F
   G   H   I


   ABDE  BCEF   x
   DEGH  EFHI   x
   x     x      x


  -3   4   2   2   2
  -4   4   3   3   4
  -5   3   3   4  -4
   4   3   3   4  -3
   3   3   3  -5  -1


   1  13  10  11   x
  -2  13  13   7   x
   5  12  14   1   x
  13  12   5  -5   x
   x   x   x   x   x

   1  13  10  11   x
  -2  13  13   7   x
   5  12  14   1   x
  13  12   5  -5   x
   x   x   x   x   x



"""

def power_level(serial, x, y):
  return ((((x + 10) * y + serial) * (x + 10)) / 100) % 10 - 5


def rack(serial, width=300, height=300):
  return [[power_level(serial, x, y) for x in xrange(1, width+1)] for y in xrange(1, height+1)]

def draw_part(rack, x, y, width=5, height=5):
  print('\n'.join(''.join('{0:4d}'.format(power_level) for power_level in r[(x-1):(x-1+width)]) for r in rack[(y-1):(y-1+height)]))

def find_best(rack):
  n = len(rack)
  best_total = 0
  best_x, best_y, best_w = 0, 0, 0

  sum_grid = [[0 for i in xrange(n+1)] for i in xrange(n+1)]

  for y in xrange(1, n+1):
    for x in xrange(1, n+1):
      sum_grid[y][x] = rack[y-1][x-1] + sum_grid[y-1][x] + sum_grid[y][x-1] - sum_grid[y-1][x-1]

  #print('\n'.join(''.join('{0:5d}'.format(cell) for cell in row) for row in sum_grid))
  #print('')

  for w in xrange(1, n+1):
    for y in xrange(n-w+1):
      for x in xrange(n-w+1):
        total = sum_grid[y+w][x+w] - sum_grid[y+w][x] - sum_grid[y][x+w] + sum_grid[y][x]
        if best_total < total:
          best_total, best_x, best_y, best_w = total, x, y, w
  
  return (best_x+1, best_y+1, best_w)


"""
print(4, power_level(8, 3, 5))
print(-5, power_level(57, 122, 79))
print(0, power_level(39, 217, 196))
print(4, power_level(71, 101, 153))

print('')
draw_part(rack(18), 32, 44)
print('')
draw_part(rack(42), 20, 60)
"""

print(find_best([
  [2, 48, 28, 24],
  [32, 9, 48, 29],
  [24, 38, 2, 12],
  [49, 3, 6, 4],
]))

print(find_best([
  [-1, -1, -1, -1],
  [-1,  1,  2,  -1],
  [-1,  3,  4,  -1],
  [-1, -1, -1, -1],
]))

"""
print('')
print((33, 45), find_best(rack(18)))

print('')
print((21, 61), find_best(rack(42)))
"""

print(find_best(rack(18)))
print(find_best(rack(42)))

print(find_best(rack(6878)))
