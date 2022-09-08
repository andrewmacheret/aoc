def points: {
    ")": 3, "]": 57, "}": 1197, ">": 25137,
    "(": 1, "[": 2, "{": 3, "<": 4,
  };

def closing: {"(": ")", "[": "]", "{": "}", "<": ">"};

def score:
  reduce split("")[] as $c (
    {
      stack: [],
      score: 0,
      valid: true
    };
    if .valid | not then
      .
    elif closing[$c] then
      .stack += [$c]
    elif closing[.stack[-1]] == $c then
      del(.stack[-1])
    else
      .score = points[$c] | .valid = false
    end
  ) | if $part == 0 then .score else (
    select(.valid) |
    reduce (.stack | reverse[]) as $c (0; . *= 5 | . += points[$c])
  ) end
;

lines | [.[] | score] | if $part == 0 then add else sort | .[(length - 1) / 2] end
