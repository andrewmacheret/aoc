#!/usr/bin/env -S bash -e

. "$( dirname "$0" )"/../common/util.sh

test 18         jq -R -r -s --argjson part 0 -f main.jq input-test-1
test 2551     jq -R -r -s --argjson part 0 -f main.jq input-real
test 9        jq -R -r -s --argjson part 1 -f main.jq input-test-1
test 1985     jq -R -r -s --argjson part 1 -f main.jq input-real
