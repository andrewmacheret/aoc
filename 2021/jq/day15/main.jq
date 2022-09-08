include "../common/util";
include "../common/pq";

lines
  | to_number_grid as $grid
  | {({x:0,y:0} | tostring): 0} as $seen
  | ($grid | dimensions) as $dim
  | {m:($dim.m*$multiplier), n:($dim.n*$multiplier)} as $bound
  | {x:($bound.m-1), y:($bound.n-1)} as $goal
  | ({} | pq_add_tasks([[0,{x:0,y:0}]])) as $q
  | {q: $q, seen: $seen, score: 0}
  | last(while(.done != true;
      if .score > 0 then
        .done = true
      else
        (.q | pq_pop) as $pair
        | .q = $pair[1]
        | $pair[0][0] as $score
        | $pair[0][1] as $xy
        | if $xy == $goal then
            .score = $score
          else
            reduce ($xy | dirs_4 | select(in_range($bound))) as $xy1 (.;
              ($xy1.y % $dim.n) as $ym
              | ($xy1.x % $dim.m) as $xm
              | (($xy1.y / $dim.n) | floor) as $yd
              | (($xy1.y / $dim.m) | floor) as $xd
              | ($score + ($grid[$ym][$xm] + $xd + $yd + 8) % 9 + 1) as $val
              | if (.seen[$xy1 | tostring] // infinite) > $val then
                  .seen[$xy1 | tostring] = $val
                  | .q = (.q | pq_add($val; $xy1))
                else . end
            )
          end
      end
    ))
  | .score
