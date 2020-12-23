#!/usr/bin/env python3
from day01.main import load, test
from collections import deque
from itertools import islice
from math import prod


class Node:
    def __init__(self, val):
        self.val = val


def load_digits(filename, script=__file__):
    return [int(digit) for line in load(filename, script=script) for digit in line]


def cup_game(numbers, moves):
    cups = [Node(i) for i in numbers]
    for a, b in zip(cups, cups[1:] + [cups[0]]):
        a.right = b
    lookup = {cup.val: cup for cup in cups}

    cup = cups[0]
    n = len(numbers)
    def decrement(x): return ((x - 2) % n) + 1
    for _ in range(moves):
        val = decrement(cup.val)
        cup.right = (c := (b := (a := cup.right).right).right).right
        while val in {a.val, b.val, c.val}:
            val = decrement(val)
        dest = lookup[val]
        dest.right, c.right, cup = a, dest.right, cup.right

    cup = lookup[1]
    while (cup := cup.right):
        yield cup.val


def part1(filename, moves):
    digits = load_digits(filename)
    return int(''.join(map(str, islice(cup_game(digits, moves), len(digits) - 1))))


def part2(filename, moves):
    digits = load_digits(filename) + list(range(10, 1000001))
    return prod(islice(cup_game(digits, moves), 2))


if __name__ == "__main__":
    test(92658374, part1('input-test-1.txt', 10))
    test(67384529, part1('input-test-1.txt', 100))
    test(49725386, part1('input.txt', 100))

    test(149245887792, part2('input-test-1.txt', 10000000))
    test(538935646702, part2('input.txt', 10000000))
