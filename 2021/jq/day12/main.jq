include "../common/util";

def dfs($node):
  if $node == "end" then
    .count = 1
  elif $node == ($node | ascii_downcase) then
    if .visited[$node] then
      if $node == "start" or .mulligan == false then
        .count = 0
      else
        .mulligan = false
      end
    else
      .visited[$node] = 1
    end
  else . end
  | .count = (.count // ([.graph[$node][] as $n | dfs($n) | .count] | add))
;

[
  lines[] | split("-")
    | ., reverse
    | {key: .[0], value: .[1]}
] | from_entries_with_lists
  | {graph: ., visited: {}, mulligan: ($part == 2)}
  | dfs("start")
  | .count
  