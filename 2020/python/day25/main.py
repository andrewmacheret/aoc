#!/usr/bin/env python3
from day01.main import load_ints, test
from itertools import count, repeat, islice, accumulate
from functools import reduce


def mul(x, y): return (x * y) % 20201227


def transform(size, subject):
    return reduce(mul, repeat(subject, size))


def find_size(key, subject=7):
    return next(i for i, x in enumerate(
        accumulate(repeat(subject), mul), 1) if x == key)


def solve(filename):
    key1, key2 = load_ints(filename, script=__file__)
    return transform(find_size(key1), key2)


if __name__ == "__main__":
    test(14897079, solve('input-test-1.txt'))
    test(4441893, solve('input.txt'))
