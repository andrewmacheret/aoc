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
  echo "Creating $FOLDER/"
  mkdir -p "$FOLDER"
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

TEMPLATE_FILE="$( ls templates/$LANG-template.* 2>/dev/null | head -1 )"
MAIN_FILE="$( ls $FOLDER/main.* 2>/dev/null | head -1 )"
if [[ $TEMPLATE_FILE != "" ]] && [[ $MAIN_FILE == "" ]]; then
  TEMPLATE_FILE_EXT="${TEMPLATE_FILE##*.}"
  MAIN_FILE="${FOLDER}/main.${TEMPLATE_FILE_EXT}"
  echo "Copying $TEMPLATE_FILE to $MAIN_FILE"
  cp "$TEMPLATE_FILE" "$MAIN_FILE"
fi

if ! [[ -f "$FOLDER/input-test-1" ]]; then
  echo "Creating $FOLDER/input-test-1"
  touch "$FOLDER/input-test-1"
fi
if ! [[ -f "$FOLDER/input-test-2" ]]; then
  echo "Creating $FOLDER/input-test-2"
  touch "$FOLDER/input-test-2"
fi
if ! [[ -f "$FOLDER/input-test-3" ]]; then
  echo "Creating $FOLDER/input-test-3"
  touch "$FOLDER/input-test-3"
fi
if ! [[ -f "$FOLDER/input-test-4" ]]; then
  echo "Creating $FOLDER/input-test-4"
  touch "$FOLDER/input-test-4"
fi
if ! [[ -f "$FOLDER/input-test-5" ]]; then
  echo "Creating $FOLDER/input-test-5"
  touch "$FOLDER/input-test-5"
fi

if ! [[ -f "$FOLDER/__init__.py" ]]; then
  echo "Creating $FOLDER/__init__.py"
  touch "$FOLDER/__init__.py"
fi

echo "Pre-emptively creating $FOLDER/input-real"
PROBLEM_INPUT_URL="https://adventofcode.com/$YEAR/day/$DAY/input"
curl $CURL_ARGS -H "Cookie: $COOKIE" "$PROBLEM_INPUT_URL" > "$FOLDER/input-real"

echo "Waiting until it's time"
echo
DAY_PADDED="$( printf "%02d" "$DAY" )"
UNTIL="$( date -jf '%Y-%m-%d %H:%M:%S %z' "${YEAR}-12-${DAY_PADDED} 05:00:00 -0000" '+%s' )"
NOW="$( date '+%s' )"
while (( "$NOW" < "$UNTIL" )); do
  NOW="$( date '+%s' )"
  tput cuu1
  echo "$(( "$UNTIL" - "$NOW" )) seconds remaining ..."
  sleep .1
done

echo "Creating $FOLDER/input-real"
PROBLEM_INPUT_URL="https://adventofcode.com/$YEAR/day/$DAY/input"
while true; do
  curl $CURL_ARGS -H "Cookie: $COOKIE" "$PROBLEM_INPUT_URL" > "$FOLDER/input-real"
  if [[ "$(cat "$FOLDER/input-real")" != *"Please don't repeatedly request this endpoint"* ]]; then
    break
  fi
  echo "Endpoint not ready yet ..."
done

find "$FOLDER" | sort
