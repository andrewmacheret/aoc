#!/usr/bin/env python3
from day01.main import load, test


def load_csv_ints(filename, script=__file__):
    return [int(token) for line in load(filename, script=script) for token in line.split(',')]


def solve(filename, goal):
    nums = load_csv_ints(filename)
    mem = {x: i for i, x in enumerate(nums[:-1], 1)}
    last = nums[-1]
    for turn in range(len(nums), goal):
        mem[last], last = turn, turn - mem[last] if last in mem else 0
    return last


if __name__ == "__main__":
    test(0, solve('input-test-1.txt', 4))
    test(3, solve('input-test-1.txt', 5))
    test(3, solve('input-test-1.txt', 6))
    test(1, solve('input-test-1.txt', 7))
    test(0, solve('input-test-1.txt', 8))
    test(4, solve('input-test-1.txt', 9))
    test(0, solve('input-test-1.txt', 10))
    test(436, solve('input-test-1.txt', 2020))
    test(206, solve('input.txt', 2020))
    test(955, solve('input.txt', 30000000))
