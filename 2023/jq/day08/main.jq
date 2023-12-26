include "../common/util";

def gcd(a; b):
  if b == 0 then a else gcd(b; a % b) end;

def lcm(a; b):
  a * b / gcd(a; b);

def find_path($graph; $path; $start; $goal):
  {node: $start, step: 0, pathIndex: 0} |
  reduce_while($goal[.node] | not;
    .node = $graph[.node][$path[.pathIndex]] |
    .pathIndex = (.pathIndex + 1) % ($path | length) |
    .step += 1
  ) | .step
;

def find_paths($graph; $path; $starts; $goals):
  $starts | keys | map(find_path($graph; $path; .; $goals));

def build_side($graph; $side; $char):
  reduce ($graph | keys)[] as $k (.;
    if ($k | split(""))[2] == $char then
      .[$side][$k] = true
    else . end
  );

line_blocks |
  (.[0][0] | split("")) as $path |
  (reduce .[1][] as $line ({};
    ([$line | scan("\\w+")]) as $m |
    .[$m[0]] = {L: $m[1], R: $m[2]}
  )) as $graph |
  . = {starts: {}, goals: {}} |
  if $part == 0 then
    .starts["AAA"] = true | .goals["ZZZ"] = true
  else
    build_side($graph; "starts"; "A") |
    build_side($graph; "goals"; "Z")
  end |
  reduce find_paths($graph; $path; .starts; .goals)[] as $f (1;
    lcm(.; $f)
  )
