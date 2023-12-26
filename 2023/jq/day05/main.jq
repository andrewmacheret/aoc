include "../common/util";

def parse_ops:
  # ignore first line of each block
  .[1:] |
  # parse each line into a tuple of [start, end, amount], and sort
  map(numbers | .[0] as $d | .[1] as $s | .[2] as $c | [$s, $s+$c, $d-$s]) |
  sort |
  # fill in gaps between intervals
  (pairwise | map(
    .[0][1] as $prev_end | .[1][0] as $next_start |
    select($prev_end < $next_start) |
    [$prev_end, $next_start]
  )) as $mid_gaps | 
  # add start gap if necessary
  .[0][0] as $first_start |
  (if $first_start > 0 then [[0, $first_start, 0]] else [] end) as $first_gap |
  # add end gap
  .[-1][1] as $last_end |
  [[$last_end, infinite, 0]] as $last_gap |
  # combine all intervals and sort again
  (. + $first_gap + $mid_gaps + $last_gap) | sort
;

def part1($all_ops):
  map(
    . as $seed |
    reduce $all_ops[] as $ops ($seed;
      . as $s |
      . + ($ops | map(select(.[0] <= $s and $s < .[1])) | .[0][2]) 
    )
  );

def part2($all_ops):
  paired |
  map(
    .[0] as $seed |
    .[1] as $seed_count |
    reduce $all_ops[] as $ops ([[$seed, $seed + $seed_count]];
      reduce .[] as $seed_range ([];
        $seed_range[0] as $seed_start |
        $seed_range[1] as $seed_end |
        . += (
          $ops | map(
            .[0] as $op_start | .[1] as $op_end | .[2] as $op_amt |
            select(
              ($seed_start <= $op_start and $op_start < $seed_end) or 
              ($seed_start <= ($op_end-1) and ($op_end-1) < $seed_end) or 
              ($op_start <= $seed_start and $seed_start < $op_end)
            ) |
            ([ $seed_start, $op_start ] | max) as $new_start |
            ([ $seed_end, $op_end ] | min) as $new_end |
            [$new_start + $op_amt, $new_end + $op_amt]
          )
        )
      )
    ) | map(.[0]) | min
  )
;

line_blocks |
  (.[1:] | map(parse_ops)) as $all_ops |
  .[0][0] | numbers |
  if $part == 0 then part1($all_ops) else part2($all_ops) end |
  min
