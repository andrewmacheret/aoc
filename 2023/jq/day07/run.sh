#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 6440         jq -R -r -s --argjson part 0  -f main.jq input-test-1
test 248105065    jq -R -r -s --argjson part 0  -f main.jq input-real

test 5905         jq -R -r -s --argjson part 1  -f main.jq input-test-1
test 249515436    jq -R -r -s --argjson part 1  -f main.jq input-real
