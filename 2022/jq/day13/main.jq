include "../common/util";

def sign: (if . > 0 then 1 else 0 end) - (if . < 0 then 1 else 0 end);

def cmp:
  (.[0] | type == "array") as $a1 | (.[1] | type == "array") as $a2
  | if $a1 and $a2 then
      [-1, (map(length) | cmp), 1][(first(transpose[] | select(index(null) | not) | cmp | select(. != 0)) // 0) + 1]
    elif $a1 then
      .[1] = [.[1]] | cmp
    elif $a2 then
      .[0] = [.[0]] | cmp
    else
      (.[0] - .[1]) | sign
    end
;

def part1: map(cmp) | to_entries | map(select(.value < 1) | .key + 1) | add;
def divider($val): map([., $val] | cmp | select(. == -1)) | add;
def part2: map(.[]) | (1 - divider(2)) * (2 - divider(6));

line_blocks | map(map(fromjson)) | if $part == 0 then part1 else part2 end
