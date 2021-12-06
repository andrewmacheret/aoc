def multiply: .[1:] + .[:1] | .[6] += .[-1];

split(",")
  | (reduce .[] as $i ({}; .[$i] += 1)) as $c
  | [ range(9) | tostring ]
  | (reduce .[] as $i ([]; . + [$c[$i] + 0])) as $c
  | [ range($days | tonumber) ]
  | reduce .[] as $_ ($c; multiply)
  | [ to_entries[] | .value ] | add
