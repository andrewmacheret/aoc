include "../common/util";

def split_ops: split("\\b"; "g") | map(select(. != ""));

def hash: reduce explode[] as $c (0; . + $c | . * 17 | . % 256);

def hashmap:
  reduce map(split_ops)[] as $op ([range(256) | {}];
    ($op[0] | hash) as $h |
    if $op[1] == "=" then
      .[$h][$op[0]] = ($op[2] | tonumber)
    else
      del(.[$h][$op[0]])
    end
  ) |
  to_entries |
  map(
    .key as $i |
    .value |
    to_entries |
    to_entries |
    map(($i+1) * (.key+1) * .value.value) |
    add
  );

lines[0] | split(",") | [map(hash), hashmap][$part] | add
