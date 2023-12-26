include "../common/util";

def monkeys:
  line_blocks | map({
    items: [.[1] | numbers[]],
    op: .[2] | split(" ")[6],
    amt: (.[2] | split(" ")[7] | try tonumber catch "old"),
    div: (.[3] | numbers[0]),
    throw: [(.[5] | numbers[0]), (.[4] | numbers[0])],
    inspections: 0
  });

monkeys |
(map(.div) | mul) as $big |
reduce range([20,10000][$part]) as $r (.;
  reduce range(length) as $x (.;
    .[$x] as $m |
    reduce $m.items[] as $i (.;
      (
        [(if $m.amt == "old" then $i else $m.amt end), $i]
        | if $m.op == "+" then add else mul end
      ) as $i
      | (($i / [3,1][$part] | floor) % $big) as $i
      | (if ($i % $m.div) == 0 then 1 else 0 end) as $test
      | .[$m.throw[$test]].items += [$i]
      | .[$x].inspections += 1
    ) | .[$x].items = []
  )
) | map(.inspections) | sort[-2:] | mul
