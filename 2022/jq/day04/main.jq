include "../common/util";

def numbers: [match("\\d+"; "g") | .string | tonumber];
def part1: (.[0] <= .[2] and .[3] <= .[1]) or (.[2] <= .[0] and .[1] <= .[3]);
def part2: .[1] >= .[2] and .[3] >= .[0];

lines | map(numbers | if if $part == 1 then part1 else part2 end then 1 else 0 end) | add
