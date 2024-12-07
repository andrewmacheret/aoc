include "common/util";

def recurse:
  .[-1] as $x
  | if length == 1 then $x
    else .[:-1] | recurse | (. + $x), (. * $x), 
      if $part == 1 then ((. | tostring) + ($x | tostring) | tonumber) else empty end
    end
;

lines | map(numbers
  | .[0] as $goal
  | .[1:] | first(recurse | select(. == $goal))
) | add
