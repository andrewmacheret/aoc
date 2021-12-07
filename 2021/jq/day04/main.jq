def parse: [ split("\n")[0:-1][] ];

def parse_guesses: [ .[0] | split(",")[] | tonumber ];

def parse_boards: [ .[2:] | join(",") | split(",,")[] | [ scan("\\d+") | tonumber ] ];

def bingo:
  .board | [
    (range(5) as $i | [range(5) as $j | .[$i*5+$j]]),
    (range(5) as $i | [range(5) as $j | .[$i+$j*5]])
  ] | any(. == [null,null,null,null,null]);

def reduce_game($guess): [
  .[]
  | (.board | index($guess.value)) as $g
  | (if $g == null then . else (.board[$g] = null) end)
  | .winfo = (if .winfo or (bingo | not) then .winfo else (
      {order: $guess.key, score: ($guess.value * (.board | add))}
    ) end)
];

parse
  | parse_guesses as $guesses
  | [ parse_boards[] | {board: ., score: null} ] as $game
  | $guesses | to_entries | reduce .[] as $guess ($game; reduce_game($guess))
  | [ .[].winfo ] | sort_by(.order)[1-$part].score
