include "../common/util";

def simulate($dim):
  .q = [range_xy($dim.m; $dim.n)]
  | .todo = true
  | last(while(.todo == true;
    reduce .q[] as $xy (.todo = false | .q = [];
      .grid[$xy.y][$xy.x] += 1
      | .todo = true
      | if (.grid[$xy.y][$xy.x]) == 10 then
          .flashes += 1
          | .q += [$xy | dirs_8 | select(in_range($dim))]
        else . end
    )
  ))
  | .grid = [.grid[] | [.[] | [., 10] | min % 10]]
;

lines
  | to_number_grid
  | dimensions as $dim
  | {grid: ., flashes: 0}
  | last(label $out | foreach range(1; $steps + 1) as $s (.;
    if .zeros then break $out else . end
    | simulate($dim)
    | if (.grid | flatten | max) == 0 and .zeros == null then
        .zeros = $s
      else . end
  ))  
  | .zeros // .flashes
