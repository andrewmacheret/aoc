#!/usr/bin/env python3
from day01.main import load, test
from day17.main import simulate_step
from collections import defaultdict

COMPASS = {
    'e':  (+2,  0),
    'w':  (-2,  0),
    'nw': (-1, -1),
    'ne': (+1, -1),
    'sw': (-1, +1),
    'se': (+1, +1),
}


def parse_path(line):
    return [a+b if a in 'ns' else b for a, b in zip(' ' + line, line + ' ') if b in 'we']


def load_paths(filename, script=__file__):
    return [parse_path(line) for line in load(filename, script=script)]


def setup_tiles(paths):
    tiles = defaultdict(lambda: -1)
    for path in paths:
        tiles[tuple(map(sum, zip(*(COMPASS[step] for step in path))))] *= -1
    return {a for a, b in tiles.items() if b == 1}


def simulate(paths, steps):
    tiles = setup_tiles(paths)
    for _ in range(steps):
        tiles = set(simulate_step(tiles, COMPASS.values(), [{2}, {1, 2}]))
    return len(tiles)


def part1(filename):
    return simulate(load_paths(filename), 0)


def part2(filename):
    return simulate(load_paths(filename), 100)


if __name__ == "__main__":
    test(10, part1('input-test-1.txt'))
    test(473, part1('input.txt'))

    test(2208, part2('input-test-1.txt'))
    test(4070, part2('input.txt'))
