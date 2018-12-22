

def solve_simplified(top):
  res = 0
  possible = [i for i in xrange(1, top+1) if top % i == 0]
  for B in possible:
    for A in possible:
      if A * B == top:
        res += B
  return res

print(solve_simplified(10551383))
