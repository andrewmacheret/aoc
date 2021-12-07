
def cost: if $part == 1 then . else . * (. + 1) / 2 end;
def compute($mid): [ .[] | $mid - . | fabs | cost ] | add;
def part1: compute(sort_by(.)[length / 2]);
def part2: [ compute(add / length | floor), compute(add / length | ceil) ] | min;

[ split(",")[] | tonumber ]
  | if $part == 1 then part1 else part2 end
