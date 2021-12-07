def parse: [ split("\n")[0:-1][] ];

def bits_to_int: reduce .[] as $i (0; . * 2 + $i);

def most_common(c; i): (
  [ [ .[]
    | split("") ]
    | transpose[c]
    | sort_by(.)
    | group_by(.)[]
    | [ (.[0] | tonumber), (. | length) ] ]
    | sort_by(.[1])
    | if (. | length) == 2 and .[0][1] == .[1][1] then i else .[-i][0] end
);

def get_rate(i): [
    range(0; .[0] | length) as $c | most_common($c; i)
  ] | bits_to_int;

def get_rating($i): [
    . as $in | [ range(0; .[0] | length) ]
      | reduce .[] as $c ($in; [
          most_common($c; $i) as $b
            | .[]
            | select((.[$c:$c+1] | tonumber) == $b)
        ])
      | .[0] | split("")[] | tonumber
  ] | bits_to_int;

parse | if $part == 1 then
    get_rate(0) * get_rate(1)
  else
    get_rating(0) * get_rating(1)
  end
