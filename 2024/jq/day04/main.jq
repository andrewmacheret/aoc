include "common/util";

def dirs_8: 
  {x:1,y:1},
  {x:1,y:0},
  {x:1,y:-1},
  {x:0,y:1},
  {x:0,y:-1},
  {x:-1,y:1},
  {x:-1,y:0},
  {x:-1,y:-1};

def diag: 
  [{x:1,y:1},
  {x:1,y:-1},
  {x:-1,y:-1},
  {x:-1,y:1}];

def part1($dim):
  [range_xy($dim) as $p
    | dirs_8 as $d
    | select(
      ({x:($p.x + $d.x*3), y:($p.y + $d.y*3)} | in_range($dim)) and
      .[$p.y + $d.y*0][$p.x + $d.x*0] == "X" and
      .[$p.y + $d.y*1][$p.x + $d.x*1] == "M" and
      .[$p.y + $d.y*2][$p.x + $d.x*2] == "A" and
      .[$p.y + $d.y*3][$p.x + $d.x*3] == "S")
    | 1];

def part2($dim):
  [range_xy($dim) as $p
    | select(.[$p.y][$p.x] == "A")
    | select($p.x >= 1 and $p.y >= 1 and $p.x < $dim.m-1 and $p.y < $dim.n-1)
    | diag as $d
    | range(4) as $i
    | select(
      .[$p.y + $d[($i+0)%4].y][$p.x + $d[($i+0)%4].x] == "M" and
      .[$p.y + $d[($i+1)%4].y][$p.x + $d[($i+1)%4].x] == "M" and
      .[$p.y + $d[($i+2)%4].y][$p.x + $d[($i+2)%4].x] == "S" and
      .[$p.y + $d[($i+3)%4].y][$p.x + $d[($i+3)%4].x] == "S")
      | 1];

lines
  | to_grid
  | if $part == 0 then part1(dimensions) else part2(dimensions) end
  | add
