include "common/util";

def inc: map( .[1] - .[0] | 0 < . and . < 4 ) | all;
def dec: map( .[0] - .[1] | 0 < . and . < 4 ) | all;

def part1: [ .[:-1], .[1:] ] | transpose | inc or dec;
def part2: [range(length) as $x | .[:$x] + .[$x+1:] | part1] | any;

lines
  | map(numbers
    | if $part == 0 then part1 else part2 end
    | if . then 1 else 0 end
  ) | add
