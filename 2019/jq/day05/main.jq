include "common/util";
include "common/prog";

init_prog(ints; [if $part == 1 then 1 else 5 end]) | [run_prog][-1]
