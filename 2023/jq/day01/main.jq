include "../common/util";

def digits: ["1", "2", "3", "4", "5", "6", "7", "8", "9"] | to_entries;
def words: ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] | to_entries;

def search($terms):
  . as $line |
  $terms | map(.key as $i | .value as $x | $line | index($x) | select(.) | [., $i]) | min | .[1] as $a |
  $terms | map(.key as $i | .value as $x | $line | rindex($x) | select(.) | [., $i]) | max | .[1] as $b |
  ($a+1) * 10 + ($b+1);

lines | map(search(if $part == 1 then digits else (digits + words) end)) | add
