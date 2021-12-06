#!/usr/bin/env -S bash -e

padding=8
. "$( dirname "$0" )"/../common/util.sh

test 5   jq -R -r -s --arg part 1 -f main.jq input-test-1
test 4873  jq -R -r -s --arg part 1 -f main.jq input-real

test 12   jq -R -r -s --arg part 2 -f main.jq input-test-1
test 19472  jq -R -r -s --arg part 2 -f main.jq input-real
