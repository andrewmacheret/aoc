#!/usr/bin/env bash
set -e

YEAR="$1"
LANG="$2"
DAY="$3"

usage() {
  echo "USAGE: $(basename "$0") <YEAR> <LANG> <DAY>"
  error "$1"
}

error() {
  echo "ERROR: $1" >&2
  exit 1
}

[[ $YEAR != '' ]] || usage 'Numeric argument YEAR is required'
[[ $LANG != '' ]] || usage 'Numeric argument LANG is required'
[[ $DAY != '' ]] || usage 'Numeric argument DAY is required'
which pandoc 2>&1 >/dev/null || error 'Requirment pandoc is not installed'

cd "$( dirname "${BASH_SOURCE[0]}" )"

FOLDER="$YEAR/$LANG/day$( printf '%02d' "$DAY" )"

if ! [[ -d "$FOLDER" ]]; then
  error "$FOLDER doesn't exist yet"
fi

if [[ -f "${FOLDER}/README.md" ]]; then
  rm "${FOLDER}/README.md"
fi

COOKIE="$( ./get-cookies.py 'https://adventofcode.com' )"
PROBLEM_DESC_URL="https://adventofcode.com/$YEAR/day/$DAY"
echo -n "Getting problem description from $PROBLEM_DESC_URL ... "
PROBLEM_DESC="$(
  curl -s -H "Cookie: $COOKIE" "$PROBLEM_DESC_URL" |
    pandoc -f html -t markdown |
    awk '$0~/^---/ {p=1} $0~/^(If you like, you can|To play,|Both parts of this puzzle are complete)/ {p=0} p==1 && $0!~/Your puzzle answer was/ {print}'
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
