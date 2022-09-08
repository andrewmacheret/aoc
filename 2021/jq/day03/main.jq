include "../common/util";

def most_common($c; $i): (
  map(split(""))
  | transpose[$c]
  | sort
  | group_by(.)
  | map({val: (.[0] | tonumber), len: length})
  | sort_by(.len)
  | if length == 2 and .[0].len == .[1].len then $i else .[-$i].val end
);

def get_rate($i): [
    range(0; .[0] | length) as $c | most_common($c; $i)
  ] | from_radix(2);

def get_rating($i):
reduce range(0; .[0] | length) as $c (.;
    most_common($c; $i) as $b
    | map(select((.[$c:$c+1] | tonumber) == $b))
  )
  | .[0]
  | split("")
  | map(tonumber)
  | from_radix(2);

lines
| if $part == 1 then
    get_rate(0) * get_rate(1)
  else
    get_rating(0) * get_rating(1)
  end
