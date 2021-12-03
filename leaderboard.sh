#!/usr/bin/env -S bash -e

cd "$( dirname "${BASH_SOURCE[0]}" )"

COOKIES="$( ./get-cookies.py https://adventofcode.com )"

LEADERBOARD="$( curl -s -H "Cookie: $COOKIES" https://adventofcode.com/2021/leaderboard/private/view/493635.json )"

DAY="$1"
SORT="$2"

(
echo "Name,Star 1, Star 2,Local Score,Global Score"
<<<"$LEADERBOARD" jq -r '[.members[] |
  {
    name: (if .name == null then "(anonymous user #" + .id + ")" else .name end),
    star1: (.completion_day_level["'"$DAY"'"]["1"].get_star_ts | if . == null then "99:99:99" else (. - 18000 | strftime("%H:%M:%S")) end),
    star2: (.completion_day_level["'"$DAY"'"]["2"].get_star_ts | if . == null then "99:99:99" else (. - 18000 | strftime("%H:%M:%S")) end),
    local: (.local_score | tostring),
    global: (.global_score | tostring),
  }] | sort_by(.'"$SORT"')[] | .name + "," + .star1 + "," + .star2 + "," + .local + "," + .global
') | column -t -s','
