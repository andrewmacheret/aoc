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
if [ -z $2 ]; then
  # <DAY>
  YEAR="$(date +"%Y")"
  DAY="$1"
else
  # <YEAR> <DAY>
  DAY="$2"
fi
LANG=$(ls 2020 | head -1)

[ -z $YEAR ] && usage 'Numeric argument YEAR is required'
[ -z $LANG ] && usage 'String argument LANG is required'
[[ $YEAR == 20?? ]] || usage "Numeric argument YEAR should be in format 20xx: '$YEAR'"
[[ $LANG == python ]] || [[ $LANG == jq ]] || usage "Unsupported language: '$LANG'"
which pandoc 2>&1 >/dev/null || error 'Requirement pandoc is not installed'

for DAY in $( seq 1 25 ); do
  ./finish-day.sh "$YEAR" "$LANG" "$DAY"
done
