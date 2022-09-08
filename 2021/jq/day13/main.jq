include "../common/util";

def parse_coords: [.[0][] | [split(",")[] | tonumber] | {x: .[0], y: .[1]}];

def parse_folds: ([.[1][] | split("=") | {key: .[0][-1:], value: (.[1] | tonumber)}]);

def fold($f):
  [.[] | [
      to_entries[]
      | if .key == $f.key and .value > $f.value then
          .value = 2 * $f.value - .value
        else . end
    ] | from_entries
  ] | unique
;

line_blocks
  | [parse_folds | if $part == 1 then .[0] else .[] end] as $folds
  | reduce $folds[] as $f (parse_coords; fold($f))
  | if $part == 1 then length else draw_coords end
