include "../common/util";

def cd($dir):
  if $dir == ".." then
    .pwd = .pwd[:(.pwd | rindex("/"))]
  else
    .pwd = .pwd + "/" + $dir
  end
;

def add_sizes($size):
  .p = .pwd
  | reduce_while_plus_1(
      (.p | length) > 0;
      .dirs[.p] += $size | .p = .p[:(.p | rindex("/"))]
    )
;

def process($parts):
  if $parts[0] == "$" and $parts[1] == "cd" then
    cd($parts[2])
  elif $parts[0] != "$" and $parts[0] != "dir" then
    add_sizes($parts[0] | tonumber)
  else
    .
  end
;

def part1:
  to_entries | map(.value | tonumber | select(. <= 100000)) | add
;

def part2:
  (30000000 - (70000000 - .[""])) as $need
  | to_entries | map(.value | tonumber) | sort | map(select(. >= $need))[0]
;

reduce (lines[1:][] | split(" ")) as $parts (
  {dirs: {}, pwd: ""};
  process($parts)
) | .dirs | if $part == 1 then part1 else part2 end
