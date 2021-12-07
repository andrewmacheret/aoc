def part1:
  sort_by(.)
  | .[length / 2] as $m
  | [ .[] | $m - . | fabs ] | add
;

def part2:
  (add / length) as $avg
  | ($avg | floor) as $m1
  | ($avg | ceil) as $m2
  | [ 
    ([ .[] | $m1 - . | fabs | . * (. + 1) / 2 ] | add),
    ([ .[] | $m2 - . | fabs | . * (. + 1) / 2 ] | add)
  ] | min
;

[ split(",")[] | tonumber ]
  | if $part == 1 then part1 else part2 end
