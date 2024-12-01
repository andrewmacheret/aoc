include "common/util";
include "common/prog";

def play:
  {prog: (init_prog(ints; []) | .data["0"] = 2), out: [0,0,0], i: 0, r: 0, grid: {}} |
  .lastx = [0,0] |
  .score = 0 |
  .prog = (.prog | step_prog) |
  until(.prog.interrupt == "HALT";
    if .prog.interrupt != "INPUT" then # "OUTPUT" or null
      .out[.i] = .prog.out |
      .i = (.i + 1) % 3 |
      if .i == 0 then
        .out[0] as $x | .out[2] as $type |
        if $x < 0 then
          .score = $type | info("score"; .score)
        elif $type >= 3 then
          .lastx[$type - 3] = $x
        else . end
      else . end
    else
      .prog.in = [(.lastx[1] - .lastx[0]) | sign]
    end |
    .prog = (.prog | step_prog)
  ) |
  .score;



if $part == 1 then
  init_prog(ints; []) | [run_prog] | slice(2; length; 3) | map(if . == 2 then 1 else 0 end) | add
else
  play
end
