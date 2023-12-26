include "../common/util";

def lines: split("\n")[:-1];
def ord: {"A":0, "B":1, "C":2, "X":0, "Y":1, "Z":2}[.];
def part1: .[1] * 1 + (.[1] - (.[0] - 1) + 3) % 3 * 3 + 1;
def part2: .[1] * 3 + (.[1] + (.[0] - 1) + 3) % 3 * 1 + 1;

lines | map(split(" ") | map(ord) | if $part == 1 then part1 else part2 end) | add
