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
which lynx 2>&1 >/dev/null || error 'Requirment lynx is not installed'

FOLDER="$YEAR/$LANG/day$( printf '%02d' "$DAY" )"
mkdir -p "$FOLDER"
lynx -dump "https://adventofcode.com/$YEAR/day/$DAY" | awk '$0~/^---/ {p=1} $0~/^   To play,/ {p=0} p==1 {print}' > "${FOLDER}/README.md"
