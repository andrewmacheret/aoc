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
  echo "Creating $FOLDER/"
  mkdir -p "$FOLDER"
fi

./get-cookies.py '.adventofcode.com' > cookies.txt

if ! [[ -f "${FOLDER}/README.md" ]]; then
  PROBLEM_DESC_URL="https://adventofcode.com/$YEAR/day/$DAY"
  echo -n "Getting problem description from $PROBLEM_DESC_URL ... "
  PROBLEM_DESC="$(
    curl -s --cookie ./cookies.txt "$PROBLEM_DESC_URL" |
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
fi

TEMPLATE_FILE="$( ls templates/$LANG-template.* 2>/dev/null | head -1 )"
MAIN_FILE="$( ls $FOLDER/main.* 2>/dev/null | head -1 )"
if [[ $TEMPLATE_FILE != "" ]] && [[ $MAIN_FILE == "" ]]; then
  TEMPLATE_FILE_EXT="${TEMPLATE_FILE##*.}"
  MAIN_FILE="${FOLDER}/main.${TEMPLATE_FILE_EXT}"
  echo "Copying $TEMPLATE_FILE to $MAIN_FILE"
  cp "$TEMPLATE_FILE" "$MAIN_FILE"
fi

if ! [[ -f "$FOLDER/input-test.txt" ]]; then
  echo "Creating $FOLDER/input-test.txt"
  touch "$FOLDER/input-test.txt"
fi

if ! [[ -f "$FOLDER/input.txt" ]]; then
  echo "Creating $FOLDER/input.txt"
  PROBLEM_INPUT_URL="https://adventofcode.com/$YEAR/day/$DAY/input"
  curl -s --cookie ./cookies.txt "$PROBLEM_INPUT_URL" > "$FOLDER/input.txt"
fi

find "$FOLDER"
