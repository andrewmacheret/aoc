include "common/util";

def to_obj: reduce to_entries[] as $e ({}; .["\($e.key)"] = $e.value);
def from_obj: reduce to_entries[] as $e ([]; .[$e.key | tonumber] = $e.value);

def ints:
  lines[0] | split(",") | map(tonumber);

def init_prog($ints; $in):
  {data: $ints | to_obj, i: 0, r: 0, in: $in};

def step_prog:
  .interrupt = null | .out = null |
  reduce_while(.interrupt == null;
    .data["\(.i)"] as $OP |
    ($OP % 100) as $op |

    def param_mode($i):
      ($OP / pow(10; $i + 1) | floor) % 10;
    def val($i):
      (.data["\(.i+$i)"] // 0) as $a |
      param_mode($i) as $m |
      if $m == 1 then $a else
        (if $m == 2 then .r else 0 end) as $offset |
        (.data["\($a + $offset)"] // 0)
      end;
    def addr($i):
      (.data["\(.i+$i)"] // 0) as $a |
      param_mode($i) as $m |
      ((if $m == 2 then .r else 0 end) + $a) as $addr |
      "\($addr)";

    # ([0, 4, 4, 2, 2, 3, 3, 4, 4, 2][$op] // 1) as $op_length |
    if $op == 1 then
      .data[addr(3)] = val(1) + val(2) |
      .i += 4
      # | info("ADD set_data(\($c)) = \($x) + \($y) = \(get_data($c))")
    elif $op == 2 then
      .data[addr(3)] = val(1) * val(2) |
      .i += 4
      # | info("MUL set_data(\($c)) = \($x) * \($y) = \(get_data($c))")
    elif $op == 3 then
      if .in[0] then
        .data[addr(1)] = .in[0] |
        del(.in[0]) |
        .i += 2
        # | info("IN  set_data(\($a)) = \(get_data($a))")
      else
        .interrupt = "INPUT"
      end
    elif $op == 4 then
      .out = val(1) |
      .interrupt = "OUTPUT" |
      .i += 2
      # | info("OUT output: \($x)")
    elif $op == 5 then
      if val(1) != 0 then .i = val(2) else .i += 3 end
      # | info("JZE jump-if-true: \($x) != 0, jump to \($y)")
    elif $op == 6 then
      if val(1) == 0 then .i = val(2) else .i += 3 end
      # | info("JNZ jump-if-false: \($x) == 0, jump to \($y)")
    elif $op == 7 then
      .data[addr(3)] = (if val(1) < val(2) then 1 else 0 end) |
      .i += 4
      # | info("LT  set_data(\($c)) = \($x) < \($y) = \(get_data($c))")
    elif $op == 8 then
      .data[addr(3)] = (if val(1) == val(2) then 1 else 0 end) |
      .i += 4
      # | info("EQ  set_data(\($c)) = \($x) == \($y) = \(get_data($c))")
    elif $op == 9 then
      .r += val(1) |
      .i += 2
      # | info("REL .r += \($x) = \(.r)")
    elif $op == 99 then
      .interrupt = "HALT"
      | info("HALT")
    else
      debug |
      error("invalid opcode \($op)")
    end
  );

def run_prog:
  while_stream(.interrupt != "HALT"; step_prog) | select(.interrupt == "OUTPUT") | .out;
