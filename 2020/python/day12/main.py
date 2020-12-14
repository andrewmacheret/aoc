#!/usr/bin/env python3
from day01.main import load, test

DIRS = {
    'E': (+1, 0),
    'N': (0, -1),
    'W': (-1, 0),
    'S': (0, +1),
}


def load_dirs(filename, script=__file__):
    return [(line[0], int(line[1:])) for line in load(filename, script=script)]


def navigate(dirs, waypoint_mode, dx, dy):
    x = y = 0
    for dn, amt in dirs:
        if dn in DIRS:
            dx2, dy2 = DIRS[dn]
            if waypoint_mode:
                dx, dy = dx + amt*dx2, dy + amt*dy2
            else:
                x, y = x + amt*dx2, y + amt*dy2
        elif dn == 'L':
            for _ in range(0, amt, 90):
                dx, dy = dy, -dx
        elif dn == 'R':
            for _ in range(0, amt, 90):
                dx, dy = -dy, dx
        elif dn == 'F':
            x, y = x + amt*dx, y + amt*dy
    return abs(x) + abs(y)


def part1(filename):
    dirs = load_dirs(filename)
    return navigate(dirs, False, 1, 0)


def part2(filename):
    dirs = load_dirs(filename)
    return navigate(dirs, True, 10, -1)


if __name__ == "__main__":
    test(25, part1('input-test-1.txt'))
    test(858, part1('input.txt'))

    test(286, part2('input-test-1.txt'))
    test(39140, part2('input.txt'))
