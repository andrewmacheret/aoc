include "../common/util";

def elves: line_blocks | map(map(tonumber) | add);

def top3: sort | .[-3:];

elves | if $part == 1 then max else top3 | add end
