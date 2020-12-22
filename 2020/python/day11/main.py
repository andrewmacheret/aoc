#!/usr/bin/env python3
from day03.main import load_grid, dirs, size, test
from collections import defaultdict


def draw_grid(grid):
    width, height = size(grid)
    for y in range(height):
        print(''.join(grid.get((x, y), '.') for x in range(width)))


def simulate_step(grid, seat_map, fill_req):
    result = {}
    for x, y in seat_map:
        seat = grid[x, y]
        count = sum(grid[x2, y2] == '#' for x2, y2 in seat_map[x, y])
        result[x, y] = 'L' if count > ((seat == '#') * fill_req) else '#'
    return result


def get_adjacent(grid):
    seats = defaultdict(list)
    for (x, y), seat in grid.items():
        if seat != '.':
            for dx, dy in dirs(2):
                x2, y2 = x+dx, y+dy
                if (x2, y2) in grid and grid[x2, y2] != '.':
                    seats[x, y].append((x2, y2))
    return seats


def get_line_of_sight(grid):
    seats = defaultdict(list)
    for (x, y), seat in grid.items():
        if seat != '.':
            for dx, dy in dirs(2):
                x2, y2 = x+dx, y+dy
                while (x2, y2) in grid:
                    if grid[x2, y2] != '.':
                        seats[x, y].append((x2, y2))
                        break
                    x2, y2 = x2+dx, y2+dy
    return seats


def solve(grid, seats, fill_req):
    last_grid = None
    while grid != last_grid:
        last_grid, grid = grid, simulate_step(grid, seats, fill_req)

    return sum(seat == '#' for seat in grid.values())


def part1(filename):
    grid = load_grid(filename, script=__file__)
    seats = get_adjacent(grid)
    return solve(grid, seats, 3)


def part2(filename):
    grid = load_grid(filename, script=__file__)
    seats = get_line_of_sight(grid)
    return solve(grid, seats, 4)


if __name__ == "__main__":
    test(37, part1('input-test-1.txt'))
    test(2346, part1('input.txt'))

    test(26, part2('input-test-1.txt'))
    test(2111, part2('input.txt'))
