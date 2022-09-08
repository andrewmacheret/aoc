def parse: split("\n")[0:-1][] | split(" | ") | [.[] | split(" ")];

def intersect:
  reduce .[1:][] as $x (.[0]; . - (. - $x))
;

def decode($wiring; $decoder):
  $decoder[[split("")[] | $wiring[.]] | sort | join("")]
;

def get_wiring:
  [ .[] | { key: length | tostring, value: split("") | sort | join("") } ]
  | from_entries_with_counters
  | with_entries(.value = ([.value | keys_unsorted[] | split("")]))
  | (.["3"][0] - .["2"][0]) as $a
  | (.["2"] + .["6"] | intersect) as $f
  | (.["2"][0] - $a - $f) as $c
  | (.["4"] + .["5"] | intersect) as $d
  | (.["4"][0] - ($a + $c + $d + $f)) as $b
  | ((.["6"] | intersect) - ($a + $b + $c + $d + $f)) as $g
  | ("abcdefg" | split("") - ($a + $b + $c + $d + $f + $g)) as $e
  | { a: $a, $b, c: $c, d: $d, e: $e, f: $f, g: $g }
  | with_entries( .key as $k | .key = .value[0] | .value = $k )
;

def count1478:
  .[] | select(in(1,4,7,8)) | 1
;

def concat_int:
  [.[] | tostring] | add | tonumber
;

{
  "cf": 1,
  "acf": 7,
  "bcdf": 4,
  "acdeg": 2,
  "acdfg": 3,
  "abdfg": 5,
  "abcefg": 0,
  "abdefg": 6,
  "abcdfg": 9,
  "abcdefg": 8,
} as $decoder
  | [
    parse
    | (.[0] | get_wiring) as $wiring
    | [ .[1][] | decode($wiring; $decoder) ]
    | if $part == 1 then count1478 else concat_int end
  ] | add // 0
