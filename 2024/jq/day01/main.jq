def part0:
  map(sort)                  # sort each array
  | transpose                # turn back into an array with 2 elements each
  | map(.[0] - .[-1] | abs)  # calculate the differences
;

def part1:
  # count occurrences in the second array
  (reduce .[1][] as $x ({}; .[$x | tostring] += 1)) as $c
  | .[0]                             # for each element in the first array
  | map(. * ($c[. | tostring] // 0)) # multiply by the count
;

split("\n")[:-1]                             # load input as lines
  | map(split("   ") | map(tonumber))        # 2 numbers per line
  | transpose                                # turn into two arrays
  | if $part == 0 then part0 else part1 end  # run the selected part
  | add                                      # sum the results
