#!/usr/bin/env python3
from math import prod

from day01.main import load, test


def load_grid(filename, script=__file__):
    rows = [line for line in load(filename, script=script)]
    return {(x, y): cell for y, row in enumerate(rows) for x, cell in enumerate(row)}


def size(grid, fn=lambda A: max(A)+1):
    return fn(x for x, y in grid), fn(y for x, y in grid)


def dimensions(grid):
    return *size(grid, min), *size(grid)


def count_trees_on_slope(grid, right, down):
    width, height = size(grid)
    trees = x = 0
    for y in range(down, height, down):
        x = (x + right) % width
        trees += grid[x, y] == '#'
    return trees


def part1(filename, right, down):
    grid = load_grid(filename)
    return count_trees_on_slope(grid, right, down)


def part2(filename):
    grid = load_grid(filename)
    return prod(count_trees_on_slope(grid, right, down) for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])


if __name__ == "__main__":
    test(7, part1('input-test-1.txt', 3, 1))
    test(254, part1('input.txt', 3, 1))

    test(336, part2('input-test-1.txt'))
    test(1666768320, part2('input.txt'))  # too low
