#!/usr/bin/env python3
from day01.main import load_ints, test
from collections import Counter
from itertools import groupby
from math import prod
from functools import cache


def get_diffs(nums):
    return (b - a for a, b in zip([0] + nums, nums + [nums[-1] + 3]))


def part1(filename):
    nums = sorted(load_ints(filename, script=__file__))
    return prod(Counter(get_diffs(nums)).values())


@cache
def fib(n, order):
    return sum(fib(n-i, order) for i in range(1, order+1)) if n > 0 else n == 0


def part2(filename):
    nums = sorted(load_ints(filename, script=__file__))
    return prod(diff == 3 or fib(len(list(parts)), 3) for diff, parts in groupby(get_diffs(nums)))


if __name__ == "__main__":
    test(35, part1('input-test-1.txt'))
    test(220, part1('input-test-2.txt'))
    test(1656, part1('input.txt'))

    test(8, part2('input-test-1.txt'))
    test(19208, part2('input-test-2.txt'))
    test(56693912375296, part2('input.txt'))
