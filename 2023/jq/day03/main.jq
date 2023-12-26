include "../common/util";

lines |
  to_grid as $grid |
  ($grid | dimensions) as $dim |
  [
    range_xy($dim) | .x as $x | .y as $y |

    # if it's a digit
    $grid[.y][.x] as $digit |
    select($digit | is_digit) |
    
    # go in all 8 directions
    dirs_8 as $gear_xy | $gear_xy |
    select(in_range($dim)) |
    
    # if it's a symbol
    $grid[.y][.x] as $gear |
    select( ($gear != ".") and ($gear | is_digit | not)) |
    
    # find the beginning and end of the number
    ($x | reduce_while(. > 0 and ($grid[$y][. - 1] | is_digit); . - 1)) as $x1 |
    ($x | reduce_while(. < $dim.m - 1 and ($grid[$y][. + 1] | is_digit); . + 1)) as $x2 |
    
    # get the number
    ([range($x1; $x2 + 1) | $grid[$y][.]] | join("") | tonumber) as $val |
    
    # save the symbol -> result mapping
    [($gear_xy | "\(.x)_\(.y)"), $val]
  ] |
  # get rid of duplicates lol
  unique |
  if $part == 0 then
    map(.[1]) | add
  else
    reduce .[] as [$xy, $val] ({}; .[$xy] += [$val]) |
    map(select(length == 2) | mul) | add
  end
