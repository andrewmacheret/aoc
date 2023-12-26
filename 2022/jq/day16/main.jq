include "../common/util";

def parse_rates: lines | map(split(" ") | [.[1], (.[4] | numbers[0])]) | from_arrays;
def parse_paths: lines | map(split(" ") | [.[1], (.[9:] | map(split(",")[0]))]) | from_arrays;
def permutations2: .[] as $x | .[] as $y | select($x != $y) | [$x, $y];
# def permutations2: ["AA", "JJ"];

def bfs($s; $p; $g):
  {seen: {}, q: [$s], round: 0}
  | (try reduce_while((.q | length) > 0;
    .q = [
      .q[] as $i
      | if $i == $g then error(.) else . end
      | $p[$i][] as $p
      | select(.seen[$p] != 1)
    ]
    | .q = [.q[] as $i | $p[$i][] as $p | ]

    | .next_q = []
    | reduce .q[] as $i (.;
      if $i == $g then error(.)
      elif .seen[$i] then
        .
      else
        reduce $p[$i][] as $p (.;
          .seen[$p] = 1
          | .next_q += [$p]
        )
      end | .q = .next_q | .round += 1
    )
  ) catch .).round;

{rates: parse_rates, paths: parse_paths}
| .positive_nodes = (.rates | map_values(select(. > 0)) | keys)
| [(.positive_nodes | permutations2) as $p | bfs($p[0]; .paths; $p[1]) + 1]