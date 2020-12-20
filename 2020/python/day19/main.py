#!/usr/bin/env python3
from day04.main import load_multiline, test
import re
from functools import cache


def build_matcher(rules):
    d = {}
    for rule in rules:
        index, subrule = rule.split(': ', 1)
        index = int(index)
        if (m := re.fullmatch(r'"(\w+)"', subrule)):
            d[index] = m.group(1)
        else:
            d[index] = []
            for part in subrule.split(' '):
                if part not in {'|', '+'}:
                    part = int(part)
                d[index].append(part)

    @cache
    def build(index):
        if type(d[index]) is str:
            return d[index]
        return '(' + ''.join(build(x) if type(x) is int else x for x in d[index]) + ')'

    pattern = re.compile(build(0))

    return lambda t: bool(re.fullmatch(pattern, t))


def load_rules(filename, script=__file__):
    rules, tests = list(load_multiline(filename, script))
    return rules, tests


def part1(filename):
    rules, tests = load_rules(filename)
    matcher = build_matcher(rules)
    return sum(matcher(t) for t in tests)


def part2(filename):
    rules, tests = load_rules(filename)

    rules.append('8: 42 +')

    # 11: 42 31 | 42 42 31 31 | 42 42 42 31 31 31 | ...
    # 42x5 and 31x5  (repeats=5) would probably be enough,
    # but half of the length of the largest string should be definitive
    repeats = max(map(len, tests)) // 2
    rules.append(
        '11: ' + ' | '.join(' '.join(['42'] * i + ['31'] * i) for i in range(1, 1 + repeats)))

    matcher = build_matcher(rules)
    return sum(matcher(t) for t in tests)


if __name__ == "__main__":
    test(2, part1('input-test-1.txt'))
    test(2, part1('input-test-2.txt'))
    test(3, part1('input-test-3.txt'))
    test(144, part1('input.txt'))

    test(12, part2('input-test-3.txt'))
    test(260, part2('input.txt'))
