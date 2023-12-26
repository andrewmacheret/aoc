include "../common/util";

(4 + $part * 10) as $x |
[lines[0] as $s | range($x, $s | length) | select(($s[.-$x:.] | split("") | unique | length) == $x)][0]
