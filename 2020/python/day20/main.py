#!/usr/bin/env python3
from day04.main import load_multiline, test
from day11.main import draw_grid
import re
from collections import defaultdict
from itertools import product
from math import prod


# counter-clockwise - 0, 90, 180, 270 degrees
DIRS_4 = [(1, 0), (0, -1), (-1, 0), (0, 1)]

SEA_MONSTER = """\
                  # \n\
#    ##    ##    ###
 #  #  #  #  #  #   
"""
SEA_MONSTER_COORDS = {(x, y) for y, row in enumerate(SEA_MONSTER.split('\n'))
                      for x, cell in enumerate(row) if cell == '#'}


def flip_vertical(x):
    return x[::-1]


def rotate_clock(x):
    return list(map(list, zip(*x[::-1])))


def rotate_counter(x):
    return list(map(list, zip(*x)))[::-1]


def parse_2d(rows):
    return [[cell for cell in row] for row in rows]


def draw_2d(grid):
    print('\n'.join(''.join(row) for row in grid))


def load_tiles(filename, script=__file__):
    return {int(re.fullmatch(r'Tile (\d+):', lines[0]).group(1)): parse_2d(lines[1:])
            for lines in load_multiline(filename, script=script)}


def solve(tiles, full):
    g = int(len(tiles) ** 0.5)
    n = len(next(iter(tiles.values())))

    # place tiles in grid

    pieces = defaultdict(dict)
    neighbors = defaultdict(dict)
    deltas = defaultdict(dict)

    def add_to_pieces(id, delta, row):
        pieces[min(tuple(row), tuple(reversed(row)))][id] = delta

    for id, tile in tiles.items():
        add_to_pieces(id, (-1, 0), [tile[i][0] for i in range(n)])
        add_to_pieces(id, (+1, 0), [tile[i][-1] for i in range(n)])
        add_to_pieces(id, (0, -1), [tile[0][i] for i in range(n)])
        add_to_pieces(id, (0, +1), [tile[-1][i] for i in range(n)])

    for ids in pieces.values():
        for id, delta in ids.items():
            neighbor = next((i for i in ids if i != id), None)
            if neighbor:
                neighbors[id][delta] = neighbor
                deltas[id][neighbor] = delta

    borders = {id for id, deltas in neighbors.items() if len(deltas) < 4}
    corners = {id for id, deltas in neighbors.items() if len(deltas) == 2}

    if not full:
        return prod(corners)

    grid = {(0, 0): next(iter(corners))}
    seen = {grid[0, 0]}

    def find_neighbors(node):
        return [next(id for id in ids if id != node) for ids in pieces.values() if len(ids) == 2 and node in ids]

    def find_right_tile(node, prioritize_border=None):
        # prioritize neigbors:
        # 1. haven't seen yet
        # 2. has 2 neighbors we have seen
        # 3. is on the border
        return sorted(find_neighbors(node), key=lambda id: (id in seen, sum(id in seen for id in find_neighbors(id)) < 2, id not in borders))[0]

    for y in range(g):
        for x in range(1, g):
            grid[x, y] = find_right_tile(grid[x-1, y])
            seen.add(grid[x, y])
        if y+1 < g:
            grid[0, y+1] = find_right_tile(grid[0, y])
            seen.add(grid[0, y+1])

    # transform tiles to correct orientation and flip if necessary, and cut off borders

    def transform(tile, flip, rotate):
        if flip == -1:
            tile = flip_vertical(tile)
        for _ in range(rotate):
            tile = rotate_counter(tile)
        return tile

    for x, y in product(range(g), range(g)):
        for flip, rotate in product((1, -1), range(4)):
            if all(DIRS_4[(DIRS_4.index(deltas[grid[x, y]][grid[x+dx, y+dy]])*flip+rotate) % 4] == (dx, dy) for dx, dy in DIRS_4 if (x+dx, y+dy) in grid):
                id = grid[x, y]
                tiles[id] = transform(tiles[id], flip, rotate)
                tiles[id] = [row[1:-1] for row in tiles[id][1:-1]]
                break

    # combine into a single grid

    z = g*(n-2)
    supergrid = [[0]*z for _ in range(z)]
    for x, y in product(range(g), range(g)):
        for x2, y2 in product(range(n-2), range(n-2)):
            supergrid[y*(n-2)+y2][x*(n-2)+x2] = tiles[grid[x, y]][y2][x2]

    # find sea monsters

    for flip, rotate in product((1, -1), range(4)):
        ultragrid = transform(supergrid, flip, rotate)

        monsters = {(x, y) for x, y in product(range(z), range(z))
                    if all(0 <= x+dx < z and 0 <= y+dy < z and ultragrid[y+dy][x+dx] in {'O', '#'}
                           for dx, dy in SEA_MONSTER_COORDS)}
        if monsters:
            for x, y in monsters:
                for dx, dy in SEA_MONSTER_COORDS:
                    ultragrid[y+dy][x+dx] = 'O'
            # draw_2d(ultragrid)

            return sum(cell == '#' for row in ultragrid for cell in row)


def part1(filename):
    tiles = load_tiles(filename)
    return solve(tiles, False)


def part2(filename):
    tiles = load_tiles(filename)
    return solve(tiles, True)


if __name__ == "__main__":
    test(20899048083289, part1('input-test-1.txt'))
    test(111936085519519, part1('input.txt'))

    test(273, part2('input-test-1.txt'), )
    test(1792, part2('input.txt'))  # between 1500 and 2000
