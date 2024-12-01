include "common/util";
include "common/prog";

init_prog(ints; []) |
  if $part == 0 then
    step_prog | .data | from_obj | tostring
  elif $part == 1 then
    .data["1"] = 12 | .data["2"] = 2 | step_prog | .data["0"]
  elif $part == 2 then
    range(0; 100) as $noun |
    range(0; 100) as $verb |
    .data["1"] = $noun | .data["2"] = $verb | step_prog | select(.data["0"] == 19690720) | $noun * 100 + $verb
  else
    error("invalid part \($part)")
  end
