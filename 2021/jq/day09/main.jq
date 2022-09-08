
def local_min($g):
  select([dirs_4 as $d | $g[.y][.x] < $g[$d.y][$d.x]] | all)
;

def fill($xy):
  {q: [$xy], grid: ., size: 0, todo: true}
  | last(
    while(.todo;
      reduce .q[] as $xy (. += {q: [], todo: false};
        if .grid[$xy.y][$xy.x] < 9 then
          .grid[$xy.y][$xy.x] = 9
          | .size += 1
          | .q += [$xy | dirs_4]
          | .todo = true
        else
          .
        end
      )
    )
  )
;

[ [ lines[] | "9" + . + "9"]
  | [[range(.[0] | length) | "9"] | join("")] as $pad
  | $pad + . + $pad
  | .[] | [split("")[] | tonumber ] ]
  | length as $n
  | (.[0] | length) as $m
  | . as $g
  | if $part == 1 then (
    [range_xy(1; $m-1; 1; $n-1) | local_min($g) | $g[.y][.x]]
    | add + length
  ) else (
    reduce range_xy(1; $m-1; 1; $n-1) as $xy (
      {sizes: [], grid: $g};
      (.grid | fill($xy)) as $res
      | .sizes += [$res.size]
      | .grid = $res.grid
    )
    | .sizes | sort[-3:] | .[0] * .[1] * .[2]
  ) end
