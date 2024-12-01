include "common/util";
include "common/prog";

# def draw_map:
#   (keys_unsorted | map(numbers | .[0]) | min) as $min_x |
#   (keys_unsorted | map(numbers | .[0]) | max) as $max_x |
#   (keys_unsorted | map(numbers | .[1]) | min) as $min_y |
#   (keys_unsorted | map(numbers | .[1]) | max) as $max_y |
#   [
#     range($min_y; $max_y + 1) as $y |
#     [range($min_x; $max_x + 1) as $x | .["\($x),\($y)"] // "?"] | join("")
#   ] | ("\n" + join("\n"));

def build_map:
  def step:
    reduce [[1, 2, 0, -1], [2, 1, 0, 1], [3, 4, -1, 0], [4, 3, 1, 0]][] as [$dir, $opp, $dx, $dy] (.;
      .x += $dx |
      .y += $dy |
      "\(.x),\(.y)" as $pos |
      if .map[$pos] == null then
        .prog.in += [$dir] |
        .prog = (.prog | step_prog) |
        .prog.out as $out |
        .map[$pos] = ["#", ".", "O"][$out] |
        if $out != 0 then
          if $out == 2 then
            .ox = .x | .oy = .y
          end |
          step |
          .prog.in += [$opp] |
          .prog = (.prog | step_prog)
        end
      end |
      .x -= $dx |
      .y -= $dy
    );
  {prog: init_prog(ints; []), x: 0, y: 0, map: {"0,0": "S"}} |
  step;

def bfs($map; $sx; $se; $goal):
  def step:
    .q[0] as $item |
    $item[0] as $r |
    $item[1] as $x |
    $item[2] as $y |
    .result = $r |
    "\($x),\($y)" as $pos |
    .q = .q[1:] |
    if .seen[$pos] == null then
      .seen[$pos] = true |
      $map[$pos] as $val |
      if $val == $goal then
        .q = []
      elif $val != "#" then
        .q += [
          [$r + 1, $x + 1, $y],
          [$r + 1, $x - 1, $y],
          [$r + 1, $x, $y + 1],
          [$r + 1, $x, $y - 1]
        ]
      end
    end;
  {q: [[0,$sx,$se]], seen: {}} |
  reduce_while(.q | length > 0; step).result;
  

build_map |
  if $part == 1 then
    bfs(.map; 0; 0; "O")
  else
    bfs(.map; .ox; .oy; "?") - 1
  end
