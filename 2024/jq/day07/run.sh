#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 3749              jq -R -r -s --argjson part 0 -f main.jq input-test-1
test 7579994664753     jq -R -r -s --argjson part 0 -f main.jq input-real
test 11387             jq -R -r -s --argjson part 1 -f main.jq input-test-1
test 438027111276610   jq -R -r -s --argjson part 1 -f main.jq input-real
