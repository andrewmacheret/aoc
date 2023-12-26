include "../common/util";

def solve:
  split("|") |
  map(numbers) |
  (reduce .[1][] as $x ({}; .["\($x)"] = 1)) as $winning |
  {
    id: .[0][0],
    matches: .[0][1:] | map($winning["\(.)"]) | add
  };

def instances:
  reduce .[] as $x ({};
    .["\($x.id)"] += 1 |
    reduce range(1; $x.matches+1) as $i (.;
      .["\($x.id + $i)"] += .["\($x.id)"]
    )
  );

lines |
  map(solve) |
  if $part == 0 then
    map(if .matches > 0 then pow(2; .matches-1) else 0 end)
  else
    instances | to_entries | map(.value)
  end | add
