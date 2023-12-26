include "../common/util";

def accumulate(f; init):
  init, foreach f[] as $row(init; . + ($row | f); . as $x | $row | (f = $x));

def calculate:
  [lines[] | split(" ")[] | try tonumber catch 0] | [accumulate(.; 1)] | to_entries[:240];

def part1: map(select((.key+1) % 40 == 20) | (.key+1) * .value) | add;

def part2:
  group_by(.key/40 | floor)
  | map( map(
      (.key % 40) as $x
      | if $x-1 <= .value and .value <= $x+1 then "#" else "." end
    ) | join("") ) | join("\n")
;

calculate | if $part == 0 then part1 else part2 end
