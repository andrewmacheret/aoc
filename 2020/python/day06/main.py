#!/usr/bin/env python3
from operator import or_, and_
from functools import reduce
from day04.main import load_multiline, test


def solve(customs, op):
    return sum(len(reduce(op, map(set, answers))) for answers in customs)


def part1(filename):
    return solve(load_multiline(filename, __file__), or_)


def part2(filename):
    return solve(load_multiline(filename, __file__), and_)


if __name__ == "__main__":
    test(6, part1('input-test-1.txt'))
    test(11, part1('input-test-2.txt'))
    test(6596, part1('input.txt'))

    test(6, part2('input-test-2.txt'))
    test(3219, part2('input.txt'))
