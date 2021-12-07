def parse: split("\n")[0:-1];

def sign: (if . > 0 then 1 else 0 end) - (if . < 0 then 1 else 0 end);
def abs: (if . >= 0 then . else -. end);

def points: . as $line
  | (.[2] - .[0]) as $delta_x
  | (.[3] - .[1]) as $delta_y
  | ($delta_x | sign) as $dx
  | ($delta_y | sign) as $dy
  | if $part == 2 or $dx == 0 or $dy == 0 then
      range(((if $delta_x != 0 then $delta_x else $delta_y end) | abs) + 1)
    else empty end
  | [$line[0] + . * $dx, $line[1] + . * $dy]
  | tostring;


[ [ parse[] | [ scan("\\d+") | tonumber ] | points ]
  | reduce .[] as $point ({}; .[$point] += 1)
  | to_entries[]
  | if .value > 1 then 1 else empty end ]
  | length
