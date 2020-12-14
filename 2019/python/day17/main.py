#!/usr/bin/env python3
from day01.main import test
from day02.main import load_memory
from day05.main import Program


def part1(filename):
    memory = load_memory(filename, script=__file__)
    prog = Program(memory)
    run = prog.run_computer()

    rows = ''.join(map(chr, run)).split('\n')
    grid = {(x, y): cell for y, row in enumerate(rows)
            for x, cell in enumerate(row)}
    intersections = [(x, y) for x, y in grid if grid[x, y] == grid.get(
        (x+1, y)) == grid.get((x-1, y)) == grid.get((x, y+1)) == grid.get((x, y-1)) == '#']
    return sum(x*y for x, y in intersections)


def parse_input(lines):
    return map(ord, ('{}\n' * len(lines)).format(*lines))


def parse_vararg_input(**args):
    return parse_input(args.values())


def part2(filename):
    memory = load_memory(filename, script=__file__)
    memory[0] = 2
    input = parse_vararg_input(
        main='A,A,B,C,B,C,B,C,C,A',
        A='L,10,R,8,R,8',
        B='L,10,L,12,R,8,R,10',
        C='R,10,L,12,R,10',
        video='n'
    )
    prog = Program(memory, input)
    run = prog.run_computer()
    return list(run)[-1]


if __name__ == "__main__":
    test(6212, part1('input.txt'))
    test(1016741, part2('input.txt'))
