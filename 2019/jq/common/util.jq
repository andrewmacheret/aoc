def reduce_do_while(cond; update):
  def _while:
    if cond then (update | _while) else . end;
  update | _while
;

def reduce_while(cond; update):
  def _while:
    if cond then (update | _while) else . end;
  _while
;

def reduce_while_plus_1(cond; update):
  reduce_while(cond; update) | update
;

def while_stream(cond; update):
  def _while:
    ., if cond then (update | _while) else empty end;
  _while
;

def reduce_op(op): reduce .[1:][] as $x (.[0]; [., $x] | op);

def gt: reduce_op(if .[0] > .[1] then 1 else 0 end);
def lt: reduce_op(if .[0] < .[1] then 1 else 0 end);
def eq: reduce_op(if .[0] == .[1] then 1 else 0 end);
def ge: reduce_op(if .[0] >= .[1] then 1 else 0 end);
def le: reduce_op(if .[0] <= .[1] then 1 else 0 end);
def ne: reduce_op(if .[0] != .[1] then 1 else 0 end);
def mul: reduce_op(.[0] * .[1]);


def counter: reduce .[] as $x ({}; .[$x] += 1);

def merge_lists:
  reduce .[] as $o (
      {};
      reduce ($o|keys_unsorted)[] as $key (
        .;
        .[$key] += [$o[$key]]
      )
    )
;

def merge_counters:
  reduce .[] as $o (
    {};
    reduce ($o|keys_unsorted)[] as $key (
      .;
      .[$key][$o[$key]] += 1
    )
  )
;

def from_arrays: map({key: .[0], value: .[1]}) | from_entries;

def entries_to_objects: map([.] | from_entries);

def from_entries_with_lists: entries_to_objects | merge_lists;

def from_entries_with_counters: entries_to_objects | merge_counters;

def values: to_entries | map(.value);

def arrays_to_counter: reduce .[] as $x ({}; .[$x[0]] += $x[1]);

def in(s): first((s == .) // empty) // false;

def lines: split("\n")[:-1];

def line: lines[0];

def line_blocks: . + "\n" | split("\n\n")[:-1] | map(split("\n"));

def numbers: [match("-?\\d+"; "g") | .string | tonumber];

def is_digit: "0" <= . and . <= "9";

def from_radix($r): reduce_op(.[0] * $r + .[1]);

def sign: ((if . > 0 then 1 else 0 end) - (if . < 0 then 1 else 0 end));

def info($info; $obj): ({info: $info, obj: $obj} | debug) as $debug | .;

def info($obj): ($obj | debug) as $debug | .;

def dirs_4:
  {x:.x,y:(.y+1)},
  {x:.x,y:(.y-1)},
  {x:(.x+1),y:.y},
  {x:(.x-1),y:.y};

def dirs_8: 
  {x:(.x+1),y:(.y+1)},
  {x:(.x+1),y:.y},
  {x:(.x+1),y:(.y-1)},
  {x:.x,y:(.y+1)},
  {x:.x,y:(.y-1)},
  {x:(.x-1),y:(.y+1)},
  {x:(.x-1),y:.y},
  {x:(.x-1),y:(.y-1)};

def range_xy($dim):
  range($dim.n) | . as $y | range($dim.m) | . as $x | {x:$x, y:$y};

def range_xy($x2;$y2):
  range($y2) | . as $y | range($x2) | . as $x | {x:$x, y:$y};

def range_xy($x1; $x2; $y1; $y2):
  range($y1; $y2) | . as $y | range($x1; $x2) | . as $x | {x:$x, y:$y};

def to_grid: map(split(""));

def to_number_grid: map(split("") | map(tonumber));

def from_grid: map(join(""));

def dimensions: { n: length, m: (.[0] | length) };

def in_range($dim): 0 <= .y and .y < $dim.n and 0 <= .x and .x < $dim.m;

def draw_coords:
    ([.[] | .x] | max + 1) as $m
  | ([.[] | .y] | max + 1) as $n
  | reduce .[] as $xy (
      [range($n) | [range($m) | "."]];
      .[$xy.y][$xy.x] = "#"
    )
  | from_grid
  | "\n" + join("\n") + "\n"
;

def slice($_start; $_end; $_step):
  [range($_start; $_end; $_step) as $x | .[$x]];

def grouper($n):
  [range($n) as $i | slice($i; length; $n)] | transpose;

def paired:
  grouper(2);

def pairwise:
  [.[:-1], .[1:]] | transpose;

def test($expected):
  if . == $expected then
    info("PASS - EXPECTED=\($expected) ACTUAL=\(.)")
  else
    error("FAIL - EXPECTED=\($expected) ACTUAL=\(.)")
  end;

def assert($msg; $cond):
  if $cond | not then
    error("assertion failed: \($msg)")
  else . end;
