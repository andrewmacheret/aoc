#!/usr/bin/env python3
from day03.main import load_grid, dirs, size, dimensions, test
from itertools import product
from operator import add


def fast_sum(grid, coord):
    total = 0
    for delta in dirs(len(coord)):
        if grid.get(tuple(map(add, coord, delta))) == '#':
            total += 1
            if total > 3:
                break
    return total


def simulate_step(grid):
    mins, sizes = dimensions(grid)
    res = {}
    for coord in product(*[range(m-1, s+1) for m, s in zip(mins, sizes)]):
        count = sum(grid.get(tuple(map(add, coord, delta))) == '#'
                    for delta in dirs(len(coord)))
        if count in ({2, 3} if grid.get(coord) == '#' else {3}):
            res[coord] = '#'
    return res


def simulate(grid, steps, num_dimensions):
    grid = {(x, y, *([0] * (num_dimensions - 2))): value for (x, y), value in grid.items() if value == '#'}
    for _ in range(steps):
        grid = simulate_step(grid)
    return len(grid.values())


def part1(filename):
    grid = load_grid(filename, script=__file__)
    return simulate(grid, 6, 3)


def part2(filename):
    grid = load_grid(filename, script=__file__)
    return simulate(grid, 6, 4)


if __name__ == "__main__":
    test(112, part1('input-test-1.txt'))
    test(384, part1('input.txt'))

    test(848, part2('input-test-1.txt'))
    test(2012, part2('input.txt'))
