#!/usr/bin/env python3
from day01.main import load, test
import re
from collections import deque
from operator import add, mul


OPS = {'+': add, '*': mul}


def load_math(filename, script=__file__):
    return [re.split(r' +', re.sub(r'([()])', r' \1 ', line).strip()) for line in load(filename, script=script)]


def evaluate_left_to_right(tokens):
    ops = deque(op for op in tokens if op in OPS)
    nums = deque(int(num) for num in tokens if num not in OPS)
    while len(nums) > 1:
        op = OPS[ops.popleft()]
        nums.appendleft(op(nums.popleft(), nums.popleft()))
    return nums.popleft()


def evaluate_addition_first(tokens):
    tokens = list(tokens)
    for op, fn in OPS.items():
        index = 1
        while True:
            try:
                index = tokens.index(op, index)
                tokens[index-1] = fn(int(tokens[index-1]),
                                     int(tokens[index+1]))
                del tokens[index:index+2]
            except ValueError:
                break
    return tokens[0]


def evaluate(expression, evaluate_tokens):
    expression = ['('] + expression + [')']
    stack = []
    for token in expression:
        if token == ')':
            tokens = deque()
            while stack[-1] != '(':
                tokens.appendleft(stack.pop())
            stack.pop()
            token = evaluate_tokens(tokens)
        stack.append(token)
    return stack[0]


def part1(filename):
    expressions = load_math(filename)
    return sum(evaluate(expression, evaluate_left_to_right) for expression in expressions)


def part2(filename):
    expressions = load_math(filename)
    return sum(evaluate(expression, evaluate_addition_first) for expression in expressions)


if __name__ == "__main__":
    test(71, part1('input-test-1.txt'))
    test(51, part1('input-test-2.txt'))
    test(26, part1('input-test-3.txt'))
    test(437, part1('input-test-4.txt'))
    test(12240, part1('input-test-5.txt'))
    test(13632, part1('input-test-6.txt'))
    test(8298263963837, part1('input.txt'))

    test(231, part2('input-test-1.txt'))
    test(51, part2('input-test-2.txt'))
    test(46, part2('input-test-3.txt'))
    test(1445, part2('input-test-4.txt'))
    test(669060, part2('input-test-5.txt'))
    test(23340, part2('input-test-6.txt'))
    test(145575710203332, part2('input.txt'))
