reduce scan("(mul\\((\\d+),(\\d+)\\)|do(?:n\\'t)?\\(\\))") as $m ({total: 0, enable: true};
  if $m[0][:2] == "do" then .enable = ($m[0][:5] != "don't")
  elif $part == 0 or .enable then .total += ($m[1:] | map(tonumber) | .[0] * .[1]) end
) | .total
