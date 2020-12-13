#!/usr/bin/env python3
from day02.main import load_regex, test
from collections import defaultdict
from functools import cache
import re


def load_bags_dict(filename, script=__file__):
    bags = defaultdict(dict)
    for container, contained in load_regex(filename, r'^(.*) bags contain (.*)\.$', script=script):
        for parts in contained.split(', '):
            count, item = re.match(r'^(\d+) (.*) bags?$', parts).groups()
            bags[container][item] = int(count)
    return bags


def load_bags(filename, script=__file__):
    for container, contained in load_regex(filename, r'^(.*) bags contain (.*)\.$', script=script):
        for parts in contained.split(', '):
            if parts != 'no other bags':
                count, item = re.match(r'^(\d+) (.*) bags?$', parts).groups()
                yield container, item, int(count)
            else:
                yield container, None, 0


def part1(filename):
    graph = defaultdict(list)
    for container, item, _ in load_bags(filename):
        graph[item].append(container)

    q = ['shiny gold']
    containers = set()
    while q:
        q = [y for x in q for y in graph[x]]
        for x in q:
            containers.add(x)
    return len(containers)


def part2(filename):
    graph = defaultdict(dict)
    for container, item, count in load_bags(filename):
        graph[container][item] = count

    @cache
    def count_bags(container):
        return 1 + sum(count_bags(item) * count for item, count in graph[container].items())

    return count_bags('shiny gold') - 1


if __name__ == "__main__":
    test(4, part1('input-test-1.txt'))
    test(265, part1('input.txt'))

    test(32, part2('input-test-1.txt'))
    test(126, part2('input-test-2.txt'))
    test(14177, part2('input.txt'))
