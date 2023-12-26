include "../common/util";

def sign: (if . > 0 then 1 else 0 end) - (if . < 0 then 1 else 0 end);

def repeat($n): if ($n == 0) then empty else ., repeat($n - 1) end;

def DIRS: {R: [1, 0], U: [0, -1], D: [0, 1], L: [-1, 0]};

def follow($h; $t):
  (t[0] - h[0]) as $dx | (t[1] - h[1]) as $dy
  | if ($dx | fabs) <= 1 and ($dy | fabs) <= 1 then $t
    else [$t[0] - ($dx | sign), $t[1] - ($dy | sign)] end;

reduce (lines[] | split(" ")) as $line (
  {seen: {"0,0":1}, snake: [[0,0] | repeat([2,10][$part])]};
  DIRS[$line[0]] as $d
  | reduce range($line[1] | tonumber) as $i (.;
    .snake[0] = [.snake[0][0] + $d[0], .snake[0][1] + $d[1]]
    | reduce range(.snake | length - 1) as $j (.;
      .snake[$j+1] = follow(.snake[$j]; .snake[$j+1])
    )
    | .seen[.snake[-1] | join(",")] = 1
  )
) | .seen | length
