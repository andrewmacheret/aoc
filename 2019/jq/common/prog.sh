#!/usr/bin/env bash
set -e

TESTS="
  ../day02/run.sh
  ../day05/run.sh
  ../day07/run.sh
  ../day09/run.sh
  ../day11/run.sh
  ../day13/run.sh
"

for FILE in $TESTS; do
  echo
  echo "Running $FILE ..."
  "$FILE"
done
