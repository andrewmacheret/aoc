include "../common/util";

def last_visible($grid; $n; $x; $y; $dx; $dy):
  try (
    reduce range(1; $n+1) as $d (0;
      ($x + $dx * $d) as $x1 | ($y + $dy * $d) as $y1
      | if 0 <= $x1 and $x1 < $n and 0 <= $y1 and $y1 < $n then . else error(. * 2 + 1) end
      | . + 1
      | if $grid[$y1][$x1] >= $grid[$y][$x] then error(. * 2) else . end
    )
  ) catch (.);

def visibles:
  lines | map(split("") | map(tonumber)) as $grid
    | ($grid | length) as $n
    | [
      range($n) as $y | range($n) as $x
      | [([1, 0], [-1, 0], [0, 1], [0, -1])]
      | map(last_visible($grid; $n; $x; $y; .[0]; .[1]))
    ];

def part1: map(map(select(. % 2 == 1)) | select(length > 0)) | length;

def part2: map(map(. / 2 | floor) | mul) | max;

visibles | if $part == 1 then part1 else part2 end
