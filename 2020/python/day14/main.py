#!/usr/bin/env python3
from day01.main import load, test
import re

FULL_MASK = int('0b' + ('1' * 36), 2)


def load_instructions(filename, script=__file__):
    for line in load(filename, script=script):
        left, right = line.split(' = ')
        if left == 'mask':
            yield 'mask', right
        else:
            yield int(re.match(r'^mem\[(\d+)\]$', left).group(1)), int(right)


def floaty_values(mask, value):
    values = [value]
    for bit in [1 << i for i in range(36) if mask[-i-1] == 'X']:
        values = [b for a in values for b in (a | bit, a & (FULL_MASK ^ bit))]
    return values


def apply_floaty_mask(memory, mask, left, right):
    for i in range(36):
        ch = mask[-i-1]
        if ch == '1':
            left |= 1 << i

    for floaty in floaty_values(mask, left):
        memory[floaty] = right


def apply_mask(memory, mask, left, right):
    for i in range(36):
        ch = mask[-i-1]
        if ch == '1':
            right |= 1 << i
        elif ch == '0':
            right &= FULL_MASK ^ (1 << i)
    memory[left] = right


def sum_memory(instructions, apply_mask, initial_mask):
    mask = initial_mask
    memory = {}
    for left, right in instructions:
        if left == 'mask':
            mask = right
        else:
            apply_mask(memory, mask, left, right)
    return sum(memory.values())


def part1(filename):
    instructions = load_instructions(filename)
    return sum_memory(instructions, apply_mask, '0' * 36)


def part2(filename):
    instructions = load_instructions(filename)
    return sum_memory(instructions, apply_floaty_mask, 'X' * 36)


if __name__ == "__main__":
    test(165, part1('input-test-1.txt'))
    test(5875750429995, part1('input.txt'))

    test(208, part2('input-test-2.txt'))
    test(5272149590143, part2('input.txt'))
