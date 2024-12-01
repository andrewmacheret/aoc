include "common/util";
include "common/prog";

def draw:
  (keys_unsorted | map(fromjson | .[0]) | min) as $min_x |
  (keys_unsorted | map(fromjson | .[0]) | max) as $max_x |
  (keys_unsorted | map(fromjson | .[1]) | min) as $min_y |
  (keys_unsorted | map(fromjson | .[1]) | max) as $max_y |
  [
    range($min_y; $max_y + 1) as $y |
    [range($min_x; $max_x + 1) as $x | if (.["[\($x),\($y)]"] // 0) == 1 then "#" else "." end] | join("")
  ] | ("\n" + join("\n"));

def turn($dir; $clockwise):
  if $clockwise then
    [-$dir[1], $dir[0]]
  else
    [$dir[1], -$dir[0]]
  end;

def paint:
  init_prog(ints; []) as $prog |
  {panels: {"[0,0]": ($part - 1)}, pos: [0,0], dir: [0,-1], prog: $prog, x: 0} |
  
  label $out | reduce_while(.prog.interrupt != "HALT";
    (.panels["\(.pos)"] // 0) as $color |
    .prog.in += [$color] |
    .prog = (.prog | step_prog) |
    if .prog.interrupt != "HALT" then
      # assert("1 \(.prog.interrupt)"; .prog.interrupt == "OUTPUT") |
      .panels["\(.pos)"] = .prog.out |
      .prog = (.prog | step_prog) |
      # assert("2 \(.prog.interrupt)"; .prog.interrupt == "OUTPUT") |
      .dir = turn(.dir; .prog.out == 1) |
      .pos = [.pos[0] + .dir[0], .pos[1] + .dir[1]] |
      .x += 1
    else . end
  ) |
  .panels;

paint | if $part == 1 then length else draw end
