#!/usr/bin/env python3
from day01.main import load, test


def load_instructions(filename, script=__file__):
    for line in load(filename, script=script):
        op, amt = line.split(' ')
        yield [op, int(amt)]


def run_prog(prog):
    acc = idx = 0
    seen = set()
    while idx not in seen:
        if idx >= len(prog):
            break
        seen.add(idx)
        op, amt = prog[idx]
        if op == 'acc':
            acc += amt
        elif op == 'jmp':
            idx += amt - 1
        idx += 1
    return idx, acc


def part1(filename):
    prog = list(load_instructions(filename))
    return run_prog(prog)[1]


def part2(filename):
    prog = list(load_instructions(filename))
    n = len(prog)
    for i in range(n):
        if prog[i][0] != 'acc':
            prog[i][0], temp = 'op' if prog[i][0] == 'jmp' else 'op', prog[i][0]
            idx, acc = run_prog(prog)
            if idx == n:
                return acc
            prog[i][0] = temp


if __name__ == "__main__":
    test(5, part1('input-test-1.txt'))
    test(1939, part1('input.txt'))

    test(8, part2('input-test-1.txt'))
    test(2212, part2('input.txt'))
