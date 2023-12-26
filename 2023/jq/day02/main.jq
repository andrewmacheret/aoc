include "../common/util";

def run_game:
  [ match("(\\d+) (.)"; "g").captures | map(.string) ] |
  reduce .[] as $x ({}; .[$x[1]] = ([.[$x[1]], ($x[0] | tonumber)] | max));

def process_game:
  ([scan("\\d+")][0] | tonumber) as $id |
  run_game |
  if $part == 1 then
    if .r <= 12 and .g <= 13 and .b <= 14 then $id else 0 end
  else
    .r * .g * .b
  end;

lines | map(process_game) | add
