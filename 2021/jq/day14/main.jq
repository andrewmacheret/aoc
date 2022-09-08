include "../common/util";

def pair_counts($poly; $rules):
  reduce range($steps) as $s (
    ($poly | split("") | [.[:-1], .[1:]] | transpose | map(join("")) | counter);
    to_entries
      | map([.key[:1] + $rules[.key], .value], [$rules[.key] + .key[1:], .value])
      | arrays_to_counter
  );

def single_counts($poly; $rules):
  reduce (pair_counts($poly; $rules) | to_entries)[] as $c (
      [$poly[:1], $poly[-1:]] | counter;
      .[$c.key[:1]] += $c.value | .[$c.key[1:]] += $c.value
    );

line_blocks
  | .[0][0] as $poly
  | (.[1] | map(split(" -> ")) | from_arrays) as $rules
  | single_counts($poly; $rules)
  | to_entries | map(.value) | sort | (.[-1] - .[0]) / 2
