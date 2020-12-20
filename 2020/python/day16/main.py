#!/usr/bin/env python3
from day04.main import load_multiline, test
import re
# import networkx as nx
# import numpy as np
# from collections import *
# from itertools import *
# from pprint import pprint
# from copy import copy, deepcopy
# from heapq import *
# from operator import *
# from functools import *
from math import prod
# import sys
# import io
# import os
# sys.setrecursionlimit(100000)


def parse_rules(lines):
    rules = {}
    for line in lines:
        key, a, b, c, d = re.match(
            r'^(.*): (\d+)-(\d+) or (\d+)-(\d+)$', line).groups()
        rules[key] = ((int(a), int(b)), (int(c), int(d)))
    return rules


def parse_ticket(line):
    return list(map(int, line.split(',')))


def load_tickets(filename, script=__file__):
    all_lines = load_multiline(filename, script=__file__)
    rules = parse_rules(next(all_lines))
    mine = parse_ticket(next(all_lines)[1])
    nearby = [parse_ticket(line) for line in next(all_lines)[1:]]
    return rules, mine, nearby


def is_ticket_valid(rules, ticket):
    return all(not all(not (a <= number <= b or c <= number <= d) for (a, b), (c, d) in rules.values()) for number in ticket)


def valid_rules(rules, numbers):
    return (key for key, ((a, b), (c, d)) in rules.items() if all((a <= number <= b or c <= number <= d) for number in numbers))


def part1(filename):
    rules, _, nearby = load_tickets(filename)
    return sum(number for ticket in nearby for number in ticket
               if all(not (a <= number <= b or c <= number <= d) for (a, b), (c, d) in rules.values()))


def part2(filename, prefix):
    rules, mine, nearby = load_tickets(filename)
    tickets = [ticket for ticket in nearby if is_ticket_valid(
        rules, ticket)] + [mine]
    n = len(mine)
    possible = {i: set(valid_rules(
        rules, [ticket[i] for ticket in tickets])) for i in range(n)}
    actual = {}
    for _ in range(n):
        i, rule = next((i, next(iter(possible_rules)))
                       for i, possible_rules in possible.items() if len(possible_rules) == 1)
        actual[rule] = i
        del possible[i]
        for i, possible_rules in possible.items():
            possible_rules.discard(rule)
    return prod(mine[number] for key, number in actual.items() if key.startswith(prefix))


if __name__ == "__main__":
    test(71, part1('input-test-1.txt'))
    test(25916, part1('input.txt'))

    test(1716, part2('input-test-2.txt', ''))
    test(2564529489989, part2('input.txt', 'departure'))
