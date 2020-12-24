#!/usr/bin/env python3
from day03.main import load_grid, dirs, size, dimensions, test
from itertools import product
from operator import add


def simulate_step(grid, dirs, counts):
    mins, sizes = dimensions(grid)
    space = max(abs(x) for coord in dirs for x in coord)
    for coord in product(*[range(m-space, s+space) for m, s in zip(mins, sizes)]):
        if sum(tuple(map(add, coord, delta)) in grid for delta in dirs) in counts[coord in grid]:
            yield coord


def simulate(grid, steps, d):
    grid = {(x, y, *([0] * (d - 2))) for (x, y), v in grid.items() if v == '#'}
    for _ in range(steps):
        grid = set(simulate_step(grid, dirs(d), [{3}, {2, 3}]))
    return len(grid)


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
