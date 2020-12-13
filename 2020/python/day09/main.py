#!/usr/bin/env python3
from day01.main import load_ints, test
from collections import deque
from itertools import combinations


def find_key(nums, size):
    window = deque()
    for num in nums:
        if len(window) == size:
            if all(a + b != num for a, b in combinations(window, 2)):
                return num
            window.popleft()
        window.append(num)


def part1(filename, size):
    nums = load_ints(filename, script=__file__)
    return find_key(nums, size)


def part2(filename, size):
    nums = list(load_ints(filename, script=__file__))
    key = find_key(nums, size)
    window = deque()
    window_sum = 0
    for num in nums:
        if window_sum < key:
            window.append(num)
            window_sum += num
        while window_sum > key:
            window_sum -= window.popleft()
        if window_sum == key:
            return max(window) + min(window)


if __name__ == "__main__":
    test(127, part1('input-test-1.txt', 5))
    test(14144619, part1('input.txt', 25))

    test(62, part2('input-test-1.txt', 5))
    test(1766397, part2('input.txt', 25))
