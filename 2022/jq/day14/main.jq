include "../common/util";

def sign: (if . > 0 then 1 else 0 end) - (if . < 0 then 1 else 0 end);

def pairs: to_entries | group_by(.key / 2 | floor) | map(map(.value));
def pairwise: [.,.[1:]] | transpose[:-1];

def wall:
  reduce .[] as $pair ({};
    $pair[0][0] as $x1 | $pair[0][1] as $y1 | $pair[1][0] as $x2 | $pair[1][1] as $y2 |
    ($x2 - $x1 | sign) as $dx | ($y2 - $y1 | sign) as $dy |
    if $dy != 0 then
      reduce range($y1; $y2+$dy; $dy) as $y (.; .[([$x1,$y] | tostring)] = 1)
    else
      reduce range($x1; $x2+$dx; $dx) as $x (.; .[([$x,$y1] | tostring)] = 1)
    end
  );

def add_floor($y): reduce range(-1000;1000) as $x (.; .[([$x,$y] | tostring)] = 1);

def parse:
  lines
  | map(numbers | pairs | pairwise | wall)
  | add
  | (keys | map(fromjson | .[1]) | max + 2) as $the_floor
  | if $part == 1 then add_floor($the_floor) else . end
  | {world: ., floor: $the_floor};

def drop_sand:
  .x = 500 | .y = 0 | .falling = true |
  reduce_while(.falling;
    if .y == .floor then
      .running = false | .falling = false
    elif .world[([.x, (.y+1)] | tostring)] == null then
      .y += 1
    elif .world[([(.x-1), (.y+1)] | tostring)] == null then
      .y += 1 | .x -= 1
    elif .world[([(.x+1), (.y+1)] | tostring)] == null then
      .y += 1 | .x += 1
    else
      if .world[([.x, .y] | tostring)] != null then
        .running = false
      else
        .world[([.x, .y] | tostring)] = 2
      end | .falling = false
    end
  );

def keep_dropping_sand: .running = true | reduce_while(.running; drop_sand);

parse | keep_dropping_sand | .world | map_values(select(. == 2)) | length
