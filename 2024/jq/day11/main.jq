include "common/util";

def do_step:
  reduce (to_entries[] |
    .key = (.key | if . == "0" then
      "1"
    elif length % 2 == 1 then
      tonumber * 2024 | tostring
    else
      (split("")[0:length/2] | join("")),
      (split("")[length/2:] | join("") | tonumber | tostring)
    end)
  ) as $e ({}; .[$e.key] += $e.value);

lines[0]
  | reduce split(" ")[] as $x ({}; .[$x] += 1)
  | reduce range($steps) as $i (.; do_step)
  | values
  | add
