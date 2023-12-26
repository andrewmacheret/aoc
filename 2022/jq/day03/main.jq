include "../common/util";

def nonunique($y): reduce .[] as $x ({}; .[$x] += 1) | to_entries | map(select(.value > $y) | .key)[];

def priortiy: . as $i | "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" | index($i);
def part1: map([.[:length/2], .[length/2:]] | map(split("") | unique | join("") ) | add | split("") | nonunique(1));
def part2: to_entries | group_by(.key/3 | floor) | map(map(.value | split("") | unique | join("")) | add | split("") | nonunique(2));

lines | if $part == 1 then part1 else part2 end | map(priortiy) | add


# def part1(data):
#   return (set(line[:len(line)//2]) & set(line[len(line)//2:]) for line in data)


# def part2(data):
#   return (reduce(and_, map(set, lines)) for lines in zip(*[iter(data)]*3))


# def priority(s):
#   return sum(ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27 for c in s)


# def solve(part, file):
#   return sum(map(priority, [part1, part2][part](load(file))))
