#!/usr/bin/env -S bash -e

usage() {
  echo "USAGE: $(basename "$0") <YEAR> [<LANG>] <DAY>" 1>&2
  echo "If <LANG> is not provided, defaults to first subfolder in <YEAR>/" 1>&2
  error "$1"
}

error() {
  echo "ERROR: $1" >&2
  exit 1
}

cd "$( dirname "${BASH_SOURCE[0]}" )"

YEAR="$1"
LANG="$2"
DAY="$3"
if [ -z $3 ]; then
  if [ -z $2 ]; then
    # <DAY>
    YEAR="$(date +"%Y")"
    DAY="$1"
  else
    # <YEAR> <DAY>
    DAY="$2"
  fi
  LANG=$(ls 2020 | head -1)
fi

[ -z $YEAR ] && usage 'Numeric argument YEAR is required'
[ -z $LANG ] && usage 'String argument LANG is required'
[ -z $DAY ] && usage 'Numeric argument DAY is required'
[[ $DAY == 0* ]] && usage "Numeric argument DAY should not start with 0: '$DAY'"
[[ $YEAR == 20?? ]] || usage "Numeric argument YEAR should be in format 20xx: '$YEAR'"
[[ $LANG == python ]] || [[ $LANG == jq ]] || usage "Unsupported language: '$LANG'"
which pandoc 2>&1 >/dev/null || error 'Requirement pandoc is not installed'

FOLDER="$YEAR/$LANG/day$( printf '%02d' "$DAY" )"

if ! [[ -d "$FOLDER" ]]; then
  usage "Folder '$FOLDER' does not exist yet"
fi

COOKIE="$( ./get-cookies.py 'https://adventofcode.com' )"
PROBLEM_DESC_URL="https://adventofcode.com/$YEAR/day/$DAY"
CURL_ARGS="--connect-timeout 5 --max-time 5 -s"

echo -n "Getting problem description from $PROBLEM_DESC_URL ... "
PROBLEM_DESC="$(
  curl $CURL_ARGS -H "Cookie: $COOKIE" "$PROBLEM_DESC_URL" |
    pandoc -f html -t markdown |
    awk '$0~/^---|^## \\-\\--/ {p=1} $0~/^(If you like, you can|To play,|Both parts of this puzzle are complete)/ {p=0} p==1 && $0!~/Your puzzle answer was/ {print}'
)"
if [[ "$PROBLEM_DESC" != "" ]]; then
  echo 'found!'
  echo "Creating ${FOLDER}/README.md"
  (
    echo "$PROBLEM_DESC"
  ) > "${FOLDER}/README.md"
else
  echo 'NOT FOUND!'
fi
