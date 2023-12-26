#!/usr/bin/env -S bash -e

cd "$( dirname "${BASH_SOURCE[0]}" )"

YEAR="$1"
DAY="$2"
SORT="$3"
[ -z $YEAR ] && YEAR="$( date '+%Y' )"
[ -z $DAY ] && DAY="$( date '+%d' )"
[ -z $SORT ] && SORT="star1"

echo "> YEAR=$YEAR DAY=$DAY SORT=$SORT" >&2

COOKIES="$( ./get-cookies.py https://adventofcode.com )"
LEADERBOARD="$( curl -s -H "Cookie: $COOKIES" "https://adventofcode.com/$YEAR/leaderboard/private/view/493635.json" )"

(
echo "#,Name,Star 1, Star 2,Local Score,Global Score"
<<<"$LEADERBOARD" jq -r '[
    .members[] |
      {
        name: (if .name == null then "(anonymous user #" + (.id | tostring) + ")" else .name end),
        star1: (.completion_day_level["'"$DAY"'"]["1"].get_star_ts | if . == null then "99:99:99" else (. - 18000 | strftime("%H:%M:%S")) end),
        star2: (.completion_day_level["'"$DAY"'"]["2"].get_star_ts | if . == null then "99:99:99" else (. - 18000 | strftime("%H:%M:%S")) end),
        local: (.local_score | tostring),
        global: (.global_score | tostring),
      } | select(.star1 != "99:99:99")
    ] | sort_by(.'"$SORT"')
    | to_entries[]
    | [ .key + 1, .value[] ]
    | join(",")
') | column -t -s','
