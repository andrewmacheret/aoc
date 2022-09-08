include "../common/util";

def is_num: type == "number";

def divmod($x): [(. / $x | floor), . % $x];

def left($val): if is_num then . + $val else [(.[0] | left($val)), .[1]] end;

def right($val): if is_num then . + $val else [.[0], (.[1] | right($val))] end;

def mag: if is_num then . else 3*(.[0] | mag) + 2*(.[1] | mag) end;

def explode($depth):
  if is_num then
    [{root: .}, [0, 0]]
  elif $depth >= 4 then
    [{root: 0, did: true}, .]
  else
    .[0] as $x | .[1] as $y
    | $x | explode($depth+1) as [{root: $x, did: $did}, [$l, $r]]
    | if $did then
        (if $r != 0 then ($y | left($r)) else $y end) as $y
        | [{root: [$x, $y], did: true}, [$l, 0]]
      else
        $y | explode($depth+1) as [{root: $y, did: $did}, [$l, $r]]
        | if $did then
            (if $l != 0 then ($x | right($l)) else $x end) as $x
            | [{root: [$x, $y], did: true}, [0, $r]]
          else
            [{root: [$x, $y]}, [0, 0]]
          end
      end
  end
;

def split:
  if is_num then
    if . > 9 then
      {root: [(./2|floor), (divmod(2)|add)], did: true}
    else
      {root: .}
    end
  else
    .[0] as $x | .[1] as $y
    | $x | split
    | if .did then
        .root = [.root, $y]
      else
        $y | split
        | .root = [$x, .root]
      end
  end
;

def combine:
  {root: ., did: true}
  | reduce_while(.did;
      reduce_while(.did; .root | explode(0)[0])
      | .root | split
    )
  | .root
;

def pick2:
  range_xy(length; length) as $_
  | select($_.x != $_.y)
  | [.[$_.x], .[$_.y]]
;

lines
| map(fromjson)
| if $part == 1 then
    reduce_op(combine) | mag
  else
    [ pick2 | combine | mag ] | max
  end
