#!/usr/bin/env python3

from z3 import Solver, Int, Real  # pip install z3-solver


from common.util import *


def intersection(coord1, coord2):
    x1,y1,_,dx1,dy1,_ = coord1
    x3,y3,_,dx3,dy3,_ = coord2
    # get a second point for coord1
    x2 = x1 + dx1
    y2 = y1 + dy1
    # get a second point for coord2
    x4 = x3 + dx3
    y4 = y3 + dy3

    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
    if ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)) == 0:
      return None
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3*y4 - y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3*y4 - y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    
    # make sure point 1 is going forward
    t1 = 0
    if dx1 != 0:
      t1 = (px - x1)/dx1
    else: # dy1 != 0
      t1 = (py - y1)/dy1
    if t1 <= 0:
      return None
    
    # make sure point 2 is going forward
    t2 = 0
    if dx3 != 0:
      t2 = (px - x3)/dx3
    else: # dy3 != 0
      t2 = (py - y3)/dy3
    if t2 <= 0:
      return None
    
    return px, py

# too slow for real input :(
def intersection2(coord1, coord2):
  x1,y1,_,dx1,dy1,_ = coord1
  x2,y2,_,dx2,dy2,_ = coord2

  # find intersecting x and y for the two lines
  # they could intersect at different times
  equations = Solver()
  x, y, t1, t2 = map(Real, ('x', 'y', 't1', 't2'))
  equations.add(x == x1 + t1*dx1)
  equations.add(y == y1 + t1*dy1)
  equations.add(x == x2 + t2*dx2)
  equations.add(y == y2 + t2*dy2)
  equations.check()
  
  # if the model is invalid, it will fail here
  try:
    model = equations.model()
  except:
    return None
  
  # get the values for x,y,t1,t2
  x,y,t1,t2 = (eval(str(model[var])) for var in (x,y,t1,t2))
  # make sure the times are positive
  if t1 <= 0 or t2 <= 0:
    return None
  
  # we got it!!!!!1111!@#!@#
  return x,y
  


def solve(part, file, lo=None, hi=None):
  coords = list(map(parse_nums, load(file)))

  if part == 0:  
    res = 0
    for a,b in combinations(coords,2):
      if point := intersection(a, b):
        if all(lo <= p <= hi for p in point):
          res += 1
    return res
  else:
    equations = Solver()
    x, y, z, dx, dy, dz = map(Int, ('x', 'y', 'z', 'dx', 'dy', 'dz'))
    for i,(x1,y1,z1,dx1,dy1,dz1) in enumerate(coords[:3]): # just need 3 of them
      t = Int(f't{i}') # different t for every coord
      # main line equation should match the coord's equation for each x,y,z
      equations.add(x + t*dx == x1 + t*dx1)
      equations.add(y + t*dy == y1 + t*dy1)
      equations.add(z + t*dz == z1 + t*dz1)
    equations.check()
    model = equations.model()
    x,y,z = (model[var].as_long() for var in (x,y,z))
    # print(x,y,z)
    return x + y + z


### THE REST IS TESTS ###

if __name__ == "__main__":
  change_dir(__file__)

  test(2, solve(part=0, file='input-test-1', lo=7, hi=27))
  test(18651, solve(part=0, file='input-real', lo=200000000000000, hi=400000000000000))

  test(47, solve(part=1, file='input-test-1'))
  test(546494494317645, solve(part=1, file='input-real'))
