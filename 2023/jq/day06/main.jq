include "../common/util";

lines |
  map(numbers) |
  if $part == 1 then map(map(tostring) | add | tonumber | [.]) else . end |
  transpose |
  map([range(1; .[0]) as $i | select((.[0] - $i)*$i > .[1])] | length) |
  mul
