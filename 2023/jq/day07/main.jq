include "../common/util";

def card_key:
  . as $c |
  if $part == 0 then "23456789TJQKA" else "J23456789TQKA" end |
  index($c);

def hand_key:
  counter | 
  .["J"] as $j |
  if $part == 1 and $j != null and $j < 5 then
    del(.["J"]) |
    .[to_entries | max_by(.value) | .key] += $j
  else . end |
  values | sort_by(-.);

lines |
  sort_by(split("")[:5] | [hand_key, map(card_key)]) |
  map(split(" ")[1] | tonumber) |
  to_entries |
  map((.key+1) * .value) |
  add
