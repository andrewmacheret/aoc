include "../common/util";

def tryit($x1; $x2; $y1; $y2):
  {x: 0, y: 0, vx: .x, vy: .y}
  | reduce_while(
      .y > $y1 and .found != 1;
      .x += .vx | .y += .vy
      | if .vx > 0 then .vx -= 1 else . end
      | .vy -= 1
      | if $x1 <= .x and .x <= $x2 and $y1 <= .y and .y <= $y2 then .found = 1 else . end
    )
  | .found // 0
;

line
| numbers
| .[0] as $x1 | .[1] as $x2 | .[2] as $y1 | .[3] as $y2
| if $part == 1 then
    $y1 * ($y1+1) / 2
  else
    [ range_xy(1; $x2 + 1; $y1; -$y1) | tryit($x1; $x2; $y1; $y2) ]
    | add
  end
