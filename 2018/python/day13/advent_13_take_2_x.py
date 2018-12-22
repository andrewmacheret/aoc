from itertools import cycle

with open('advent_13_input.txt') as fp:
    lines = fp.readlines()

m = {}; carts = {}; dir_d = {'<': -1, '>': 1, '^': 1j, 'v': -1j}
for i, row in enumerate(lines):
    for j, c in enumerate(row[0:len(row)-1]):
        loc = j-i*1j
        if c in r'/\+':
            m[loc] = c
        elif c in dir_d:
            carts[loc] = dir_d[c], cycle([1j, 1, -1j])

while len(carts) > 1:
    for loc in sorted(carts, key=lambda x: (-x.imag, x.real)):
        if loc not in carts:
            continue  # deleted due to collision
        dxn, turn = carts.pop(loc)  # take out cart
        loc += dxn  # update position

        if loc in carts:  # handle collision
            print('collision!', loc, '(cart', loc - dxn)
            del carts[loc]
            continue

        track = m.get(loc)  # update direction
        if track == '+':
            dxn = dxn * next(turn)
        elif track is not None: #/ or \
            dxn *= 1j * (2*((track == '/') ^ (dxn.real == 0))-1)
            
        carts[loc] = dxn, turn  # put cart back onto tracks

print(carts)