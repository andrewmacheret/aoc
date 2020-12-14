#!/usr/bin/env python3
from day01.main import load, test
from itertools import count


def load_schedule(filename, script=__file__):
    lines = load(filename, script=script)
    return int(lines[0]), lines[1].split(',')


def part1(filename):
    start, ids = load_schedule(filename)
    ids = sorted(int(id) for id in ids if id != 'x')
    return next((t - start) * id for t in count(start) for id in ids if t % id == 0)


def part2(filename):
    ids = [(i, int(id))
           for i, id in enumerate(load_schedule(filename)[1]) if id != 'x']

    t, step = 0, 1
    for i, id in ids:
        while (t+i) % id != 0:
            t += step
        step *= id
    return t


if __name__ == "__main__":
    test(295, part1('input-test-1.txt'))
    test(6559, part1('input.txt'))

    test(3417, part2('input-test-2.txt'))
    test(754018, part2('input-test-3.txt'))
    test(779210, part2('input-test-4.txt'))
    test(1261476, part2('input-test-5.txt'))
    test(1202161486, part2('input-test-6.txt'))

    test(1068781, part2('input-test-1.txt'))
    test(626670513163231, part2('input.txt'))
